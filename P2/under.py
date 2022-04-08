import re


Knowledge_Base = list()
numSentencias= 0
listaPreguntas= list()


def leer_Archivo():
	file = 'entrada.txt'
	archivo = open(file, 'r')

	print('#1 : lineas')
	lineas = archivo.readlines()
	for x in lineas:
		print(x)

	lin = lineas[0].strip()
	print('#2 lin: ', lin)
	numPreguntas = int( lin )

	for i in range(1,numPreguntas +1):
		listaPreguntas.append(lineas[i].strip())

	numSentencias= int(lineas[numPreguntas+1])


	for i in range(numPreguntas+2, numPreguntas + numSentencias +2):
		Knowledge_Base.append(lineas[i].strip())
	archivo.close()

	print('#3 listaPreguntas: ')
	for i in listaPreguntas:
		print (i)
	print('#4 KnowledgeBase: ')
	for i in Knowledge_Base:
		print (i)

	return Knowledge_Base, listaPreguntas


[Knowledge_Base, listaPreguntas]=leer_Archivo()


	
def parseKB( base_conocimiento):

	sentencias_negativas= dict()
	sentencias_positivas= dict()

	for item in base_conocimiento:
		
