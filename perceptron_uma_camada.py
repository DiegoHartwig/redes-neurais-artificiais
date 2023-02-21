# -*- coding: utf-8 -*-
"""
Implementando Perceptron de uma camada
Exercício 1
soma = entradas * pesos
soma = (1 * 0.8) + (7 * 0.1) + (5 *0)
soma = 0.8 + 0.7 + 0
soma = 1.5
"""

entradas = [1, 7, 5]
pesos = [0.8, 0.1, 0]

def soma(e, p):
    s = 0
    for i in range(3):
        s += e[i] * p[i]
    return s
        
s = soma(entradas, pesos)

def stepFunction(soma):
    if(soma >= 1):
        return 1
    return 0

resultado1 = stepFunction(s)

print(f"Resultado do exercício 1: {resultado1}")

"""
Exercício 2
soma = (-1 * 0.8) + (7 * 0.1) + (5 *0)
soma = -0.8 + 0.7
soma = -01
"""

entradas = [-1, 7, 5]
pesos = [0.8, 0.1, 0]

def soma(e, p):
    s = 0
    for i in range(3):
        s += e[i] * p[i]
    return s
        
s = soma(entradas, pesos)

def stepFunction(soma):
    if(soma >= 1):
        return 1
    return 0

resultado2 = stepFunction(s)

print(f"Resultado do exercício 2: {resultado2}")
