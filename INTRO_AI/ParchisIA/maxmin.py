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

 ##FICHAS PLAYER
H1=np.array([(-1,0,0),(-1,0,1),(-1,0,2),(-1,0,3)])#[posicion,bloueada,ID]

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
	print(h)
	return h;

def mover(N):
	h=heuristicaPlayer()
	ficha=h[0][2]
	pi=H1[ficha][0] #pi=poscion inicial 
	for i in range(0,N):
		tablero[pi]=i
		print(H1)

	
	
	#print(H1)


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
        	print('SALE UN CINCO')
        	salen=2
        	c=0
        	for x in H1:
        		if(H1[c][0]==-1 and (tablero[4][0]!=2 or tablero[4][1]!=2) and (tablero[4][0]!=1 and tablero[4][1]!=1) and salen !=0):
        			print(H1[c][2])
        			salen =salen-1
        			H1[c][0]=4
        			tablero[4][0]+=1
        		c=c+1
        	if (salen==2):
        		print('No salen fichas')
        		mover(5)
        		#print(H1)
    else:
        print('Juega A.I.')
        turno=1
        contador=contador+1

    if(contador==50):
        ganador=True

print(tablero)




