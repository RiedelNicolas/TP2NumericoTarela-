#Alumnos:
#Cambiano Agustín: 102291
#Riedel Nicolás: 102130


from constant import *
from metodos_numericos import *
import math
import csv

def aceleracion_primer_tramo(alpha, beta, velocidad, altura):
    return - ACELERACION_GRAVEDAD+beta*math.exp(altura/alpha)*(velocidad**2)


def aceleracion_tercer_tramo(n, velocidad):
    return - ACELERACION_GRAVEDAD + n*(velocidad**2)

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

    while (altura_actual >= ALTURA_APERTURA_PARACAIDAS):

        """
        velocidad_intermedia_1=calculo_intermedio_1_RK4(k, alpha, beta, velocidad_actual, posicion)
        velocidad_intermedia_2=calculo_intermedio_2_RK4(k, alpha, beta, velocidad_actual, velocidad_intermedia_1, posicion)
        velocidad_intermedia_3=calculo_intermedio_2_RK4(k, alpha, beta, velocidad_actual, velocidad_intermedia_2, posicion)

        velocidad_actual= velocidad_actual+(k/6)*(aceleracion(un, t0+n*k)+2*aceleracion(un_intermedio_1, t0+n*k+k/2)+2*aceleracion(un_intermedio_2, t0+n*k+k/2)+f(un_intermedio_3, t0+n*k+k))
        altura_actual=

    RK4_con_valor_previo(k, n_inicial, n_final, f, u_inicial, t0)
        """

        velocidades.append(velocidad_actual)
        alturas.append(altura_actual)

        #q1_velocidad=k*f1(Xn,Yn)
        q1_velocidad = k*aceleracion_primer_tramo(alpha, beta, velocidad_actual, altura_actual)
        #q2_altura=k*f2(Xn)<---Depende solo de la velocidad
        q1_altura = k*velocidad_actual

        #q2_velocidad=k*f1(Xn+q1x/2,Yn+q1y/2)
        q2_velocidad = k*aceleracion_primer_tramo(alpha, beta, velocidad_actual+0.5*q1_velocidad, altura_actual+0.5*q1_altura)
        #q2_altura=k*f1(Xn+q1x/2)
        q2_altura = k*(velocidad_actual+0.5*q1_velocidad)

        q3_velocidad = k*aceleracion_primer_tramo(alpha, beta, velocidad_actual+0.5*q2_velocidad, altura_actual+0.5*q2_altura)
        q3_altura = k*(velocidad_actual+0.5*q2_velocidad)

        q4_velocidad = k*aceleracion_primer_tramo(alpha, beta, velocidad_actual+q3_velocidad, altura_actual+0.5*q2_altura)
        q4_altura = k*(velocidad_actual+q3_velocidad)

        velocidad_actual=velocidad_actual+(1/6)*(q1_velocidad+q2_velocidad+q3_velocidad+q4_velocidad)
        altura_actual=altura_actual+(1/6)*(q1_altura+q2_altura+q3_altura+q4_altura)

    return velocidades, alturas

def obtener_velocidad_y_altura_RK4_segundo_tramo():
    return


def obtener_velocidad_y_altura_RK4_tercer_tramo(k, n):

    altura_actual = no_se
    velocidad_actual = no_se
    velocidades=[]
    alturas=[]

    while (altura_actual >= 0):

        velocidades.append(velocidad_actual)
        alturas.append(altura_actual)

        """
        #BORRAR PRINTS
        print(velocidad_actual)
        print(altura_actual)
        """

        #q1_velocidad=k*f1(Xn,Yn)
        q1_velocidad = k*aceleracion_tercer_tramo(n, velocidad_actual)
        #q2_altura=k*f2(Xn)<---Depende solo de la velocidad
        q1_altura = k*velocidad_actual

        #q2_velocidad=k*f1(Xn+q1x/2,Yn+q1y/2)
        q2_velocidad = k*aceleracion_tercer_tramo(n, velocidad_actual+0.5*q1_velocidad)
        #q2_altura=k*f1(Xn+q1x/2)
        q2_altura = k*(velocidad_actual+0.5*q1_velocidad)

        q3_velocidad = k*aceleracion_tercer_tramo(n, velocidad_actual+0.5*q2_velocidad)
        q3_altura = k*(velocidad_actual+0.5*q2_velocidad)

        q4_velocidad = k*aceleracion_tercer_tramo(n, velocidad_actual+q3_velocidad)
        q4_altura = k*(velocidad_actual+q3_velocidad)

        velocidad_actual=velocidad_actual+(1/6)*(q1_velocidad+q2_velocidad+q3_velocidad+q4_velocidad)
        altura_actual=altura_actual+(1/6)*(q1_altura+q2_altura+q3_altura+q4_altura)

    return velocidades, alturas




def exportar_valores(nombre_archivo,errores):
    with open(nombre_archivo+".csv", "w") as archivo_valores:
        writer=csv.writer(archivo_valores)
        listas_valores=map(lambda x:[x], valores)
        for valor in listas_errores:
            writer.writerow(valor)

def obtener_alpha_y_beta():

    #LA VELOCIDAD MAXIMA ES EN CAIDA LIBRE
    #HAY QUE IR PROBANDO VALORES DE ALPHA Y BETA PARA QUE LA CANTIDAD DE
    #TIEMPO DE CALIDA LIBRE Y LA VELOCIDAD MAXIMA SEA LA DEL TP

    k=0.05

    alpha_minimo=ALPHA_MINIMO
    alpha_maximo=ALPHA_MAXIMO
    alpha_medio=(alpha_minimo+alpha_maximo)/2

    beta_minimo=BETA_MINIMO
    beta_maximo=BETA_MAXIMO
    beta_medio=(beta_minimo+beta_maximo)/2


    velocidades,alturas = obtener_velocidad_y_altura_RK4_primer_tramo(k, alpha_medio, beta_medio)
    velocidad_maxima = abs(min(velocidades))
    tiempo_caida_libre = len(alturas)*k
    error_relativo_velocidad = abs(velocidad_maxima-VELOCIDAD_MAXIMA)/VELOCIDAD_MAXIMA
    error_relativo_tiempo_caida_libre = abs(tiempo_caida_libre-TIEMPO_CAIDA_LIBRE)/TIEMPO_CAIDA_LIBRE
    while ((error_relativo_velocidad > 0.01)or(error_relativo_tiempo_caida_libre > 0.01)):
        break



    #print(velocidades)
    #print(alturas)

    print(abs(min(velocidades)))


def TP2():

    print("La velocidad maxima es: ", VELOCIDAD_MAXIMA)
    obtener_alpha_y_beta()




    return

TP2()
