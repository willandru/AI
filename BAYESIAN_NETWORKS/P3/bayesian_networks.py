
#READ THE BAYESIAN NETWORK FROM A .txt FILE
with open('net_Rain_train.txt','r') as nodos:
	text=nodos.read()
lista_nodos=text.split('\n')
print('Los nodos leidos son: ', lista_nodos)


#CAPTURAR el nombre de los nodos con dependencias(head) && capturar los valores de los nodos(tail)
head_list = []
tail_list=[]
predicate=[]

for line in lista_nodos:
	yim=line
	head=yim.split('{')
	predicate.append(yim.split('('))
	tail=yim.split(')')
	head_list.append(head[0])
	tail_list.append(tail[1])
	
#CREAR LISTA DE DEPENDENCIAS

dependencias=[]

for word in head_list:
	a=word.replace(')', '')
	b=a.split('(')
	dependencias.append(b[1])
	

#PREPARAR LAS LISTAS

tls=[]
for j in tail_list:
	j=j.replace('{','').replace('}','').split(',')
	tls.append(j)
deps=[]
for i in dependencias:
	deps.append(i.split(','))
nodes=[]
for x in predicate:
	nodes.append(x[0])

print('nodes: ', nodes)
print('deps: ', deps)
print('values: ', tls)



#SOLICITAR LAS PROPBAILIDADES :

i=0
for tabla in nodes:
	print('-'*90)
	print('TABLA DE PROBABILIDAD PARA :' , tabla)

	for probabilidades in tls[i]:
		print(probabilidades)
		txt_0=str(probabilidades)
		txt_1=str(tabla)
		txt_2=''
		for D in deps[i]:
			if D=='' and len(deps[i])== 1:
				txt_2+=' and'+str(D)+'='
				print('P('+txt_1+'='+txt_0+')')
				print()
			elif D !='' and len(deps[i])== 1:

				print('Hola')
			else:
				print('Mundo')
				txt_2+=' and'+str(D)+'='
				given=txt_2[4:]
				print('P('+txt_1+'='+txt_0+'|'+given+')')
		
		

		#SEARCH FOR DEPENDENCIE IN NODE TO GET ITS POSITION

		print()

		


			 



	i+=1
