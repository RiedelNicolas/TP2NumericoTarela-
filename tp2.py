#Alumnos:
#Cambiano Agustín: 102291
#Riedel Nicolás: 102130

import math
import csv


NUMERO_DE_PADRON = 102291
ALTURA_INICIAL = 38969 #metros
MASA_FELIX = 75
ACELERACION_GRAVEDAD = 9.80665 #m/(s**2)
VELOCIDAD_MAXIMA_EN_KM_H = 1250+NUMERO_DE_PADRON/1000 #Km/h
VELOCIDAD_MAXIMA = (1000/3600)*VELOCIDAD_MAXIMA_EN_KM_H #m/s
TIEMPO_CAIDA_LIBRE = 256 #segundos
ALTURA_APERTURA_PARACAIDAS = 1500 #metros
TIEMPO_APERTURA_PARACAIDAS = 3 #segundos
TIEMPO_TOTAL_SALTO = 450+NUMERO_DE_PADRON/1000 #segundos
VELOCIDAD_INICIAL = 0
ALPHA_MINIMO = 4000
ALPHA_MAXIMO = 10000
BETA_MINIMO = 0.001
BETA_MAXIMO = 0.01
n_MINIMO = 0.1
n_MAXIMO = 1





def aceleracion_primer_tramo(alpha, beta, velocidad, altura):
    return - ACELERACION_GRAVEDAD+beta*math.exp(-altura/alpha)*(velocidad**2)


def aceleracion_segundo_y_tercer_tramo(n, velocidad):
    return - ACELERACION_GRAVEDAD + n*(velocidad**2)



def obtener_velocidad_y_altura_RK4_primer_tramo(k, alpha, beta):

    altura_actual = ALTURA_INICIAL
    velocidad_actual = VELOCIDAD_INICIAL
    velocidades=[]
    alturas=[]

    while (altura_actual >= ALTURA_APERTURA_PARACAIDAS):

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

        q4_velocidad = k*aceleracion_primer_tramo(alpha, beta, velocidad_actual+q3_velocidad, altura_actual+q3_altura)
        q4_altura = k*(velocidad_actual+q3_velocidad)

        velocidad_actual=velocidad_actual+(1/6)*(q1_velocidad+2*q2_velocidad+2*q3_velocidad+q4_velocidad)
        altura_actual=altura_actual+(1/6)*(q1_altura+2*q2_altura+2*q3_altura+q4_altura)



    return velocidades, alturas


def obtener_velocidad_y_altura_RK4_segundo_tramo(k, factor, velocidad_inicial, altura_inicial, alpha, beta):

    altura_actual = altura_inicial
    velocidad_actual = velocidad_inicial
    velocidades=[]
    alturas=[]

    paso_actual=1

    while (k*paso_actual <= 3):

        #q1_velocidad=k*f1(Xn,Yn)
        q1_velocidad = k*aceleracion_segundo_y_tercer_tramo(beta*math.exp(-ALTURA_APERTURA_PARACAIDAS/alpha)+factor*(k*paso_actual), velocidad_actual)
        #q2_altura=k*f2(Xn)<---Depende solo de la velocidad
        q1_altura = k*velocidad_actual

        #q2_velocidad=k*f1(Xn+q1x/2,Yn+q1y/2)
        q2_velocidad = k*aceleracion_segundo_y_tercer_tramo(beta*math.exp(-ALTURA_APERTURA_PARACAIDAS/alpha)+factor*(k*paso_actual+k/2), velocidad_actual+0.5*q1_velocidad)
        #q2_altura=k*f1(Xn+q1x/2)
        q2_altura = k*(velocidad_actual+0.5*q1_velocidad)

        q3_velocidad = k*aceleracion_segundo_y_tercer_tramo(beta*math.exp(-ALTURA_APERTURA_PARACAIDAS/alpha)+factor*(k*paso_actual+k/2), velocidad_actual+0.5*q2_velocidad)
        q3_altura = k*(velocidad_actual+0.5*q2_velocidad)

        q4_velocidad = k*aceleracion_segundo_y_tercer_tramo(beta*math.exp(-ALTURA_APERTURA_PARACAIDAS/alpha)+factor*(k*paso_actual+k), velocidad_actual+q3_velocidad)
        q4_altura = k*(velocidad_actual+q3_velocidad)

        velocidad_actual=velocidad_actual+(1/6)*(q1_velocidad+2*q2_velocidad+2*q3_velocidad+q4_velocidad)
        altura_actual=altura_actual+(1/6)*(q1_altura+2*q2_altura+2*q3_altura+q4_altura)

        velocidades.append(velocidad_actual)
        alturas.append(altura_actual)

        paso_actual+=1

    diferencia_de_tiempo=k*(paso_actual-1)

    n_actual=beta*math.exp(-ALTURA_APERTURA_PARACAIDAS/alpha)+factor*(k*paso_actual)

    return velocidades, alturas, n_actual, diferencia_de_tiempo


