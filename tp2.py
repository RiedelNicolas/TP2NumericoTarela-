#Alumnos:
#Cambiano Agustín: 102291
#Riedel Nicolás: 102130


from constant import *
from metodos_numericos import *
from math import *

def aceleracion(alpha, beta, velocidad, posicion):
    #argumentos: (alpha, beta, velocidad, posicion, t), t esta para
    #que siga el formato
    return - ACELERACION_GRAVEDAD+beta*exp(posicion/alpha)*(velocidad**2)

def mismo_valor(x):
    return x

def obtener_velocidad_y_altura_RK4_primer_tramo(k, ):

    altura_actual = ALTURA_INICIAL

    velocidades=[VELOCIDAD_INICIAL]
    alturas=[ALTURA_INICIAL]

    while (altura>ALTURA_APERTURA_PARACAIDAS):
        pass

    RK4_con_valor_previo(k, n_inicial, n_final, f, u_inicial, t0)


def TP2():



    return

TP2()
