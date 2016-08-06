from visual import *
import math
import numpy as np

scene = display(title='Coulomb', x=0, y=0, width=900, height=900, autocenter=true, background=color.gray(0.2))

########## Modify ##########
Q1 = 20e-6
Q2 = -22e-6
Q3 = -15e-6
Q4 = 7e-6

pos_Q1 = (0.1, 0.1, 0.2)
pos_Q2 = (-0.1, -0.1, 0.1)
pos_Q3 = (-0.3, 0.1, -0.1)
pos_Q4 = (0.1, 0.1, -0.1)
############################

# Magnitude for each vector
magQ1 = sqrt(pos_Q1[0]**2 + pos_Q1[1]**2 + pos_Q1[2]**2)
magQ2 = sqrt(pos_Q2[0]**2 + pos_Q2[1]**2 + pos_Q2[2]**2)
magQ3 = sqrt(pos_Q3[0]**2 + pos_Q3[1]**2 + pos_Q3[2]**2)
magQ4 = sqrt(pos_Q4[0]**2 + pos_Q4[1]**2 + pos_Q4[2]**2)

# Distance between each molecule
distanceF1_2 = sqrt((pos_Q1[0] - pos_Q2[0])**2 + (pos_Q1[1] - pos_Q2[1])**2 + (pos_Q1[2] - pos_Q2[2])**2)
distanceF1_3 = sqrt((pos_Q1[0] - pos_Q3[0])**2 + (pos_Q1[1] - pos_Q3[1])**2 + (pos_Q1[2] - pos_Q3[2])**2)
distanceF1_4 = sqrt((pos_Q1[0] - pos_Q4[0])**2 + (pos_Q1[1] - pos_Q4[1])**2 + (pos_Q1[2] - pos_Q4[2])**2)

# Dot Products
Q1DotQ2 = np.dot(pos_Q1, pos_Q2)
Q1DotQ3 = np.dot(pos_Q1, pos_Q3)
Q1DotQ4 = np.dot(pos_Q1, pos_Q4)

# Angles
angleF1_2 = math.degrees(np.arccos(Q1DotQ2 / abs(magQ1*magQ2)))
angleF1_3 = math.degrees(np.arccos(Q1DotQ3 / abs(magQ1*magQ3)))
angleF1_4 = math.degrees(np.arccos(Q1DotQ4 / abs(magQ1*magQ4)))

# Calculating magnitude of Forces...
magF1_2_abs = 9e9 * abs(Q1 * Q2) / math.pow(distanceF1_2, 2)
magF1_3_abs = 9e9 * abs(Q1 * Q3) / math.pow(distanceF1_3, 2)
magF1_4_abs = 9e9 * abs(Q1 * Q4) / math.pow(distanceF1_4, 2)

magF1_2 = 9e9 * Q1 * Q2 / math.pow(distanceF1_2, 2)
magF1_3 = 9e9 * Q1 * Q3 / math.pow(distanceF1_3, 2)
magF1_4 = 9e9 * Q1 * Q4 / math.pow(distanceF1_4, 2)


distance_list = [abs(distanceF1_2), abs(distanceF1_3), abs(distanceF1_4)]
#list = [abs(F1_2x), abs(F1_2y), abs(F1_2z), abs(F1_3x), abs(F1_3y), abs(F1_3z), abs(F1_4x), abs(F1_4y), abs(F1_4z)]

min_distance = abs( min(x for x in distance_list if x > 0) )
scale_value = abs( min(x for x in distance_list if x > 0) ) * 0.03
scale_distance = abs( min(x for x in distance_list if x > 0) ) * 0.06


# Calculating new coordinates...
F1_2x = pos_Q2[0] * (scale_distance * magF1_2_abs) - pos_Q1[0] * (scale_distance * magF1_2_abs)
F1_2y = pos_Q2[1] * (scale_distance * magF1_2_abs) - pos_Q1[1] * (scale_distance * magF1_2_abs)
F1_2z = pos_Q2[2] * (scale_distance * magF1_2_abs) - pos_Q1[2] * (scale_distance * magF1_2_abs)

if (Q1 > 0 and Q2 > 0) or (Q1 < 0 and Q2 < 0):
	F1_2x = F1_2x * -1
	F1_2y = F1_2y * -1 
	F1_2z = F1_2z * -1
	 
F1_3x = pos_Q3[0] * (scale_distance * magF1_3_abs) - pos_Q1[0] * (scale_distance * magF1_3_abs)
F1_3y = pos_Q3[1] * (scale_distance * magF1_3_abs) - pos_Q1[1] * (scale_distance * magF1_3_abs)
F1_3z = pos_Q3[2] * (scale_distance * magF1_3_abs) - pos_Q1[2] * (scale_distance * magF1_3_abs)

if (Q1 > 0 and Q3 > 0) or (Q1 < 0 and Q3 < 0):
	F1_3x = F1_3x * -1
	F1_3y = F1_3y * -1 
	F1_3z = F1_3z * -1

F1_4x = pos_Q4[0] * (scale_distance * magF1_4_abs) - pos_Q1[0] * (scale_distance * magF1_4_abs)
F1_4y = pos_Q4[1] * (scale_distance * magF1_4_abs) - pos_Q1[1] * (scale_distance * magF1_4_abs)
F1_4z = pos_Q4[2] * (scale_distance * magF1_4_abs) - pos_Q1[2] * (scale_distance * magF1_4_abs)

if (Q1 > 0 and Q4 > 0) or (Q1 < 0 and Q4 < 0):
	F1_4x = F1_4x * -1
	F1_4y = F1_4y * -1 
	F1_4z = F1_4z * -1

