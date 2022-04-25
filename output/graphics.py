# importing various libraries
import sys

import numpy as np
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import random

import pandas as pd
from math import pi


# main window
# which inherits QDialog
class Chart(QDialog):

    # constructor
    def __init__(self, parent=None):
        super(Chart, self).__init__(parent)

        # a figure instance to plot on
        self.figure = plt.figure()

        # this is the Canvas Widget that
        # displays the 'figure'it takes the
        # 'figure' instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        # Just some button connected to 'plot' method
        self.button = QPushButton('Plot')

        # adding action to the button
        self.button.clicked.connect(self.radar_chart)

        # creating a Vertical Box layout
        layout = QVBoxLayout()

        # adding tool bar to the layout
        layout.addWidget(self.toolbar)

        # adding canvas to the layout
        layout.addWidget(self.canvas)

        # adding push button to the layout
        layout.addWidget(self.button)

        # setting layout to the main window
        self.setLayout(layout)

        self.radar_chart()

    # action called by the push button
    def plot(self):
        # random data
        data = [random.random() for i in range(10)]

        # clearing old figure
        self.figure.clear()

        # create an axis
        ax = self.figure.add_subplot(111)

        # plot data
        ax.plot(data, '*-')

        # refresh canvas
        self.canvas.draw()

    def radar_chart(self):
        # Set data
        df = pd.DataFrame({
            'group': ['A', 'B', 'C', 'D'],
            'var1': [4.2, 0, 0, 0],
            'var2': [5, 0, 0, 0],
            'var3': [3.9, 0, 0, 0],
            'var4': [4.4, 0, 0, 0],
            'var5': [4.8, 0, 0, 0]
        })

        # clearing old figure
        self.figure.clear()

        # number of variable
        categories = list(df)[1:]
        N = len(categories)

        # We are going to plot the first line of the data frame.
        # But we need to repeat the first value to close the circular graph:
        values = df.loc[0].drop('group').values.flatten().tolist()
        values += values[:1]

        # Угол оси
        angles = [n / float(N) * 2 * pi for n in range(N)]
        angles += angles[:1]

        # Initialise the spider plot
        # ax = plt.subplot(111, polar=True)
        # create an axis
        ax = self.figure.add_subplot(111, polar=True)
        # Заголовок
        ax.set_title("Проходной балл на бюджет")

        # Draw one axe per variable + add labels
        # Draw ylabels
        ax.set_rlabel_position(0)
        plt.xticks(angles[:-1], categories, color='grey', size=12)
        plt.yticks(np.arange(1, 6), ['1', '2', '3', '4', '5'],
                   color='grey', size=12)

        # Устанавливаем радиус
        ax.set_ylim(-0.1, 5.5)

        # Plot data
        ax.plot(angles, values, linewidth=1, linestyle='solid')

        # Fill area
        ax.fill(angles, values, 'b', alpha=0.1)

        # refresh canvas
        self.canvas.draw()


# driver code
if __name__ == '__main__':
    # creating apyqt5 application
    app = QApplication(sys.argv)

    # creating a window object
    main = Chart()

    # showing the window
    main.show()

    # loop
    sys.exit(app.exec_())
