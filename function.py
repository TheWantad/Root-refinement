import sympy as sp
import os
import sys
import random
from CHM import equation

def f(t, mode = 0,equation=equation):
    try:
        if mode == 0:
            result = equation.subs(x, t)
        elif mode >= 1:
            derivative = sp.diff(equation, x, mode)
            result = derivative.subs(x, t)
    except ZeroDivisionError:
        print(result)
        sys.exit('Ошибка: деление на ноль')
    return result


def intervalle(a,b):
    if f(a) >= 0:
        signa = "+"
    else:
        signa = "—"

    c = (a+b)/2
    if f(c) > 0:
        if signa == "+":
            a = c
        else:
            b = c
    else:
        if signa == "—":
            a = c
        else:
            b = c
    return a,b


def intervall(a,b,Epsilon):
    i=0
    E=abs(a-b)
    ta,tb=a,b
    while E>=Epsilon:
        i+=1
        ta,tb = intervalle(ta,tb)
        E=abs(ta-tb)
    t=(ta+tb)/2
    return print(f'Метод Интервалов\nx ≈ {t:.10f} ± {E:.15f} |i = {i}\n')


def chord(a,b,Epsilon):
    E=abs(a-b)
    i=0
    t=0
    if (f(a,1) * f(a,2)) > 0:
        tn = a
        while E>=Epsilon:
            i+=1
            t = tn
            tn = t - ((f(t)*(b-t))/(f(b)-f(t)))
            E=abs(t-tn)
    elif (f(a,1) * f(a,2)) < 0:
        tn = b
        while E>=Epsilon:
            i+=1
            t = tn
            tn = a - ((f(a)*(t-a))/(f(t)-f(a)))
            E=abs(t-tn)
    t=(t+tn)/2
    return print(f'Метод хорд\nx ≈ {t:.10f} ± {E:.15f} |i = {i}\n')

def tangent(a,b,Epsilon):
    if (f(a,1) * f(a,2)) > 0:
        tn=b
    elif (f(a,1) * f(a,2)) < 0:
        tn=a
    E=abs(a-b)
    i=0
    t=0
    while E>Epsilon:
        i+=1
        t = tn
        tn = float(t - f(t)/f(t,1))
        E=abs(t-tn)
    t=(t+tn)/2
    return print(f'Метод Касательных\nx ≈ {t:.10f} ± {E:.15f} |i = {i}\n')

def combined(a,b,Epsilon):
    an=a
    bn=b
    E=abs(an-bn)
    i=0
    if (f(a,1) * f(a,2)) > 0:
        while E>=Epsilon:
            i+=1
            an=an - ((f(an)*(bn-an))/(f(bn)-f(an)))
            bn=float(bn - f(bn)/f(bn,1))
            E=abs(an-bn)
    elif (f(a,1) * f(a,2)) < 0:
        while E>=Epsilon:
            i+=1
            bn=bn - ((f(bn)*(an-bn))/(f(an)-f(bn)))
            an=float(an - f(an)/f(an,1))
            E=abs(an-bn)
    x=(an+bn)/2
    return print(f'Метод комбинированный\nx ≈ {x:.10f} ± {E:.15f} |i = {i}\n')

def Iteration(a,b,Epsilon):
    k=max(abs(f(a,1)),abs(f(b,1)))/2 + 1
    x=random.uniform(a,b)
    E=abs(a-b)
    i=0
    while E>=Epsilon:
        i=i+1
        xn=x
        x=x-f(x)/k
        E=abs(xn-x)
    return print(f'Метод итераций\nx ≈ {x:.10f} ± {E:.15f} |i = {i} \n')

def dont_touch(a,b):

    # Очистка экрана
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    j=True
    while j:
        j=False
        if (f(a,1) > 0 and f(b,1) < 0) or (f(a,1) < 0 and f(b,1) > 0) or f(a,1) == 0 or f(b,1) == 0:
            j=True
            a,b = intervalle(a,b)
        if (f(a,2) > 0 and f(b,2) < 0) or (f(a,2) < 0 and f(b,2) > 0) or f(a,2) == 0 or f(b,2) == 0:
            j=True
            a,b = intervalle(a,b)

