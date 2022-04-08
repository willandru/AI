import re  #libreria de expresiones regulares/compara cadenas y si son iguales

# Declaración
#KB=Base de conocimientos= reglas
#Sentencias = reglas

KB = list()
numero_sentencias = 0
listaPreguntas = list()
numPreguntas = 0

# Separa y retorna la  base de conocimientos  y preguntas
# el numero de sentencias es la cantidad de proposiciones que definen la logica del algoritmo
# la lista de preguntas son las sentencias que deseo comprobar
def leer_archivo():
    # Archivo a leer
    file = 'entrada.txt'
    archivo_de_entrada = open(file, 'r')
    lineas = archivo_de_entrada.readlines()
    #Caracter que va recorriendo todo el archivo
    line = lineas[0].strip()
    numPreguntas = int(line)
    # Se obtienen las preguntas que se van a comprobar
    # Lee el archivo y guarda todas las preguntas en la lista
    for i in range(1, numPreguntas + 1):
        listaPreguntas.append(lineas[i].strip())
    numero_sentencias = int(lineas[numPreguntas + 1])
    # Obtener las sentencias
    print('####LISTA DE PREGUNTAS#######')
    for i in listaPreguntas:
        print(i)
    print('##################')    
    # Lee el archivo y guarda todas las sentencias en la lista
    for i in range(numPreguntas + 2, numPreguntas + numero_sentencias + 2):
        KB.append(lineas[i].strip())
    archivo_de_entrada.close()
    print('####BASE DEL CONOCIMIENTO#######')
    for i in KB:
        print(i)
    print('##################')    
    # Devolver las preguntas y la base de conocimientos que se obtiene  del archivo de entrada
    return listaPreguntas, KB


# En esta función se busca retornar las sentencias negativas y positivas, esto se consigue gracias a dividir la lista en cadenas y de esas cadenas sacar los elementos que tienen el símbolo de negación, esto se guarda en un diccionario, y lo que no tiene la negación se guarda en el diccionario de sentencias_positivas


def parseKB(base_conocimiento):
    # Declaración de los diccionarios para las sentencias
    # Los diccionarios permiten almacenar los valores de una forma ordenada y que no admite duplicados
    # Se usa un diccionario para almacenar las sentencias que va encontrando positivas
    # Se usa un diccionario para almacenar las sentencias que tienen negativos

    sentencias_negativas = dict()
    sentencias_positivas = dict()
    # Se recorren los objetos que se encuentran dentro de la lista reglas
    for item in base_conocimiento:
      # Divide la lista en cadenas: Cuando encuentre en la lista el objeto que tenga el separador '|', eso lo convierte en cadena. Lo divide para generar dos secuencias distintas
        data = item.split('|')
        for i in data:
          # Reemplaza los símbolos ' ' que están en cada una de las cadenas divididas por '' para no tener ningún espacio
            i = i.replace(' ', '')
            if i[0] == '~':
                b = i[1:]
                # La variable b Guarda las reglas que encuentra negativas para que se guarden en uno de los diccionarios
                b = b.split("(")[0]
                #Se utiliza el try para agregrar un objeto a la lista de sentencias_negativas, en este caso agregar la sentencia que se encuentre negativa dentro de la lista y se verifica por medio del key si el elemento al que se intenta acceder no existe en un diccionario, si no existe, se actualiza en el diccionario el objeto que se quiere agregar
                try:
                    sentencias_negativas[b].append(item)
                except KeyError:
                    sentencias_negativas[b] = [item]
            else:
                # Guarda las sentencias que encuentra positivas, realizando el mismo proceso del try y verificando si está en un diccionario o actualizando el diccionario si no está el objeto
                i = i.split("(")[0]
                try:
                    sentencias_positivas[i].append(item)
                except KeyError:
                    sentencias_positivas[i] = [item]
    print('Sentencias Negativas: ')
    for i in sentencias_negativas:
        print(i)
    print('Sentencias Postivas: ')
    for i in sentencias_positivas:
        print(i)
    
    return sentencias_negativas, sentencias_positivas


