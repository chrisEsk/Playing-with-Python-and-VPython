from visual import *
from visual.controls import *
import math

#Variables globales
radius_length = 15
t = 1
initial_omega = 55
omega = initial_omega
earth_radius = 2

label_data = label(pos=(-20,-20,0), text='', color=color.green)
label_aceleration = label(pos=(radius_length/2,0,0), text='a', color=color.green)
# Objetos
earth = sphere(pos=(radius_length, 0, 0), radius=earth_radius, material=materials.earth, make_trail=false)
string = arrow(pos=(radius_length,0,0), color=color.green, axis=(-1*radius_length,0,0), shaftwidth=0.5)


def animate():
	print omega
	global t
	global radius_length
	global label_data
	global label_aceleration
	deltaT = 0.005

	velocidad = math.radians(omega)
	aceleracion = radius_length*(velocidad*velocidad)
	text_vAngular = ' v_angular = %.2f rad/s' % velocidad
	text_rad = '\n a_rad = %.2f m/s2' % aceleracion
	text_radio = '\n radio = %.2f m' % radius_length
	label_data.text = text_vAngular + text_rad + text_radio
	
	
	
	reset_rotation = false 
	while reset_rotation is false:
		cos = math.cos(math.radians(omega * t))
		sin = math.sin(math.radians(omega * t))
        #Calculo del origen de la flecha
		pos_x = radius_length * cos
		pos_y = radius_length * sin
		#Calculo del fin de la flecha
		axis_x_arrow = pos_x*-1
		axis_y_arrow = pos_y *-1
		
		
		vector = (pos_x, pos_y, 0)
		vector_acel_label = (pos_x/2, pos_y/2, 0)
		axis = (axis_x_arrow, axis_y_arrow, 0)
		#se cambia la posicion inicial de la bola
		earth.pos = vector
		#se cambia la posicion inicial de la flecha
		string.pos = vector
		#se cambia la posicion del fin de la flecha
		string.axis = axis

		label_aceleration.pos = vector_acel_label

		t += deltaT
		if t > 5000:
			reset_rotation = true
		rate(500)

#Funcion para cambiar el omega
def recalculateOmega(value):
    global omega 
    omega = value
    print 'Omega changed!'
    animate()

#Funcion para cambiar el radio
def recalculateRadio(value):
    global radius_length 
    radius_length = value
    print 'Radio changed!'
    animate()


#Definicion de botones para cambiar omega
omega_plus = button( pos=(-40,30), width=60, height=60, text='Omega +', action=lambda: recalculateOmega(omega + 5) )
omega_minus = button( pos=(-40,-60), width=60, height=60, text='Omega -', action=lambda: recalculateOmega(omega - 5) )

#Definicion de botones para cambiar radio
radius_length_plus = button( pos=(50,30), width=60, height=60, text='Radio +', action=lambda: recalculateRadio(radius_length + 1) )
radius_length_minus = button( pos=(50,-60), width=60, height=60, text='Radio -', action=lambda: recalculateRadio(radius_length - 1) )
c = controls(title='Control de velocidad y radio', x=800, y=400, width=300, height=300, range=100)

animate()
