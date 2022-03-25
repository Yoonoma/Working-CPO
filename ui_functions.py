## ==> GUI FILE
from PySide2 import QtCore
from PySide2.QtCore import QPropertyAnimation


from ui_main import Ui_MainWindow

class UIFunctions(Ui_MainWindow):

    def toggleMenu(self, maxWidth, enable):
        if enable:

            # GET WIDTH
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 70

            # SET MAX WIDTH
            if width == 70:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

'''







      ## ARRAY mas_GPA_paid11
        ############################################################

        self.mas_GPA_paid11 = [QtWidgets.QLineEdit(self.frame_lbl_grade_point_averag_paid9_4) for _ in
                               range(self.SIZE_GRADE_POINT_AVERAG_PAID_11)]

        for i in range(self.SIZE_GRADE_POINT_AVERAG_PAID_11):
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.mas_GPA_paid11[i].sizePolicy().hasHeightForWidth())
            self.mas_GPA_paid11[i].setSizePolicy(sizePolicy)
            self.mas_GPA_paid11[i].setMinimumSize(QtCore.QSize(70, 35))
            self.mas_GPA_paid11[i].setMaximumSize(QtCore.QSize(70, 16777215))
            font = QtGui.QFont()
            font.setPointSize(13)
            self.mas_GPA_paid11[i].setFont(font)
            self.mas_GPA_paid11[i].setStyleSheet("background-color: rgb(238, 238, 236);")
            self.mas_GPA_paid11[i].setInputMask("")
            self.mas_GPA_paid11[i].setMaxLength(6)
            self.mas_GPA_paid11[i].setAlignment(QtCore.Qt.AlignCenter)
            self.mas_GPA_paid11[i].setObjectName(f"mas_GPA_paid11_{i}")
            self.verticalLayout_grade_point_averag_paid11.addWidget(self.mas_GPA_paid11[i])

            ## ARRAY mas_GPA_budget11
            ############################################################

            self.mas_GPA_budget11 = [QtWidgets.QLineEdit(self.frame_lbl_grade_point_averag_paid9_3) for _ in
                                     range(self.SIZE_GRADE_POINT_AVERAG_BUDGET_11)]
            for i in range(self.SIZE_GRADE_POINT_AVERAG_BUDGET_11):
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.mas_GPA_budget11[i].sizePolicy().hasHeightForWidth())
                self.mas_GPA_budget11[i].setSizePolicy(sizePolicy)
                self.mas_GPA_budget11[i].setMinimumSize(QtCore.QSize(70, 35))
                self.mas_GPA_budget11[i].setMaximumSize(QtCore.QSize(70, 16777215))
                font = QtGui.QFont()
                font.setPointSize(13)
                self.mas_GPA_budget11[i].setFont(font)
                self.mas_GPA_budget11[i].setStyleSheet("background-color: rgb(238, 238, 236);")
                self.mas_GPA_budget11[i].setInputMask("")
                self.mas_GPA_budget11[i].setMaxLength(6)
                self.mas_GPA_budget11[i].setAlignment(QtCore.Qt.AlignCenter)
                self.mas_GPA_budget11[i].setObjectName(f"mas_GPA_budget11{i}")
                self.laout_grade_point_averag_budget11.addWidget(self.mas_GPA_budget11[i])




        ###################################################################
        ## HOLDER
        ###################################################################

        # TOP 50
        for i in range(self.SIZE_TOP50):
            self.mas_top50[i].setPlaceholderText(_translate("MainWindow", "100"))

        # GPA_paid11
        for i in range(self.SIZE_GRADE_POINT_AVERAG_PAID_11):
            self.mas_GPA_paid11[i].setPlaceholderText(_translate("MainWindow", "2.1"))

        # GPA_paid9
        for i in range(self.SIZE_GRADE_POINT_AVERAG_BUDGET_9):
            self.mas_GPA_paid9[i].setPlaceholderText(_translate("MainWindow", "5.0"))

        # GPA_budget11
        for i in range(self.SIZE_GRADE_POINT_AVERAG_BUDGET_11):
            self.mas_GPA_budget11[i].setPlaceholderText(_translate("MainWindow", "3.9"))

        self.btn_input_save.setText(_translate("MainWindow", "Сохранить"))
        self.btn_input_next.setText(_translate("MainWindow", "Далее"))

        # GPA_budget9
        for i in range(self.SIZE_GRADE_POINT_AVERAG_BUDGET_9):
            self.mas_GPA_budget9[i].setPlaceholderText(_translate("MainWindow", "4.5"))

'''