from calculos.flexao import ResultadoFlexao


def montar_linha_flexao(nome_viga: str, resultado: ResultadoFlexao) -> dict[str, object]:
    return {
        "viga": nome_viga,
        "Md (kN.m)": round(resultado.md_kn_m, 2),
        "d (mm)": round(resultado.d_mm, 1),
        "x/d": round(resultado.x_d, 3),
        "As calc (cm2)": round(resultado.as_calc_cm2, 2),
        "As min (cm2)": round(resultado.as_min_cm2, 2),
        "As nec (cm2)": round(resultado.as_necessaria_cm2, 2),
        "As adot (cm2)": round(resultado.arranjo.as_adotada_cm2, 2),
        "arranjo": resultado.arranjo.descricao,
        "camadas": resultado.arranjo.n_camadas,
        "status": resultado.status,
        "observacoes": "; ".join(resultado.observacoes),
    }
