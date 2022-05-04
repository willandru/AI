

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
		#print(probabilidades)
		txt_0=str(probabilidades)
		txt_1=str(tabla)
		txt_2=''
		j=0
		to_find=[]
		for D in deps[i]:
			if D=='' and len(deps[i])== 1:
				txt_2+=' and'+str(D)+'='
				print('P('+txt_1+'='+txt_0+')')
				
			elif D !='' and len(deps[i])== 1:
				txt_2+=str(D)+'='
				given=txt_2
				
				to_find.append(str(D))

				
				u=0
				for buscar in nodes:
					if buscar==to_find[0]:
						for F in tls[u]:
							print('P('+txt_1+'='+txt_0+'|'+given+''+F+')')
					u+=1


			else:
				print('Mundo')
				if j==0:
					txt_2+=str(D)+'='
					to_find.append(str(D))
				else:
					txt_2+=' and '+str(D)+'='
					to_find.append(str(D))
					given=txt_2
					
				
			j+=1
		v=[]
		if len(deps[i])>1:
			print(to_find)
			print('P('+txt_1+'='+txt_0+'|'+given+')')			
			
			for word in to_find:
				u=0
				for buscar in nodes:
				

					if word.replace(' ','') == buscar.replace(' ',''):
						pos=u
						
						break

					u+=1
				v.append(pos)

			print('Same: ', v)
			combine_lists=[]
			for pos in v:
				combine_lists.append(tls[pos])
			alfa=len(combine_lists)
			print('Combined LIst: ', combine_lists)
			print('alfa: ', alfa)
			
			#Make vector BETA
			beta=[]
			size_probas=1

			for tl in combine_lists:
				n=len(tl)
				size_probas=size_probas*n
				l=list(range(n))
				beta.append(l)
			print(beta)

			#Make Probas:
			probas=[]

			print(size_probas)

			for i in beta[0]:
				for j in beta[1]:
					x=[i,j]
					probas.append(x)
			print(probas)

			# Make the combinations from 2-n
			P=[]
			t=0
			for x in range(alfa):
				if x>1:
					print('betax ',beta[x])
					m=len(beta[x])
					print('M: ', m)
					if P:
						probas=P
					print('PORBAS:', probas)
					print('MI VECTOR: ', P)
					for value in beta[x]:
						print('que value es:', value)
						
						
						for pp in probas:
							k=[]
							print('k:', k)
							print('esto es pp:', pp)
							print(pp, value)
							for i in pp:
								print(i)
								k.append(i)
							k.append(value)
							print('k:', k)
							print(k)
							P.append(k)
					
							
							
			print(P)
						


					
		
		

			





		

		#SEARCH FOR DEPENDENCIE IN NODE TO GET ITS POSITION



		


			 



	i+=1
