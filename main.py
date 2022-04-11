import sys

from datetime import date
from os import system

import xlsxwriter

from PyQt5 import QtWidgets

# GUI FILE

from ui_main import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Checks
        self.ErrorInput = False  # Ошибка ввода от пользователя
        self.FlagSave = False  # Проврка на запись данных
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

        # PAGES
        ########################################################################

        self.test_user()

        # PAGE 1
        self.CountErrorInput = 0
        self.ui.btn_page_input.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_input))

        self.ui.btn_input_save.clicked.connect(self.act_btn_input_save)
        self.ui.btn_input_next.clicked.connect(self.act_btn_input_next)

        # PAGE 2
        self.ui.btn_page_output.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_output))

        self.ui.btn_output_next.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_graph))
        self.ui.btn_output_back.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_input))

        # PAGE 3
        self.ui.btn_page_gpraph.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_graph))
        self.ui.btn_graph_back.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_output))

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

    def detect_proportion(self) -> None:

        self.proportion_stud_fulltime = float(self.ui.le_count_stud_fulltime.text()) / float(
            self.ui.le_count_stud.text()) * 100.0
        self.proportion_stud_absentia = float(self.ui.le_count_stud_absentia.text()) / float(
            self.ui.le_count_stud.text()) * 100.0
        self.proportion_stud_parttime = float(self.ui.le_count_stud_parttime.text()) / float(
            self.ui.le_count_stud.text()) * 100.0

        if 99 < self.proportion_stud_parttime + self.proportion_stud_absentia + self.proportion_stud_fulltime > 101:
            self.ErrorInput = True
            self.ui.le_count_stud.setStyleSheet("background-color: rgba(200, 0, 0, 0.75);")
            self.ui.le_count_stud_fulltime.setStyleSheet("background-color: rgba(200, 0, 0, 0.75);")
            self.ui.le_count_stud_absentia.setStyleSheet("background-color: rgba(200, 0, 0, 0.75);")
            self.ui.le_count_stud_parttime.setStyleSheet("background-color: rgba(200, 0, 0, 0.75);")
            self.CountErrorInput += 1
        else:
            self.ui.le_count_stud.setStyleSheet("background-color: rgb(238, 238, 236);\n"
                                                "border: 1px solid;")
            self.ui.le_count_stud_fulltime.setStyleSheet("background-color: rgb(238, 238, 236);\n"
                                                         "border: 1px solid;")
            self.ui.le_count_stud_absentia.setStyleSheet("background-color: rgb(238, 238, 236);\n"
                                                         "border: 1px solid;")
            self.ui.le_count_stud_parttime.setStyleSheet("background-color: rgb(238, 238, 236);\n"
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
        else:
            self.detect_proportion()
            self.ErrorInput = False
            self.save_data()

    def save_data(self):
        self.count_stud_top50 = sum([int(obj.text()) for obj in self.ui.mas_top50])
        self.GPA_budget9 = sum(
            [float(obj.text()) for obj in self.ui.mas_GPA_budget9]) / self.ui.SIZE_GRADE_POINT_AVERAG_BUDGET_9
        self.GPA_paid9 = sum(
            [float(obj.text()) for obj in self.ui.mas_GPA_paid9]) / self.ui.SIZE_GRADE_POINT_AVERAG_PAID_9
        self.GPA_budget11 = sum(
            [float(obj.text()) for obj in self.ui.mas_GPA_budget11]) / self.ui.SIZE_GRADE_POINT_AVERAG_BUDGET_11
        self.GPA_paid11 = sum(
            [float(obj.text()) for obj in self.ui.mas_GPA_paid11]) / self.ui.SIZE_GRADE_POINT_AVERAG_PAID_11

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
        self.FlagSave = True

    def test_user(self):
        self.ui.le_count_stud.setText("150")
        self.ui.le_count_stud_paid.setText("150")
        self.ui.le_count_stud_budget.setText("90")
        self.ui.le_count_stud_fulltime.setText("50")
        self.ui.le_count_stud_absentia.setText("50")
        self.ui.le_count_stud_parttime.setText("50")

        for obj in self.ui.mas_top50:
            obj.setText("1")

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
