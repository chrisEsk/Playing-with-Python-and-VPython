# .__          __ .          ,          .___                 .
# [__) _ ._.  /  `|_ ._.* __-+-* _.._   [__  __ _.. .*.  , _ |
# |   (_)[    \__.[ )[  |_)  | |(_][ )  [____) (_](_|| \/ (/,|
#                                                |            

from visual import *
import numpy as np
import math

#### Modificar estas Variables #######
pos_A = (1, 2, 3)
pos_B = (2, -2, 1)
######################################

# Cambiando display settings: 
scene = display(title='Cross Product', x=0, y=0, width=800, height=800, autocente=true, background=color.gray(0.2))

sphere(pos=(0, 0, 0), radius=0.2, color=color.red, material=materials.marble, opacity=0.5)
x_arrow_positive = arrow(pos=(0, 0, 0), axis=(8, 0, 0), shaftwidth=0.1, color=color.black, material=materials.rough)
x_arrow_negative = arrow(pos=(0, 0, 0), axis=(-8, 0, 0), shaftwidth=0.1, color=color.black, material=materials.rough)
y_arrow_positive = arrow(pos=(0, 0, 0), axis=(0, 8, 0), shaftwidth=0.1, color=color.black, material=materials.rough)
y_arrow_negative = arrow(pos=(0, 0, 0), axis=(0, -8, 0), shaftwidth=0.1, color=color.black, material=materials.rough)
z_arrow_positive = arrow(pos=(0, 0, 0), axis=(0, 0, 8), shaftwidth=0.1, color=color.black, material=materials.rough)
z_arrow_negative = arrow(pos=(0, 0, 0), axis=(0, 0, -8), shaftwidth=0.1, color=color.black, material=materials.rough)


vector_A = arrow(pos=(0,0,0), axis=(pos_A), shaftwidth=0.1, color=color.green, material=materials.wood)
vector_B = arrow(pos=(0,0,0), axis=(pos_B), shaftwidth=0.1, color=color.green, material=materials.wood)

# Numpy al rescate!
cross_Product = np.cross(pos_A, pos_B)

info = 'A= ' + str(pos_A[0]) + 'i + ' + str(pos_A[1]) + 'j + ' + str(pos_A[2]) + 'k'
info += '\nB= ' + str(pos_B[0]) + 'i + ' + str(pos_B[1]) + 'j + ' + str(pos_B[2]) + 'k'
info += '\nAxB= ' + str(cross_Product[0]) + 'i + ' + str(cross_Product[1]) + 'j + ' + str(cross_Product[2]) + 'k'

vector_Cross_Product = arrow(pos=(0,0,0), axis=(cross_Product), shaftwidth=0.1, color=color.yellow, material=materials.wood)

label(pos=(-5, 5, 0), text=info, color=color.green)

label_A = label(pos=vector_A.axis/2, text='A', color=color.green)
label_B = label(pos=vector_B.axis/2, text='B', color=color.green)
label_AxB = label(pos=vector_Cross_Product.axis/2, text='AxB', color=color.green)

text(text='X+', axis=x_arrow_positive.axis, pos=x_arrow_positive.axis + (0.2, -0.2, 0), height=0.4)
text(text='X-', axis=x_arrow_negative.axis, pos=x_arrow_negative.axis + (-0.2, -0.2, 0), height=0.4)
text(text='Y+', axis=y_arrow_positive.axis, pos=y_arrow_positive.axis + (0, 0.2, 0), height=0.4)
text(text='Y-', axis=y_arrow_negative.axis, pos=y_arrow_negative.axis + (0, -0.2, 0), height=0.4)
text(text='Z+', axis=z_arrow_positive.axis, pos=z_arrow_positive.axis + (0, 0, 0.2), height=0.4)
text(text='Z-', axis=z_arrow_negative.axis, pos=z_arrow_negative.axis + (0, 0, -0.2), height=0.4)

