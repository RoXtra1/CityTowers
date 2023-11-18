from random import random, shuffle  # для случайного определения блоков, недоступных для расположения башен
import matplotlib.pyplot as plt     # для графического отображения
import numpy as np                  # для создания координатной матрицы


class CityGrid:
    def __init__(self, size, block_prob=0.3):
        self.size = size    # добавлена для упрощенного присваивания размера квадратной сетке
        self.rows = size
        self.cols = size
        self.grid = [[0 for _ in range(size)] for _ in range(size)]  # создаем пустую сетку, где все блоки доступны

        self.towers = []            # список башен
        self.unavailable = []       # список координат недоступных районов
        self.rng = 2

        for y in range(size):                        # Заблокированные кварталы
            for x in range(size):
                if random() <= block_prob:           # Задаем вероятность блокировки квартала
                    self.grid[y][x] = 1              # 1 - обозначает черный, недоступный район
                    self.unavailable.append((y, x))  # сохраняем координаты недоступных районов

    def add_tower(self, row, col):  # добавляем башню в список
        tower = (row, col, self.rng)
        self.towers.append(tower)

    def is_covered(self, row, col): # проверяем покрыт ли блок хотя бы одной из существующих башен
        for tower in self.towers:
            t_row, t_col, rng = tower
            if abs(t_row - row) <= rng and abs(t_col - col) <= rng:
                return True
        return False

    def is_tow_around(self, y, x):
        for r in range(y-1,y+2):
            for c in range(x-1, x+2):
                if (r,c,self.rng) in self.towers:
                    return True
        return False

    def optimize_placement(self):
        while self.unavailable:                         # пока на поле есть недоступные блоки
            tower_placed = False
            block = self.unavailable.pop(0)             # берем первый недоступный блок
            row, col = block
            if not self.is_covered(row, col):           # если блок не покрыт действием
                rng = self.rng
                size = self.size

                # проходимся по территории вокруг блока на расстоянии радиуса действия башни в случайном порядке
                r = list(range(row - rng, row + rng+1))
                c = list(range(col - rng, col + rng+1))
                shuffle(r)
                shuffle(c)
                for y in r:
                    for x in c:
                        # если блок не за границей, доступен, на нем и рядом нет башни и башня пока не ставилась
                        if (not tower_placed and 0 <= y < size and 0 <= x < size and self.grid[y][x] == 0 and
                            (y,x,self.rng) not in self.towers and not self.is_tow_around(y, x)):

                            self.add_tower(y, x)            # ставим башню в первую доступную клетку в радиусе действия
                            tower_placed = True

                            # Удаляем покрытые блоки из списка недоступных
                            for i in range(y - rng, y + rng + 1):
                                for j in range(x - rng, x + rng + 1):
                                    if (i, j) in self.unavailable:
                                        self.unavailable.remove((i, j))
                            break   # заканчиваем поиск подходящего для башни места
                else:
                    continue
                break

    def find_most_reliable_path(self, tower1, tower2):
        # Ваш код для поиска наиболее надежного пути между двумя башнями
        pass

    def visualize(self):
        plt.figure(figsize=(self.size, self.size))
        plt.xlim([-0.5, self.size-0.5])
        plt.ylim([-0.5, self.size-0.5])
        plt.xticks(np.arange(0, self.size, 1))
        plt.yticks(np.arange(0, self.size, 1))
        plt.imshow(self.grid, cmap='Greys')                     # Отображаем районы в черно-белом формате
        for i in range(self.rows-1):
            plt.axhline(i + 0.5, color='black', linewidth=0.7)  # Горизонтальные линии сетки
        for j in range(self.cols-1):
            plt.axvline(j + 0.5, color='black', linewidth=0.7)  # Вертикальные линии сетки

        for tower in self.towers:  # Визуализация покрытия вышек
            row, col, rng = tower
            plt.scatter(col, row, color='green', marker='o', s=250)         # отображаем башню (зеленый круг)

            # создаем 2 матрицы для сочетания координат х и у площади покрытия
            x, y = np.meshgrid(np.arange(col - rng, col + rng + 1), np.arange(row - rng, row + rng + 1))
            plt.scatter(x, y, color='red', marker='s', alpha=0.4, s=60)     # отображаем зоны действия башен

        plt.tight_layout()
        plt.show()


if __name__ == '__main__':
    city = CityGrid(10)                     # Создаем сетку размером 20x20 со стандартной вероятностью блокировки 0.3
    city.optimize_placement()               # оптимально располагаем башни
    city.visualize()                        # Визуализация сетки с башнями и покрытием
