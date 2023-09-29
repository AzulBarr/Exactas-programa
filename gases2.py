#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import matplotlib.pyplot as plt

def dar_pasito(x, y, vx, vy, dt):
    xt = x + vx * dt
    yt = y + vy * dt
    return (xt, yt)

def rebotar_der(x, vx, x_max):
    mod_v = 0
    if x > x_max:
        x = x - 2*(x - x_max)
        vx = -vx
        mod_v = abs(vx)    
    return (x, vx, mod_v)

def rebotar_arr(y, vy, y_max):
    mod_v = 0
    if y > y_max:
        y = y - 2*(y - y_max)
        vy = -vy
        mod_v = abs(vy)
    return (y, vy, mod_v)

def rebotar_izq(x, vx, x_min):
    mod_v = 0
    if x < x_min:
        x = x - 2*(x - x_min)
        vx = -vx
        mod_v = abs(vx)
    return (x, vx, mod_v)

def rebotar_aba(y, vy, y_min):
    mod_v = 0
    if y < y_min:
        y = y - 2*(y - y_min)
        vy = -vy
        mod_v = abs(vy)
    return (y, vy, mod_v)

def cond_ini(l, vmax, npart):
    xx = []
    yy = []
    vv_x = []
    vv_y = []
    for j in range(npart):
        vx = (random.random()*2-1)*vmax
        vy = (random.random()*2-1)*vmax
        x =  (random.random()*2-1)*l
        y = (random.random()*2-1)*l
        vv_x.append(vx)
        vv_y.append(vy)
        xx.append(x)
        yy.append(y)
    return (xx, yy, vv_x, vv_y)

def hacer_dinamica(npasos, npart, l, vmax, dt):
    vel_acum = 0
    volumen = l * l
    temperatura = vmax ** 2
    for i in range(npasos):
        for k in range(npart):
            x[k], y[k] = dar_pasito(x[k], y[k], vx[k], vy[k], dt)
            y[k], vy[k], mod_v = rebotar_arr(y[k], vy[k], y_max)
            vel_acum += mod_v
            x[k], vx[k], mod_v = rebotar_der(x[k], vx[k], x_max)
            vel_acum += mod_v
            x[k], vx[k], mod_v = rebotar_izq(x[k], vx[k], x_min)
            vel_acum += mod_v
            y[k], vy[k], mod_v = rebotar_aba(y[k], vy[k], y_min)
            vel_acum += mod_v
            print(k, x[k], y[k], file = archivo)
        
        presion = vel_acum/(npasos * dt * 4 * l)  
    return (presion, volumen, temperatura)

dt = 0.1
nombre_archivo = "trayectoria_varias"
archivo = open(nombre_archivo + ".txt", "w")
npart = 100
print(npart, file = archivo)
print(" ", file = archivo)
#print(numero_particulas, x, y, file = archivo)
l = 5
vmax = 1
npasos = 1000
x, y, vx, vy = cond_ini(l, vmax, npart)
x_min = -l
x_max = l
y_min = -l
y_max = l
presiones = []
temperaturas = []

presion, vol, temperatura = hacer_dinamica(npasos, npart, l, 0.5, dt)
presiones.append(presion)   
temperaturas.append(temperatura)

presion, vol, temperatura = hacer_dinamica(npasos, npart, l, 1, dt)
presiones.append(presion)   
temperaturas.append(temperatura)     

presion, vol, temperatura = hacer_dinamica(npasos, npart, l, 2, dt)
presiones.append(presion)   
temperaturas.append(temperatura)

presion, vol, temperatura = hacer_dinamica(npasos, npart, l, 3, dt)
presiones.append(presion)   
temperaturas.append(temperatura)


plt.plot(presiones, temperaturas, color = "blueviolet")
