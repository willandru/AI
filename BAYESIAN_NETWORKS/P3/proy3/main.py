#Imports
import copy
from decimal import Decimal

#-----------------------------------Funciones y definiciones------------------------------
Total = 1


#Agarra lo que hay en literal es decir una linea del input y la divide por splits = no | light
def dividirVariable(variable):
    variable = variable.strip()
    dividir = variable.split(' = ')
    variable = dividir[0].strip()
    valor = dividir[1].strip()
    valor = True if valor == '+' else False
    return variable, valor  #devuelve el valor una vez se divide buscando relaciones con = +

#bayesnet = lista de nodos
#ordena los nodos en orden topologico es decir(grafo acíclico dirigido)
def OrdenamientoTopologico(bayesnet):
    nodos = bayesnet.keys()
    nodosOrdenados = []

    while len(nodosOrdenados) < len(nodos):
        for nodo in nodos:
            if nodo not in nodosOrdenados and all(
                    parent in nodosOrdenados
                    for parent in bayesnet[nodo]['Padres']):
                nodosOrdenados.append(nodo)

    return nodosOrdenados  #busca un nodo que no se encuentre en la lista ordenada y que sus padres si esten en lista ordenada y de esto cumplirse lo agrega


#Retorna unicamente el nodo que fue solicitado por la consulta.
def seleccionNodos(evidence, bayesnet, nodosOrdenados):
    nodosAñadidos = set(evidence.keys())
    nodoPresente = [
        True if x in nodosAñadidos else False for x in nodosOrdenados
    ]

    while len(nodosAñadidos) != 0:
        popNode = nodosAñadidos.pop()
        for parent in bayesnet[popNode]['Padres']:
            nodosAñadidos.add(parent)
            parentIndex = nodosOrdenados.index(parent)
            nodoPresente[parentIndex] = True

    newNodosOrdenados = []
    for nodo in nodosOrdenados:
        if nodoPresente[nodosOrdenados.index(nodo)] == True:
            newNodosOrdenados.append(nodo)

    return newNodosOrdenados  #busca los nodos que coinciden con la evidencia enviada retornandolos en una lista ordenada


# Devuelve la probabilidad usando enumeración dadas las variables requeridas (vars), las variables de evidencia (e) y la red bayesiana.
def enumeracion(vars, e, redbayes):
    if len(vars) == 0:
        return 1.0

    Y = vars[0]

    if Y in e:
        result = probabilidad(Y, e, redbayes) * enumeracion(
            vars[1:], e, redbayes)
    else:
        sumProbability = []
        e2 = copy.deepcopy(e)
        for y in [True, False]:
            e2[Y] = y
            sumProbability.append(
                probabilidad(Y, e2, redbayes) *
                enumeracion(vars[1:], e2, redbayes))
        result = sum(sumProbability)
        print("Variable Oculta: " + Y)
        print('\n')
        print("Evidencia" , e2)
        print('\n')
        print("Resultado: " , result)
        print('\n')

    return result


#retorna la probabilidad de una variable dada y sus nodos padres en evidencia
def probabilidad(Y, e, redBayes):

    if redBayes[Y]['type'] == 'decision':
        return 1.0

    if len(redBayes[Y]['Padres']) == 0:
        if e[Y] == True:
            return float(redBayes[Y]['prob'])
        else:
            return 1.0 - float(redBayes[Y]['prob'])
            #Esta probabilidad funciona con la condicional desde el else. Se utiliza la funcion probabilidad que aparece en la linea 62 en la función enumeración 
    else:
        TupladePadres = tuple(e[parent] for parent in redBayes[Y]['Padres'])

        if e[Y] == True:
            return float(redBayes[Y]['condprob'][TupladePadres])
        else:
            return 1 - float(redBayes[Y]['condprob'][TupladePadres])


#Input & construccion de estructuras de datos--------------------------------

#lista de colecciones de redes de bayes
redBayes = {}
nodosOrdenados = []
#Querys: Tiene toda la lista de consultas que se dan en el archivo 
consultaCadena = []
#LEER EL ARCHIVO

filename = 'input.txt'
inputFile = open(filename)

#Construccion de consultas con el input
lineasLeidas = inputFile.readline().strip()
while lineasLeidas != '******':
    consultaCadena.append(lineasLeidas)
    lineasLeidas = inputFile.readline().strip()

