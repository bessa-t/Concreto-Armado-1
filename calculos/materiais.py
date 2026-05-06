# calculos/materiais.py

from dataclasses import dataclass

@dataclass
class concreto:
    fck: float #MPa
    gama_d : float = 1.4
    E: float #Mpa

@dataclass
class aço:
    fyk: float #Mpa
    gama_d : float = 1.15
    E: float = 210000 #Mpa
