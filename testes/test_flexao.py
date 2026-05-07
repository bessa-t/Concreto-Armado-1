import unittest

from calculos.flexao import verificar_flexao_viga
from calculos.materiais import Aco, Concreto
from calculos.secoes import SecaoRetangular


class TestFlexao(unittest.TestCase):
    def test_verificacao_flexao_retorna_resultado_consistente(self):
        resultado = verificar_flexao_viga(
            secao=SecaoRetangular(bw=20, h=50),
            concreto=Concreto(fck=30, E=30672),
            aco=Aco(fyk=500),
            mk_kn_m=85,
            cobrimento_cm=3,
            diametro_estribo_mm=5,
            diametro_barra_estimado_mm=12.5,
        )

        self.assertGreater(resultado.as_calc_cm2, 0)
        self.assertGreaterEqual(resultado.as_necessaria_cm2, resultado.as_min_cm2)
        self.assertGreaterEqual(resultado.arranjo.as_adotada_cm2, resultado.as_necessaria_cm2)
        self.assertLess(resultado.x_d, 0.45)


if __name__ == "__main__":
    unittest.main()
