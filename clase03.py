
from random import randint
import statistics

#1
def crear_album(figus_total):
	album = []
	for i in range(figus_total):
    	album.append(0)
	return album

def hay_alguno(album, elem):
	hay = False
	for i in range(len(album)):
    	if album[i] == elem:
        	hay = True
	return hay

def comprar_una_figu(figus_total):
	figurita = randint(0, figus_total-1)
	return figurita

def cuantas_figus(figus_total):
	cantidad = 0
	album = crear_album(figus_total)
	while hay_alguno(album,0):
    	figurita = comprar_una_figu(figus_total)
    	album[figurita] = 1
    	cantidad += 1
	return cantidad

def experimentar(figus_total, n_rep):
	lista = []
	for i in range(n_rep):
    	cantidad = cuantas_figus(figus_total)
    	lista.append(cantidad)
	return lista

#2
def generar_paquete(figus_total, figus_paquete):
	paquete = []
	for i in range(figus_paquete):
    	paquete.append(randint(0,figus_total-1))
	return paquete

def cuantos_paquetes(figus_total, figus_paquete):
	album = crear_album(figus_total)
	cantidad = 0
	while hay_alguno(album,0):
    	paquete = generar_paquete(figus_total, figus_paquete)
    	for i in range(figus_paquete):
        	figu = paquete[i]
        	album[figu] = 1
    	cantidad += 1
	return cantidad

def experimentar_con_paquetes(figus_total, figus_paquete, n_rep):
	lista = []
	for i in range(n_rep):
    	cantidad = cuantos_paquetes(figus_total, figus_paquete)
    	lista.append(cantidad)
	return lista

#optativos 1
lista1 = experimentar_con_paquetes(670, 5, 100)
#print(lista1)

def elementosMenorIgualAN(lista,n):
	contador = 0
	for i in range(len(lista)):
    	if lista[i] <= n:
        	contador += 1
	return contador

cantidadPosible = str(elementosMenorIgualAN(lista1,1200))
#print(cantidadPosible + "%")

#2

def cuantosPaquetes90(lista):
	cantidadPaquetes = 100
	probabilidad = elementosMenorIgualAN(lista, 100)
	while probabilidad < 90:
    	cantidadPaquetes += 1
    	probabilidad = elementosMenorIgualAN(lista, cantidadPaquetes)
	return cantidadPaquetes

#print(cuantosPaquetes90(lista1))   	 
 
#3   
'''670 figus paquete de 5 que no se repiten
necesito 134 paquetes'''

#guia 4
def cantidad(n, lista):
   contador = 0
   for i in range(len(lista)):
   	if lista[i] == n:
       	contador += 1
   return contador

def masRepetido(a):
   cantidadmayor = cantidad(a[0],a)
   mayor = a[0]
   for i in range(len(a)):
   	if cantidadmayor < cantidad(a[i], a):
       	mayor = a[i]
       	cantidadmayor = cantidad(a[i],a)  
   return mayor

def noHayNinguno(n, list):
	res = True
	for i in range(len(list)):
    	if list[i] == n:
        	res = False
	return res
   	 
def masRepetidos(a):
   cantidadmayor = 0
   mayores = []
   for i in range(len(a)):
   	if cantidadmayor < cantidad(a[i], a):
       	mayores = []
       	mayores.append(a[i])
       	cantidadmayor = cantidad(a[i],a)  
   	elif cantidadmayor == cantidad(a[i], a):
       	if noHayNinguno(a[i], mayores):
           	mayores.append(a[i])
   return mayores

lista2 = "jkhaiufhiaubfiabwaf"
#print(masRepetidos(lista2))
