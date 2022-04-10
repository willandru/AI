
LIBRERIAS REQUERIDAS:
pip install -U scikit-fuzzy

PARA PROBAR EL PROGRAMA:
python propinas.py


EXPLICACION

Se utilizó la libreria de python sckit-fuzzy, la cual contiene todas las funciones necesarias para realziar un sistema difuso.

#1 Declarando las variables de entrada y de salida:
Utilizando el módulo control de esta libreria, es posible indicar cuales son las variables de entrada y cuales son las variables de salida del sistema, así como indicar el rango de cada variable

#2. ASIGNAMOS MEMBRESIAS: Aplicar funciones de pertenencia y determinar el grado de pertenencia para cada valor
Aqui utilizamos la libreria menicionada para hacer uso de funciones como trimf(x, [a,b,c]), gaussmf(x, mean , standar_deviation). Así mismo se determinan los conjuntos difusos para cada variable

#3. HACER LOS CONJUNTOS DE REGLAS (IF THEN): Basado en la matriz de reglas y en la relacion logica de las variables lingüisticas.

#4 Se genera el modelo del sistema con las reglas elaboradas antes.

#5 Se solicita al usuario que ingrese el input de las variables

#6 Se hace la fuzzificacion del input y luego se hace la defuzzificacion del Output.

#7 Se imprime el resultado