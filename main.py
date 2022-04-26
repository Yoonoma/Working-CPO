import sys
from math import pi

import numpy as np
import pandas as pd
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox

import output
from ui_main import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Checks
        self.ErrorInput = False  # Ошибка ввода от пользователя
        self.FlagSave = False  # Проверка на запись данных
        self.ErrorProportion = False

        self.msg_text = ''
        self.data_chart = pd.DataFrame({
            'group': ['main', 'budget', 'paid'],
            '09.02.03': [4.2, 4.2, 2],
            '09.02.04': [5, 3.7, 2],
            '10.02.01': [3.9, 4.6, 4],
            '11.02.04': [4.4, 3.8, 2.3],
            'var5': [4.8, 3.6, 3.3],
            'var6': [4.8, 4.8, 3.3],
            'var7': [4.8, 4.5, 3.3],
            'var8': [4.9, 4.6, 3.3],
            'var9': [4.4, 4.3, 3.3],
            'var10': [4.8, 3.9, 3.3],
            'var11': [4.5, 4.5, 3.3],
            'var12': [4.8, 3.5, 3.3],
            'var13': [4.8, 4.7, 3.3],
            'var14': [4.8, 4.4, 3.3],
            'var15': [4.1, 4.5, 3.3],
            'var16': [4.2, 3.9, 3.3],
            'var17': [4.1, 3.7, 3.3],
            'var18': [4.8, 3.9, 3.3],
            'var19': [4.3, 4.6, 3.3],
            'var20': [4.8, 4.6, 3.3],
            'var21': [4.4, 4.5, 3.3]
        })

        self.CountErrorInput = 0

        # Data
        self.count_stud_top50 = 0
        self.GPA_paid9 = 0
        self.GPA_budget9 = 0
        self.GPA_paid11 = 0
        self.GPA_budget11 = 0

        # Specific gravity
        self.proportion_stud_fulltime = 0  # 1.2
        self.proportion_stud_absentia = 0
        self.proportion_stud_parttime = 0
        self.proportion_stud_budget = 0  # 1.3
        self.proportion_stud_top50 = 0  # 1.4.1

        # Устанавливаем основное окно
        self.ui.Pages_Widget.setCurrentWidget(self.ui.page_input)

        # PAGES
        ########################################################################

        self.test_user()

        # MENU
        self.ui.btn_page_input.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_input))
        self.ui.btn_page_output.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_output))
        self.ui.btn_page_gpraph.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_graph))

        self.ui.btn_page_report.clicked.connect(self.report)
        self.ui.btn_graph_report.clicked.connect(self.report)
        # PAGE 1

        self.ui.btn_input_save.clicked.connect(self.act_btn_input_save)
        self.ui.btn_input_next.clicked.connect(self.act_btn_input_next)

        # PAGE 2

        self.ui.btn_output_next.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_graph))
        self.ui.btn_output_back.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_input))

        # PAGE 3
        self.ui.btn_graph_back.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_output))

        # TEST
        #self.ui.Pages_Widget.setCurrentWidget(self.ui.page_graph)
        #self.ui.checkBox_main.setChecked(1)
        #self.ui.checkBox_budget.setChecked(1)
        #self.ui.checkBox_paid.setChecked(1)


        #self.chart_create()
        self.ui.btn_graph_update.clicked.connect(self.chart_create)

        # Exit
        self.ui.btn_close.clicked.connect(self.close)

    ########################################################################
    ## INPUT
    ########################################################################

    def act_btn_input_save(self) -> None:
        self.checking_values()
        self.handler_btn_error(self.ui.btn_input_next)
        self.handler_btn_error(self.ui.btn_input_save)

    def act_btn_input_next(self) -> None:
        self.checking_values()
        self.handler_btn_error(self.ui.btn_input_save)
        self.handler_btn_error(self.ui.btn_input_next)
        if not self.ErrorInput:
            self.ui.Pages_Widget.setCurrentWidget(self.ui.page_output)
            self.ui.lo_count_stud.setText(self.ui.le_count_stud.text())
            self.ui.lo_proportion_stud_fulltime.setText('{:.2f}%'.format(self.proportion_stud_fulltime))
            self.ui.lo_proportion_stud_budget.setText('{:.2f}%'.format(self.proportion_stud_budget))
            self.ui.lo_count_stud_top50.setText(str(self.count_stud_top50))
            self.ui.lo_proportion_stud_top50.setText('{:.2f}%'.format(self.proportion_stud_top50))
            self.ui.lo_GPA_budget9.setText('{:.2f}'.format(self.GPA_budget9))
            self.ui.lo_GPA_paid9.setText('{:.2f}'.format(self.GPA_paid9))
            self.ui.lo_GPA_budget11.setText('{:.2f}'.format(self.GPA_budget11))
            self.ui.lo_GPA_paid11.setText('{:.2f}'.format(self.GPA_paid11))

    '''Проверка данных '''

    def detect_error_input(self, obj, enable_array=0) -> None:
        if enable_array:
            for operand in obj:
                try:
                    float(operand.text())
                    operand.setStyleSheet("background-color: rgb(238, 238, 236);\n"
                                          "border: 1px solid;")
                except ValueError:
                    self.CountErrorInput += 1
                    operand.setStyleSheet("background-color: rgb(196, 0, 0);\n"
                                          "border: 1px solid;")
        else:
            try:
                int(obj.text())
                obj.setStyleSheet("background-color: rgb(238, 238, 236);\n"
                                  "border: 1px solid;")
            except ValueError:
                self.CountErrorInput += 1
                obj.setStyleSheet("background-color: rgb(196, 0, 0);\n"
                                  "border: 1px solid;")

    def detect_error_proportion(self) -> None:

        self.proportion_stud_fulltime = float(self.ui.le_count_stud_fulltime.text()) / float(
            self.ui.le_count_stud.text()) * 100.0
        self.proportion_stud_absentia = float(self.ui.le_count_stud_absentia.text()) / float(
            self.ui.le_count_stud.text()) * 100.0
        self.proportion_stud_parttime = float(self.ui.le_count_stud_parttime.text()) / float(
            self.ui.le_count_stud.text()) * 100.0

        if 99 < self.proportion_stud_parttime + self.proportion_stud_absentia + self.proportion_stud_fulltime > 101:
            self.ErrorInput = True
            self.ErrorProportion = True

            self.ui.le_count_stud.setStyleSheet("background-color: rgba(200, 0, 0, 0.75);border: 1px solid;")
            self.ui.le_count_stud_fulltime.setStyleSheet("background-color: rgba(200, 0, 0, 0.75);border: 1px solid;")
            self.ui.le_count_stud_absentia.setStyleSheet("background-color: rgba(200, 0, 0, 0.75);border: 1px solid;")
            self.ui.le_count_stud_parttime.setStyleSheet("background-color: rgba(200, 0, 0, 0.75);border: 1px solid;")

            self.msg_text += "\nОшибка: формы обучения."
        else:
            self.ErrorProportion = False
            self.ui.le_count_stud.setStyleSheet("background-color: rgb(238, 238, 236);\n"
                                                "border: 1px solid;")
            self.ui.le_count_stud_fulltime.setStyleSheet("background-color: rgb(238, 238, 236);\n"
                                                         "border: 1px solid;")
            self.ui.le_count_stud_absentia.setStyleSheet("background-color: rgb(238, 238, 236);\n"
                                                         "border: 1px solid;")
            self.ui.le_count_stud_parttime.setStyleSheet("background-color: rgb(238, 238, 236);\n"
                                                         "border: 1px solid;")

        if int(self.ui.le_count_stud_budget.text()) + int(self.ui.le_count_stud_paid.text()) != int(
                self.ui.le_count_stud.text()):
            self.ErrorInput = True
            self.ErrorProportion = True

            self.ui.le_count_stud_budget.setStyleSheet("background-color: rgba(200, 0, 0, 0.75);border: 1px solid;")
            self.ui.le_count_stud_paid.setStyleSheet("background-color: rgba(200, 0, 0, 0.75);border: 1px solid;")

            self.msg_text += '\nОшибка: Количество бюджетников и платников не совпадают с общим количеством студентов.'
        else:
            self.ErrorProportion = False
            self.ui.le_count_stud_budget.setStyleSheet("background-color: rgb(238, 238, 236);\n"
                                                       "border: 1px solid;")
            self.ui.le_count_stud_paid.setStyleSheet("background-color: rgb(238, 238, 236);\n"
                                                     "border: 1px solid;")

    def detect_error_count_stud(self):
        if sum([int(obj.text()) for obj in self.ui.mas_top50]) > int(self.ui.le_count_stud.text()):
            self.ErrorInput = True
            [obj.setStyleSheet("background-color: rgb(196, 0, 0);\n"
                               "border: 1px solid;") for obj in self.ui.mas_top50]
            self.ui.le_top50.setStyleSheet("background-color: rgb(196, 0, 0);\n"
                                           "border: 1px solid;")
            self.ui.le_top50.setText('')
            self.msg_text += "Ошибка: количество студентов, соответствующих списку топ 50 наиболее востребованных профессий, превышает общее количество студентов."
        else:
            [obj.setStyleSheet("background-color: rgb(238, 238, 236);\n"
                               "border: 1px solid;") for obj in self.ui.mas_top50]
            self.ui.le_top50.setStyleSheet("background-color: rgb(238, 238, 236);\n"
                                           "border: 1px solid;")

    def handler_btn_error(self, btn) -> None:
        if self.ErrorInput:
            btn.setStyleSheet("QPushButton {\n"
                              "    color: rgb(255, 255, 255);\n"
                              "    background-color: rgb(196, 0, 0);\n"
                              "    border: 0px solid;\n"
                              "}\n"
                              "QPushButton:hover {\n"
                              "    background-color: rgb(150, 170, 255);\n"
                              "}")

        else:
            btn.setStyleSheet("QPushButton {\n"
                              "    color: rgb(255, 255, 255);\n"
                              "    background-color: rgb(35, 35, 35);\n"
                              "    border: 0px solid;\n"
                              "}\n"
                              "QPushButton:hover {\n"
                              "    background-color: rgb(85, 170, 255);\n"
                              "}")

    def checking_values(self):
        # Counter Error
        self.CountErrorInput = 0
        self.msg_text = ''

        # Main Input
        self.detect_error_input(self.ui.le_count_stud)
        self.detect_error_input(self.ui.le_count_stud_fulltime)
        self.detect_error_input(self.ui.le_count_stud_absentia)
        self.detect_error_input(self.ui.le_count_stud_parttime)

        self.detect_error_input(self.ui.le_count_stud_paid)
        self.detect_error_input(self.ui.le_count_stud_budget)

        # TOP 50
        self.detect_error_input(self.ui.mas_top50, 1)

        # GPA 9 classes
        self.detect_error_input(self.ui.mas_GPA_paid9, 1)
        self.detect_error_input(self.ui.mas_GPA_budget9, 1)

        # GPA 11 classes
        self.detect_error_input(self.ui.mas_GPA_paid11, 1)
        self.detect_error_input(self.ui.mas_GPA_budget11, 1)

        if self.CountErrorInput >= 1:
            self.ErrorInput = True
            self.msg_text = f"Ошибка ввода данных, проверьте корректность данных, заполните {self.CountErrorInput} полей"
        else:
            self.ErrorInput = False
            self.detect_error_count_stud()
            self.detect_error_proportion()
        if self.msg_text:
            self.showDialogError(self.msg_text)
        self.save_data()

    def save_data(self):
        if not self.ErrorInput and not self.ErrorProportion:
            self.count_stud_top50 = sum([int(obj.text()) for obj in self.ui.mas_top50])
            self.GPA_budget9 = sum(
                [float(obj.text()) for obj in self.ui.mas_GPA_budget9]) / self.ui.SIZE_GRADE_POINT_AVERAG
            self.GPA_paid9 = sum(
                [float(obj.text()) for obj in self.ui.mas_GPA_paid9]) / self.ui.SIZE_GRADE_POINT_AVERAG
            self.GPA_budget11 = sum(
                [float(obj.text()) for obj in self.ui.mas_GPA_budget11]) / self.ui.SIZE_GRADE_POINT_AVERAG
            self.GPA_paid11 = sum(
                [float(obj.text()) for obj in self.ui.mas_GPA_paid11]) / self.ui.SIZE_GRADE_POINT_AVERAG

            self.proportion_stud_fulltime = float(self.ui.le_count_stud_fulltime.text()) / float(
                self.ui.le_count_stud.text()) * 100.0
            self.proportion_stud_absentia = float(self.ui.le_count_stud_absentia.text()) / float(
                self.ui.le_count_stud.text()) * 100.0
            self.proportion_stud_parttime = float(self.ui.le_count_stud_parttime.text()) / float(
                self.ui.le_count_stud.text()) * 100.0

            self.proportion_stud_budget = float(self.ui.le_count_stud_budget.text()) / float(
                self.ui.le_count_stud.text()) * 100.0
            self.proportion_stud_top50 = self.count_stud_top50 / float(self.ui.le_count_stud.text()) * 100.0

            self.ui.le_top50.setText(str(self.count_stud_top50))
            self.ui.le_grade_point_averag_budget9.setText(str(self.GPA_budget9))
            self.ui.le_grade_point_averag_paid9.setText(str(self.GPA_paid9))
            self.ui.le_grade_point_averag_budget11.setText(str(self.GPA_budget11))
            self.ui.le_grade_point_averag_paid11.setText(str(self.GPA_paid11))

            self.data_output = (
                ['1.1', 'Общая численность студентов', int(self.ui.le_count_stud.text())],
                ['1.2',
                 'Удельный вес численности студентов, обучающихся по очной форме обучения в общей численности студентов',
                 f'{round(self.proportion_stud_fulltime, 2)}'.replace('.', ',') + '%'],
                ['1.3',
                 'Удельный вес численности студентов, обучающихся за счет средств соответствующих бюджетов бюджетной системы РФ в общей численности студентов',
                 f'{round(self.proportion_stud_budget, 2)}'.replace('.', ',') + '%'],
                ['1.4',
                 'Общая численность студентов, обучающихся по профессиям и специальностям, соответствующим  списку 50 наиболее востребованных на рынке труда',
                 self.count_stud_top50],
                ['1.4.1',
                 'Удельный вес численности студентов, обучающихся по профессиям и специальностям, соответствующим  списку 50 наиболее востребованных на рынке труда, в общей численности студентов',
                 f'{round(self.proportion_stud_top50, 2)}'.replace('.', ',') + '%'],
                ['1.5',
                 'Средний балл аттестата об основном общем образовании и результатов отбора студентов, принятых на обучение по очной форме обучения(бюджетники) ',
                 f"{self.GPA_budget9}"[:4]],
                ['1.5.1',
                 'Средний балл аттестата об основном общем образовании и результатов отбора студентов, принятых на обучение по очной форме обучения(платники) ',
                 f"{self.GPA_paid9}"[:4]],
                ['1.6',
                 'Средний балл аттестата об среднем общем образовании и результатов отбора студентов, принятых на обучение по очной форме обучения(бюджетники) ',
                 f"{self.GPA_paid11}"[:4]],
                ['1.6.1',
                 'Средний балл аттестата об среднем общем образовании и результатов отбора студентов, принятых на обучение по очной форме обучения(платники) ',
                 f"{self.GPA_paid11}"[:4]]
            )

            self.FlagSave = True

    # Диалоговое окно создания отчета
    def report(self):
        if self.FlagSave:
            self.report_win = output.ReportWindow(self.data_output)
            self.report_win.show()
        else:
            self.showDialogError("Ошибка: Данные не сохранены.")

    # График
    def chart_create(self):
        # Очищаем наш холст
        self.ui.sc.axes.cla()
        # Статус чекбоксов
        state = []
        # Цвета паутин
        color = ['#429bf4', 'green', 'r']
        # Инициализируем имена точек
        categories = list(self.data_chart)[1:]
        N = len(categories)
        # Устанавливаем угол осей для нашего графика
        angles = [n / float(N) * 2 * pi for n in range(N)]
        angles += angles[:1]

        # Устанавливаем заголовок графику
        self.ui.sc.axes.set_title("Проходной балл на бюджет", position=(0.5, 1.1), ha='center')
        # Корректируем оси графика
        self.ui.sc.axes.set_theta_offset(pi / 2.7)
        self.ui.sc.axes.set_theta_direction(-1)
        # Устанавливаем границы радиус
        self.ui.sc.axes.set_ylim(-0.1, 5.5)
        # Устанавливаем тики на графике
        self.ui.sc.axes.set_rlabel_position(0)
        self.ui.sc.axes.set_xticks(angles[:-1], categories, color='#222222', size=12)
        self.ui.sc.axes.set_yticks(np.arange(1, 6), ['1', '2', '3', '4', '5'],
                                   color='black', size=12)

        # Проверяем чекбосы
        if self.ui.checkBox_main.isChecked():
            state.append(0)
        if self.ui.checkBox_budget.isChecked():
            state.append(1)
        if self.ui.checkBox_paid.isChecked():
            state.append(2)

        # Создаем DataFrame
        for i in state:
            values = self.data_chart.loc[i].values.flatten().tolist()
            name_label = values[0]
            values = values[1:] + values[1:2]

            self.ui.sc.axes.plot(angles, values, '.-', color=color[i], linewidth=1, label=name_label)
            self.ui.sc.axes.fill(angles, values, color=color[i], alpha=0.1)

        # Устанавливаем легенду для графика
        self.ui.sc.axes.legend(fontsize=10,
                               ncol=3,  # количество столбцов
                               facecolor='white',  # цвет области
                               edgecolor='r',  # цвет крайней линии
                               title='Легенда',  # заголовок
                               title_fontsize='13',  # размер шрифта заголовка
                               loc='best', bbox_to_anchor=(0.89, 0.6, 0.5, 0.5)
                               )
        # Рисуем график
        self.ui.sc.draw()

    # Помощь
    '''Доп'''

    def showHelp(self):
        pass

    def showDialogError(self, text):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(text)
        msgBox.setWindowTitle("Ошибка")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()

    def test_user(self):
        self.ui.le_count_stud.setText("150")
        self.ui.le_count_stud_paid.setText("100")
        self.ui.le_count_stud_budget.setText("50")
        self.ui.le_count_stud_fulltime.setText("50")
        self.ui.le_count_stud_absentia.setText("50")
        self.ui.le_count_stud_parttime.setText("50")

        for obj in self.ui.mas_top50:
            obj.setText("10")

        [obj.setText("4.0") for obj in self.ui.mas_GPA_paid9]
        [obj.setText("4.5") for obj in self.ui.mas_GPA_budget9]
        [obj.setText("4.2") for obj in self.ui.mas_GPA_paid11]
        [obj.setText("4.9") for obj in self.ui.mas_GPA_budget11]


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = MainWindow()
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
