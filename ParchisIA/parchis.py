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
	print('PRAPARANDO EL CAMINO...******')		
	for i in range(1,1+N):
		print(posicion_inicial	)
		print(i)
		print(posicion_inicial+i)
		print(tablero_fichas[int(posicion_inicial+i)])
		if( tablero_fichas[int(posicion_inicial+i)]==1 and tablero_tipo[int(posicion_inicial+i)]==2 and tablero_seguros[int(posicion_inicial+i)]!=1):
			enemy_posicion=int(posicion_inicial+i)
			uid=buscarEnemy(enemy_posicion) #ID de la ficha del enemigo
			fichas_posicion_IA[uid]= -1
			tablero_tipo[enemy_posicion]=0
			print('RIVAL COMIDO******')						 #ACA SE PONE LA FICHA DEL ENEMIGO EN LA CARCEL , SE UBICA LA NUESTRA
		elif(tablero_fichas[int(posicion_inicial+i)]==2):
			barrera_posicion=int(posicion_inicial+i)
			barrera=True
			torres=int(posicion_inicial+i)
			print('BARRERA ENCONTRADA******')		
	return barrera

def moverP1(N):
	h=heuristicaP1()
	z=h[0] #ID
	w=h[1]
	
	posicion_inicial=int(fichas_posicion_P1[z])
	barrera=False
	if posicion_inicial !=-1:
		barrera=prepararCaminoP1(N,posicion_inicial) #Se mandan a la carcel y se buscan barreras

	if barrera:
		moverA= torres - posicion_inicial
		moverB= (posicion_inicial+N)- torres
		
		tablero_fichas[int(fichas_posicion_P1[z])]-=1
		tablero_fichas[int(fichas_posicion_P1[w])]-=1

		tablero_tipo[int(fichas_posicion_P1[z])]=0
		tablero_tipo[int(fichas_posicion_P1[w])]=0

		fichas_posicion_P1[z]+=moverA
		fichas_posicion_P1[w]+=moverB

		tablero_tipo[int(fichas_posicion_P1[z])]=1
		tablero_tipo[int(fichas_posicion_P1[w])]=1
	else:
		print('Moviendo:')
		print(N)
		tablero_fichas[int(fichas_posicion_P1[z])]-=1
		tablero_fichas[int(fichas_posicion_P1[z])+N]+=1
		tablero_tipo[int(fichas_posicion_P1[z])]=0
		fichas_posicion_P1[z]+=N
		tablero_tipo[int(fichas_posicion_P1[z])]=1

	

def noHayFichasAfuera():
	todosEnCasa=False
	for x in fichas_posicion_P1:
		if(fichas_posicion_P1.sum()==-4):
			todosEnCasa=True
	return todosEnCasa


ganador=False
turno=1
contador=0
while(not ganador):
    if(turno==1):
        print(tablero_fichas)
        print('Juega Player')
        turno=0
        contador=contador+1
        dado=lanzar()
        print(dado)
        todosEnCasa=noHayFichasAfuera()


        if(dado==5):
        	print('SALE UN CINCO*****')
        	salen=2
        	c=0
        	for x in fichas_posicion_P1:
        		if(fichas_posicion_P1[c]==-1 and (tablero_fichas[4]!=2) and salen !=0):
        			print(fichas_posicion_P1[c])
        			salen =salen-1
        			fichas_posicion_P1[c]=4
        			tablero_fichas[4]+=1
        		c=c+1
        	if (salen==2):
        		print('No salen fichas')
        		moverP1(5)

        	
        elif dado==6 and not todosEnCasa:
        	print('Sale un SEIS******')

        else:
        	if not todosEnCasa:
        		print('HOLA MUNDO')
        		moverP1(dado)
        	
        		#print(H1)
        print(tablero_fichas)
    else:
        print('Juega A.I.')
        turno=1
        contador=contador+1

    if(contador==55):
        ganador=True

print(tablero_fichas)
	
			
		







			


	







