#Vectores - Christian Esquivel - Fisica 1

import math
import sys
MagnitudA = AnguloA = MagnitudB = AnguloB = None

def printMenu():
	menu = ["0. EXIT",
			"1. Definir magnitud de A",
			"2. Definir angulo de A",
			"3. Definir magnitud de B",
			"4. Definir angulo de B",
			"5. Calcular R y Producto Punto",
			"6. Ver Información"]
	print("\n---Menu Principal---\n" + "\n".join(menu))
	return;

def getInfo():
	print("|A| =\t\t" + str(MagnitudA))
	print("Angulo A =\t" + str(AnguloA))
	print("|B| =\t\t" + str(MagnitudB))
	print("Angulo B =\t" + str(AnguloB))
	execute()
	return;

def magA():
	try:
		global MagnitudA 
		MagnitudA = float(input("Deme la magnitud del vector A: "))
		print("|A| = " + str(MagnitudA))
	except:
		print("Dato Erroneo! No se asigno el valor.")
	execute()
	return;

def angA():
	try:
		global AnguloA 
		AnguloA = float(input("Deme el angulo del vector A: "))
		print("Angulo A = " + str(AnguloA))
	except:
		print("Dato Erroneo! No se asigno el valor.")
	execute()
	return;

def magB():
	try:
		global MagnitudB 
		MagnitudB = float(input("Deme la magnitud del vector B: "))
		print("|B| = " + str(MagnitudB))
	except:
		print("Dato Erroneo! No se asigno el valor.")
	execute()
	return;

def angB():
	try:
		global AnguloB
		AnguloB = float(input("Deme el angulo del vector B: "))
		print("Angulo B = " + str(AnguloB))
	except:
		print("Dato Erroneo! No se asigno el valor.")
	execute()
	return;

def calcR():
	AllGood = True

	if MagnitudA is None:
		print("La magnitud de A no se ha definido")
		AllGood = False
	if AnguloA is None:
		print("El angulo de A no se ha definido")
		AllGood = False
	if MagnitudB is None:
		print("La magnitud de B no se ha definido")
		AllGood = False
	if AnguloB is None: 
		print("El angulo de B no se ha definido")
		AllGood = False

	if AllGood:
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
	execute()
	return;

def execute():
	try:
		printMenu()
		options = {	1 : magA,
				2 : angA,
				3 : magB,
				4 : angB,
				5 : calcR,
				6 : getInfo, }
		Option = int(input("Que desea hacer?: "))
		options[Option]()
	except:
		if Option == 0:
			exit();
		print("Tecla no valida!")
		execute()
	return;
execute()