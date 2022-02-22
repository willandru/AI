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

print(lanzar())

ganador=False

while(not ganador):
    print('playing...')