def obtener_velocidad_y_altura_RK4_tercer_tramo(k, n, altura_inicial, velocidad_inicial):

    altura_actual = altura_inicial
    velocidad_actual = velocidad_inicial
    velocidades=[]
    alturas=[]

    while (altura_actual >= 0):

        #q1_velocidad=k*f1(Xn,Yn)
        q1_velocidad = k*aceleracion_segundo_y_tercer_tramo(n, velocidad_actual)
        #q2_altura=k*f2(Xn)<---Depende solo de la velocidad
        q1_altura = k*velocidad_actual

        #q2_velocidad=k*f1(Xn+q1x/2,Yn+q1y/2)
        q2_velocidad = k*aceleracion_segundo_y_tercer_tramo(n, velocidad_actual+0.5*q1_velocidad)
        #q2_altura=k*f1(Xn+q1x/2)
        q2_altura = k*(velocidad_actual+0.5*q1_velocidad)

        q3_velocidad = k*aceleracion_segundo_y_tercer_tramo(n, velocidad_actual+0.5*q2_velocidad)
        q3_altura = k*(velocidad_actual+0.5*q2_velocidad)

        q4_velocidad = k*aceleracion_segundo_y_tercer_tramo(n, velocidad_actual+q3_velocidad)
        q4_altura = k*(velocidad_actual+q3_velocidad)

        velocidad_actual=velocidad_actual+(1/6)*(q1_velocidad+2*q2_velocidad+2*q3_velocidad+q4_velocidad)
        altura_actual=altura_actual+(1/6)*(q1_altura+2*q2_altura+2*q3_altura+q4_altura)

        velocidades.append(velocidad_actual)
        alturas.append(altura_actual)

    return velocidades, alturas



def obtener_velocidad_y_altura_euler_primer_tramo(k, alpha, beta):

    altura_actual = ALTURA_INICIAL
    velocidad_actual = VELOCIDAD_INICIAL
    velocidades=[]
    alturas=[]

    while (altura_actual >= ALTURA_APERTURA_PARACAIDAS):

        velocidades.append(velocidad_actual)
        alturas.append(altura_actual)

        aux=velocidad_actual

        velocidad_actual=velocidad_actual+k*aceleracion_primer_tramo(alpha, beta, velocidad_actual, altura_actual)
        altura_actual=altura_actual+k*aux

    return velocidades, alturas


def obtener_velocidad_y_altura_euler_segundo_tramo(k, factor, velocidad_inicial, altura_inicial, alpha, beta):

    altura_actual = altura_inicial
    velocidad_actual = velocidad_inicial
    velocidades=[]
    alturas=[]

    paso_actual=1

    while (k*paso_actual <= 3):

        altura_actual=altura_actual+k*velocidad_actual
        velocidad_actual=velocidad_actual+k*aceleracion_segundo_y_tercer_tramo(beta*math.exp(-ALTURA_APERTURA_PARACAIDAS/alpha)+factor*(k*paso_actual), velocidad_actual)

        velocidades.append(velocidad_actual)
        alturas.append(altura_actual)

        paso_actual+=1

    diferencia_de_tiempo=k*(paso_actual-1)

    n_actual=beta*math.exp(-ALTURA_APERTURA_PARACAIDAS/alpha)+factor*(k*paso_actual)

    return velocidades, alturas, n_actual, diferencia_de_tiempo



