import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

plt.style.use('bmh')

distancia_10= np.array([0.3,0.5,0.7,0.9,1.3,1.7,2.3,2.9,3.6,4.5,5.3,6.3,7.4,8.7,10.0,11.4,12.8,14.4,16.1,17.9,19.7,21.6,23.9,26.1,28.3,30.3,32.6,35.2,37.8,40.5,43.2,46.1,49.0,52.1,55.3,58.5,61.7,65.1,68.6,72.1,75.7,79.4,83.3,87.2,91.2,95.1])

tiempo_10 = np.arange(0, 1.15, 0.025)

distancia_02 = np.array([0.05,0.15,0.25,0.45,0.75,1.15,1.65,2.05,2.5,3.0,3.5,4.1,4.65,5.25,5.85,6.45,7.1,7.8,8.5,9.2,10.0,10.9,11.7,12.4,13.3,14.1,15.0,16.0,17.0,18.0,19.0,20.1,21.2,22.2,23.4,24.5,25.7,27.9,29.2,30.5,31.8,33.1,34.4,35.7,37.1,38.4,39.8,41.3,42.8,44.3,45.9,47.5,49.1,50.7,52.3,54.0,55.8,57.6,59.5,61.3,63.1,64.9,66.7,68.5,70.4,72.3,74.2,76.2,78.2,80.2,82.3,84.4,86.5,88.7,91.1])

tiempo_02 = np.arange(0, 1.875, 0.025)

distancia_15 = np.array([0.1,0.2,0.25,0.3,0.6,1.0,1.6,2.3,3.2,4.3,5.5,6.8,8.3,10.0,11.8,13.8,13.8+2.1,13.8+4.4,13.8+6.8,13.8+9.3,13.8+12.0,13.8+15.0,28.8+3.0,28.8+6.2,28.8+9.5,28.8+13.0,41.8+3.6,41.8+11.3,53.1+4.0,53.1+8.2,53.1+12.6,65.7+4.1,65.7+9.2,65.7+14.0,79.7+5.1,79.7+10.3,95.0])

tiempo_15 = np.arange(0, 0.925, 0.025)

def modelo(x, a, b, c):
    return a * x**2 + b * x + c

popt_10, pcov_10 = curve_fit(modelo, tiempo_10, distancia_10)
popt_02, pcov_02 = curve_fit(modelo, tiempo_02, distancia_02)
popt_15, pcov_15 = curve_fit(modelo, tiempo_15, distancia_15)

x_modelo_10 = np.linspace(0, 1.125, 50)
x_modelo_15 = np.linspace(0, 0.9, 50)
x_modelo_02 = np.linspace(0, 1.85, 50)

plt.scatter(tiempo_15, distancia_15, label="Inclinacion 15.0 grados", s=20, c="C0")
plt.scatter(tiempo_10, distancia_10, label="Inclinacion 10.0 grados", s=20, marker="v", c="C0")
plt.scatter(tiempo_02, distancia_02, label="Inclinacion 2.0 grados", s=20, marker="s", c="C0")

plt.plot(x_modelo_15, modelo(x_modelo_15, *popt_15), 'r-', label="g ="+f' {(popt_15[0]/np.sin(np.pi/12))*2:.1f}'+r' $[cm/s^2]$')
plt.plot(x_modelo_10, modelo(x_modelo_10, *popt_10), 'r-', label="g ="+f' {(popt_10[0]/np.sin(np.pi/18))*2:.1f}'+r' $[cm/s^2]$', linestyle=(0,(1,1)))
plt.plot(x_modelo_02, modelo(x_modelo_02, *popt_02), 'r-', label="g ="+f' {(popt_02[0]/np.sin(0.0436332))*2:.1f}'+r' $[cm/s^2]$', linestyle=(0,(3,1,1,1,1,1)))

plt.legend(loc='best')
plt.xlabel("Tiempo "+r'$[s]$')
plt.ylabel("Distancia "+r'$[cm]$')

print(popt_02[0], popt_10[0], popt_15[0 ])

plt.show()