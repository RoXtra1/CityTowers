from random import random                   # для случайного определения блоков, недоступных для расположения башен
import matplotlib.pyplot as plt             # для графического отображения
import numpy as np                          # для создания координатной матрицы


class CityGrid:
    def __init__(self, rows, cols, block_prob):
        self.rows = rows
        self.cols = cols
        self.towers = []
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]  # Создаем пустую сетку

        for i in range(rows):               # Заблокированные блоки
            for j in range(cols):
                if random() < block_prob:   # Задаем вероятность блокировки квартала
                    self.grid[i][j] = 1

    def add_tower(self, row, col, range):
        tower = (row, col, range)
        self.towers.append(tower)

    def visualize(self):
        plt.imshow(self.grid, cmap='Greys')  # Отображаем сетку в черно-белом формате

        for tower in self.towers:            # Визуализация покрытия вышек
            row, col, range = tower
            x, y = np.meshgrid(np.arange(col - range, col + range + 1), np.arange(row - range, row + range + 1))
            plt.scatter(x, y, color='red', marker='s')

        plt.show()


if __name__ == '__main__':
    city = CityGrid(10, 10, 0.3)    # Создаем сетку размером 10x10 с вероятностью блокировки 0.3
    city.add_tower(2, 3, 2)              # Размещаем вышку в квартале (2, 3) с диапазоном 2 блока
    city.visualize()                                    # Визуализация сетки с вышкой и ее покрытием
