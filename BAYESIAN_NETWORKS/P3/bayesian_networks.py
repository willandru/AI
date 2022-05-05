

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
	
print(head_list)
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


datos_cargados=False
word_dict={}
if datos_cargados:
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

		i+=1


if not datos_cargados:
	with open('probas_rain.txt','r') as f:
	    datos = f.read()
	    dic_vals= datos.split('\n')
	    for row in dic_vals:
	    	fila=row.split(':')
	    	word_dict.update({fila[0]:fila[1]})
else:
	with open("probas_rain.txt", 'w') as f: 
	    for key, value in word_dict.items(): 
	        f.write('%s:%s\n' % (key, value))


#print('Your DICTIONARY: ', word_dict)


print('\n'*4)
print('INFERENCE: ')
while(True):

	QUERY=input('?- ')
	QUERY=QUERY.replace('P(', ' ').replace(' ','').replace(')', '').split(',')
	Q=[]
	for Z in QUERY:
		Q.append(Z.split('='))
	

	A=[]
	B=[]

	for q in Q:
		A.append(q[0])
		B.append(q[1])

	

	#SABER SI TIENE VARIABLES OCULTAS O NO
	Oculta=False
	
	C=[]

	for head in A:
		No_Oculta=False
		

		#Buscar la posicion de la cabeza
		ii=0
		for x in nodes:
			
			if x==head:
				pos=ii
			ii+=1
		ab=deps[pos]

		

		for y in ab:
			#C.append(y)
			if y == '':
				
				pass
			else:
				C.append(y)
				#Buscar posicion
				jj=0
				for xx in nodes:
					
					
					if xx==y:
						
						poz=jj
					jj+=1

					
				abc=deps[poz]
				
				for z in abc:
					
					if z=='':
						pass
					else:
						C.append(z)

				
				for z in A:
					
					if z==y or y=='':
						No_Oculta=True
				
		
		
		if not No_Oculta:
			Oculta=True

	
	l4 = [x for x in C if x not in A]
	l4=list(dict.fromkeys(l4))
	print('variables ocultas: ',l4)

#LA QUERY NO TIENE VARIABLES OCULTAS:

	if not l4:
		print('La Query NO tiene variables ocultas')
	
		D=[]
		H=[]
		for busc in A:
			i=0
			for h in nodes:
				if busc==h:
					D.append(deps[i])
				i+=1
		j=0
		for proba in A:
			txt='P('+str(proba)+'='+B[j]
			#look for value of proba	
			txt_2='|'
			for depp in D[j]:
				
				if depp=='':
					txt_2=')'
				else:
					
					#look for value
					k=0
					for f in A:
						
						if depp==f:
							
							ans=str(B[k])
							txt_2+= depp+'= '+ans+' ,'
						k+=1

					#look for value of teh dependencies
			txt_2+=')'
			txt+=txt_2
			txt=txt.replace('))',')').replace(',)',')').replace(' ', '')
			
			H.append(txt)


			j+=1

		

		#GET PROBABILITIES
		Q=[]
		for i in H:
			for key, value in word_dict.items():
				if sorted(i)==sorted(key):
					Q.append(value)


		resp=1
		for i in Q:
			resp=resp*float(i)

		print('La probabilidad del evento es: ', resp)







#QUERY CON VARIABLES OCULTAS:		
	else:
		print('La Query TIENE VARIABLES OCULTAS: ')
		print('variables conocidas: ',A)
		print('Valores conocidos: ', B)
		l3 = [x for x in C if x not in A]
		l3=list(dict.fromkeys(l3))
		print('variables ocultas: ',l3)

		K=[] # PARA PONER LOS NODOS PADRES
		for head in A:
			k=0
			for pos in nodes:
				if head==pos:
					K.append(deps[k])
				k+=1

		print(K)

		#Make probas:
		l=0
		W=[]
		for proba in A:
			
			txt='P('+str(proba)+'= '+str(B[l])+'|'
			
			li=K[l]
			txt1=''

			for word in li:
				print('aca,',word)
				hidden=False
				for x in l3:
					if x==word:
						print(word,' es una OCULTA')
						hidden=True
						#FIND THE OCULT WORD VALUES
						u=0
						for w in nodes:
							if w==word:
								z_tail=tls[u]
								
								print('z-tail',z_tail)
								for z in z_tail:
									print('Z in ',z)
									txt1=str(word)+'='+str(z)+','
									W[l].append(txt1)
										
									print(txt+txt1)

							u+=1

				if not hidden:
					print(word,'NO es oculta')
					y=0
					for ind in A:
						if ind==word:
							res=B[y]
						y+=1
					txt1+=str(word)+'='+str(res)+','
					print('aca: ', txt+txt1)
			


					
			l+=1
			


			

		






