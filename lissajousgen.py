import numpy as np
import time


class lissajous_figure:
    """
    Фигуры Лиссажу.
    Задаётся набором точек с координатами x и y.
    """
    def __init__(self, x_array, y_array):
        self.x_arr=x_array
        self.y_arr=y_array


class LissajousGenerator:
    """
    Генерирует фигуры Лиссажу с заданными параметрами
    """
    def __init__(self, resolution=20):
        self.set_resolution(resolution)
        
        # Эта задержка эмулирует процедуру инициализации следующей версии генератора.
        # Задержка будет убрана после обновления.
        # Пока не трогать.
        # P.S. В новом генераторе задержка будет только при инициализации.
        # Фигуры будут генерироваться так же быстро, как и сейчас.
        time.sleep(1)

    def set_resolution(self, resolution):
        """
        resolution определяет количество точек в кривой
        """
        self._resolution = resolution
        
    def get_random_figure(self):
        """
        Функция создает фигуру Лиссажу со случайными значениями частот и случайным разрешением.
        """
        freq_x = np.random.randint(1, 10)
        freq_y = np.random.randint(1, 10)
        resolution = np.random.randint(20, high=1000)
        params = {
                  'freq_x':freq_x,
                  'freq_y':freq_y,
                  'resolution':resolution
                 }
        return self.generate_figure(freq_x, freq_y, resolution), params
        
    def generate_figure(self, freq_x, freq_y, resolution):
        """
        Генерирует фигуру (массивы x и y координат точек) с заданными частотами.
        """
        self.set_resolution(resolution)
        t = np.linspace(0, 2 * np.pi, self._resolution)
        x = np.sin(freq_x * t)
        y = np.sin(freq_y * t)
        return lissajous_figure(x, y)
