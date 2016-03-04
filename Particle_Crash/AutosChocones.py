# .__          __ .          ,          .___                 .
# [__) _ ._.  /  `|_ ._.* __-+-* _.._   [__  __ _.. .*.  , _ |
# |   (_)[    \__.[ )[  |_)  | |(_][ )  [____) (_](_|| \/ (/,|
#                                                |            
# Fisica 1 - Universidad Cenfotec
# Este script simula el movimiento de 2 particulas y determina la colision de una con la otra basandose en
# ecuaciones de movimiento rectilineo con aceleracion constante

from visual import *
import math

#### Modificar estas Variables #######
Initial_Position_Ball_1 = -100
Initial_Velocity_Ball_1 = 15
Acceleration_Ball_1 = 0

Initial_Position_Ball_2 = -50
Initial_Velocity_Ball_2 = 0
Acceleration_Ball_2 = 2
#######################################

# Cambiando display settings: 
scene = display(title='Paticle Crash!', x=0, y=0, width=900, height=550, center=(0, 0, 0), background=color.gray(0.2))

# Radio de las esferas:
sphere_Radius = 15

# Se definen vectores de posiciones iniciales de las bolas:
initial_pos_ball_1 = (Initial_Position_Ball_1, 0, 0)
initial_pos_ball_2 = (Initial_Position_Ball_2, 0, 0)

# Caracteristicas de bola 1:
ball1 = sphere(pos=initial_pos_ball_1, radius=sphere_Radius, color=color.cyan, material=materials.marble)
ball1.velocity = vector(Initial_Velocity_Ball_1, 0, 0)
ball1.acceleration = vector(Acceleration_Ball_1, 0, 0)

# Caracteristicas de bola 2:
ball2 = sphere(pos=initial_pos_ball_2, radius=sphere_Radius, color=color.red, material=materials.marble)
ball2.velocity = vector(Initial_Velocity_Ball_2, 0, 0)
ball2.acceleration = vector(Acceleration_Ball_2, 0, 0)

# Ecuaciones para calcular determinante:
a = 0.5 * Acceleration_Ball_1 - 0.5 * Acceleration_Ball_2
b = Initial_Velocity_Ball_1 - Initial_Velocity_Ball_2
c = Initial_Position_Ball_1 - Initial_Position_Ball_2

discriminant = (b * b) - (4 * a * c)
doubleColisionDetected = false
point_of_impact_2 = -9000

# Si el determinante es mayor o igual a 0, se calcula la cuadratica para sacar los tiempos de choque:
if discriminant < 0:
	label_Info = label(pos=(0, 5, 0), text='No collision detected!', color=color.green)
	time = 8.0
	point_of_impact = -9000
	print 'No point of impact.'
else:
	t1 = (-b + math.sqrt(discriminant)) / (2 * a) 
	t2 = (-b - math.sqrt(discriminant)) / (2 * a)
	if t1 > 0:
		time = t1
		if t2 > 0:
			# Doble colision!
			doubleColisionDetected = true
			point_of_impact_2 = Initial_Position_Ball_1 + Initial_Velocity_Ball_1 * t2 + 0.5 * Acceleration_Ball_1 * t2 * t2	
			pointer = arrow(pos=(point_of_impact_2, 60, 0), axis=(0, -40, 0), shaftwidth=10, color=color.yellow)
	else:
		if t2 > 0 :
			time = t2
	# Calculo del punto de impacto e impresion de informacion util
	point_of_impact = Initial_Position_Ball_1 + Initial_Velocity_Ball_1 * time + 0.5 * Acceleration_Ball_1 * time * time
	print 'Crash detected! Time of colision: ' + str('%.2f' % time)  + 's'
	print 'Point of Impact: ' + str('%.2f' % point_of_impact) + 'm'
	if doubleColisionDetected: 
		print 'Second Crash detected! Time of Second colision: ' + str('%.2f' % t2)  + 's'
		print 'Second Point of Impact: ' + str('%.2f' % point_of_impact_2) + 'm'
		label_Impact = label(pos=(point_of_impact, -40, 0), text=str('First Impact: ' + '%.2f' % point_of_impact + 'm\nTime of First Impact: ' + str('%.2f' % time) + 's\nSecond Impact: ' + '%.2f' % point_of_impact_2 + 'm\nTime of Second Impact: ' + str('%.2f' % t2) + 's'), color=color.green)
	else:
		label_Impact = label(pos=(point_of_impact, -40, 0), text=str('Impact: ' + '%.2f' % point_of_impact + 'm\nTime of Impact: ' + str('%.2f' % time) + 's'), color=color.green)
	pointer = arrow(pos=(point_of_impact, 60, 0), axis=(0, -40, 0), shaftwidth=10, color=color.yellow)

# Informacion de los labels y arrows
info_ball_1 = 'X1: ' + str(Initial_Position_Ball_1) + 'm'
info_ball_2 = 'X2: ' + str(Initial_Position_Ball_2) + 'm'
 
label_Info = label(pos=(Initial_Position_Ball_1, 60, 0), text=info_ball_1, color=color.green)
label_Info = label(pos=(Initial_Position_Ball_2, 60, 0), text=info_ball_2, color=color.green)

pointer = arrow(pos=(Initial_Position_Ball_1, 50, 0), axis=(0, -30, 0), shaftwidth=10, color=color.cyan)
pointer = arrow(pos=(Initial_Position_Ball_2, 50, 0), axis=(0, -30, 0), shaftwidth=10, color=color.red)

cache_ball1 = sphere(pos=initial_pos_ball_1, radius=0, color=color.yellow)
cache_ball2 = sphere(pos=initial_pos_ball_2, radius=0, color=color.yellow)

# Simulacion de movimiento
deltaT = 0.005
t = 0
while t <= 3 * time:
    rate(500)
    ball1.pos = cache_ball1.pos + ball1.velocity * t + (0.5) * ball1.acceleration * t * t
    ball2.pos = cache_ball2.pos + ball2.velocity * t + (0.5) * ball2.acceleration * t * t
    if round(ball1.pos[0], 0) == round(point_of_impact, 0) or round(ball1.pos[0], 0) == round(point_of_impact_2, 0):
    	rate(5)
    	ball1.color = color.yellow
    	ball2.color = color.yellow
    else: 
    	ball1.color = color.cyan
    	ball2.color = color.red
    t += deltaT