def obtener_velocidad_y_altura_euler_tercer_tramo(k, n, altura_inicial, velocidad_inicial):

    altura_actual = altura_inicial
    velocidad_actual = velocidad_inicial
    velocidades=[]
    alturas=[]

    while (altura_actual >= 0):

        velocidad_actual=velocidad_actual+k*aceleracion_segundo_y_tercer_tramo(n, velocidad_actual)
        altura_actual=altura_actual+k*velocidad_actual

        velocidades.append(velocidad_actual)
        alturas.append(altura_actual)

    return velocidades, alturas



def exportar_valores(nombre_archivo, valores):
    with open(nombre_archivo+".csv", "w") as archivo_valores:
        writer=csv.writer(archivo_valores)
        listas_valores=map(lambda x:[x], valores)
        for valor in listas_valores:
            writer.writerow(valor)


def exportar_valores_con_enters(nombre_archivo, valores, cantidad_enters):
    with open(nombre_archivo+".csv", "w") as archivo_valores:
        writer=csv.writer(archivo_valores)
        listas_valores=map(lambda x:[x], valores)
        for valor in listas_valores:
            writer.writerow(valor)
            for i in range(cantidad_enters):
                writer.writerow('\t')





def obtener_alpha_y_beta():


    alpha=6490
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

    return alpha, beta

def obtener_n(ultima_altura, ultima_velocidad, tiempo_transcurrido, alpha, beta):

    k=0.1

    factor_maximo=(1-beta*math.exp(-1500/alpha))/3
    factor_minimo=(0.1-beta*math.exp(-1500/alpha))/3

    factor_actual=factor_minimo

    print("Factor maximo:", factor_maximo)
    print("Factor minimo:", factor_minimo)

    cambio_factor=0.001

    velocidades_segundo_tramo, alturas_segundo_tramo, n, diferencia_de_tiempo = obtener_velocidad_y_altura_RK4_segundo_tramo(k, factor_minimo, ultima_velocidad, ultima_altura, alpha, beta)
    velocidades_tercer_tramo, alturas_tercer_tramo = obtener_velocidad_y_altura_RK4_tercer_tramo(k, n, alturas_segundo_tramo[len(alturas_segundo_tramo)-1], velocidades_segundo_tramo[len(velocidades_segundo_tramo)-1])

    tiempo_total=tiempo_transcurrido+diferencia_de_tiempo+len(alturas_tercer_tramo)
    print("Tiempo total:", tiempo_total)


    error_relativo_tiempo_total=abs(TIEMPO_TOTAL_SALTO-tiempo_total)/TIEMPO_TOTAL_SALTO

    while error_relativo_tiempo_total>0.005 and n<1:
        velocidades_segundo_tramo, alturas_segundo_tramo, n, diferencia_de_tiempo = obtener_velocidad_y_altura_RK4_segundo_tramo(k, factor_actual, ultima_velocidad, ultima_altura, alpha, beta)
        velocidades_tercer_tramo, alturas_tercer_tramo = obtener_velocidad_y_altura_RK4_tercer_tramo(k, n, alturas_segundo_tramo[len(alturas_segundo_tramo)-1], velocidades_segundo_tramo[len(velocidades_segundo_tramo)-1])

        tiempo_total=tiempo_transcurrido+diferencia_de_tiempo+len(alturas_tercer_tramo)*k
        print("Factor:", factor_actual)
        print("n:", n)
        print("Tiempo total:", tiempo_total)
        print("Diferencia con tiempo total real:", TIEMPO_TOTAL_SALTO-tiempo_total)
        print()
        error_relativo_tiempo_total=abs(TIEMPO_TOTAL_SALTO-tiempo_total)/TIEMPO_TOTAL_SALTO
        factor_actual+=cambio_factor

    return n

