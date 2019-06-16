#f recibe "un" y "tn" para dar su resultado
def euler(k, n, f, u0=0, t0=0):


    #REVISAR SI ESTA BIEN


    #tn=t0+nk

    if n=0:
        return u0

    un=euler(k, n-1, f, u0, t0)

    return un+k*f(un, t0+n*k)

#HACER EULER CON VALOR PREVIO, PARA NO TENER QUE HACER
#TODOS LOS CALCULOS CADA VEZ QUE SE QUIERA OBTENER UN
#VALOR DE LA FUNCION DISCRETIZADA
def euler_con_valor_previo():
    return



def calculo_intermedio_1_RK4(k, f, un, t):

    return un+(k/2)*f(un,t)

def calculo_intermedio_2_RK4(k, f, un, t):

    return return un+k*f(un,t+k/2)


def runge_kuta_orden_4(k, n, f, u0=0, t0=0):

    if n=0:
        return u0

    un=runge_kuta_orden_4(k, n-1, f, u0, t0)
    un_intermedio_1= calculo_intermedio_1_RK4(k, n, f, un, t0+n*k)
    un_intermedio_2= calculo_intermedio_1_RK4(k, n, f, un_intermedio_1, t0+n*k+k/2)
    un_intermedio_3= calculo_intermedio_2_RK4(k, n, f, un_intermedio_2, t0+n*k+k/2)


    return un+(k/6)*(f(un, t0+n*k)+2*f(un_intermedio_1, t0+n*k+k/2))+2*f(un_intermedio_2, t0+n*k+k/2)+f(un_intermedio_3, t0+n*k+k))




    return
