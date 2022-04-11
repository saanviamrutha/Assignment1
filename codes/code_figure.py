import matplotlib.pyplot as plt
import numpy as np
import mpmath as mp
from numpy import *

#generating a circle
angle = np.linspace(0, 2 * np.pi, 150)
radius = 5
x = radius * np.cos(angle)
y = radius * np.sin(angle)

#generating axes
figure, axes = plt.subplots(1)
axes.plot(x, y)
axes.set_aspect(1)
plt.xlabel('$x$')
plt.ylabel('$y$')

AC = radius*tan(70/180*np.pi)
AD = 2*radius*mp.cot(55/180*np.pi)

#annotating the points
a = [0,0,0,2*radius*mp.cot(55/180*np.pi),radius*sin(70/180*np.pi),radius*tan(70/180*np.pi)]
b = [0,5,-5,-5,-radius*cos(70/180*np.pi),-5]
text = ["O", "B", "A", "D", "E","C"]

# plotting scatter plot
plt.scatter(a, b)

# Loop for annotation of all points
for i in range(len(a)):
    plt.annotate(text[i], (a[i]+0.2, b[i] + 0.2))

plt.plot(a,b,marker='o',color='none')

#drawing the lines AC,
a1 = [0,AD]
b1 = [5,-5]
plt.plot(a1,b1,color='black')
a2 = [0,AC]
b2 = [0,-5]
plt.plot(a2,b2,color='black')
a3 = [0,AC]
b3 = [-5,-5]
plt.plot(a3,b3,color='black')
a4 = [0,0]
b4 = [-5,5]
plt.plot(a4,b4,color='black')

plt.grid()
plt.show()