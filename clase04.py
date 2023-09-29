from random import random
import matplotlib.pyplot as plt
import numpy as np
 
def generar_bosque(n):
	bosque = []
	for i in range(n):
     	bosque.append(0)
	return bosque

def suceso_aleatorio(p):
	return random() < p

def brotes(bosque, p):
	for i in range(len(bosque)):
    	if suceso_aleatorio(p):
        	bosque[i] = 1
	return bosque

def cuantos(bosque, tipo_celda):
	contador = 0
	for i in range(len(bosque)):
    	if bosque[i] == tipo_celda:
        	contador += 1
	return contador

def rayos(bosque,f):
	for i in range(len(bosque)):
    	if suceso_aleatorio(f) and bosque[i] == 1:
        	bosque[i] = -1
	return bosque
       	 
def propagacion(bosque):
	for i in range(len(bosque)-1):
    	if bosque[i] == -1 and bosque[i+1] == 1:
        	bosque[i+1] = -1
	for i in range(len(bosque)-1, 0,-1):
    	if bosque[i] == -1 and bosque[i-1] == 1:
        	bosque[i-1] = -1
	return bosque

def limpieza(bosque):
	for i in range(len(bosque)):
    	if bosque[i] == -1:
        	bosque[i] = 0
	return bosque

def suma_elem(lista):
   suma = 0
   i = 0
   while i < len(lista):
   	suma = suma + lista[i]
   	i += 1
   return suma

def promedio(lista, k):
   suma = suma_elem(lista)
   promedio = suma / k
   return promedio

def dinamica1(n, a, p, f):
	cantidadArboles = []
	bosque = generar_bosque(n)
	for i in range(a):
    	brotes(bosque, p)
    	rayos(bosque, f)
    	propagacion(bosque)
    	limpieza(bosque)
    	cantidadArboles.append(cuantos(bosque, 1))
	return cantidadArboles

def dinamica2(n, a, p, f):
	cantidadArboles = []
	bosque = generar_bosque(n)
	for i in range(a):
    	brotes(bosque, p)
    	rayos(bosque, f)
    	propagacion(bosque)
    	limpieza(bosque)
    	cantidadArboles.append(cuantos(bosque, 1))
	prom = promedio(cantidadArboles, a)
	return prom

   	 
#print(dinamica2(100, 500, 0.8, 0.02))   
#0.5 es el valor optimo para p

'''https://aprendeconalf.es/docencia/python/manual/matplotlib/
a = 10    
dina = dinamica1(10, a, 0.8, 0.02)
print(dina)  	 

fig, ax = plt.subplots()
ax.plot(list(range(a)), dina, color = 'tab:purple')
plt.show()'''

x = np.arange(0,1,0.01).tolist()

def ejecutarDin(n, a, x, f):
	listaPromedios = []
	for i in range(len(x)):
    	promedio = dinamica2(n, a, x[i], f)
    	listaPromedios.append(promedio)
	return listaPromedios

y = ejecutarDin(100, 500, x, 0.02)
plt.plot(x,y,  color = 'tab:pink')
plt.show()