#Construyendo la red bayesiana desde el input
lineasLeidas = ' '
while lineasLeidas != '':
    #Declarando lista de nodos padres
    nodoPadre = []
    # entrada del nombre de los nodos
    lineasLeidas = inputFile.readline().strip()

    nodosyPadres = lines = lineasLeidas.split(' | ')
    node = nodosyPadres[0].strip()

    if len(nodosyPadres) != 1:
        nodoPadre = nodosyPadres[1].strip().split(' ')

    redBayes[node] = {}
    redBayes[node]['Padres'] = nodoPadre
    redBayes[node]['Hijos'] = []

    #Se insertan los nodos hijos de todos los nodos padres
    for parent in nodoPadre:
        redBayes[parent]['Hijos'].append(node)

    # Entrada de las probabilidades

    if len(nodoPadre) == 0:
        lineasLeidas = inputFile.readline().strip()
        if lineasLeidas == 'decision':
            #Nodo de desicion
            redBayes[node]['type'] = 'decision'
        else:
            #Nodo con porbabilidad prioritaria
            redBayes[node]['type'] = 'normal'
            redBayes[node]['prob'] = lineasLeidas
    else:
      #Se tiene en cuenta la probabilidad para realizar este proyecto, de esta linea se pasa a la probabilidad: linea 96
        #Nodos con probabilidad condicional
        condprob = {}
        for i in range(0, pow(2, len(nodoPadre))):
            lineasLeidas = inputFile.readline().strip()
            lines = lineasLeidas.split(' ')
            prob = lines[0]
            lines = lines[1:]
            verdadero = tuple(True if x == '+' else False for x in lines)
            condprob[verdadero] = prob

        redBayes[node]['type'] = 'normal'
        redBayes[node]['condprob'] = condprob

    lineasLeidas = inputFile.readline().strip()

#-------------------------------Declaracion del archivo de salida (respuesta)----------------------------------------
outputFile = open('output.txt', 'w')

#print BayesNet
#--------------------------------Proceso inferencial de la consulta---------------------------------------------

#Aca ordenamos los nodos con ordenamiento topologico
nodosOrdenados = OrdenamientoTopologico(redBayes)

#inferencia a todas las entradas de la consulta
outputFile.write('-----------------------------------------------')
outputFile.write('\n')
outputFile.write('Probabilidades de consultas')
outputFile.write('\n')
outputFile.write('-----------------------------------------------')
outputFile.write('\n')
outputFile.write('Consultas                         Probabilidades')
outputFile.write('\n')
outputFile.write('\n')
for consulta in consultaCadena:

    consultaEvidencia = {}
    observarEvidencia = {}

    operacion = consulta[:consulta.index('(')]
    operacion = operacion.strip()

    if operacion == 'P':

        separadorDado = False
        result = 1.0

        variables = consulta[consulta.index('(') + 1:consulta.index(')')]
        orIndex = variables.index('|') if '|' in variables else -1

        #entra aca cuando la consulta y la evidencia esta dada
        #xvar esta la variable "consulta"
        #xval esta la evidencia
        if orIndex != -1:
            separadorDado = True
            dividir = variables[:variables.index(' | ')]

            xvariables = dividir.strip()
            xvariables = xvariables.split(',')
            for xvariable in xvariables:
                xvariable = xvariable.strip()
                xVar, xVal = dividirVariable(xvariable)
                consultaEvidencia[xVar] = xVal

            dividir = variables[variables.index(' | ') + 3:]
        #entra aca si solo la evidencia esta dada
        else:
            dividir = variables

        variables = dividir.strip()
        variables = variables.split(',')
        for variable in variables:
            variable = variable.strip()
            var, val = dividirVariable(variable)
            consultaEvidencia[var] = val
            observarEvidencia[var] = val

        #Calculos
        if separadorDado == True:
            #numerador calculo
            sortedNodesForNumerator = seleccionNodos(consultaEvidencia,
                                                     redBayes, nodosOrdenados)
            numerator = enumeracion(sortedNodesForNumerator, consultaEvidencia,
                                    redBayes)

            #denominador calculo
            sortedNodesForDenominator = seleccionNodos(observarEvidencia,
                                                       redBayes,
                                                       nodosOrdenados)
            denominator = enumeracion(sortedNodesForDenominator,
                                      observarEvidencia, redBayes)
            print("operación probabilidad que ocurra")
            print(numerator,' / ',denominator)
            result = numerator / denominator

        else:
            sortedNodesForQuery = seleccionNodos(observarEvidencia, redBayes,
                                                 nodosOrdenados)
            result = enumeracion(sortedNodesForQuery, observarEvidencia,
                                 redBayes)

        #imprimir toda la evidencia
        #imprimir oslo la evidencia observada

        result = Decimal(str(result + 1e-8)).quantize(Decimal('.0001'))
        #imprimir resultado
        print("PROBABILIDAD DE QUE OCURRA")
        print(result)
        print("PROBABILIDAD DE QUE NO OCURRA")
        print(1-result)
        print('\n')
        print('----------------------------')
        print('\n')
        Total = result * Total
        outputFile.write(consulta + '  --->   ')
        outputFile.write(str(result))
        outputFile.write('\n')

#-----------------------------OUTPUT FINAL--------------------------------
outputFile.write('\n')
outputFile.write('-----------------------------------------------')
outputFile.write('\n')
outputFile.write('Resultado:')
outputFile.write('\n')
outputFile.write(str(Total))
outputFile.write('\n')
outputFile.write('-----------------------------------------------')
outputFile.write('\n')
outputFile.close()
with open('output.txt', 'rb+') as finalStripFile:
  #Establece la posicion actual del archivo y el 2 significa buscar en relación con el final del archivo
    finalStripFile.seek(0, 2)
    size = finalStripFile.tell()
    finalStripFile.truncate(size - 1)
    finalStripFile.close()
print(" RED DE BAYES! ")
print("\n")
print(redBayes)