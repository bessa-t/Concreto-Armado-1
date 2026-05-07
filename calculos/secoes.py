from dataclasses import dataclass


@dataclass
class SecaoRetangular:
    """Secao retangular com dimensoes em cm."""

    bw: float
    h: float

    @property
    def bw_mm(self) -> float:
        return self.bw * 10

    @property
    def h_mm(self) -> float:
        return self.h * 10

    @property
    def area_concreto_cm2(self) -> float:
        return self.bw * self.h


# Alias para compatibilidade com notebooks antigos.
secao_retangular = SecaoRetangular