#  las constantes de la lista de preguntas
def constantes(pregunta):
    variable = re.search('\((.*?)\)', pregunta).group(1)

    print('VARIABLE: ', variable)
    return variable


# Retorna si una sentencia tiene una variable o si no la tiene (Empieza por Mayúcula)
def comprobarMayus(KB):
    if "|" in KB:
        return False
        # Guarda en una lista constante los elementos de las sentencias, divide las sentencias hasta encontrar ",", las guarda en cadenas y comprueban con el método isupper si lo que está en cada una de las cadenas generadas está en mayúsculas. Si es así, retorna true y si no, retorna false
    const_list = re.search('\((.*?)\)', KB).group(1)
    const = const_list.split(",")
    for val in const:
        if not val[0].isupper():
            return False
    return True

#UNIFICACIÓN
# 1. Si se tiene una variable O y una variable P, al igualar ambas variables: O = P entonces son variables unificables.
# 2. Si no son unificables, se busca el símbolo más a la izquierda de O que se diferencia de su semejante en P.


def unificacion(preguntaNegacion, copia_pregunta, sentencias_positivas,
                sentencias_negativas, sentenciasVariables):
    print('UNIFICACION : ')
    print('Pregunta Negacion: ', preguntaNegacion)
    print('Copia Pregunta: ',copia_pregunta) 
    print('Sentencias Positivas: ',sentencias_positivas) 
    print('Sentencias Negativas: ',sentencias_negativas)
    print('Sentencias Variables: ',sentenciasVariables)
    if preguntaNegacion[0] != '~': # si no encuentra '~' significa que la pregunta es negativa
        para_emparejar = preguntaNegacion.split("(")[0]
        #Se utiliza el try para agregrar lo que se encuentra dentro de la variable para_emparejar que se encuentran en las sentencias_negativas, y eso guardarlo en value, si en un diccionario no existe dicho valor se actualiza el diccioanrio en este caso de sentencias_negativas y se agrega el valor 
        try:
            value = sentencias_negativas[para_emparejar]
        except KeyError:
            return False

        for sentencia in value:
            try:
                copia_pregunta_temp = copia_pregunta
                pregunta_temp = preguntaNegacion
                if sentencia in sentenciasVariables:
                    ret1, l1 = remove(copia_pregunta_temp, sentencia[1:])
                    ret2 = 1
                    l2 = ""
                else:
                    ret1, l1 = remove(copia_pregunta_temp, pregunta_temp)
                    ret2, l2 = remove(sentencia, "~" + pregunta_temp)
                    # elimina de las listas la pregunta positiva y guarda en las variables ret1 y ret 2 las preguntas negativas y su negación (positivas) 
                if ret1 == 0 or ret2 == 0:
                    continue
                else:
                  # Busca las sentencias que estén en el arreglo y empieza a guardarlas en las variables l1 o l2 y luego verifica cuantos axiomas se encuentran en la sentencia y los copia en variables
                    if l1 == '' and l2 != '':
                        copia_pregunta_temp = l2
                    elif l2 == '' and l1 != '':
                        copia_pregunta_temp = l1
                    elif l1 == '' and l2 == '':
                        copia_pregunta_temp = ''
                    else:
                        copia_pregunta_temp = l2 + " | " + l1


                    if copia_pregunta_temp == '':
                        return True
                    else:
                        if "|" in copia_pregunta_temp:
                          # Divide lo que hay en copia_pregunta_temp y cuando encuentre un "|" lo guarda en la variabla data como cadenas 
                            data = copia_pregunta_temp.split("|")
                            # i es un token que recorre el arreglo data que contiene las "preguntas" (en realidad son axiomas de la sentencia compuesta divida por el caracter "|") que estaban almacenadas en copia_pregunta_temp
                            for i in data:
                                i = i.replace(" ", "")
                                if unificacion(i, copia_pregunta_temp,
                                               sentencias_positivas,
                                               sentencias_negativas,
                                               sentenciasVariables):
                                    return True
                                else:
                                    break
                                    # si la llamada recursiva retorna false esto indica que hay un problema con el caracter "|" y se sale a seguir con el procedimiento estandar evaluando la llamada recursiva con copia_pregunta_temp como parametro principal en lugar del token i
                        else:
                            if unificacion(copia_pregunta_temp,
                                           copia_pregunta_temp,
                                           sentencias_positivas,
                                           sentencias_negativas,
                                           sentenciasVariables):
                                return True
                            else:continue
                                
            except RuntimeError as re:
                if re.args[0] == 'maximum recursion depth exceeded':
                    return False

        return False

    else:
        para_emparejar = preguntaNegacion.split("(")[0]
        #Se utiliza el try para agregrar lo que se encuentra dentro de la variable para_emparejar que se encuentran en las sentencias_negativas, y eso guardarlo en value, si en un diccionario no existe dicho valor se actualiza el diccioanrio en este caso de sentencias_positivas y se agrega el valor 
        try:
            value = sentencias_positivas[para_emparejar[1:]]
        except KeyError:
            return False
        for sentencia in value:
          
            try:
                copia_pregunta_temp = copia_pregunta
                pregunta_temp = preguntaNegacion
                if sentencia in sentenciasVariables:
                    ret_val1, l1 = remove(copia_pregunta_temp, "~" + sentencia)
                    ret_val2 = 1
                    l2 = ""
                else:
                    ret_val1, l1 = remove(copia_pregunta_temp, pregunta_temp)
                    ret_val2, l2 = remove(sentencia, pregunta_temp[1:])
                    # elimina de las listas la pregunta negativa y guarda en las variables ret1 y ret 2 las preguntas positivas 
                if ret_val1 == 0 or ret_val2 == 0:
                    continue
                else:
                  # Busca las sentencias que estén en el arreglo y empieza a guardarlas en las variables l1 o l2 y luego verifica cuantos axiomas se encuentran en la sentencia y los copia en variables
                    if l1 == '' and l2 != '':
                        copia_pregunta_temp = l2
                    elif l2 == '' and l1 != '':
                        copia_pregunta_temp = l1
                    elif l1 == '' and l2 == '':
                        copia_pregunta_temp = ''
                    else:
                        copia_pregunta_temp = l2 + " | " + l1

                    if copia_pregunta_temp == '':
                        return True
                    else:
                        if "|" in copia_pregunta_temp:
                          # Divide lo que hay en copia_pregunta_temp y cuando encuentre un "|" lo guarda en la variabla data como cadenas 
                            data = copia_pregunta_temp.split("|")
                            # i es un token que recorre el arreglo data que contiene las "preguntas" (en realidad son axiomas de la sentencia compuesta divida por el caracter "|") que estaban almacenadas en copia_pregunta_temp
                            for i in data:
                                i = i.replace(" ", "")
                                if unificacion(i, copia_pregunta_temp,
                                               sentencias_positivas,
                                               sentencias_negativas,
                                               sentenciasVariables):
                                    return True
                                else:
                                    break
                                 # si la llamada recursiva retorna false esto indica que hay un problema con el caracter "|" y se sale a seguir con el procedimiento estandar evaluando la llamada recursiva con copia_pregunta_temp como parametro principal en lugar del token i

                        else:
                            if unificacion(copia_pregunta_temp,
                                           copia_pregunta_temp,
                                           sentencias_positivas,
                                           sentencias_negativas,
                                           sentenciasVariables):
                                return True
                            else:
                                continue
            except RuntimeError as re:
                if re.args[0] == 'maximum recursion depth exceeded':
                    return False
        return False





