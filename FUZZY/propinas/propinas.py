import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

#1. DECLARAMOS LAS VARIABLES

#VARIABLES DE ENTRADA Y VARIABLES DE SALIDA
calidad_comida = ctrl.Antecedent(np.arange(0,11,1), 'calidad_comida')
servicio = ctrl.Antecedent(np.arange(0,11,1), 'servicio')
propina = ctrl.Consequent(np.arange(0,26,1), 'tip')


#2. ASIGNAMOS MEMBRESIAS:

#aUTO-MEMBERSHIP FUNCTION POPULATION
calidad_comida.automf(5)
servicio.automf(5)

#Manually: trimf = triangular membership function

propina['low']= fuzz.trimf(propina.universe, [0,0,13])
propina['medium']= fuzz.trimf(propina.universe, [0,13,25])
propina['high']= fuzz.trimf(propina.universe, [13,25,25])

# To view the plots:

#quality['average'].view() #EL conjunto "AVERAGE" se resaltará
#service.view()
#tip.view()

#3. HACER LOS CONJUNTOS DE REGLAS (IF THEN)

rule1 = ctrl.Rule(calidad_comida['poor'] | servicio['poor'], propina['low'])
rule2=ctrl.Rule(calidad_comida['average'] ,propina['medium'])
rule3= ctrl.Rule(calidad_comida['good'] | servicio['good'], propina['high'])

#4. DEFINIR EL CONTROL DEL SISTEMA

tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])

tipping= ctrl.ControlSystemSimulation(tipping_ctrl)

# 5. DEFINIR LAS ENTRADAS NUMPERICAS PARA CADA VARIABLE DE ENTRADA
tipping.input['calidad_comida']=10
tipping.input['servicio'] = 9.8

# HACER LA FUZZYFICACION Y DESFUZZIFICACION DEL SISTEMA
tipping.compute()
# IMPRIMIR LOS RESULTADOS

print(tipping.output['propina'])
#tip.view(tipping)


