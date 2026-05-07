from dataclasses import dataclass
from math import sqrt

from calculos.armaduras import ArranjoArmadura, escolher_arranjo
from calculos.materiais import Aco, Concreto
from calculos.secoes import SecaoRetangular
from calculos.unidades import kn_m_para_n_mm, mm2_para_cm2


@dataclass(frozen=True)
class ResultadoFlexao:
    md_kn_m: float
    d_mm: float
    fcd_mpa: float
    fyd_mpa: float
    x_mm: float
    x_d: float
    z_mm: float
    as_calc_mm2: float
    as_calc_cm2: float
    as_min_mm2: float
    as_min_cm2: float
    as_necessaria_mm2: float
    as_necessaria_cm2: float
    arranjo: ArranjoArmadura
    status: str
    observacoes: tuple[str, ...]


def altura_util(
    h_cm: float,
    cobrimento_cm: float,
    diametro_estribo_mm: float,
    diametro_barra_mm: float,
) -> float:
    return h_cm * 10 - cobrimento_cm * 10 - diametro_estribo_mm - diametro_barra_mm / 2


def area_aco_minima_mm2(secao: SecaoRetangular, rho_min: float = 0.0015) -> float:
    return rho_min * secao.bw_mm * secao.h_mm


def linha_neutra_retangular_simples(
    md_n_mm: float,
    bw_mm: float,
    d_mm: float,
    fcd_mpa: float,
) -> float:
    a = 0.272 * fcd_mpa * bw_mm
    b = -0.68 * fcd_mpa * bw_mm * d_mm
    c = md_n_mm
    delta = b**2 - 4 * a * c

    if delta < 0:
        raise ValueError("Momento solicitante acima da capacidade com armadura simples.")

    x1 = (-b - sqrt(delta)) / (2 * a)
    x2 = (-b + sqrt(delta)) / (2 * a)
    candidatos = [x for x in (x1, x2) if x > 0]
    if not candidatos:
        raise ValueError("Nao foi encontrada linha neutra positiva.")
    return min(candidatos)


def verificar_flexao_viga(
    secao: SecaoRetangular,
    concreto: Concreto,
    aco: Aco,
    mk_kn_m: float,
    gamma_f: float = 1.4,
    cobrimento_cm: float = 3.0,
    diametro_estribo_mm: float = 5.0,
    diametro_barra_estimado_mm: float = 12.5,
    rho_min: float = 0.0015,
) -> ResultadoFlexao:
    md_kn_m = gamma_f * mk_kn_m
    md_n_mm = kn_m_para_n_mm(md_kn_m)
    d = altura_util(secao.h, cobrimento_cm, diametro_estribo_mm, diametro_barra_estimado_mm)
    fcd = concreto.fcd
    fyd = aco.fyd

    x = linha_neutra_retangular_simples(md_n_mm, secao.bw_mm, d, fcd)
    x_d = x / d
    z = d - 0.4 * x
    as_calc = md_n_mm / (fyd * z)
    as_min = area_aco_minima_mm2(secao, rho_min=rho_min)
    as_necessaria = max(as_calc, as_min)

    arranjo = escolher_arranjo(
        as_necessaria_mm2=as_necessaria,
        bw_cm=secao.bw,
        cobrimento_cm=cobrimento_cm,
        diametro_estribo_mm=diametro_estribo_mm,
    )

    observacoes: list[str] = []
    if x_d > concreto.limite_x_d:
        observacoes.append(
            f"x/d = {x_d:.3f} maior que o limite {concreto.limite_x_d:.2f}; verificar armadura dupla."
        )
    if as_calc < as_min:
        observacoes.append("Armadura minima governou o dimensionamento.")
    if arranjo.status != "OK":
        observacoes.append("Arranjo de barras precisa ser revisto na largura da viga.")

    status = "OK" if not observacoes else "REVER"

    return ResultadoFlexao(
        md_kn_m=md_kn_m,
        d_mm=d,
        fcd_mpa=fcd,
        fyd_mpa=fyd,
        x_mm=x,
        x_d=x_d,
        z_mm=z,
        as_calc_mm2=as_calc,
        as_calc_cm2=mm2_para_cm2(as_calc),
        as_min_mm2=as_min,
        as_min_cm2=mm2_para_cm2(as_min),
        as_necessaria_mm2=as_necessaria,
        as_necessaria_cm2=mm2_para_cm2(as_necessaria),
        arranjo=arranjo,
        status=status,
        observacoes=tuple(observacoes),
    )
