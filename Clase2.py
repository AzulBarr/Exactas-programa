import random
from random import randint

def tirar_dado():
    tirada = randint(1, 6)
    return tirada

def tirar_varias_veces(n):
    lista = []
    for tirar in range(n):
        lista.append(tirar_dado())
    return lista

def es_tirada_ganadora(lista_dados):
    i = 0
    res = True
    while i < len(lista_dados):
        if lista_dados[i] == 6:
            res = False
        i += 1
    return res

def jugar_varios_j1(k, n):
    ganadores = []
    for jugadores in range(k):
        ganoperdio = es_tirada_ganadora(tirar_varias_veces(n))
        ganadores.append(ganoperdio)
    return ganadores

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

# Pone segunda - Juego 2

def tirar_hasta_seis():
    tirada = 0
    lista = []
    while tirada != 6:
        tirada = tirar_dado()
        lista.append(tirada)
    return lista

def cuanto_suman(lista_dados):
    suma = suma_elem(lista_dados)
    return suma

def ganador_perdedor():
    if cuanto_suman(tirar_hasta_seis()) == 20:
        ganoperdio = True
    else:
        ganoperdio = False
    return ganoperdio

def jugar_varios_j2(k):
    ganadores = []
    for jugadores in range(k):
        ganadores.append(ganador_perdedor())
    return ganadores

#juego3 Diez Mil

def tirar_dados():
    dados = tirar_varias_veces(5)
    return dados

def sumar_puntos(lista_dados):
    puntaje = 0
    for i in range(5):
        if lista_dados[i] == 1:
            puntaje += 100
        elif lista_dados[i] == 5:
            puntaje += 50
    return puntaje

def jugar_ronda():
    puntos = []
    for jugadores in range(4):
          puntaje = sumar_puntos(tirar_dados())
          puntos.append(puntaje)
    return puntos

def acumular_puntos(puntajes_acumulados, puntajes_ronda):
    puntajes_actualizado = []
    for i in range(4):
        puntos = puntajes_acumulados[i] + puntajes_ronda[i]
        puntajes_actualizado.append(puntos)
    return puntajes_actualizado

def hay_10mil(puntajes):
    res = False
    for i in range(4):
        if puntajes[i] >= 10000:
            res = True
    return res

def jugar_varios_j3():
    puntajes = [0,0,0,0]
    res = False
    while res == False:
        puntajes = acumular_puntos(puntajes,jugar_ronda())
        res = hay_10mil(puntajes)
    i = 0
    while i < 4:
        if puntajes[i] >= 10000:
            ganador = i
            i += 4
        else:
            i += 1
    return ganador

