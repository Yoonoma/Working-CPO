import sys
from math import pi

import matplotlib
import numpy as np
from matplotlib import pyplot as plt

matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure



class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111, polar=True)
        super(MplCanvas, self).__init__(fig)




"""class RadarChart(QtWidgets.QMainWindow):
    def __init__(self, data_frame):
        super(RadarChart, self).__init__()
        self.df = pd.DataFrame(data_frame)

        # Создаем объект FigureCanvas из Maptlotlib FigureCanvas
        self.sc = MplCanvas(self, width=5, height=4, dpi=100)

        self.draw()
        self.show()


    def draw(self):
        self.df = pd.DataFrame({
            'group': ['A', 'B', 'C', 'D'],
            'var1': [4.2, 4.2, 2, 4.2],
            'var2': [5, 3.3, 2, 2.3],
            'var3': [3.9, 4.6, 4, 1.2],
            'var4': [4.4, 2.1, 5, 2.3],
            'var5': [4.8, 2.5, 2.9, 3.3],
            'var6': [4.8, 2.5, 2.9, 3.3],
            'var7': [4.8, 2.5, 2.9, 3.3],
            'var8': [4.8, 2.5, 2.9, 3.3],
            'var9': [4.8, 2.5, 2.9, 3.3],
            'var10': [4.8, 2.5, 2.9, 3.3],
            'var11': [4.8, 2.5, 2.9, 3.3],
            'var12': [4.8, 2.5, 2.9, 3.3],
            'var13': [4.8, 2.5, 2.9, 3.3],
            'var14': [4.8, 2.5, 2.9, 3.3],
            'var15': [4.8, 2.5, 2.9, 3.3],
            'var16': [4.8, 2.5, 2.9, 3.3],
            'var17': [4.8, 2.5, 2.9, 3.3],
            'var18': [4.8, 2.5, 2.9, 3.3],
            'var19': [4.8, 2.5, 2.9, 3.3],
            'var20': [4.8, 2.5, 2.9, 3.3],
            'var21': [4.8, 2.5, 2.9, 3.3]
        })
        # Инициализируем имена точек
        categories = list(self.df)[1:]
        N = len(categories)
        # Устанавливаем угол осей для нашего графика
        angles = [n / float(N) * 2 * pi for n in range(N)]
        angles += angles[:1]



        # Устанавливаем заголовок графику
        self.sc.axes.set_title("Проходной балл на бюджет", position=(0.5, 1.1), ha='center')
        # Корректируем оси графика
        self.sc.axes.set_theta_offset(pi / 2.7)
        self.sc.axes.set_theta_direction(-1)
        # Устанавливаем границы радиус
        self.sc.axes.set_ylim(-0.1, 5.5)
        # Устанавливаем тики на графике
        self.sc.axes.set_rlabel_position(0)
        self.sc.axes.set_xticks(angles[:-1], categories, color='grey', size=12)
        self.sc.axes.set_yticks(np.arange(1, 6), ['1', '2', '3', '4', '5'],
                           color='black', size=12)

        # Создаем DataFrame
        # Ind1
        values = self.df.loc[0].drop('group').values.flatten().tolist()
        values += values[:1]
        self.sc.axes.plot(angles, values, '.-', linewidth=1, label="group A")
        self.sc.axes.fill(angles, values, 'b', alpha=0.1)

        # Ind2
        values = self.df.loc[1].drop('group').values.flatten().tolist()
        values += values[:1]
        self.sc.axes.plot(angles, values, '.-', linewidth=1, label="group B")
        self.sc.axes.fill(angles, values, 'r', alpha=0.1)

        # Ind3
        values = self.df.loc[2].drop('group').values.flatten().tolist()
        values += values[:1]
        self.sc.axes.plot(angles, values, '.-', linewidth=1, label="group B")
        self.sc.axes.fill(angles, values, 'grey', alpha=0.5)

app = QtWidgets.QApplication(sys.argv)
w = RadarChart(pd.DataFrame({
            'group': ['A', 'B', 'C', 'D'],
            'var1': [4.2, 4.2, 2, 4.2],
            'var2': [5, 3.3, 2, 2.3],
            'var3': [3.9, 6.6, 4, 1.2],
            'var4': [4.4, 2.1, 5, 2.3],
            'var5': [4.8, 2.5, 2.9, 3.3],
            'var6': [4.8, 2.5, 2.9, 3.3],
            'var7': [4.8, 2.5, 2.9, 3.3],
            'var8': [4.8, 2.5, 2.9, 3.3],
            'var9': [4.8, 2.5, 2.9, 3.3],
            'var10': [4.8, 2.5, 2.9, 3.3],
            'var11': [4.8, 2.5, 2.9, 3.3],
            'var12': [4.8, 2.5, 2.9, 3.3],
            'var13': [4.8, 2.5, 2.9, 3.3],
            'var14': [4.8, 2.5, 2.9, 3.3],
            'var15': [4.8, 2.5, 2.9, 3.3],
            'var16': [4.8, 2.5, 2.9, 3.3],
            'var17': [4.8, 2.5, 2.9, 3.3],
            'var18': [4.8, 2.5, 2.9, 3.3],
            'var19': [4.8, 2.5, 2.9, 3.3],
            'var20': [4.8, 2.5, 2.9, 3.3],
            'var21': [4.8, 2.5, 2.9, 3.3]
        }))
app.exec_()"""
