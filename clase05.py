import numpy as np
import matplotlib.pyplot as plt
import imageio
import os
    
def guardar_foto(t, paso):
	dir_name = "/home/clinux01/Descargas/output"
	if not os.path.exists(dir_name): # me fijo si no existe el directorio
    	os.mkdir(dir_name) #si no existe lo creo

	ax = plt.gca()
	file_name = os.path.join(dir_name, "out{:05}.png".format(paso))
	plt.imshow(t, vmin=-1, vmax=3)
	ax.set_title("Copos tirados: {}".format(paso+1)) #titulo
	plt.savefig(file_name)

def hacer_video(cant_fotos):
	dir_name = "/home/clinux01/Descargas/output"
	lista_fotos=[]
	for i in range (cant_fotos):
    	file_name = os.path.join(dir_name, "out{:05}.png".format(i))
    	lista_fotos.append(imageio.imread(file_name))

	video_name = os.path.join(dir_name, "avalancha.mp4")
	# genero el video con 10 Copos por segundo. Explorar otros valores:
	imageio.mimsave(video_name, lista_fotos, fps=10)
	print('Estamos trabajando en el directorio', os.getcwd())
	print('y se guardo el video:', video_name)

def probar(n, pasos=200):
	t = crear_tablero(n)
	for i in range(pasos):
    	paso(t)
    	guardar_foto(t, i)

	hacer_video(pasos)
	return t

def crear_tablero(n):
	t = np.repeat(0, (n+2)*(n+2)).reshape(n+2,n+2)
	for i in range(n+2):
    	t[(0,i)] = -1
    	t[(n+1,i)] = -1
    	t[(i,0)] = -1
    	t[(i,n+1)] = -1
	return t
t1 = crear_tablero(7)

def es_borde(tablero, coord):
	return tablero[coord] == -1

def tirar_copo(tablero, coord):
	tablero[coord] += 1
	return tablero

def vecinos_de(tablero, coord):
	vecinos = []
	x = coord[0]
	y = coord[1]
	lista = [(x-1,y), (x,y+1), (x+1,y), (x,y-1)]
	for i in range(len(lista)):
    	if tablero[lista[i]] != -1:
        	vecinos.append(lista[i])
	return vecinos

def desbordar_posicion(tablero, coord):
	if tablero[coord] >= 4:
    	tablero[coord] -= 4
    	vecinos = vecinos_de(tablero, coord)
    	for i in range(len(vecinos)):
        	tablero[vecinos[i]] += 1
	return tablero

def desbordar_valle(tablero):
	cantidad_filas = tablero.shape[0]
	cantidad_columnas = tablero.shape[1]
	for i in range(cantidad_filas -1):
    	for j in range(cantidad_columnas -1):
        	if tablero[(i,j)] >= 4:
            	desbordar_posicion(tablero, (i,j))
	return tablero

def hay_que_desbordar(tablero):
	res = False
	cantidad_filas = tablero.shape[0]
	cantidad_columnas = tablero.shape[1]
	for i in range(cantidad_filas -1):
    	for j in range(cantidad_columnas -1):
        	if tablero[(i,j)] >= 4:
            	res = True
	return res

def estabilizar(tablero):
	while (hay_que_desbordar(tablero)):
    	desbordar_valle(tablero)
	return tablero

def paso(tablero):
	n = tablero.shape[1]
	tirar_copo(tablero, (int(n/2), int(n/2)))
	estabilizar(tablero)
	return tablero

probar(7)
