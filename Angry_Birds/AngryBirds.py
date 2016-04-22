from visual import *
import math

USR_Angle = 100
USR_Initial_Velocity = 37

#Validacion de la velocidad
if USR_Initial_Velocity <= 0:
	print 'Velocidad debe ser un numero positivo'
	exit()
	
#Validacion del angulo
if USR_Angle >180 or USR_Angle < 0 :
	print 'El angulo debe ser mayor a 180'
	exit()
	
	
# Cambiando display settings: 
scene = display(title='Angry Birds v0.0.0.1', width=1024, height=768, autocenter=true, background=color.gray(0.3))

# Radio de las esferas:
sphere_Radius = 2

gravity = 9.8

X_Initial = 0

# Se definen vectores de posiciones iniciales de las bolas:
ball_pos = (X_Initial, 0, 0)

# Caracteristicas de bola 1:
ball = sphere(pos=ball_pos, radius=sphere_Radius, color=color.red, material=materials.marble, make_trail=true)
ball.velocity = vector(USR_Initial_Velocity, 0)
ball.light = local_light(pos=ball_pos, color=color.red)

# Tiempo total de vuelo
time = (2 * USR_Initial_Velocity * math.sin(math.radians(USR_Angle))) / gravity

# Tiempo que toma para alcanzar altura maxima
Y_Time_Highest_Point = (USR_Initial_Velocity * math.sin(math.radians(USR_Angle))) / gravity

# Altura maxima
Y_Highest_Point = (USR_Initial_Velocity * math.sin(math.radians(USR_Angle))) * Y_Time_Highest_Point - 0.5 * gravity * math.pow(Y_Time_Highest_Point, 2)

# Punto X de altura maxima
X_Highest_Point = USR_Initial_Velocity * math.cos(math.radians(USR_Angle)) * Y_Time_Highest_Point

# Rango o distancia desde el origen hasta que toca suelo
X_Range = USR_Initial_Velocity * math.cos(math.radians(USR_Angle)) * time

info = 'V0 = ' + str(USR_Initial_Velocity) + 'm/s, Angulo = ' + str(USR_Angle) + '*\n'
info += 'Tiempo total: ' + str(round(time, 2)) + 's\n'
info += 'Tiempo en punto mas alto: ' + str(round(Y_Time_Highest_Point, 2)) + 's\n'
info += 'Altura Maxima en Y: ' + str(round(Y_Highest_Point, 2)) + 'm\n'
info += 'Altura Maxima en X: ' + str(round(X_Highest_Point, 2)) + 'm\n'
info += 'Rango en X: ' + str(round(X_Range, 2)) + 'm'

print info

# Piso
centerOfTrayectory = X_Range - (X_Range / 2)
if X_Range <= 0:
   floor = box(pos=(centerOfTrayectory,-2,0), size=(200 + 20,0.2,5), color=color.orange, material=materials.wood)
else:
    floor = box(pos=(centerOfTrayectory,-2,0), size=(X_Range + 20,0.2,5), color=color.orange, material=materials.wood)

# Labels
labelStart = label(pos=(centerOfTrayectory, -35, 0), text='*click* para empezar!', color=color.green, border= 10, radius=10)

# Canon
canon = cylinder(pos=(0, 0, 0), axis=(5,0,0), radius=1.3, color=color.gray(0.3), material=materials.rough)
left= sphere(pos=(0, -1, 1), radius=1.5, color=color.gray(0.1), material=materials.rough)
right = sphere(pos=(0,-1, -1), radius=1.5, color=color.gray(0.1), material=materials.rough)

#Arboles
tree1_cyl  = cylinder(pos=(-10, -2, -1), axis=(0,10,0), radius=1, color=color.blue, material=materials.rough)
tree1_ball  = sphere(pos=(-10, 6, -1), radius=4, color=color.green, material=materials.marble, make_trail=true)

tree2_cyl  = cylinder(pos=(60, -2, -1), axis=(0,10,0), radius=1, color=color.blue, material=materials.rough)
tree2_ball  = sphere(pos=(60, 6, -1), radius=4, color=color.green, material=materials.marble, make_trail=true)

# Cajas
box = box(pos=(X_Range,0.5,0), axis=(0.5,0,0), length=5, height=5, width=5, material=materials.wood, up=(0,1,0)) 

start = false
loadingCanon = true
deltaT = 0.005
i = 0

ball.radius = 0

#Espera click del usuario para inicial la simulacion
scene.waitfor('click')
print '\n- Inicio de Animacion -'
while i <= USR_Angle:
	#Se calcula el punto del eje x donde termina el cañon
	canon.axis[0] = 5 * math.cos(math.radians(i))
	#Se calcula el punto del eje y donde termina el cañon
	canon.axis[1] = 5 * math.sin(math.radians(i))
	i += 0.05
	rate(500)
	
ball.radius = sphere_Radius
labelStart.text = info
start = true
	

highestPointYLabel = label(pos=(X_Highest_Point,Y_Highest_Point + 10, 0), text=str('%.2f' % Y_Highest_Point) + 'm', color=color.green, border= 10, radius=10)
rangeLabel = label(pos=(X_Range, 20, 0), text=str('%.2f' % X_Range) + 'm', color=color.green, border= 10, radius=10)
highestPointArrow = arrow(pos=(X_Highest_Point,Y_Highest_Point + 5, 0), axis=(0,-5,0), shaftwidth=0.5, color=color.yellow)
rangeArrow = arrow(pos=(X_Range, 10, 0), axis=(0,-5,0), shaftwidth=0.5, color=color.yellow)

# Simulacion de movimiento
t = 0
while t <=  time:
	rate(500)
	x = ( USR_Initial_Velocity * math.cos(math.radians(USR_Angle)) ) * t
	y = ( USR_Initial_Velocity * math.sin(math.radians(USR_Angle)) ) * t - 0.5 * gravity * (t * t)
	ball_pos = (x, y, 0)
	ball.pos = ball_pos
	ball.light.pos = ball_pos
	t += deltaT

ball.color = color.white
box.color = color.red
box.opacity = 0.2