def operar_con_RK4(alpha, beta, n, k):

    velocidades_primer_tramo,alturas_primer_tramo=obtener_velocidad_y_altura_RK4_primer_tramo(k, alpha, beta)

    n=obtener_n(alturas_primer_tramo[len(alturas_primer_tramo)-1], velocidades_primer_tramo[len(velocidades_primer_tramo)-1], (len(velocidades_primer_tramo)-1)*k, alpha, beta)

    print("El valor de n es:", n)

    factor=(n-beta*math.exp(-ALTURA_APERTURA_PARACAIDAS/alpha))/3
    velocidades_segundo_tramo,alturas_segundo_tramo, n_actual, diferencia_de_tiempo=obtener_velocidad_y_altura_RK4_segundo_tramo(k, factor, velocidades_primer_tramo[len(velocidades_primer_tramo)-1], alturas_primer_tramo[len(alturas_primer_tramo)-1], alpha, beta)

    velocidades_tercer_tramo,alturas_tercer_tramo=obtener_velocidad_y_altura_RK4_tercer_tramo(k, n, alturas_segundo_tramo[len(alturas_segundo_tramo)-1], velocidades_segundo_tramo[len(velocidades_segundo_tramo)-1])

    aceleracion_apertura_paracaidas=(abs(velocidades_segundo_tramo[0]-velocidades_primer_tramo[len(velocidades_primer_tramo)-1]))/k


    velocidades=velocidades_primer_tramo+velocidades_segundo_tramo+velocidades_tercer_tramo
    alturas=alturas_primer_tramo+alturas_segundo_tramo+alturas_tercer_tramo

    exportar_valores("velocidades_RK4", map(lambda x:-x, velocidades))
    exportar_valores("alturas_RK4", alturas)

    g_sentido=aceleracion_apertura_paracaidas/ACELERACION_GRAVEDAD

    return velocidades, alturas, abs(velocidades_primer_tramo[len(velocidades_primer_tramo)-1]), g_sentido


def obtener_velocidad_maxima(velocidades):

    velocidad=min(velocidades)

    return abs(velocidad),velocidades.index(velocidad)


def operar_con_euler(alpha, beta, n, k):

    velocidades_primer_tramo,alturas_primer_tramo=obtener_velocidad_y_altura_euler_primer_tramo(k, alpha, beta)

    print("Tiempo final primer tramo:", (len(velocidades_primer_tramo)-1)*k)

    factor=(n-beta*math.exp(-ALTURA_APERTURA_PARACAIDAS/alpha))/3
    velocidades_segundo_tramo,alturas_segundo_tramo, n_actual, diferencia_de_tiempo=obtener_velocidad_y_altura_euler_segundo_tramo(k, factor, velocidades_primer_tramo[len(velocidades_primer_tramo)-1], alturas_primer_tramo[len(alturas_primer_tramo)-1], alpha, beta)

    velocidades_tercer_tramo,alturas_tercer_tramo=obtener_velocidad_y_altura_euler_tercer_tramo(k, n, alturas_segundo_tramo[len(alturas_segundo_tramo)-1], velocidades_segundo_tramo[len(velocidades_segundo_tramo)-1])

    velocidades=velocidades_primer_tramo+velocidades_segundo_tramo+velocidades_tercer_tramo
    alturas=alturas_primer_tramo+alturas_segundo_tramo+alturas_tercer_tramo

    exportar_valores("velocidades_euler", map(lambda x:-x, velocidades))
    exportar_valores("alturas_euler", alturas)

    #velocidad_maxima,indice=obtener_velocidad_maxima(velocidades)
    #print("Velocidad maxima Euler:",velocidad_maxima)
    #print("Tiempo velocidad maxima Euler:", indice*k)
    #print("Altura velocidad maxima Euler:", alturas[indice])
    #print("Tiempo de caida Euler", (len(alturas)-1)*k)

    return velocidades, alturas


def orden_de_euler(alturas_primer_tramo_RK4, alturas_primer_tramo_euler, alpha, beta):

    k2=1

    velocidades_2, alturas_2=obtener_velocidad_y_altura_euler_primer_tramo(k2, alpha, beta)

    indice_altura_n_grande=100
    error_euler_2= abs(alturas_2[indice_altura_n_grande]-alturas_primer_tramo_RK4[indice_altura_n_grande*10])
    error_euler_1= abs(alturas_primer_tramo_euler[indice_altura_n_grande*10]-alturas_primer_tramo_RK4[indice_altura_n_grande*10])

    return math.log(error_euler_2/error_euler_1)/math.log(1/0.1)


