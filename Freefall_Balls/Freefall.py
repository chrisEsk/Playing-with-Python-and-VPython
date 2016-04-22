
# .__          __ .          ,          .___                 .
# [__) _ ._.  /  `|_ ._.* __-+-* _.._   [__  __ _.. .*.  , _ |
# |   (_)[    \__.[ )[  |_)  | |(_][ )  [____) (_](_|| \/ (/,|
#                                                |            

from visual import *
import math

# Bola Izquierda:
Initial_Position_Y_Ball_1 = 10
# Bola Derecha:
Initial_Position_Y_Ball_2 = 6

#Label
label_Info = label(pos=(0, -3, 0), text=':', color=color.green)
label_t_Actual = label(pos=(0, -6, 0), text='T actual', color=color.green, border= 10, radius=10)

#Radio de las esferas:
sphere_Radius = 0.5

#Acelaracion de las bolas:
gravity = -9.8

#Piso:
wallR = box(pos=(0,0 - sphere_Radius,0), size=(6,0.2,8), color=color.yellow, material=materials.bricks)

#Se definen vectores de posiciones iniciales de las bolas:
initial_pos_ball_1 = (-1, Initial_Position_Y_Ball_1, 0)
initial_pos_ball_2 = (2, Initial_Position_Y_Ball_2, 0)

#Caracteristicas de bola 1:
ball1 = sphere(pos=initial_pos_ball_1, radius=sphere_Radius, color=color.cyan, material=materials.marble)
ball1.velocity = vector(0, 0, 0)
ball1.aceleracion = vector(0, gravity, 0)

#Caracteristicas de bola 2:
ball2 = sphere(pos=initial_pos_ball_2, radius=sphere_Radius, color=color.red, material=materials.marble)
ball2.aceleracion = vector(0, gravity, 0)

time = math.sqrt(2 * (0- float(Initial_Position_Y_Ball_1)) / gravity )

#Asignar velocidad de bola 2 
ball2Velocity = (0 - Initial_Position_Y_Ball_2 - 0.5 * gravity * (math.pow(time, 2))) / (float(time))
ball2.velocity = vector(0, ball2Velocity, 0)

label_Info.text = 'T caida: ' + str('%.2f' % time) + 's\nV: ' + str('%.3f' % ball2.velocity[1])

#Hack para utilizar en ecuaciones de movimiento:
cache_ball1 = sphere(pos=initial_pos_ball_1, radius=0, color=color.red)
cache_ball2 = sphere(pos=initial_pos_ball_2, radius=0, color=color.red)

deltaT = 0.005
t = 0
while t <= time:
    rate(100)
    ball1.pos = cache_ball1.pos + ball1.velocity * t + (0.5) * ball1.aceleracion * t * t
    ball2.pos = cache_ball2.pos + ball2.velocity * t + (0.5) * ball2.aceleracion * t * t
    t += deltaT
    label_t_Actual.text = 'T actual: ' + str('%.2f' % t) + 's'
