# -*- coding: utf-8 -*-

import math
import random

#Ejercicio 1

def absoluto(a):
    return abs(a)

#Ejercicio 2

def suma_enteros(a,b):
    return a+b

#Ejercicio 3

def celsius_a_farenheit(c):
    return 9/5*c+32

#Ejercicio 4

def area_esfera(r):
    return 4*math.pi*r**2

#Ejercicio 5

def a_b_c(a,b,c):
    assert a==b
    assert b<c
    assert c>a
    print('a, b y c cumplen las condiciones!')
    return

#Ejercicio 6

def euclidea(p1,p2):
    return math.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)

#Ejercicio 7

def res(x,y):
    return 5*x**3+math.sqrt(x**2+y**2)+math.exp(math.log(x))

#Ejercicio 8

init=[1,2,3,4,5]
#Es una lista. Se podría considerar un array numérico

#Ejercicio 9

lista=[1,4,5,4,6,4,7]
for i in range(len(lista)):
    if lista[i]==4:
        lista[i]=10
       
#Ejercicio 10

def collatz(a):
    r=0
    while(a!=1):
        r=r+1
        if a%2==0:
            a=a/2
        else:
            a=3*a+1
           
    return r

def lista_collatz(a):
    r=a
    for i in range(len(a)):
        r[i]=collatz(a[i])
    print(r)
    return r

#Ejercicio 11

matrix=[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
for i in range(6):
    for j in range(3):
        matrix[i][j]=random.randint(-5, 5)

#Ejercicio 12

def cuantos(m,a):
    r=0
    for i in m:
        for j in i:
            if j==a:
                r=r+1
    return r

#Ejercicio 13

def entre_4_y_7(m):
    for i in m:
        for j in i:
            if j>=4 and j<=7:
                return True
    return False

#Ejercicio 14

def cuantos_aciertos(m,b):
    ret=[0,0]
    for i in range(len(m)):
        if m[i]>=0 and b[i]:
           ret[0]=ret[0]+1
        else:
            if m[i]<0 and not b[i]:
                ret[1]=ret[1]+1
    return ret
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            




