def orden_de_RK4(alturas_primer_tramo_RK4, alpha, beta):

    k2=1
    k3=5

    velocidades_2, alturas_2=obtener_velocidad_y_altura_RK4_primer_tramo(k2, alpha, beta)
    velocidades_3, alturas_3=obtener_velocidad_y_altura_RK4_primer_tramo(k3, alpha, beta)

    indice_altura_n_grande=20

    error_RK4_3=abs(alturas_3[indice_altura_n_grande]-alturas_primer_tramo_RK4[indice_altura_n_grande*50])
    error_RK4_2=abs(alturas_2[indice_altura_n_grande*5]-alturas_primer_tramo_RK4[indice_altura_n_grande*50])

    return math.log(error_RK4_3/error_RK4_2)/math.log(k3/k2)





def agregar_enters(lista, cantidad):

    for i in range(cantidad):
        lista.append('\n')


def comparacion_de_datos_euler(euler_anterior, alpha, beta, n):

    velocidades_euler_2, alturas_euler_2=obtener_velocidad_y_altura_euler_primer_tramo(1, alpha, beta)
    velocidades_euler_3, alturas_euler_3=obtener_velocidad_y_altura_euler_primer_tramo(5, alpha, beta)

    exportar_valores_con_enters("alturas_euler_k=1", alturas_euler_2, 9)
    exportar_valores_con_enters("alturas_euler_k=5", alturas_euler_3, 49)



def comparacion_de_datos_RK4(RK4_anterior, alpha, beta, n):

    velocidades_RK4_2, alturas_RK4_2=obtener_velocidad_y_altura_RK4_primer_tramo(1,alpha, beta)
    velocidades_RK4_3, alturas_RK4_3=obtener_velocidad_y_altura_RK4_primer_tramo(5,alpha, beta)

    exportar_valores_con_enters("alturas_RK4_k=1", alturas_RK4_2, 9)
    exportar_valores_con_enters("alturas_RK4_k=5", alturas_RK4_3, 49)


def TP2():

    print("Alumnos:")
    print("Cambiano Agustín, padrón:102291")
    print("Riedel Nicolás, padrón:102130")

    print("La velocidad maxima exacta es: ", VELOCIDAD_MAXIMA)
    alpha_calculada,beta_calculada=obtener_alpha_y_beta()

    print("Alpha:", alpha_calculada)
    print("Beta:", beta_calculada)


    alpha=6496
    beta=0.00480
    k=0.1
    n=0.3884

    velocidades_RK4, alturas_RK4, velocidad_terminal, g=operar_con_RK4(alpha, beta, n, k)

    velocidades_euler, alturas_euler=operar_con_euler(alpha, beta, n, k)

    error_euler_velocidades=[]
    error_euler_alturas=[]

    for i in range(len(velocidades_euler)-1):
        error_euler_velocidades.append(abs(velocidades_RK4[i]-velocidades_euler[i]))
        error_euler_alturas.append(abs(alturas_RK4[i]-alturas_euler[i]))


    exportar_valores("errores_altura_euler", error_euler_alturas)
    exportar_valores("errores_velocidad_euler", error_euler_velocidades)

    velocidad_maxima,paso_velocidad_maxima=obtener_velocidad_maxima(velocidades_RK4)
    print("Velocidad maxima encontrada:", velocidad_maxima)
    print("Tiempo de la velocidad maxima:", paso_velocidad_maxima*k)
    print("Altura velocidad maxima:", alturas_RK4[paso_velocidad_maxima])
    print("Velocidad terminal:", velocidad_terminal)
    print("Gs de aceleracion:", g)
    print("Orden de Euler:", orden_de_euler(alturas_RK4, alturas_euler, alpha, beta))
    print("Orden de RK4:", orden_de_RK4(alturas_RK4, alpha, beta))


    comparacion_de_datos_euler(alturas_euler, alpha, beta, n)
    comparacion_de_datos_RK4(alturas_RK4, alpha, beta, n)


    return

TP2()
