#Alumnos:
#Cambiano Agustín: 102291
#Riedel Nicolás: 102130


from constant import *
from metodos_numericos import *
from math import *

def aceleracion(alpha, beta, velocidad, posicion):
    return - ACELERACION_GRAVEDAD+beta*exp(posicion/alpha)*(velocidad**2)


def TP2():



    return

TP2()
