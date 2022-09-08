# TAREA NO. 3 (CÁLCULO DE PI)
# BIOMECANICA JUEVES, EQUIPO 1
#Brenda Giselle Hinojosa
#Armando Rincon Reyes
#Cynthia Belén Gerrero Pardo
#Juan Jose Prado Luna
#Luis Fernando Martinez Ovalle
from multiprocessing import Pool
from random import randint
import statistics
import time
import numpy as np
import matplotlib.pyplot as plt

width = 10000
heigth = width
radio = width

npuntos = 0
ndentro = 0
radio2 = radio*radio
replicas = 250
promediopi = []

if __name__ == '__main__':
        with Pool(6) as p:
            inicio = time.time()
            for j in range(replicas):
                    for i in range(1,100000):
                        t_0 = time.time()
                        x = randint(0,width)
                        y = randint(0,width)
                        npuntos += 1
                        if x*x + y*y <= radio2:
                            ndentro += 1
                        pi = ndentro * 4 /npuntos
                        promediopi.append(pi)
                        t_1 = time.time()
                        t_f = t_1 - t_0
                        t_m = t_f * 1000000
                    print(statistics.mean(promediopi))
                    print("tiempo: {}µs.".format(t_m)) 
            final = time.time()
            delta = final - inicio 
            minutos = delta/60
            print("tiempo: {}s.".format(delta))   
            print("tiempo: {}minutos.".format(minutos))   

v=[0,1000000,0,3.8]
plt.plot(promediopi,"b--")
plt.xlabel('Tiempo en microsegundos (µs)')
plt.ylabel('Valores de pi')
plt.title('Tarea 3 Equipo #1 Biomecánica Jueves')
plt.axis(v)
plt.grid()
plt.show()
