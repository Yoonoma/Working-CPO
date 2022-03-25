import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QIntValidator, QRegExpValidator

# GUI FILE
from ui_main import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Input Restriction
        self.setValidator()

        # PAGES
        ########################################################################

        # PAGE 1
        self.ErrorInput = False
        self.ui.Btn_Menu_Input.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_input))

        self.ui.btn_input_save.clicked.connect(lambda: self.checking_values())

        # PAGE 2
        self.ui.Btn_Menu_Output.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_output))

        # PAGE 3
        self.ui.Btn_Menu_Graph.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_output))

    def detect(self, obj, enable_array=0):
        if enable_array:
            for operand in obj:
                try:
                    float(operand.text())
                    operand.setStyleSheet("background-color: rgb(255, 255, 255);")
                except:
                    if not self.ErrorInput:
                        self.ErrorInput = True
                    operand.setStyleSheet("background-color: rgba(196, 0, 0, 0.75);")
        else:
            try:
                int(obj.text())
                obj.setStyleSheet("background-color: rgb(255, 255, 255);")
            except:
                if not self.ErrorInput:
                    self.ErrorInput = True
                obj.setStyleSheet("background-color: rgba(196, 0, 0, 0.75);")

    def checking_values(self):
        # Main Input
        self.detect(self.ui.le_count_stud)
        self.detect(self.ui.le_count_stud_paid)
        self.detect(self.ui.le_count_stud_budget)
        self.detect(self.ui.le_count_stud_fulltime)
        self.detect(self.ui.le_count_stud_absentia)
        self.detect(self.ui.le_count_stud_parttime)

        # TOP 50
        self.detect(self.ui.mas_top50, 1)

        # GPA 9 classes
        self.detect(self.ui.mas_GPA_paid9, 1)
        self.detect(self.ui.mas_GPA_budget9, 1)

        # GPA 11 classes
        self.detect(self.ui.mas_GPA_paid11, 1)
        self.detect(self.ui.mas_GPA_budget11, 1)

        if self.ErrorInput:
            self.ui.btn_input_save.setStyleSheet("QPushButton {\n"
                                                 "    color: rgb(255, 255, 255);\n"
                                                 "    background-color: rgba(196, 0, 0, 0.5);\n"
                                                 "    border: 0px solid;\n"
                                                 "}\n"
                                                 "QPushButton:hover {\n"
                                                 "    background-color: rgb(150, 170, 255);\n"
                                                 "}")
            self.ErrorInput = False
        else:
            self.ui.btn_input_save.setStyleSheet("QPushButton {\n"
                                                 "    color: rgb(255, 255, 255);\n"
                                                 "    background-color: rgb(35, 35, 35);\n"
                                                 "    border: 0px solid;\n"
                                                 "}\n"
                                                 "QPushButton:hover {\n"
                                                 "    background-color: rgb(85, 170, 255);\n"
                                                 "}")
        return self.ErrorInput

    def save_data(self, enable) -> None:
        if enable:
            # TOP 50
            count_stud_top50 = 0
            print(type(self.ui.mas_GPA_budget11[0]))
            for i in range(self.ui.SIZE_TOP50):
                count_stud_top50 += int(self.ui.mas_top50[i].text())
        self.ui.le_top50.setText(str(count_stud_top50))

    def setValidator(self) -> None:
        validator_int = QIntValidator(0, 1000, self)
        validator_double = QRegExpValidator(QRegExp(r'^(?:0|[2-5])\.[0-9]+$'))

        self.ui.le_count_stud.setValidator(validator_int)
        self.ui.le_count_stud_paid.setValidator(validator_int)
        self.ui.le_count_stud_budget.setValidator(validator_int)
        self.ui.le_count_stud_absentia.setValidator(validator_int)
        self.ui.le_count_stud_fulltime.setValidator(validator_int)
        self.ui.le_count_stud_parttime.setValidator(validator_int)

        for i in range(self.ui.SIZE_TOP50):
            self.ui.mas_top50[i].setValidator(validator_int)

        for i in range(self.ui.SIZE_GRADE_POINT_AVERAG_PAID_9):
            self.ui.mas_GPA_paid9[i].setValidator(validator_double)

        for i in range(self.ui.SIZE_GRADE_POINT_AVERAG_BUDGET_9):
            self.ui.mas_GPA_budget9[i].setValidator(validator_double)

        for i in range(self.ui.SIZE_GRADE_POINT_AVERAG_PAID_11):
            self.ui.mas_GPA_paid11[i].setValidator(validator_double)

        for i in range(self.ui.SIZE_GRADE_POINT_AVERAG_BUDGET_11):
            self.ui.mas_GPA_budget11[i].setValidator(validator_double)

    def test_user(self):
        pass


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = MainWindow()
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
