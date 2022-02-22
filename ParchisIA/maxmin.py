import numpy as np
import random

print('Inicializar fichas JUgador')
P1=np.array([-1,0])
P2=P1
P3=P1
P4=P1

print('DONE')


print('Inicializar Fichas I.A')
F1=P1
F2=F1
F3=F1
F4=F1

print('DONE')

print('Inicializar tablero')
tablero= np.zeros([68,3])

tablero[4][2]=1
tablero[11][2]=1
tablero[16][2]=1
tablero[21][2]=1
tablero[28][2]=1
tablero[33][2]=1
tablero[38][2]=1
tablero[45][2]=1
tablero[50][2]=1
tablero[55][2]=1
tablero[62][2]=1
tablero[67][2]=1

print('DONE')

H1=np.array([P1,P2,P3,P4])

def lanzar():
    return random.randint(1,6)


ganador=False
turno=1
contador=0


while(not ganador):
    if(turno==1):
        print('Juega Player')
        turno=0
        contador=contador+1
        print(contador)

        




        dado=lanzar()
        if(dado==5):
            print('Un 5 ')
        elif(dado==6):
            print('Un 6')

    else:
        print('Juega A.I.')
        turno=1
        contador=contador+1
        print(contador)
        dado=lanzar()
        if(dado==5):
            print('Un 5')
        elif(dado==6):
            print('Un 6')



    if(contador==20):
        ganador=True




