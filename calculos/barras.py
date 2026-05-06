# calculos/barras.py

# Dicionário baseado no Quadro 4.1 - Características das barras de aço
# Unidades seguem o padrão técnico brasileiro para cálculo estrutural.

tabela_barras = {
    # Chave (float): Bitola nominal da barra/fio em milímetros (mm)
    # area: Área da seção transversal em centímetros quadrados (cm²)
    # peso: Peso linear em kgf/m (equivalente a daN/m)
    # perimetro: Perímetro da seção em centímetros (cm)
    
    3.2:  {"polegada": None,    "area": 0.080, "peso": 0.063, "perimetro": 1.00},
    4.0:  {"polegada": None,    "area": 0.125, "peso": 0.100, "perimetro": 1.25},
    5.5:  {"polegada": None,    "area": 0.240, "peso": 0.186, "perimetro": 1.73},
    6.3:  {"polegada": '1/4"',  "area": 0.315, "peso": 0.248, "perimetro": 2.00},
    8.0:  {"polegada": '5/16"', "area": 0.500, "peso": 0.393, "perimetro": 2.50},
    10.0: {"polegada": '3/8"',  "area": 0.800, "peso": 0.624, "perimetro": 3.15},
    12.5: {"polegada": '1/2"',  "area": 1.250, "peso": 0.988, "perimetro": 4.00},
    16.0: {"polegada": '5/8"',  "area": 2.000, "peso": 1.570, "perimetro": 5.00},
    20.0: {"polegada": '3/4"',  "area": 3.150, "peso": 2.480, "perimetro": 6.30},
    22.5: {"polegada": '7/8"',  "area": 4.000, "peso": 3.120, "perimetro": 7.10},
    25.0: {"polegada": '1"',    "area": 5.000, "peso": 3.930, "perimetro": 8.00},
    32.0: {"polegada": '1.25"', "area": 8.000, "peso": 6.240, "perimetro": 10.0},
}