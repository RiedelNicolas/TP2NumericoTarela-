#Alumnos:
#Cambiano Agustín: 102291
#Riedel Nicolás: 102130


from constant import *
from metodos_numericos import *
import math
import csv

def aceleracion_primer_tramo(alpha, beta, velocidad, altura):
    return - ACELERACION_GRAVEDAD+beta*math.exp(-altura/alpha)*(velocidad**2)


#def aceleracion_segundo_tramo(factor, velocidad, t, tiempo_inicial, alpha, beta):
#    return - ACELERACION_GRAVEDAD + (beta*math.exp(1500/alpha)+factor*(t-tiempo_inicial))*(velocidad**2)

def aceleracion_segundo_y_tercer_tramo(n, velocidad):
    return - ACELERACION_GRAVEDAD + n*(velocidad**2)


#def aceleracion_tercer_tramo(n, velocidad):
#    return - ACELERACION_GRAVEDAD + n*(velocidad**2)

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


#Guarda en el ultimo lugar de cada lista la altura y velocidad del instante siguiente
#al intervalo
def obtener_velocidad_y_altura_RK4_primer_tramo(k, alpha, beta):

    altura_actual = ALTURA_INICIAL
    velocidad_actual = VELOCIDAD_INICIAL
    velocidades=[VELOCIDAD_INICIAL]
    alturas=[ALTURA_INICIAL]

    while (altura_actual >= ALTURA_APERTURA_PARACAIDAS):

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

        q4_velocidad = k*aceleracion_primer_tramo(alpha, beta, velocidad_actual+q3_velocidad, altura_actual+q3_altura)
        q4_altura = k*(velocidad_actual+q3_velocidad)

        velocidad_actual=velocidad_actual+(1/6)*(q1_velocidad+2*q2_velocidad+2*q3_velocidad+q4_velocidad)
        altura_actual=altura_actual+(1/6)*(q1_altura+2*q2_altura+2*q3_altura+q4_altura)

        velocidades.append(velocidad_actual)
        alturas.append(altura_actual)

    return velocidades, alturas



#Guarda en el ultimo lugar de cada lista la altura y velocidad del instante siguiente
#al intervalo
def obtener_velocidad_y_altura_RK4_segundo_tramo(k, n, factor, velocidad_inicial):

    altura_actual = altura_inicial
    velocidad_actual = velocidad_inicial
    velocidades=[velocidad_inicial]
    alturas=[altura_inicial]

    paso_actual=1

    while (k*paso_actual <= 3):

        #q1_velocidad=k*f1(Xn,Yn)
        q1_velocidad = k*aceleracion_segundo_y_tercer_tramo(beta*math.exp(ALTURA_APERTURA_PARACAIDAS/alpha)+factor*(k*paso_actual), velocidad)
        #q2_altura=k*f2(Xn)<---Depende solo de la velocidad
        q1_altura = k*velocidad_actual

        #q2_velocidad=k*f1(Xn+q1x/2,Yn+q1y/2)
        q2_velocidad = k*aceleracion_segundo_y_tercer_tramo(beta*math.exp(ALTURA_APERTURA_PARACAIDAS/alpha)+factor*(k*paso_actual+k/2), velocidad_actual+0.5*q1_velocidad)
        #q2_altura=k*f1(Xn+q1x/2)
        q2_altura = k*(velocidad_actual+0.5*q1_velocidad)

        q3_velocidad = k*aceleracion_segundo_y_tercer_tramo(beta*math.exp(ALTURA_APERTURA_PARACAIDAS/alpha)+factor*(k*paso_actual+k/2), velocidad_actual+0.5*q2_velocidad)
        q3_altura = k*(velocidad_actual+0.5*q2_velocidad)

        q4_velocidad = k*aceleracion_segundo_y_tercer_tramo(beta*math.exp(ALTURA_APERTURA_PARACAIDAS/alpha)+factor*(k*paso_actual+k), velocidad_actual+q3_velocidad)
        q4_altura = k*(velocidad_actual+q3_velocidad)

        velocidad_actual=velocidad_actual+(1/6)*(q1_velocidad+2*q2_velocidad+2*q3_velocidad+q4_velocidad)
        altura_actual=altura_actual+(1/6)*(q1_altura+2*q2_altura+2*q3_altura+q4_altura)

        velocidades.append(velocidad_actual)
        alturas.append(altura_actual)

        paso_actual+=1

    diferencia_de_tiempo=k*paso_actual

    n_actual=beta*math.exp(ALTURA_APERTURA_PARACAIDAS/alpha)+factor*(k*paso_actual)

    return velocidades, alturas, n_actual, diferencia_de_tiempo


def obtener_velocidad_y_altura_RK4_tercer_tramo(k, n, altura_inicial, velocidad_inicial, tiempo_inicial):

    altura_actual = altura_inicial
    velocidad_actual = velocidad_inicial
    velocidades=[]
    alturas=[]

    while (altura_actual >= 0):

        velocidades.append(velocidad_actual)
        alturas.append(altura_actual)

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

        velocidad_actual=velocidad_actual+(1/6)*(q1_velocidad+2*q2_velocidad+2*q3_velocidad+q4_velocidad)
        altura_actual=altura_actual+(1/6)*(q1_altura+2*q2_altura+2*q3_altura+q4_altura)

    return velocidades, alturas




