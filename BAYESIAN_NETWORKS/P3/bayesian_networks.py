
#READ THE BAYESIAN NETWORK FROM A .txt FILE
with open('net_Rain_train.txt','r') as nodos:
	text=nodos.read()
lista_nodos=text.split('\n')
print('Los nodos leidos son: ', lista_nodos)


#CAPTURAR el nombre de los nodos con dependencias(head) && capturar los valores de los nodos(tail)
head_list = []
tail_list=[]

for line in lista_nodos:
	yim=line
	head=yim.split('{')
	tail=yim.split(')')
	head_list.append(head[0])
	tail_list.append(tail[1])
	
#CREAR LISTA DE DEPENDENCIAS

dependencias=[]

for word in head_list:
	a=word.replace(')', '')
	b=a.split('(')
	dependencias.append(b[1])
	

print('HEADS: ',head_list)
print('TAILS: ', tail_list)
print('DEPS : ', dependencias)


cont=0
for nodo in head_list:
	dep=dependencias[cont]
	tail=tail_list[cont]

	print('***PARA EL NODO: ', nodo)

	depend=dep.split(',')
	for DP in depend:
		if not len(DP)==0:
			DP=DP+'('
			print('FIND: ',DP)
			for x in head_list:
				print(x.find(DP))
			
	cont+=1





#SOLICITAR LAS PROPBAILIDADES :



