########################################################################################################################
#Definición de reglas y hechos iniciales.
reglas = [['Z', '&', 'L', 'S'], ['A', '&', 'N', 'E'], ['B', '|', 'M', 'Z'], ['A', 'M'],
          ['Q', '&', '-W', '&', '-Z', 'N'], ['L', '&', 'M', 'E'], ['B', '&', 'C', 'Q']]
hechos = ['A', 'L']
cumplidas = []
# reglas representa las reglas del sistema, hechos representa la base de hechos inicial.
# y cumplidas es la lista de reglas que se van cumpliendo tras cada iteración.
print('Hechos iniciales:', hechos)

# Definición de funciones.

def buscar():  # Busca si existe al menos un hecho presente en la regla.
    for hecho in hechos:
        if hecho in regla:
            return True
    return False

def negacion(caracter):  # Valida la negacion de un caracter.
    if caracter[0:1] == '-':  # Verifica si el primer caracter es una negacion.
        return True
    else:
        return False


def validar(caracter,pos):  # Valida la condición dada, sea una conjuncion (&), una disyuncion (|) o un caracter negado.
    if caracter == '&':
        if negacion(regla[pos - 1]) and negacion(regla[pos + 1]):  # En caso de que ambos sean negaciones.
            if validar(regla[pos - 1], pos-1) and validar(regla[pos + 1], pos+1):
                return True
            else:
                return False
        elif negacion(regla[pos - 1]) and not negacion(regla[pos + 1]):  # En caso de que el primero sea negacion y el segundo no.
            if validar(regla[pos - 1], pos-1) and regla[pos + 1] in hechos:
                return True
            else:
                return False
        elif not negacion(regla[pos - 1]) and negacion(regla[pos + 1]): # En caso de que el primero no y el segundo si.
            if regla[pos - 1] in hechos and validar(regla[pos + 1], pos+1):
                return True
            else:
                return False
        elif not negacion(regla[pos - 1]) and not negacion(regla[pos + 1]): # En caso de que ninguno esté negado.
            if regla[pos - 1] in hechos and regla[pos + 1] in hechos:
                return True
            else:
                return False
    elif caracter == '|':
        if negacion(regla[pos - 1]) and negacion(regla[pos + 1]):  # En caso de que ambos sean negaciones.
            if validar(regla[pos - 1], pos-1) or validar(regla[pos + 1], pos+1):
                return True
            else:
                return False
        elif negacion(regla[pos - 1]) and not negacion(regla[pos + 1]):  # En caso de que el primero sea negacion y el segundo no.
            if validar(regla[pos - 1], pos-1) or regla[pos + 1] in hechos:
                return True
            else:
                return False
        elif not negacion(regla[pos - 1]) and negacion(regla[pos + 1]): # En caso de que el primero no y el segundo si.
            if regla[pos - 1] in hechos or validar(regla[pos + 1], pos+1):
                return True
            else:
                return False
        elif not negacion(regla[pos - 1]) and not negacion(regla[pos + 1]): # En caso de que ninguno esté negado.
            if regla[pos - 1] in hechos or regla[pos + 1] in hechos:
                return True
            else:
                return False
    else:
        if caracter in hechos:
            return False
        else:
            return True
########################################################################################################################
# Inicio del programa.

iteraciones = 0 #Contador de iteraciones del sistema.
cambio = True #Inicializa el ciclo de iteraciones.
while cambio:
    iteraciones = iteraciones + 1 #Incrementa las iteraciones en 1.
    print()
    print("Iteracion N° ", iteraciones)  # Imprime la iteracción actual.
    cambio = False  # Por defecto, se toma que el sistema no sufre cambios.
    cont = 0  # Inicializa el contador de reglas.
    for regla in reglas:
        cont = cont + 1  # Incrementa el contador de reglas en 1.
        cumple = True  # Por defecto, se toma que todas las reglas son verdaderas.
        if cont not in cumplidas:  # Se revisa que la regla actual no se haya cumplido ya, para no re-visitarla.
            if buscar():  # Llama a la función buscar() para descartar la regla si no cumple requisitos.
                print("Regla N°",cont,":", regla)  # Imprime la regla actual.
                contchar = 0  # Inicializa el contador de caracteres.
                for caracter in regla:  # Busca conjunciones y disyunciones en la regla.
                    contchar = contchar + 1  # Incrementa el contador de caracteres en 1.
                    if caracter == '&' or caracter == '|':
                        if not validar(caracter,contchar-1):  # Si alguna de las condiciones es falsa,
                            cumple = False         # se dice que la regla no se cumple.
                    elif negacion(caracter):  # Se verifica si la negación es verdadera.
                        pos = contchar-1  # Posición del caracter negado.
                        if regla[pos-1] != '&'  and regla[pos+1] != '&': # Se verifica que no sea parte de una conjuncion.
                            if regla[pos-1] != '|' and regla[pos+1] != '|':  # Se verifica que no sea parte de una disyuncion.
                                if not validar(caracter, contchar-1): 
                                    cumple = False
                if cumple:  # En caso que la regla se cumpla, se agrega el resultado a la base de hechos.
                    print("La regla se cumple.")
                    if regla[-1] not in hechos:  # Verifica que el resultado no sea parte ya de la base de hechos.
                        hechos.append(regla[-1])  # Agrega el resultado a la base de hechos.
                        print('Los nuevos hechos son:', hechos)  # Imprime la nueva base de hechos.
                        cambio = True  # Establece que hubo un cambio, por lo tanto, habrá otra iteración.
                        cumplidas.append(cont)  # Agrega la regla actual a la lista de reglas cumplidas.
                else:
                    print("La regla no se cumple.")
    print("Reglas cumplidas:", cumplidas)  # Imprime las reglas que se han cumplido hasta el momento.