# k = caracter o string 
# remueve una pregunta o axioma de una gran pregunta compuesta o un arreglo de preguntas individuales
def remove(k, pregunta):
    flag, newq, news = sustitucion(k, pregunta)
    if flag == 1:
        if newq in news:
            news1 = news.replace(newq, "")
        else:
            start = news.find(pregunta.split("(")[0])
            end = news.find(')', start)
            to_del = news[start:end + 1]
            news1 = news.replace(to_del, "")
        if " |  | " in news1:
            news2 = news1.replace(" |  | ", " | ")
            return 1, news2
        elif news1[:3] == " | ":
            news2 = news1[3:]
            return 1, news2
        elif news1[-3:] == " | ":
            news2 = news1[:-3]
            return 1, news2
        else:
            return 1, news1
    else:
        return 0, news


#   1. Si es el primero (predicado), entonces no son unificables.
#   2. Si es uno de los argumentos, entonces sean r1, r2 los términos en los que son distintos.
#       a) Si ninguno de los dos es una variable,entonces las cláusulas no son unificables.
#        Si uno de ellos es una variable tampoco serán unificables, está presente en las variables del otro.
#       b) Si r1 es una variable z y no está entre las variables del otro r2, entonces haremos la sustitución: p = {z/r2}
# 3. Volver al paso 1.

