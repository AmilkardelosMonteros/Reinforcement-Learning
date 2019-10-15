#!/usr/bin/env python3
from board import TicTacToe as ttt
from agent_value_iteration import Agent_value_iteration as agent_vi
import numpy as np
from numpy.linalg import norm as norma
import seaborn as sb
import matplotlib.pyplot as plt
def Matriz():
    test_board = ttt()
    player = agent_vi()
    matrix = []
    player.play_n_random_steps(1000)
    dim = len(player.values)
    y = np.repeat(0,dim)
    print(dim)
    epsilon= 0.01
    i = 0
    while True:
        player.value_iteration()
        x = np.array(list(player.values.values()))
        matrix.append(x)
        i+=1
        if norma(x-y) < epsilon:
            break
        y = x
    matrix = np.flip(matrix,axis = 0)
    matrix.reshape((i,dim))
    return matrix


def write(datos,nombre):
    np.savetxt(nombre,datos)

def read(nombre):
    np.loadtxt(nombre)
 
data = Matriz()
nombre = 'borrame.txt'
write(data,nombre)


##heat_map = sb.heatmap(data)	
#plt.show()
