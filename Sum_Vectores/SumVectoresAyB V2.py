#Vectores - Christian Esquivel - Fisica 1

import math
import sys

MagnitudA = AnguloA = MagnitudB = AnguloB = None

def calulateResults():
	print("===Resultado===")
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
	print("Ax = " + ('%.2f' % Ax))
	print("Ay = " + ('%.2f' % Ay))
	print("Bx = " + ('%.2f' % Bx))
	print("By = " + ('%.2f' % By))
	print("Ri = " + ('%.2f' % Rx))
	print("Rj = " + ('%.2f' % Ry))
	print("|R| = " + ('%.2f' % MagnitudR) + ", Angulo: " + ('%.2f' % AnguloR))
	print("Producto Punto: " + ('%.2f' % PPunto))
	print("===============")

def getInfo():
	print("==Informacion==")
	print("|A| =\t\t" + str(MagnitudA))
	print("Angulo A =\t" + str(AnguloA))
	print("|B| =\t\t" + str(MagnitudB))
	print("Angulo B =\t" + str(AnguloB))

def execute():
	global MagnitudA
	global AnguloA
	global MagnitudB
	global AnguloB
	try:
		print("Deme los valores separados por coma y espacio (Ejemplo: 3, 38, 2.5, 38.02): ")
		MagnitudA, AnguloA, MagnitudB, AnguloB = input("-MagnitudA, -AnguloA, -MagnitudB, -AnguloB: ").split(', ')
		MagnitudA = float(MagnitudA)
		AnguloA = float(AnguloA)
		MagnitudB = float(MagnitudB)
		AnguloB = float(AnguloB)
		getInfo()
		calulateResults()
		execute()
	except:
		print("Error en el ingreso de parametros")
		execute()
execute()