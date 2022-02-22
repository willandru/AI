import numpy as np
import random


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


H1=np.array([(-1,0,0),(-1,0,1),(-1,0,2),(-1,0,3)]) ##FICHAS PLAYER



def lanzar():
    return random.randint(1,6)

print(H1)
def heuristicaPlayer():
	contador=0
	for x in H1:
		fin=68
		inicio=H1[contador][0]
		distancia= fin-inicio
		H1[contador][1]=distancia
		contador+=1
	h= H1[H1[:,1].argsort()]
	return h;







ganador=False
turno=1
contador=0
while(not ganador):
    if(turno==1):
        print('Juega Player')
        turno=0
        contador=contador+1
        dado=lanzar()

        if(dado==5):
        	salen=2
        	c=0
        	for x in H1:
        		if(H1[c][0]==-1 and tablero[4][2] != 2 and salen !=0):
        			print(H1[c][2])
        			salen =salen-1
        		c=c+1
        	if (salen==2):
        		print('No salen fichas')
        		





    else:
        print('Juega A.I.')
        turno=1
        contador=contador+1

    if(contador==3):
        ganador=True




