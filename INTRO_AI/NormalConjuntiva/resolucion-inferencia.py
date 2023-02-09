def unificar(vec, pi):
    
    #BUSCAR EN "BK"
    print('PARA UNIFICAR: ', vec)
    #Para buscar en BK, buscamos el sustantivo opuesto de la lista por resolver
    palabra=''
    if pi[0][0]=='¬':
        palabra=pi[0][1:]
        
    else:
        palabra='¬'+pi[0][:]
        
    dicti ={}
    cont=0
    
    #Hacemos el diccionario
    p=pi[1:]
    #p.pop(0)
    for x in vec:
        for y in x:
            if y== palabra:
                t=x[1:]
                for j in t:
                    dicti[p[cont]]=j
                    cont+=1


    #print('DICTIONARY: ', dicti)

    #UNIFICAR

    #print('Unificar el diccionario con input vec')
    pos_regla=0
    new_vec=[]
    pos_r=0
    #print('******', vec)
    for x in vec:
        new_vec.append([])
        for y in x:
            #print('Esto es Y:', y)
            temp=y
            if y[0].isupper():
                for key, value in dicti.items():
                    #print('Key ... ', key, 'Valuee .... ', value, 'Y... ', y)
                    if y==value:
                        #print('Holi')
                        #print('Go in: y:', y)
                        temp=y.replace(y,key)
                        #print('temp', temp)
                        #print('Goin out: y:', y)
            new_vec[pos_r].append(temp)
        pos_r+=1
    #print('******', new_vec)

    return new_vec
    


   
def resolver(uni):
    #print('Resolviendo ...')

    pos_sus=0
    #a y b, son para poner las posiciones de los elementos a eliminar
    a=-5
    b=-5  

    # Se toma 1 sustantivo y se compara con los demas sustantivos, para encontrar los contrarios
    for regla in uni:
        sustantivo=regla[0]
        pos_com=0
        for buscar in uni:
            comparar=buscar[0]
            
            if sustantivo[0]=='¬':
                x=sustantivo[1:]
                if x== comparar:
                    a=pos_sus
                    b=pos_com
                    break
            else:
                x=comparar[1:]
                if sustantivo==x:
                    a=pos_sus
                    b=pos_com
                    break
            pos_com+=1

        pos_sus+=1
        
    #Si se encontraron dos sustantivos opuestos, se eliminan de la lista por resolver
    if a >=0 and b>=0 and (uni[a][1:] == uni[b][1:]) :
        uni.pop(a)
        uni.pop(b)
        #print('ACA SE DEVUELVE:' , uni)
        print('TRUE')
        return uni
    else:
        #print('ACA SE DEVUELVE:' ,  uni)
        print('FALSE')
        return []














#Open and Read txt file
with open("forma_normal_conjuntiva.txt", "r") as datos:
    text=datos.read()
lista= text.split('\n')
#Impirmir la base de conocimiento KB:
for i in lista:
    print(i)
print('-'*25)


#Guardamos cada hecho de la regla que estan separados por "|"
a=[]
for x in lista:
   a.append(x.split('|'))
print('A: ', a)

#Guardamos cada uno de los hechos en una lista de listas
b=[]
for x in a:
    i=0
    c=[]
    for y in x:
        c.append([])
        c[i].append(y)
        i+=1
    b.append(c)

print('B: ',b)

#Guardamos, los sustantivos y los atomos de cada lista
F=[]

for x in b:
    i=0
    E=[]
    for y in x:
        E.append([])
        yas=y[0].replace('(',',')
        yas=yas.replace(')','')
        E[i].append(yas.split(','))
        i+=1
    F.append(E)
print('F:', F)


#INICIO DEL MAIN LOOP
go=True

while(go):
    #INSERT YOUR QUERY
    q=input('?- ')
    query=q
    query=query.replace(')','')
    query=query.replace('(',',')
    pregunta=query.split(',')

    predicado=pregunta[0]
    atomos=pregunta[1:]

    negar_pregunta='¬'+q

    pregunta_negada=[]
    x= negar_pregunta.replace('(',',')
    x=x.replace(')','')
    x=x.split(',')
    
    #AGREGAR LA PREGUNTA NEGADA A LA LISTA DE HECHOS POR RESOLVER
    pregunta_negada+=x
    
    por_resolver=[pregunta_negada]


    
    #MIENTRAS QUE HAYAN HECHOS POR RESOLVER
    while(por_resolver):
        para_unificar=''
        pi=''
        sustantivo=''
        for pi in por_resolver:
            #DEBEMOS BUSCAR EL SUSTANTIVO CONTRARIO EN LA "KB"
            if pi[0][0]=='¬':
                sustantivo=pi[0][1:]
            else:
                sustantivo='¬'+pi[0]
            #BUSCAR EL SUSTANTIVO EN LA "KB"
            for buscar in F:
                for x in buscar:
                    for y in x:
                        for z in y:
                            if z==sustantivo:
                                para_unificar= buscar
            #ENCONTRAMOS LA REGLA EN "KB" QUE PODEMOS UNIFICAR Y RESOLVER
            extracting=[]
            for x in para_unificar:
                for y in x:
                    extracting.append(y)
            
            #UNIFICAMOS LO QUE EXTRAJIMOS DE LA "KB" + LO QUE TENÍAMOS POR RESOLVER
            to_unificar=extracting+por_resolver


            #UNIFICAR
            vec= unificar(to_unificar, pi)
            #RESOLVER
            por_resolver=resolver(vec)

            #DESPUES DE RESUELTO, CORTAMOS PARA INICIAR DE NUEVO LA BUSQUEDA EN LA "KB"
            

            break



        


               

