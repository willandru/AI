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

torres=0
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

def buscarEnemy(N):
	for i in range(0,4):
		if(fichas_posicion_IA[i]==N):
			return i

def prepararCaminoP1(N,j):
	barrera=False
	posicion_inicial=j
	print(N)
	print(j)
	for i in range(1,1+N):
		if( tablero_fichas[posicion_inicial+i]==1 and tablero_tipo[posicion_inicial+i]==2 and tablero_seguros[posicion_inicial+i]!=1):
			enemy_posicion=posicion_inicial+i
			uid=buscarEnemy(enemy_posicion) #ID de la ficha del enemigo
			fichas_posicion_IA[uid]= -1
			tablero_tipo[enemy_posicion]=0						 #ACA SE PONE LA FICHA DEL ENEMIGO EN LA CARCEL , SE UBICA LA NUESTRA
		elif(tablero_fichas[posicion_inicial+i]==2):
			barrera_posicion=posicion_inicial+i
			barrera=True
			torres=posicion_inicial+i
	return barrera

def moverP1(N):
	h=heuristicaP1()
	z=h[0] #ID
	w=h[1]
	
	posicion_id=fichas_posicion_P1[z]
	


	barrera=prepararCaminoP1(N,posicion_inicial) #Se mandan a la carcel y se buscan barreras
	if barrera:
		moverA= torres - posicion_inicial
		moverB= (posicion_inicial+N)- torres
		
		tablero_fichas[fichas_posicion_P1[z]]-=1
		tablero_fichas[fichas_posicion_P1[w]]-=1

		tablero_tipo[fichas_posicion_P1[z]]=0
		tablero_tipo[fichas_posicion_P1[w]]=0

		fichas_posicion_P1[z]+=moverA
		fichas_posicion_P1[w]+=moverB

		tablero_tipo[fichas_posicion_P1[z]]=1
		tablero_tipo[fichas_posicion_P1[w]]=1
	else:
		print('Moviendo:')
		print(N)
		tablero_fichas[fichas_posicion_P1[z]]-=1
		tablero_tipo[fichas_posicion_P1[z]]=0
		fichas_posicion_P1[z]+=N
		tablero_tipo[fichas_posicion_P1[z]]=1

	

def noHayFichasAfuera():
	todosEnCasa=False
	for x in fichas_posicion_P1:
		if(fichas_posicion_P1.sum()==-4)
			todosEnCasa=True
	return todosEnCasa


ganador=False
turno=1
contador=0
while(not ganador):
    if(turno==1):
    	enCarcel=noHayFichasAfuera()
        print('Juega Player')
        turno=0
        contador=contador+1
        dado=lanzar()


        if(dado==5):
        	if enCarcel:
        		
        	print('SALE UN CINCO*****')
        elif dado==6:
        	print('Sale un SEIS******')

        else:
        	moverP1(dado)
        	
        		#print(H1)
    else:
        print('Juega A.I.')
        turno=1
        contador=contador+1

    if(contador==5):
        ganador=True

print(tablero_fichas)
	
			
		







			


	