# Reemplaza las constantes por variables
# Sentencia: Son las proposiciones o axiomas
 
def sustitucion(sentencia, pregunta):
    predicado = pregunta.split("(")[0]
    constant = constantes(pregunta)
    cons_list = constant.split(",")
    count = 0
    data = sentencia.split("|")
    flag = 0
    #Recorrer mientras hayan axiomas
    for i in data:
        m = i.split("(")[0]
        m = m.replace(' ', '')
        if m == predicado:
            #Obtiene las variables
            __vars = re.search(r'\((.*?)\)', i).group(1)
            #var_list es una lista de variables en caso de estar separadas por coma
            var_list = __vars.split(",")
            
            #Recorre cada variable
            for j in var_list:
                if j[0].isupper() and cons_list[count][0].islower():
                    pregunta = test(cons_list[count], pregunta, j)
                    flag = 1
                    count += 1
                elif j[0].islower() and cons_list[count][0].isupper():
                    sentencia = test(j, sentencia, cons_list[count])
                    flag = 1
                    count += 1
                elif j[0].isupper() and cons_list[count][0].isupper():
                    if j == cons_list[count]:
                        pregunta = pregunta
                        sentencia = sentencia
                        flag = 1
                    else:
                        flag = 0
                        break
                    count += 1
                elif j[0].islower() and cons_list[count][0].islower():
                    if not (j == cons_list[count]):
                        sentencia = test(j, sentencia, cons_list[count])
                        pregunta = pregunta
                        flag = 1
                    else:
                        sentencia = sentencia
                        pregunta = pregunta
                        flag = 1
                    count += 1
            if flag == 1:
                break
    if flag == 0:
        return 0, pregunta, sentencia
    else:
        return 1, pregunta, sentencia


# Reemplaza en la cadena with_replace
def test(word, to_replace, with_replace):
    big_regex = re.compile(r'\b%s\b' % r'\b|\b'.join(map(re.escape, word)))
    a = big_regex.sub(with_replace, to_replace)
    return (a)


def main():
    lista_de_preguntas, sentencias = leer_archivo()
    sentencias_negativas, sentencias_positivas = parseKB(sentencias)
    sentenciasVariables = []
    for a in sentencias:
        if comprobarMayus(a):
            sentenciasVariables.append(a)
    # Negar la sentencia a probar
    for pregunta in lista_de_preguntas:
        if pregunta[0] == '~':
            # Toma la parte no negada de la consulta
            preguntaNegacion = pregunta[1:]
            if unificacion(preguntaNegacion, preguntaNegacion, sentencias_positivas,
                           sentencias_negativas, sentenciasVariables):
                print("__________________")
                print("true")
            else:
                print("__________________")
                print("false")
        else:
            preguntaNegacion = "~" + pregunta  # Niega la consulta
            if unificacion(preguntaNegacion, preguntaNegacion, sentencias_positivas,
                           sentencias_negativas, sentenciasVariables):
                print("__________________")
                print("true")
            else:
                print("__________________")
                print("false")


if __name__ == '__main__':
    main()
