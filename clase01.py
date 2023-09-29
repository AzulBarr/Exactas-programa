# 1
def masLarga(l1, l2):
   if len(l1) > len(l2):
       res = l1
   elif len(l1) == len(l2):
       res = "son igual de largas"
   else:
       res = l2
   return res


l1 = [1, 4, 8, 12, 16, 32, 63]
l2 = [2, 2, 2, 2, 8, 8, 80]
res = masLarga(l1, l2)
print(res)


# 2
def cant5(l):
   i = 0
   count = 0
   while i < len(l):
       if l[i] == 5:
           count += 1
       i += 1
   return count


l = [1, 2, 5, 5, 5, 6]
lis2 = [2]
lis3 = [3, 5, 2]
cantidad = cant5(lis3)
print(cantidad)


# 3
def change(l, n):
   for i in range(len(l)):
       if l[i] % 2 == 0 and l[i] < n:
           l[i] = 0
   return l


lis = [2, 2, 2, 2, 8, 8, 80, 80]
change(lis, 40)
print(lis)


# 4
def pasosCollatz(n):
   count = 0
   while n > 1:
       if n % 2 == 0:
           n = n / 2
       else:
           n = n * 3 + 1
       count += 1
   return count

n = int(input("número mayor a 1: "))
pasos = pasosCollatz(n)
print(pasos)

guia:
''''#1
def volverLaSuma(n1,n2):
   suma = n1 + n2
   return suma

print(volverLaSuma(3,7))

#2
def fahrenheitACelsius(f):
   c = (f-32)*5/9
   return c
f = int(input("fahrenheit: "))
print('{} °F son {} °C'.format(f, fahrenheitACelsius(f)))

#3
def perimetroCuadrado(lado):
   perim = 4*lado
   return perim
print(perimetroCuadrado(4))

#4
def areaRectangulo(lado1,lado2):
   area = lado1 * lado2
   return area
print(areaRectangulo(3,6))

#5
def obtenerValor(precio):
   pago = 0.65 * precio
   return pago
print(obtenerValor(100))

#6
def obtenerValor2(precio,descuento):
   x = (100-descuento)/100
   pago = x * precio
   return pago
print(obtenerValor2(100,35))

#7
def esTriplaPitagotica(cateto1,cateto2,hipotenusa):
   cuadradosCatetos = cateto1 * cateto1 + cateto2 * cateto2
   cuadradoHipotenusa = hipotenusa **2
   esTripla = cuadradosCatetos == cuadradoHipotenusa
   return esTripla
print(esTriplaPitagotica(3,4,5))

#1
def multx2(x,y):
   mult = x*y
   return mult
print(multx2(4,5))

#2
def evalPoli(a,b,c,x):
   evaluacion = a*(x*x) + b*x + c
   return evaluacion
print(evalPoli(1,2,3,5))

#3
def fatality(n):
   x = n
   n2 = multx2(n1,2)
   n3 = multx2(n2,2)
   fatal = evalPoli(x,n2,n3,x)
   return fatal
print(fatality(3))

'''
