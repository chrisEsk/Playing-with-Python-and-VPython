# > python SumVectoresAyB.py -MagnitudA 3 -AnguloA 38 -MagnitudB 2.4 -AnguloB 63

import math
import sys

MagnitudA = AnguloA = MagnitudB = AnguloB = None

# Calcula los resultados del vector R y Producto Punto
def calulateResults():
	Ax = Ay = Bx = By = Rx = Ry = MagnitudR = AnguloR = PPunto = 0.0
	Ax = MagnitudA * math.cos(math.radians(AnguloA))
	Ay = MagnitudA * math.sin(math.radians(AnguloA))
	Bx = MagnitudB * math.cos(math.radians(AnguloB))
	By = MagnitudB * math.sin(math.radians(AnguloB))
	Rx = Ax + Bx
	Ry = Ay + By
	MagnitudR = math.hypot(Rx, Ry)
	AnguloR = math.degrees(math.atan2(Ry, Rx))
	PPunto = (Ax * Bx) + (Ay * By)
	print("R = " + ('%.2f' % Rx) + "i + " + ('%.2f' % Ry) + "j")
	print("|R| = " + ('%.2f' % MagnitudR))
	print("Direccion R = " + ('%.2f' % AnguloR))
	print("Producto Punto: " + ('%.2f' % PPunto))

# Main function del script
def execute():
	global MagnitudA
	global AnguloA
	global MagnitudB
	global AnguloB
	try:
		# Busqueda de indices respectivos en sys.args
		MagnitudA_Index = (sys.argv).index("-MagnitudA")
		MagnitudB_Index = (sys.argv).index("-MagnitudB")
		AnguloA_Index = (sys.argv).index("-AnguloA")
		AnguloB_Index = (sys.argv).index("-AnguloB")
		# Asignacion de valores respectivos de vector A y B
		MagnitudA = float(sys.argv[MagnitudA_Index + 1])
		AnguloA = float(sys.argv[AnguloA_Index + 1])
		MagnitudB = float(sys.argv[MagnitudB_Index + 1])
		AnguloB = float(sys.argv[AnguloB_Index + 1])
		# Verificar que la magnitud no sea negativa
		if (MagnitudA <= 0.0) or (MagnitudB <= 0.0):
			print("Error! Se detecto una magnitud menor o igual a 0")
		else:
			calulateResults()
	except:
		print("Error en el ingreso de parametros")
		
# Llamada al main fuction
execute()
