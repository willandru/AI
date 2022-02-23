import numpy as np
import random


def llenarSegurosEnTablero():
	for x in range(0,68):
		if (x==4 or x==11 or x==16 or x==21 or x==28 or x==33 or x==38 or x==45 or x==50 or x==55 or x==62 or x==67 ):
			tablero_seguros[x]=1
	print(tablero_seguros)

tablero_fichas= np.zeros(68)
tablero_tipo= np.zeros(68)
tablero_seguros= np.zeros(68)
llenarSegurosEnTablero()

fichas_posicion_P1= np.ones(4)*-1
fichas_posicion_IA= np.ones(4)*-1

fichas_a_mover_P1= np.array([(0,0),(1,0),(2,0),(3,0)])
fichas_a_mover_IA= np.array([(0,0),(1,0),(2,0),(3,0)])

#fichas_posicion_P1[2]=5

def lanzar():
    return random.randint(1,6)

def heuristicaP1():
	contador=0
	for x in range(0,4):
		fin=67
		inicio=fichas_posicion_P1[x]
		distancia= fin-inicio
		fichas_a_mover_P1[contador][1]=distancia
		contador+=1
	#print(fichas_a_mover_P1)
	h= fichas_a_mover_P1[:,1].argsort()
	#print(h)
	return h

#heuristicaP1()

def comerAI():
	pass

def moverP1(N):
	h=heuristicaP1()
	z=h[0] #ID

	posicion_inicial=fichas_posicion_P1[z]

	for i in range(1,1+N):
		if( tablero_fichas[posicion_inicial+i]==1 and tablero_fichas[posicion_inicial+i]==2 ):
			comerAI()
			tablero_fichas[posicion_inicial+i-1]-=1
			tablero_fichas[posicion_inicial+i]+=1



	








