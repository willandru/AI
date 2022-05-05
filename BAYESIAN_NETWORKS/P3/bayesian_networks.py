

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

word_dict={}

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
				ult='P('+txt_1+'='+txt_0+')'
				ult=ult.replace(' ','')
				p00=input(ult+':')
				word_dict.update({ult:p00 })
				
			elif D !='' and len(deps[i])== 1:
				txt_2+=str(D)+'='
				given=txt_2
				
				to_find.append(str(D))

				
				u=0
				for buscar in nodes:
					if buscar==to_find[0]:
						for F in tls[u]:
							fin='P('+txt_1+'='+txt_0+'|'+given+''+F+')'
							fin=fin.replace(' ','')
							p01=input(fin+':')
							word_dict.update({fin:p01})
					u+=1


			else:
				if j==0:
					txt_2+=str(D)+'='
					to_find.append(str(D))
				else:
					txt_2+=','+str(D)+'='
					to_find.append(str(D))
					given=txt_2
					
				
			j+=1
		v=[]
		if len(deps[i])>1:
						
			for word in to_find:
				u=0
				for buscar in nodes:
					if word.replace(' ','') == buscar.replace(' ',''):
						pos=u
						
						break

					u+=1
				v.append(pos)

			
			combine_lists=[]
			for pos in v:
				combine_lists.append(tls[pos])
			alfa=len(combine_lists)
			
			
			#Make vector BETA
			beta=[]
			size_probas=1

			for tl in combine_lists:
				n=len(tl)
				size_probas=size_probas*n
				l=list(range(n))
				beta.append(l)
			
			#Make Probas:
			probas=[]

			
			for z in beta[0]:
				for j in beta[1]:
					x=[z,j]
					probas.append(x)
			

			if len(deps[i])==2:
				for X in probas:
					z=v[0]
					j=v[1]
					word_1=str(tls[z][X[0]])
					word_2= str(tls[j][X[1]])
					a=given.split(',')
					t_1=str(a[0])
					t_2=str(a[1])
					final_txt=t_1+word_1+','+t_2+word_2
					final='P('+txt_1+'='+txt_0+'|'+final_txt+')'
					final=final.replace(' ','')
					p02=input(final+':')
					word_dict.update({final:p02})
			

			# Make the combinations from 2-n
			P=[]
			t=0
			got_it=False

			continua=True

			for x in range(alfa):
				
				if P:
					probas=P
					P=[]
				
				if x>1:
					m=len(beta[x])
					for value in beta[x]:
						for pp in probas:
							k=[]
							for y in pp:
								k.append(y)
							k.append(value)
							P.append(k)

			if len(P)== size_probas:
				for p in P:
					traslate=[]
					TAILS=[]
					for h in v:
						TAILS.append(tls[h])
					k=[]
					o=0
					for pos in p:
						k.append(TAILS[o][pos])
						o+=1
					len_ans=len(k)
					TXT=''
					for w in range(len_ans):
						TEMP=str(to_find[w])+'='+str(k[w])
						TXT+=',' +TEMP
					TXT=TXT[1:]

					fT='P('+txt_1+'='+txt_0+'|'+TXT+')'
					ff=fT.replace(' ','')
					p03=input(ff+':')
					word_dict.update({ff:p03})
						


					
		
		

			





		

		#SEARCH FOR DEPENDENCIE IN NODE TO GET ITS POSITION



		


			 



	i+=1


print(word_dict)
