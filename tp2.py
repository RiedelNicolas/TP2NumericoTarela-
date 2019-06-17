#Alumnos:
#Cambiano Agustín: 102291
#Riedel Nicolás: 102130


from constant import *
from metodos_numericos import *
from math import *

def aceleracion(alpha, beta, velocidad, altura):
    #argumentos: (alpha, beta, velocidad, posicion, t), t esta para
    #que siga el formato
    return - ACELERACION_GRAVEDAD+beta*exp(altura/alpha)*(velocidad**2)


"""
def velocidad(x):
    return x

def calculo_intermedio_1_RK4(k, alpha, beta, velocidad, altura):
    return velocidad+(k/2)*aceleracion(alpha, beta, velocidad, altura)

def calculo_intermedio_2_RK4(k, alpha, beta, velocidad, velocidad_intermedia_1, altura):
    return velocidad+(k/2)*aceleracion(alpha, beta, velocidad_intermedia_1, posicion)

def calculo_intermedio_3_RK4(k, alpha, beta, velocidad, velocidad_intermedia_2, altura):
    return un+k*aceleracion(alpha, beta, velocidad_intermedia_2, altura)
"""

def obtener_velocidad_y_altura_RK4_primer_tramo(k, alpha, beta):

    altura_actual = ALTURA_INICIAL
    velocidad_actual = VELOCIDAD_INICIAL
    velocidades=[]
    alturas=[]

    while (altura_actual > ALTURA_APERTURA_PARACAIDAS):

        """
        velocidad_intermedia_1=calculo_intermedio_1_RK4(k, alpha, beta, velocidad_actual, posicion)
        velocidad_intermedia_2=calculo_intermedio_2_RK4(k, alpha, beta, velocidad_actual, velocidad_intermedia_1, posicion)
        velocidad_intermedia_3=calculo_intermedio_2_RK4(k, alpha, beta, velocidad_actual, velocidad_intermedia_2, posicion)

        velocidad_actual= velocidad_actual+(k/6)*(aceleracion(un, t0+n*k)+2*aceleracion(un_intermedio_1, t0+n*k+k/2)+2*aceleracion(un_intermedio_2, t0+n*k+k/2)+f(un_intermedio_3, t0+n*k+k))
        altura_actual=

    RK4_con_valor_previo(k, n_inicial, n_final, f, u_inicial, t0)
        """

        velocidades.add(velocidad_actual)
        alturas.add(altura_actual)

        #q1_velocidad=k*f1(Xn,Yn)
        q1_velocidad = k*aceleracion(alpha, beta, velocidad_actual, altura_actual)
        #q2_altura=k*f2(Xn)<---Depende solo de la velocidad
        q1_altura = k*velocidad_actual

        #q2_velocidad=k*f1(Xn+q1x/2,Yn+q1y/2)
        q2_velocidad = k*aceleracion(alpha, beta, velocidad_actual+0.5*q1_velocidad, altura_actual+0.5*q1_altura)
        #q2_altura=k*f1(Xn+q1x/2)
        q2_altura = k*(velocidad_actual+0.5*q1_velocidad)

        q3_velocidad = k*aceleracion(alpha, beta, velocidad_actual+0.5*q2_velocidad, altura_actual+0.5*q2_altura)
        q3_altura = k*(velocidad_actual+0.5*q2_velocidad)

        q4_velocidad = k*aceleracion(alpha, beta, velocidad_actual+q3_velocidad, altura_actual+0.5*q2_altura)
        q4_altura = k*(velocidad_actual+q3_velocidad)

        velocidad_actual=velocidad_actual+(1/6)*(q1_velocidad+q2_velocidad+q3_velocidad+q4_velocidad)
        altura_actual=altura_actual+(1/6)*(q1_altura+q2_altura+q3_altura+q4_altura)

    return velocidades, alturas

def TP2():



    return

TP2()
