import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

#1.DECLARAMOS LAS VARIABLES DE ENTRADA Y SALIDA

#INPUTS
calidad_comida = ctrl.Antecedent(np.arange(0,101,1), 'calidad_comida')
servicio = ctrl.Antecedent(np.arange(0,101,1), 'servicio')
#OUTPUT
propina = ctrl.Consequent(np.arange(0,101,1), 'propina')

#2. ASIGNAMOS MEMBRESIAS:

#aUTO-MEMBERSHIP FUNCTION POPULATION

calidad_comida['desagradable']= fuzz.trimf(calidad_comida.universe, [0,0,20])
calidad_comida['mediocre']= fuzz.gaussmf(calidad_comida.universe,30,15)
calidad_comida['normal']= fuzz.gaussmf(calidad_comida.universe, 50,5.0)
calidad_comida['rica']= fuzz.trimf(calidad_comida.universe, [50,70,85])
calidad_comida['deliciosa']= fuzz.gbellmf(calidad_comida.universe, 20,70,100)

servicio['nulo']= fuzz.trimf(propina.universe, [0,0,20])
servicio['malo']= fuzz.trimf(propina.universe, [15,20,40])
servicio['normal']= fuzz.trimf(propina.universe, [30,50,60])
servicio['bueno']= fuzz.trimf(propina.universe, [50,70,85])
servicio['excelente']= fuzz.trimf(propina.universe, [75,100,100])

propina['minimo']= fuzz.trimf(propina.universe, [0,0,20])
propina['poca']= fuzz.trimf(propina.universe, [15,20,40])
propina['media']= fuzz.trimf(propina.universe, [30,50,60])
propina['moderada']= fuzz.trimf(propina.universe, [50,70,85])
propina['alta']= fuzz.trimf(propina.universe, [75,100,100])

#3. HACER LOS CONJUNTOS DE REGLAS (IF THEN)

rule1 = ctrl.Rule(calidad_comida['desagradable'] | servicio['nulo'], propina['minimo'])
rule2=ctrl.Rule(calidad_comida['mediocre'] | servicio['malo'] ,propina['poca'])
rule3= ctrl.Rule(calidad_comida['normal'] | servicio['normal'], propina['media'])
rule4=ctrl.Rule(calidad_comida['rica'] | servicio['bueno'], propina['moderada'])
rule5=ctrl.Rule(calidad_comida['deliciosa'] | servicio['excelente'], propina['alta'])

#4. DEFINIR EL CONTROL DEL SISTEMA

tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
tipping= ctrl.ControlSystemSimulation(tipping_ctrl)

# 5. DEFINIR LAS ENTRADAS NUMPERICAS PARA CADA VARIABLE DE ENTRADA
input_calidad=int(input('Inserte su puntaje para "CALIDA DE COMIDA" (1-100): '))
input_servicio=int(input('Inserte su puntaje para el "SERVICIO" (1-100): '))
tipping.input['calidad_comida']=input_calidad
tipping.input['servicio'] = input_servicio

#6. HACER LA FUZZYFICACION Y DESFUZZIFICACION DEL SISTEMA
tipping.compute()

#7. IMPRIMIR LOS RESULTADOS
output_propina= tipping.output['propina']
print('La propina apropiada sería :',output_propina)