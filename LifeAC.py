import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
import copy

class Cell:
    """This class
    :param value: rule"""

    def __init__(self, posicion):
        self.name = f'C_{posicion[0]}_{posicion[1]}'
        self.posicion = posicion
        self.vecinos = list()
        self.life = 0

    def pattern(self):
        #print(f'vecninos {self.vecinos}')
        len_pattern = 2**(self.vecinos + 1)
        for i in range(len_pattern):
            pattern_t = self.decimal_to_binary(i, 3)
            self.list_pattern.append(np.array(list(pattern_t), dtype = int))

    def get_vecinos(self, matriz):
        #print(f"Pos {self.posicion}")
        for i in range(self.posicion[0] - 1, self.posicion[0] + 2):
            for j in range(self.posicion[1] - 1, self.posicion[1] + 2):
                #print(f'pos i {i} and j {j}')
                if (i != self.posicion[0]) or (j !=self.posicion[1]):
                    self.vecinos.append(matriz[i][j])
        
        print(self.vecinos)
        return self.vecinos
    
    def dies(self):
        self.life = 0
    
    def lives(self):
        self.life = 1

    def __repr__(self):
      return f'{self.name}'
        

class Grid:

    """Cellular Automata.py
    Class Automata
    :param value: rule
    """
    def __init__(self, len, h, steps, num_cells_i, cell_random = 1, *args):
        self.name = f'Linear_CA_transito'
        self.cells = list()
        self.estados = 2
        self.matrix_CA = list()
        self.len = len
        self.h = h
        self.num_cells_i = num_cells_i
        self.cell_random = cell_random
        self.args = args
        self.steps = steps
        self.binary_matrix = np.zeros([self.h + 2, self.len + 2])
        

    def create_CA(self):
        # Create matrix for CA with a single cell at the middle
        #self.matrix_CA = np.zeros([self.len + 1, self.h + 1])
        self.matrix_CA = [[Cell((j,i)) for i in range(0, self.len + 2)] for j in range(self.h + 2)]

        print(self.matrix_CA)

        # add active cells
        if self.cell_random == 1:
            while self.num_cells_i > 0:
                #pos_x = random.sample(range(1, self.len), self.num_cells_i)
                #pos_y = random.sample(range(1, self.h), self.num_cells_i)
                pos_x = random.randint(1, self.len)
                pos_y = random.randint(1, self.h)

                cell = Cell((pos_y, pos_x))

                if cell.life != 1:   
                    cell.lives()
                    self.cells.append(cell)
                    self.matrix_CA[pos_y][pos_x] = cell
                    self.binary_matrix[pos_y, pos_x] = 1
                
                self.num_cells_i = self.num_cells_i - 1
            #for num_cell in range(self.num_cells_i - 1):

                
        else:
            for pos in self.args:
                cell = Cell(pos)
                cell.lives()
                self.cells.append(cell)
                self.matrix_CA[pos[0]][pos[1]] = cell
                self.binary_matrix[pos[0], pos[1]] = 1

        return self.matrix_CA
    
    def count_alive_neigh(self, vecinos):
        alive = 0
        for vecino in vecinos:
            #print(f'{vecino} life {vecino.life}')
            if vecino.life == 1:
                alive = alive + 1
        return alive
    
    def update_matrix(self):
        new_matrix = copy.deepcopy(self.matrix_CA)
        for i in range(1, self.h + 1):
            for j in range(1, self.len + 1):
                print(f'i {i} j {j}')
                print(f'Obj {self.matrix_CA[i][j].name}')
                vecinos = self.matrix_CA[i][j].get_vecinos(self.matrix_CA)
                
                count_alive = self.count_alive_neigh(vecinos)
                print(f"with {count_alive}")
                if count_alive <= 1 or count_alive >= 4:
                    new_matrix[i][j].dies()
                    self.binary_matrix[i,j] = 0
                    
                    #print(f'Obj {self.matrix_CA[i][j]}')
                    print(f"vecinos dies")

                elif count_alive == 3:
                    new_matrix[i][j].lives()
                    self.binary_matrix[i,j] = 1

                    #print(f'Obj {self.matrix_CA[i][j]}')
                    print(f"vecinos lives")

        
        self.matrix_CA = new_matrix
        print(self.binary_matrix)
        return self.binary_matrix
    
    def __repr__(self):
      return f'{self.matrix_CA}'