# Spheres with new coordinates
if Q1 > 0:
	Q1Sphere = sphere(pos=pos_Q1, radius=scale_value, color=color.red)
else:
	Q1Sphere = sphere(pos=pos_Q1, radius=scale_value, color=color.blue)
	
if Q2 > 0:
	Q2Sphere = sphere(pos=pos_Q2, radius=scale_value, color=color.red)
else:
	Q2Sphere = sphere(pos=pos_Q2, radius=scale_value, color=color.blue)
	
if Q3 > 0:
	Q3Sphere = sphere(pos=pos_Q3, radius=scale_value, color=color.red)
else:
	Q3Sphere = sphere(pos=pos_Q3, radius=scale_value, color=color.blue)
	
if Q4 > 0:
	Q4Sphere = sphere(pos=pos_Q4, radius=scale_value, color=color.red)
else:
	Q4Sphere = sphere(pos=pos_Q4, radius=scale_value, color=color.blue)


# Guidelines 
x_arrow_positive = arrow(pos=pos_Q1, axis=(0.1, 0, 0), shaftwidth=0.001, color=color.black, material=materials.rough)
x_arrow_negative = arrow(pos=pos_Q1, axis=(-0.1, 0, 0), shaftwidth=0.001, color=color.black, material=materials.rough)
y_arrow_positive = arrow(pos=pos_Q1, axis=(0, 0.1, 0), shaftwidth=0.001, color=color.black, material=materials.rough)
y_arrow_negative = arrow(pos=pos_Q1, axis=(0, -0.1, 0), shaftwidth=0.001, color=color.black, material=materials.rough)
z_arrow_positive = arrow(pos=pos_Q1, axis=(0, 0, 0.1), shaftwidth=0.001, color=color.black, material=materials.rough)
z_arrow_negative = arrow(pos=pos_Q1, axis=(0, 0, -0.1), shaftwidth=0.001, color=color.black, material=materials.rough)


# Q Labels
infoQ1 = 'Q1 = ' + str(Q1) + 'uC'
label(pos=(pos_Q1[0], pos_Q1[1] +(pos_Q1[1]*0.3) , pos_Q1[2]), text=infoQ1, color=color.green)

infoQ2 = 'Q2 = ' + str(Q2) + 'uC'
label(pos=(pos_Q2[0], pos_Q2[1] +(pos_Q2[1]*0.3) , pos_Q2[2]), text=infoQ2, color=color.green)

infoQ3 = 'Q3 = ' + str(Q3) + 'uC'
label(pos=(pos_Q3[0], pos_Q3[1] +(pos_Q3[1]*0.3) , pos_Q3[2]), text=infoQ3, color=color.green)

infoQ4 = 'Q4 = ' + str(Q4) + 'uC'
label(pos=(pos_Q4[0], pos_Q4[1] +(pos_Q4[1]*0.3) , pos_Q4[2]), text=infoQ4, color=color.green)
	
scene.waitfor('click')

arrow_F1_2 = arrow(pos=pos_Q1, axis=(F1_2x, F1_2y, F1_2z), shaftwidth = scale_value*0.5, color=color.white)
arrow_F1_3 = arrow(pos=pos_Q1, axis=(F1_3x, F1_3y, F1_3z), shaftwidth= scale_value*0.5,  color=color.white)
arrow_F1_4 = arrow(pos=pos_Q1, axis=(F1_4x, F1_4y, F1_4z), shaftwidth= scale_value*0.5,  color=color.white)

# Info strings and labels
infoF1_2 = '|F1-2|: ' + str(magF1_2_abs) + ' N'
label(pos=(pos_Q1[0]+F1_2x, pos_Q1[1]+F1_2y*0.8+pos_Q1[1]*0.2, pos_Q1[2]+F1_2z*0.8) , text=infoF1_2, color=color.green)

infoF1_3 = '|F1-3|: ' + str(magF1_3_abs) + 'N'
label(pos=(pos_Q1[0]+F1_3x*0.8, pos_Q1[1]+F1_3y*0.8+pos_Q1[1]*0.2, pos_Q1[2]+F1_3z*0.8) , text=infoF1_3, color=color.green)

infoF1_4 = '|F1-4|: ' + str(magF1_4_abs) + 'N'
label(pos=(pos_Q1[0]+F1_4x*0.8, pos_Q1[1]+F1_4y*0.8+pos_Q1[1]*0.2, pos_Q1[2]+F1_4z*0.8) , text=infoF1_4, color=color.green)


# Calculating Total Force Coordinates and magnitude

C1_2x = pos_Q2[0] - pos_Q1[0]
C1_2y = pos_Q2[1] - pos_Q1[1]
C1_2z = pos_Q2[2] - pos_Q1[2]

C1_3x = pos_Q3[0] - pos_Q1[0]
C1_3y = pos_Q3[1] - pos_Q1[1]
C1_3z = pos_Q3[2] - pos_Q1[2]

C1_4x = pos_Q4[0] - pos_Q1[0]
C1_4y = pos_Q4[1] - pos_Q1[1]
C1_4z = pos_Q4[2] - pos_Q1[2]

X = C1_2x + C1_3x + C1_4x
Y = C1_2y + C1_3y + C1_4y
Z = C1_2z + C1_3z + C1_4z

a = X - pos_Q1[0] 
b = Y - pos_Q1[1]
c = Z - pos_Q1[2]

scene.waitfor('click')

arrow_FTotal = arrow(pos=pos_Q1, axis=(a,b,c), shaftwidth = scale_value*0.5, color=color.green)
total_mag = magF1_2 + magF1_3 + magF1_4
info_FTot = 'FTotal = ' + str(abs(total_mag)) + 'N'
label(pos=arrow_FTotal.axis * 0.3, text=info_FTot, color=color.white)
