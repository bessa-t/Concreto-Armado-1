from dataclasses import dataclass
from math import ceil

from calculos.barras import tabela_barras


@dataclass(frozen=True)
class ArranjoArmadura:
    n_barras: int
    bitola_mm: float
    as_adotada_mm2: float
    as_adotada_cm2: float
    n_camadas: int
    barras_por_camada: int
    espacamento_horizontal_mm: float
    status: str

    @property
    def descricao(self) -> str:
        return f"{self.n_barras} phi {self.bitola_mm:g} mm"


def area_barra_mm2(bitola_mm: float) -> float:
    try:
        return tabela_barras[bitola_mm]["area"] * 100
    except KeyError as exc:
        raise ValueError(f"Bitola nao cadastrada: {bitola_mm} mm") from exc


def verificar_arranjo(
    as_necessaria_mm2: float,
    bw_cm: float,
    cobrimento_cm: float,
    diametro_estribo_mm: float,
    bitola_mm: float,
    espacamento_min_mm: float | None = None,
) -> ArranjoArmadura:
    area = area_barra_mm2(bitola_mm)
    n_barras = max(2, ceil(as_necessaria_mm2 / area))
    phi = bitola_mm
    largura_livre_mm = bw_cm * 10 - 2 * cobrimento_cm * 10 - 2 * diametro_estribo_mm
    espac_min = espacamento_min_mm or max(20, phi)

    barras_por_camada = max(1, int((largura_livre_mm + espac_min) // (phi + espac_min)))
    n_camadas = ceil(n_barras / barras_por_camada)

    barras_primeira = min(n_barras, barras_por_camada)
    if barras_primeira > 1:
        espac_h = (largura_livre_mm - barras_primeira * phi) / (barras_primeira - 1)
    else:
        espac_h = largura_livre_mm - phi

    status = "OK" if barras_por_camada >= 2 and espac_h >= espac_min else "REVER_ARRANJO"
    as_adotada_mm2 = n_barras * area

    return ArranjoArmadura(
        n_barras=n_barras,
        bitola_mm=bitola_mm,
        as_adotada_mm2=as_adotada_mm2,
        as_adotada_cm2=as_adotada_mm2 / 100,
        n_camadas=n_camadas,
        barras_por_camada=barras_por_camada,
        espacamento_horizontal_mm=espac_h,
        status=status,
    )


def escolher_arranjo(
    as_necessaria_mm2: float,
    bw_cm: float,
    cobrimento_cm: float,
    diametro_estribo_mm: float,
    bitolas_mm: tuple[float, ...] = (8.0, 10.0, 12.5, 16.0, 20.0, 25.0),
) -> ArranjoArmadura:
    candidatos = [
        verificar_arranjo(
            as_necessaria_mm2=as_necessaria_mm2,
            bw_cm=bw_cm,
            cobrimento_cm=cobrimento_cm,
            diametro_estribo_mm=diametro_estribo_mm,
            bitola_mm=bitola,
        )
        for bitola in bitolas_mm
    ]

    candidatos_ok = [c for c in candidatos if c.status == "OK"]
    base = candidatos_ok or candidatos
    return min(base, key=lambda c: (c.status != "OK", c.n_camadas, c.as_adotada_mm2))
