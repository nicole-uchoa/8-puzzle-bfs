import numpy as np
from numpy.random import default_rng
import re

class Matriz():
    def __init__(self):
        self.end = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def check_ideal(self, matriz):  # verifica se a matriz está no estado final
        if np.array_equal(matriz, self.end):
            return True
        else:
            return False

    def check_tem_solucao(self, puzzle):
        ninversao = 0
        count = 0

        puzzle_list = eval(puzzle)
        puzzle_list= list(i for j in puzzle_list for i in j) # matriz to list
        
        #percorre a lista e calcula quantas inversões de valores existem
        for n in puzzle_list:
            for i in range(count,8):
                valor = puzzle_list[i+1]
                if n > valor and valor != 0:
                    ninversao += 1
            count += 1
        #se o numero de inversões for par é solucionável, se for ímpar não é solucionável                  
        if (ninversao % 2) != 0:
            return False
        else: return True

    def print_matriz(self, matriz):
        for row in matriz:
            print ('  '.join(map(str, row)))

    def gera_matriz_aleatória(self):
        #gera matriz aleatória entre 0 e 8 
        rng = default_rng()
        puzzle = rng.choice(range(0,9), size=(3, 3), replace=False)
        puzzle = str(puzzle)
        puzzle = re.sub('\n', ',', puzzle)
        puzzle = re.sub(' ', ', ', puzzle)
        puzzle = re.sub(',,', ', ', puzzle)
        return puzzle