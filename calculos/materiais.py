from dataclasses import dataclass


@dataclass
class Concreto:
    """Propriedades do concreto em MPa."""

    fck: float
    E: float
    gamma_c: float = 1.4
    alpha_cc: float = 0.85

    @property
    def fcd(self) -> float:
        return self.alpha_cc * self.fck / self.gamma_c

    @property
    def limite_x_d(self) -> float:
        return 0.45 if self.fck <= 50 else 0.35


@dataclass
class Aco:
    """Propriedades do aco em MPa."""

    fyk: float
    gamma_s: float = 1.15
    E: float = 210000

    @property
    def fyd(self) -> float:
        return self.fyk / self.gamma_s


# Aliases para compatibilidade com notebooks antigos.
concreto = Concreto
aco = Aco
aço = Aco
