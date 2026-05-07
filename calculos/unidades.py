"""Conversoes usadas nos calculos estruturais."""


def cm_para_mm(valor_cm: float) -> float:
    return valor_cm * 10


def mm2_para_cm2(valor_mm2: float) -> float:
    return valor_mm2 / 100


def cm2_para_mm2(valor_cm2: float) -> float:
    return valor_cm2 * 100


def kn_m_para_n_mm(valor_kn_m: float) -> float:
    return valor_kn_m * 1_000_000


def n_mm_para_kn_m(valor_n_mm: float) -> float:
    return valor_n_mm / 1_000_000