def exportar_valores(nombre_archivo, valores):
    with open(nombre_archivo+".csv", "w") as archivo_valores:
        writer=csv.writer(archivo_valores)
        listas_valores=map(lambda x:[x], valores)
        for valor in listas_valores:
            writer.writerow(valor)


def obtener_alpha_y_beta_2():


    #alpha=ALPHA_MINIMO
    #mejor alpha por ahora 6463
    alpha=6463
    beta=BETA_MINIMO
    k=0.1

    diferencia_alpha=1
    diferencia_beta=0.0001

    velocidades,alturas=obtener_velocidad_y_altura_RK4_primer_tramo(k, alpha, beta)


    velocidad_maxima_actual = abs(min(velocidades)  )
    tiempo_de_caida_actual = len(alturas)*k
    error_relativo_velocidad = abs(velocidad_maxima_actual-VELOCIDAD_MAXIMA)/VELOCIDAD_MAXIMA
    error_relativo_tiempo_caida_libre = abs(tiempo_de_caida_actual-TIEMPO_CAIDA_LIBRE)/TIEMPO_CAIDA_LIBRE

    print("Alpha:", alpha)
    print("Beta:", beta)
    print("Velocidad maxima:", velocidad_maxima_actual)
    print("Diferencia velocidad maxima", VELOCIDAD_MAXIMA-velocidad_maxima_actual)
    print("Tiempo de caida libre:", tiempo_de_caida_actual)
    print("Diferencia tiempo de caida:", TIEMPO_CAIDA_LIBRE-tiempo_de_caida_actual)
    print()

    while (error_relativo_velocidad > 0.005 or error_relativo_tiempo_caida_libre > 0.005):

        velocidades,alturas=obtener_velocidad_y_altura_RK4_primer_tramo(k, alpha, beta)


        velocidad_maxima_actual = abs(min(velocidades))
        tiempo_de_caida_actual = len(alturas)*k
        error_relativo_velocidad = abs(velocidad_maxima_actual-VELOCIDAD_MAXIMA)/VELOCIDAD_MAXIMA
        error_relativo_tiempo_caida_libre = abs(tiempo_de_caida_actual-TIEMPO_CAIDA_LIBRE)/TIEMPO_CAIDA_LIBRE

        print("Alpha:", alpha)
        print("Beta:", beta)
        print("Velocidad maxima:", velocidad_maxima_actual)
        print("Diferencia velocidad maxima", VELOCIDAD_MAXIMA-velocidad_maxima_actual)
        print("Tiempo de caida libre:", tiempo_de_caida_actual)
        print("Diferencia tiempo de caida:", TIEMPO_CAIDA_LIBRE-tiempo_de_caida_actual)
        print()

        beta+=diferencia_beta

        if beta>=BETA_MAXIMO:
            beta=BETA_MINIMO
            alpha+=diferencia_alpha

    return


def obtener_n(tiempo_transcurrido, alpha, beta):

    k=0.1

    factor_maximo=(1-beta*math.exp(1500/alpha))/3
    factor_minimo=(0.1-beta*math.exp(1500/alpha))/3

    print("Factor maximo:", factor_maximo)
    print("Factor minimo:", factor_minimo)

    velocidades_segundo_tramo, alturas_segundo_tramo, n, diferencia_de_tiempo = obtener_velocidad_y_altura_RK4_segundo_tramo(k, factor_minimo, altura_inicial, velocidad_inicial)
    velocidades_tercer_tramo, alturas_tercer_tramo = obtener_velocidad_y_altura_RK4_tercer_tramo(k, n, alturas_segundo_tramo[len(alturas_segundo_tramo)-1], velocidades_segundo_tramo[len(velocidades_segundo_tramo)-1], tiempo_transcurrido+diferencia_de_tiempo)

    tiempo_total=tiempo_transcurrido+diferencia_de_tiempo+len(alturas_tercer_tramo)
    print("Tiempo total:", tiempo_total)

    return



def TP2():

    print("La velocidad maxima es: ", VELOCIDAD_MAXIMA)
    #obtener_alpha_y_beta()
    #obtener_alpha_y_beta_2()

    alpha=6496
    beta=0.00480
    k=0.1
    velocidades,alturas=obtener_velocidad_y_altura_RK4_primer_tramo(k, alpha, beta)

    #print(velocidades)
    #print(alturas)

    exportar_valores("velocidades_tramo_1", map(lambda x:-x, velocidades))
    exportar_valores("alturas_tramo_1", alturas)

    #QUE VALOR SE USA AL ABRIR EL PARACAIDAS? EL SIGUIENTE QUE SE TENDRIA
    #SI NO SE HUBIESE ABIERTO?

    #se usa -2 porque en la ultima posicion se guarda el valor despues de abrir el paracaidas
    print("Velocidad terminal: ",abs(velocidades[len(velocidades)-2]))


    #SACAR QUE SE CALCULA LA VELOCIDAD Y ALTURA DEL PRIMER PASO DEL METODO SIGUIENTE
    #CON EL METODO ANTERIOR

    obtener_n(k*len(velocidades), alpha, beta)

    return

TP2()
