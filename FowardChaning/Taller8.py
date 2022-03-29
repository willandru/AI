########################################################################################################################
#Definición de reglas y hechos iniciales.
reglas = [['Z', '&', 'L', 'S'], ['A', '&', 'N', 'E'], ['B', '|', 'M', 'Z'], ['A', 'M'],
          ['Q', '&', '-W', '&', '-Z', 'N'], ['L', '&', 'M', 'E'], ['B', '&', 'C', 'Q']]
hechos = ['A', 'L']
cumplidas = []
# reglas representa las reglas del sistema, hechos representa la base de hechos inicial.
# y cumplidas es la lista de reglas que se van cumpliendo tras cada iteración.
print('SIMULADOR DE HECHOS Y REGLAS CON PREDICADOS')
print('Reglas Iniciales:')
for j in reglas:
    print(j)
print('Hechos iniciales:')
print(hechos)
print('-'*50)
################################################################################
# Definición de funciones.
# Busca si existe al menos un hecho presente en la regla.
def buscar():  
    for hecho in hechos:
        if hecho in regla[:-1]:
            return True
    return False

def negacion(caracter):  # Valida la negacion de un caracter.
    if caracter[0:1] == '-':  # Verifica si el primer caracter es una negacion.
        return True
    else:
        return False


################################################################################
# Inicio del programa.

iteraciones = 0 #Contador de iteraciones del sistema.
cambio = True #Inicializa el ciclo de iteraciones.

while cambio:
    iteraciones = iteraciones + 1 #Incrementa las iteraciones en 1.
    print(' ')
    print("            ITERACION N° ", iteraciones)  
    cambio = False  
    cont = 0  
    for regla in reglas:
        
        cont = cont + 1  
        cumple = False  
        
        if cont not in cumplidas: 
            if buscar():  
                print("Regla N°",cont,":", regla)  
                contchar = 0  
                rule=[]
                ruless=[]
                
                for caracter in regla[:-1]:  
                    
                    if caracter == '&':
                        ruless.append('and')
                        rule.append(caracter)                        
                    
                    elif caracter == '|':
                        rule.append(caracter)
                        ruless.append('or')

                    elif negacion(caracter):  # Se verifica si la negación es verdadera.
                        if caracter in hechos:
                            ruless.append('1')
                        else:
                            ruless.append('0')
                    else:
                        if caracter in hechos:
                            ruless.append('1')
                        else:
                            ruless.append('0')

                    
                    contchar = contchar + 1 
                
                if 'and' in ruless:
                    if '0' in ruless:
                        cumple=False
                        print('No se cumple')
                    else:
                        cumple=True

                elif 'or' in ruless:
                    if '1' in ruless:
                        cumple=True
                    else:
                        cumple=False

                elif len(ruless)==1 and ruless[0]=='1':
                    cumple=True




                if cumple:  # En caso que la regla se cumpla, se agrega el resultado a la base de hechos.
                    print("++LA REGLA SE CUMPLE++.")
                    if regla[-1] not in hechos:  # Verifica que el resultado no sea parte ya de la base de hechos.
                        hechos.append(regla[-1])  # Agrega el resultado a la base de hechos.
                        print('Los nuevos hechos son:', hechos)  # Imprime la nueva base de hechos.
                        cambio = True  # Establece que hubo un cambio, por lo tanto, habrá otra iteración.
                        cumplidas.append(cont)  # Agrega la regla actual a la lista de reglas cumplidas.
                else:
                    print("--La regla NO se cumple--")

    print("Reglas cumplidas:", cumplidas)  # Imprime las reglas que se han cumplido hasta el momento.
   