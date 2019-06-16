#f recibe "un" y "tn" para dar su resultado
def _euler(valores, k, n, f, u0=0, t0=0):

    #tn=t0+nk

    if n==0:
        valores.append(u0)
        return u0

    un=_euler(k, n-1, f, u0, t0)

    un_siguiente=un+k*f(un, t0+n*k)
    valores.append(un_siguiente)

    return un_siguiente

#n debe ser mayor o igual a 0
#devuelve lista de los valores desde n=0 hasta n
def euler(k, n, f, u0=0, t0=0):
    valores=[]
    _euler(valores, k, n, f, u0, t0)
    return valores


#HACER EULER CON VALOR PREVIO, PARA NO TENER QUE HACER
#TODOS LOS CALCULOS CADA VEZ QUE SE QUIERA OBTENER UN
#VALOR DE LA FUNCION DISCRETIZADA

#Devuelve el valor de la funcion en t=t0+n_final*k
#Tiene que recibir el n del que se quiere partir, con el valor
#de la funcion en el punto que le corresponde a ese n (n_final)
def euler_con_valor_previo(k, n_inicial, n_final, f, u_inicial, t0=0):

    #tn=t0+nk
    if n==n_inicial:
        return u_inicial

    un=euler_con_valor_previo(k, n_inicial, n_final-1, f, u_inicial, t0)

    return un+k*f(un, t0+n*k)



def calculo_intermedio_1_RK4(k, f, un, t):

    return un+(k/2)*f(un,t)

def calculo_intermedio_2_RK4(k, f, un, t):

    return un+k*f(un,t+k/2)


def _runge_kuta_orden_4(valores, k, n, f, u0=0, t0=0):

    if n==0:
        valores.add(u0)
        return u0

    un=runge_kuta_orden_4(k, n-1, f, u0, t0)
    un_intermedio_1= calculo_intermedio_1_RK4(k, f, un, t0+n*k)
    un_intermedio_2= calculo_intermedio_1_RK4(k, f, un_intermedio_1, t0+n*k+k/2)
    un_intermedio_3= calculo_intermedio_2_RK4(k, f, un_intermedio_2, t0+n*k+k/2)

    un_siguiente= un+(k/6)*(f(un, t0+n*k)+2*f(un_intermedio_1, t0+n*k+k/2)+2*f(un_intermedio_2, t0+n*k+k/2)+f(un_intermedio_3, t0+n*k+k))

    valores.add(un_siguiente)

    return un_siguiente


def runge_kuta_orden_4(valores, k, n, f, u0=0, t0=0):

    valores= []
    _runge_kuta_orden_4(k, n, f, u0, t0)
    return valores


#La misma ide que con euler_con_valor_previo pero con
#runge kuta de orden 4
def RK4_con_valor_previo(k, n_inicial, n_final, f, u_inicial, t0=0):

    if n==0:
        return n_inicial

    un= RK4_con_valor_previo(k, n_final-1, f, u_inicial, t0)
    un_intermedio_1= calculo_intermedio_1_RK4(k, f, un, t0+n*k)
    un_intermedio_2= calculo_intermedio_1_RK4(k, f, un_intermedio_1, t0+n*k+k/2)
    un_intermedio_3= calculo_intermedio_2_RK4(k, f, un_intermedio_2, t0+n*k+k/2)

    return un+(k/6)*(f(un, t0+n*k)+2*f(un_intermedio_1, t0+n*k+k/2)+2*f(un_intermedio_2, t0+n*k+k/2)+f(un_intermedio_3, t0+n*k+k))
