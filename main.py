import random                               # для случайного определения блоков, недоступных для башен
import matplotlib.pyplot as plt             # для графического отображения


class CityGrid:
    def __init__(self, rows, cols, block_prob):
        self.rows = rows
        self.cols = cols
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]  # создаем пустую сетку

        for i in range(rows):                                        # помечаем заблокированные блоки
            for j in range(cols):
                if random.random() < block_prob:  # Задаем вероятность блокировки квартала
                    self.grid[i][j] = 1

    def visualize(self):
        plt.imshow(self.grid, cmap='Greys')  # Отображаем сетку в черно-белом формате
        plt.show()


if __name__ == '__main__':
    city = CityGrid(10, 10, 0.3)  # Создается сетка размером 10x10 с вероятностью блокировки 0.3
    city.visualize()  # Визуализация сетки
