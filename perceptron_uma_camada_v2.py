# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 11:49:10 2023

@author: diego

Implementando Perceptron de uma camada utilizando numpy
Exercício 1
soma = entradas * pesos
soma = (1 * 0.8) + (7 * 0.1) + (5 *0)
soma = 0.8 + 0.7 + 0
soma = 1.5
"""
import numpy as np

entradas = np.array([1, 7, 5])
pesos = np.array([0.8, 0.1, 0])

def soma(e, p):
    return e.dot(p)
        
s = soma(entradas, pesos)

def stepFunction(soma):
    if(soma >= 1):
        return 1
    return 0

resultado1 = stepFunction(s)

print(f"Resultado do exercício 1: {resultado1}")


