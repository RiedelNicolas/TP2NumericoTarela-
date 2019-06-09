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


def runge_kuta_orden_4():
    return
