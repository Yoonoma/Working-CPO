from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QIntValidator, QRegExpValidator, QPixmap

from output.canvas import MplCanvas

import resource_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 800)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 800))
        MainWindow.setStyleSheet("background-color: rgb(45, 45, 45);font:Roboto;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        ##############################################################
        ## DATA
        ###############################################################
        ## Text lable arrays
        self.lbl_text_top50 = ("09.02.03 ПРОГРАММИРОВАНИЕ В КОМПЬЮТЕРНЫХ СИСТЕМАХ",
                               "09.02.07 ИНФОРМАЦИОННЫЕ СИСТЕМЫ И ПРОГРАММИРОВАНИЕ",
                               "10.02.04 ОБЕСПЕЧЕНИЕ ИНФОРМАЦИОННОЙ БЕЗОПАСНОСТИ ТЕЛЕКОММУНИКАЦИОННЫХ СИСТЕМ",
                               "11.02.16 МОНТАЖ, ТЕХНИЧЕСКОЕ ОБСЛУЖИВАНИЕ И РЕМОНТ ЭЛЕКТРОННЫХ ПРИБОРОВ И УСТРОЙСТВ",
                               "15.02.10 МЕХАТРОНИКА И МОБИЛЬНАЯ РОБОТОТЕХНИКА (ПО ОТРАСЛЯМ)",
                               "15.02.15 ТЕХНОЛОГИЯ МЕТАЛЛООБРАБАТЫВАЮЩЕГО ПРОИЗВОДСТВА",
                               "54.01.20 ГРАФИЧЕСКИЙ ДИЗАЙНЕР")

        self.lbl_text_GPA = ("09.02.03 ПРОГРАММИРОВАНИЕ В КОМПЬЮТЕРНЫХ СИСТЕМАХ",
                             "09.02.04 ИНФОРМАЦИОННЫЕ СИСТЕМЫ (ПО ОТРАСЛЯМ)",
                             "09.02.07 ИНФОРМАЦИОННЫЕ СИСТЕМЫ И ПРОГРАММИРОВАНИЕ",
                             "10.02.01 ОРГАНИЗАЦИЯ И ТЕХНОЛОГИЯ ЗАЩИТЫ ИНФОРМАЦИИ",
                             "10.02.04 ОБЕСПЕЧЕНИЕ ИНФОРМАЦИОННОЙ БЕЗОПАСНОСТИ ТЕЛЕКОММУНИКАЦИОННЫХ СИСТЕМ",
                             "11.02.04 РАДИОТЕХНИЧЕСКИЕ КОМПЛЕКСЫ И СИСТЕМЫ УПРАВЛЕНИЯ КОСМИЧЕСКИХ ЛЕТАТЕЛЬНЫХ АППАРАТОВ",
                             "11.02.16 МОНТАЖ, ТЕХНИЧЕСКОЕ ОБСЛУЖИВАНИЕ И РЕМОНТ ЭЛЕКТРОННЫХ ПРИБОРОВ И УСТРОЙСТВ",
                             "12.02.06 БИОТЕХНИЧЕСКИЕ И МЕДИЦИНСКИЕ АППАРАТЫ И СИСТЕМЫ",
                             "12.02.08 ПРОТЕЗНО-ОРТОПЕДИЧЕСКАЯ И РЕАБИЛИТАЦИОННАЯ ТЕХНИКА",
                             "15.02.10 МЕХАТРОНИКА И МОБИЛЬНАЯ РОБОТОТЕХНИКА (ПО ОТРАСЛЯМ)",
                             "5.02.15 ТЕХНОЛОГИЯ МЕТАЛЛООБРАБАТЫВАЮЩЕГО ПРОИЗВОДСТВА",
                             "23.02.03 ТЕХНИЧЕСКОЕ ОБСЛУЖИВАНИЕ И РЕМОНТ АВТОМОБИЛЬНОГО ТРАНСПОРТА",
                             "24.02.01 ПРОИЗВОДСТВО ЛЕТАТЕЛЬНЫХ АППАРАТОВ",
                             "38.02.01 ЭКОНОМИКА И БУХГАЛТЕРСКИЙ УЧЕТ (ПО ОТРАСЛЯМ)",
                             "40.02.01 ПРАВО И ОРГАНИЗАЦИЯ СОЦИАЛЬНОГО ОБЕСПЕЧЕНИЯ",
                             "29.02.04 КОНСТРУИРОВАНИЕ, МОДЕЛИРОВАНИЕ И ТЕХНОЛОГИЯ ШВЕЙНЫХ ИЗДЕЛИЙ",
                             "38.02.04 КОММЕРЦИЯ (ПО ОТРАСЛЯМ)",
                             "38.02.07 БАНКОВСКОЕ ДЕЛО",
                             "43.02.08 СЕРВИС ДОМАШНЕГО И КОММУНАЛЬНОГО ХОЗЯЙСТВА",
                             "54.01.20 ГРАФИЧЕСКИЙ ДИЗАЙНЕР",
                             "54.02.01 ДИЗАЙН (ПО ОТРАСЛЯМ)")

        ## SIZE ARRAYS
        self.SIZE_TOP50 = len(self.lbl_text_top50)
        self.SIZE_GRADE_POINT_AVERAG = len(self.lbl_text_GPA)

        ## ARRRAYS
        self.mas_top50 = []
        self.mas_GPA_budget9 = []
        self.mas_GPA_paid9 = []
        self.mas_GPA_budget11 = []
        self.mas_GPA_paid11 = []

        ## Label
        self.lst_label_top50 = []
        self.lst_label_GPA_budget9 = []
        self.lst_label_GPA_paid9 = []
        self.lst_label_GPA_budget11 = []
        self.lst_label_GPA_paid11 = []

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Top_Bar = QtWidgets.QFrame(self.centralwidget)
        self.Top_Bar.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Top_Bar.setFont(font)
        self.Top_Bar.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Top_Bar.setObjectName("Top_Bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_toggle = QtWidgets.QFrame(self.Top_Bar)
        self.frame_toggle.setMaximumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.frame_toggle.setFont(font)
        self.frame_toggle.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.frame_toggle.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_toggle.setObjectName("frame_toggle")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Btn_Toggle = QtWidgets.QPushButton(self.frame_toggle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)
        self.Btn_Toggle.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.Btn_Toggle.setFont(font)
        self.Btn_Toggle.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Btn_Toggle.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "border: 0px solid;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/res/menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_Toggle.setIcon(icon)
        self.Btn_Toggle.setObjectName("Btn_Toggle")
        self.verticalLayout_2.addWidget(self.Btn_Toggle)
        self.horizontalLayout.addWidget(self.frame_toggle)
        self.frame_top = QtWidgets.QFrame(self.Top_Bar)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.frame_top.setFont(font)
        self.frame_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.horizontalLayout.addWidget(self.frame_top)
        self.verticalLayout.addWidget(self.Top_Bar)
        self.Content = QtWidgets.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Content.setFont(font)
        self.Content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Content.setObjectName("Content")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Content)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_left_menu = QtWidgets.QFrame(self.Content)
        self.frame_left_menu.setMinimumSize(QtCore.QSize(80, 0))
        self.frame_left_menu.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(4)
        self.frame_left_menu.setFont(font)
        self.frame_left_menu.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left_menu.setObjectName("frame_left_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_top_menus = QtWidgets.QFrame(self.frame_left_menu)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.frame_top_menus.setFont(font)
        self.frame_top_menus.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_menus.setObjectName("frame_top_menus")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setContentsMargins(1, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btn_page_input = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_page_input.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_page_input.sizePolicy().hasHeightForWidth())
        self.btn_page_input.setSizePolicy(sizePolicy)
        self.btn_page_input.setMinimumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.btn_page_input.setFont(font)
        self.btn_page_input.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_page_input.setStyleSheet("QPushButton {\n"
                                          "    color: rgb(255, 255, 255);\n"
                                          "    background-color: rgb(35, 35, 35);\n"
                                          "    border: 0px solid;\n"
                                          "    text-align: left;\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "    background-color: rgb(85, 170, 255);\n"
                                          "}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/res/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_page_input.setIcon(icon1)
        self.btn_page_input.setObjectName("btn_page_input")
        self.verticalLayout_4.addWidget(self.btn_page_input)
        self.btn_page_output = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_page_output.setMinimumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.btn_page_output.setFont(font)
        self.btn_page_output.setStyleSheet("QPushButton {\n"
                                           "    color: rgb(255, 255, 255);\n"
                                           "    background-color: rgb(35, 35, 35);\n"
                                           "    border: 0px solid;\n"
                                           "    text-align: left;\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "    background-color: rgb(85, 170, 255);\n"
                                           "}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/res/output.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_page_output.setIcon(icon2)
        self.btn_page_output.setCheckable(False)
        self.btn_page_output.setAutoRepeat(False)
        self.btn_page_output.setAutoExclusive(False)
        self.btn_page_output.setObjectName("btn_page_output")
        self.verticalLayout_4.addWidget(self.btn_page_output)
        self.btn_page_gpraph = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_page_gpraph.setMinimumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.btn_page_gpraph.setFont(font)
        self.btn_page_gpraph.setStyleSheet("QPushButton {\n"
                                           "    color: rgb(255, 255, 255);\n"
                                           "    background-color: rgb(35, 35, 35);\n"
                                           "    border: 0px solid;\n"
                                           "    text-align: left;\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "    background-color: rgb(85, 170, 255);\n"
                                           "}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/res/graph.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_page_gpraph.setIcon(icon3)
        self.btn_page_gpraph.setObjectName("btn_page_gpraph")
        self.verticalLayout_4.addWidget(self.btn_page_gpraph)

        # Excel output
        self.btn_page_report = QtWidgets.QPushButton(self.frame_top_menus)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_page_report.sizePolicy().hasHeightForWidth())
        self.btn_page_report.setSizePolicy(sizePolicy)
        self.btn_page_report.setMinimumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.btn_page_report.setFont(font)
        self.btn_page_report.setStyleSheet("QPushButton {\n"
                                           "    color: rgb(255, 255, 255);\n"
                                           "    background-color: rgb(35, 35, 35);\n"
                                           "    border: 0px solid;\n"
                                           "    text-align: left;\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "    background-color: rgb(85, 170, 255);\n"
                                           "}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/res/excel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_page_report.setIcon(icon4)
        self.btn_page_report.setObjectName("btn_page_report")
        self.verticalLayout_4.addWidget(self.btn_page_report)

        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, QtCore.Qt.AlignTop)
        self.frame_close = QtWidgets.QFrame(self.frame_left_menu)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.frame_close.setFont(font)
        self.frame_close.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_close.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_close.setObjectName("frame_close")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_close)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")

        ## Icon Button Help

        self.btn_help = QtWidgets.QPushButton(self.frame_close)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.btn_help.setFont(font)
        self.btn_help.setStyleSheet("QPushButton {\n"
                                    "    background-color: rgba(255, 255, 255, 0);\n"
                                    "    border: none;\n"
                                    "}\n"
                                    "QPushButton:hover {\n"
                                    "    background-color: rgb(85, 170, 255);\n"
                                    "}")
        self.btn_help.setText("")
        icon5 = QtGui.QIcon()
        self.pixmap = QPixmap("LightOff.png")
        icon5.addPixmap(QtGui.QPixmap("res/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_help.setIcon(icon5)
        self.btn_help.setIconSize(QtCore.QSize(64, 64))
        self.btn_help.setObjectName("btn_help")
        self.verticalLayout_9.addWidget(self.btn_help)

        ## Icon Button Close
        self.btn_close = QtWidgets.QPushButton(self.frame_close)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.btn_close.setFont(font)
        self.btn_close.setStyleSheet("QPushButton {\n"
                                     "    background-color: rgba(255, 255, 255, 0);\n"
                                     "    border: none;\n"
                                     "}\n"
                                     "QPushButton:hover {\n"
                                     "    background-color: rgb(85, 170, 255);\n"
                                     "}")
        self.btn_close.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/res/close_white.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_close.setIcon(icon5)
        self.btn_close.setIconSize(QtCore.QSize(64, 64))
        self.btn_close.setObjectName("btn_close")
        self.verticalLayout_9.addWidget(self.btn_close)

        self.verticalLayout_3.addWidget(self.frame_close, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout_2.addWidget(self.frame_left_menu)
        self.frame_pages = QtWidgets.QFrame(self.Content)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.frame_pages.setFont(font)
        self.frame_pages.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pages.setObjectName("frame_pages")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.Pages_Widget = QtWidgets.QStackedWidget(self.frame_pages)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Pages_Widget.setFont(font)
        self.Pages_Widget.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.Pages_Widget.setObjectName("Pages_Widget")
        self.page_input = QtWidgets.QWidget()
        self.page_input.setObjectName("page_input")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page_input)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.scrollArea = QtWidgets.QScrollArea(self.page_input)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.scrollArea.setFont(font)
        self.scrollArea.setStyleSheet(" QScrollBar:vertical {\n"
                                      "    border: none;\n"
                                      "    background: rgb(45, 45, 68);\n"
                                      "    width: 14px;\n"
                                      "    margin: 15px 0 15px 0;\n"
                                      "    border-radius: 0px;\n"
                                      " }\n"
                                      "\n"
                                      "/*  HANDLE BAR VERTICAL */\n"
                                      "QScrollBar::handle:vertical {    \n"
                                      "    background-color: rgb(80, 80, 122);\n"
                                      "    min-height: 30px;\n"
                                      "    border-radius: 7px;\n"
                                      "}\n"
                                      "QScrollBar::handle:vertical:hover{    \n"
                                      "    background-color: rgb(85, 170, 255);\n"
                                      "}\n"
                                      "QScrollBar::handle:vertical:pressed {    \n"
                                      "    background-color: rgb(85, 170, 255);\n"
                                      "}\n"
                                      "\n"
                                      "/* BTN TOP - SCROLLBAR */\n"
                                      "QScrollBar::sub-line:vertical {\n"
                                      "    border: none;\n"
                                      "    background-color: rgb(59, 59, 90);\n"
                                      "    height: 15px;\n"
                                      "    border-top-left-radius: 7px;\n"
                                      "    border-top-right-radius: 7px;\n"
                                      "    subcontrol-position: top;\n"
                                      "    subcontrol-origin: margin;\n"
                                      "}\n"
                                      "QScrollBar::sub-line:vertical:hover {    \n"
                                      "    background-color: rgb(85, 170, 255);\n"
                                      "}\n"
                                      "QScrollBar::sub-line:vertical:pressed {    \n"
                                      "    background-color: rgb(85, 170, 255);\n"
                                      "}\n"
                                      "\n"
                                      "/* BTN BOTTOM - SCROLLBAR */\n"
                                      "QScrollBar::add-line:vertical {\n"
                                      "    border: none;\n"
                                      "    background-color: rgb(59, 59, 90);\n"
                                      "    height: 15px;\n"
                                      "    border-bottom-left-radius: 7px;\n"
                                      "    border-bottom-right-radius: 7px;\n"
                                      "    subcontrol-position: bottom;\n"
                                      "    subcontrol-origin: margin;\n"
                                      "}\n"
                                      "QScrollBar::add-line:vertical:hover {    \n"
                                      "    background-color: rgb(85, 170, 255);\n"
                                      "}\n"
                                      "QScrollBar::add-line:vertical:pressed {    \n"
                                      "    background-color: rgb(85, 170, 255);\n"
                                      "}\n"
                                      "\n"
                                      "/* RESET ARROW */\n"
                                      "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
                                      "    background: none;\n"
                                      "}\n"
                                      "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
                                      "    background: none;\n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "\n"
                                      "/* HORIZONTAL SCROLLBAR - HOMEWORK */\n"
                                      "QScrollBar:horizontal {\n"
                                      "   \n"
                                      "}\n"
                                      "QScrollBar::handle:horizontal {\n"
                                      "    \n"
                                      "}\n"
                                      "QScrollBar::add-line:horizontal {\n"
                                      "    \n"
                                      "}\n"
                                      "QScrollBar::sub-line:horizontal {\n"
                                      "    \n"
                                      "}\n"
                                      "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
                                      "{\n"
                                      "\n"
                                      "}\n"
                                      "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
                                      "{\n"
                                      "\n"
                                      "}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaInput = QtWidgets.QWidget()
        self.scrollAreaInput.setGeometry(QtCore.QRect(0, 0, 1182, 2308))
        self.scrollAreaInput.setObjectName("scrollAreaInput")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaInput)
        self.gridLayout.setObjectName("gridLayout")
        self.le_grade_point_averag_budget9 = QtWidgets.QLineEdit(self.scrollAreaInput)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_grade_point_averag_budget9.sizePolicy().hasHeightForWidth())
        self.le_grade_point_averag_budget9.setSizePolicy(sizePolicy)
        self.le_grade_point_averag_budget9.setMinimumSize(QtCore.QSize(0, 0))
        self.le_grade_point_averag_budget9.setMaximumSize(QtCore.QSize(65, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.le_grade_point_averag_budget9.setFont(font)
        self.le_grade_point_averag_budget9.setStyleSheet("background-color: rgb(238, 238, 236);\n"
                                                         "border: 1px solid;")
        self.le_grade_point_averag_budget9.setInputMask("")
        self.le_grade_point_averag_budget9.setMaxLength(4)
        self.le_grade_point_averag_budget9.setAlignment(QtCore.Qt.AlignCenter)
        self.le_grade_point_averag_budget9.setObjectName("le_grade_point_averag_budget9")
        self.gridLayout.addWidget(self.le_grade_point_averag_budget9, 9, 2, 1, 1)
        self.lbl_top50 = QtWidgets.QLabel(self.scrollAreaInput)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_top50.sizePolicy().hasHeightForWidth())
        self.lbl_top50.setSizePolicy(sizePolicy)
        self.lbl_top50.setMinimumSize(QtCore.QSize(1000, 40))
        self.lbl_top50.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.lbl_top50.setFont(font)
        self.lbl_top50.setStyleSheet("background-color: rgb(198, 198, 255);\n"
                                     "border: 1px solid;")
        self.lbl_top50.setObjectName("lbl_top50")
        self.gridLayout.addWidget(self.lbl_top50, 7, 1, 1, 1)
        self.lbl_title1 = QtWidgets.QLabel(self.scrollAreaInput)
        self.lbl_title1.setMinimumSize(QtCore.QSize(50, 40))
        self.lbl_title1.setMaximumSize(QtCore.QSize(50, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_title1.setFont(font)
        self.lbl_title1.setStyleSheet("background-color: rgb(92, 92, 92);\n"
                                      "border: 1px solid;\n"
                                      "")
        self.lbl_title1.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_title1.setObjectName("lbl_title1")
        self.gridLayout.addWidget(self.lbl_title1, 0, 0, 1, 1)
        self.lbl_count_stud_fulltime = QtWidgets.QLabel(self.scrollAreaInput)
        self.lbl_count_stud_fulltime.setMinimumSize(QtCore.QSize(1000, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.lbl_count_stud_fulltime.setFont(font)
        self.lbl_count_stud_fulltime.setStyleSheet("background-color: rgb(198, 198, 198);\n"
                                                   "border: 1px solid;")
        self.lbl_count_stud_fulltime.setObjectName("lbl_count_stud_fulltime")
        self.gridLayout.addWidget(self.lbl_count_stud_fulltime, 2, 1, 1, 1)
        self.lbl_num_5 = QtWidgets.QLabel(self.scrollAreaInput)
        self.lbl_num_5.setMinimumSize(QtCore.QSize(0, 0))
        self.lbl_num_5.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_num_5.setFont(font)
        self.lbl_num_5.setStyleSheet("background-color: rgb(191, 192, 192);\n"
                                     "border: 1px solid;\n"
                                     "")
        self.lbl_num_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_num_5.setObjectName("lbl_num_5")
        self.gridLayout.addWidget(self.lbl_num_5, 9, 0, 1, 1)
        self.le_count_stud_parttime = QtWidgets.QLineEdit(self.scrollAreaInput)
        self.le_count_stud_parttime.setMinimumSize(QtCore.QSize(0, 35))
        self.le_count_stud_parttime.setMaximumSize(QtCore.QSize(65, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.le_count_stud_parttime.setFont(font)
        self.le_count_stud_parttime.setStyleSheet("background-color: rgb(238, 238, 236);\n"
                                                  "border: 1px solid;")
        self.le_count_stud_parttime.setInputMask("")
        self.le_count_stud_parttime.setMaxLength(4)
        self.le_count_stud_parttime.setAlignment(QtCore.Qt.AlignCenter)
        self.le_count_stud_parttime.setObjectName("le_count_stud_parttime")
        self.gridLayout.addWidget(self.le_count_stud_parttime, 4, 2, 1, 1)
        self.lbl_title2 = QtWidgets.QLabel(self.scrollAreaInput)
        self.lbl_title2.setMinimumSize(QtCore.QSize(1000, 40))
        self.lbl_title2.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_title2.setFont(font)
        self.lbl_title2.setStyleSheet("background-color: rgb(92, 92, 92);\n"
                                      "border: 1px solid;\n"
                                      "")
        self.lbl_title2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_title2.setObjectName("lbl_title2")
        self.gridLayout.addWidget(self.lbl_title2, 0, 1, 1, 1)
        self.lbl_num_1_6 = QtWidgets.QLabel(self.scrollAreaInput)
        self.lbl_num_1_6.setMinimumSize(QtCore.QSize(0, 0))
        self.lbl_num_1_6.setMaximumSize(QtCore.QSize(50, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_num_1_6.setFont(font)
        self.lbl_num_1_6.setStyleSheet("background-color: rgb(191, 192, 192);\n"
                                       "border: 1px solid;\n"
                                       "")
        self.lbl_num_1_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_num_1_6.setObjectName("lbl_num_1_6")
        self.gridLayout.addWidget(self.lbl_num_1_6, 6, 0, 1, 1)
        self.scrollArea_lbl_grade_point_averag_budget11 = QtWidgets.QScrollArea(self.scrollAreaInput)
        self.scrollArea_lbl_grade_point_averag_budget11.setMinimumSize(QtCore.QSize(1000, 310))
        self.scrollArea_lbl_grade_point_averag_budget11.setMaximumSize(QtCore.QSize(16777215, 350))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.scrollArea_lbl_grade_point_averag_budget11.setFont(font)
        self.scrollArea_lbl_grade_point_averag_budget11.setFrameShape(QtWidgets.QFrame.Box)
        self.scrollArea_lbl_grade_point_averag_budget11.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea_lbl_grade_point_averag_budget11.setWidgetResizable(True)
        self.scrollArea_lbl_grade_point_averag_budget11.setObjectName("scrollArea_lbl_grade_point_averag_budget11")
        self.scrollAreaWidget_budget11 = QtWidgets.QWidget()
        self.scrollAreaWidget_budget11.setGeometry(QtCore.QRect(0, 0, 1003, 348))
        self.scrollAreaWidget_budget11.setObjectName("scrollAreaWidget_budget11")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.scrollAreaWidget_budget11)
        self.gridLayout_5.setObjectName("gridLayout_5")

        ############################################################
        ## ARRAY GPA budget 11 classes
        ############################################################

        for i in range(self.SIZE_GRADE_POINT_AVERAG):
            self.mas_GPA_budget11.append(QtWidgets.QLineEdit(self.scrollAreaWidget_budget11))
            self.mas_GPA_budget11[i] = QtWidgets.QLineEdit(self.scrollAreaWidget_budget11)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.mas_GPA_budget11[i].sizePolicy().hasHeightForWidth())
            self.mas_GPA_budget11[i].setSizePolicy(sizePolicy)
            self.mas_GPA_budget11[i].setMinimumSize(QtCore.QSize(70, 35))
            self.mas_GPA_budget11[i].setMaximumSize(QtCore.QSize(70, 16777215))
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(13)
            self.mas_GPA_budget11[i].setFont(font)
            self.mas_GPA_budget11[i].setStyleSheet("background-color: rgb(238, 238, 236);\n"
                                                   "border: 1px solid;")
            self.mas_GPA_budget11[i].setMaxLength(4)
            self.mas_GPA_budget11[i].setAlignment(QtCore.Qt.AlignCenter)
            self.mas_GPA_budget11[i].setObjectName(f"mas_GPA_budget11_{i}")
            self.gridLayout_5.addWidget(self.mas_GPA_budget11[i], i, 1, 1, 1)

        ## LABEL

        for i in range(self.SIZE_GRADE_POINT_AVERAG):
            self.lst_label_GPA_budget11.append(QtWidgets.QLabel(self.scrollAreaWidget_budget11))
            self.lst_label_GPA_budget11[i].setEnabled(True)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.lst_label_GPA_budget11[i].sizePolicy().hasHeightForWidth())
            self.lst_label_GPA_budget11[i].setSizePolicy(sizePolicy)
            self.lst_label_GPA_budget11[i].setMinimumSize(QtCore.QSize(850, 35))
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(11)
            self.lst_label_GPA_budget11[i].setFont(font)
            self.lst_label_GPA_budget11[i].setStyleSheet("background-color: rgb(211, 215, 207);")
            self.lst_label_GPA_budget11[i].setFrameShape(QtWidgets.QFrame.Box)
            self.lst_label_GPA_budget11[i].setObjectName(f"lst_label_GPA_budget11_{i}")
            self.gridLayout_5.addWidget(self.lst_label_GPA_budget11[i], i, 0, 1, 1)

        self.scrollArea_lbl_grade_point_averag_budget11.setWidget(self.scrollAreaWidget_budget11)
        self.gridLayout.addWidget(self.scrollArea_lbl_grade_point_averag_budget11, 15, 1, 1, 1)
        self.scrollArea_lbl_grade_point_averag_budget9 = QtWidgets.QScrollArea(self.scrollAreaInput)
        self.scrollArea_lbl_grade_point_averag_budget9.setMinimumSize(QtCore.QSize(1000, 310))
        self.scrollArea_lbl_grade_point_averag_budget9.setMaximumSize(QtCore.QSize(16777215, 350))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.scrollArea_lbl_grade_point_averag_budget9.setFont(font)
        self.scrollArea_lbl_grade_point_averag_budget9.setFrameShape(QtWidgets.QFrame.Box)
        self.scrollArea_lbl_grade_point_averag_budget9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea_lbl_grade_point_averag_budget9.setWidgetResizable(True)
        self.scrollArea_lbl_grade_point_averag_budget9.setObjectName("scrollArea_lbl_grade_point_averag_budget9")
        self.scrollAreaWidget_budget9 = QtWidgets.QWidget()
        self.scrollAreaWidget_budget9.setGeometry(QtCore.QRect(0, 0, 1003, 348))
        self.scrollAreaWidget_budget9.setObjectName("scrollAreaWidget_budget9")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidget_budget9)
        self.gridLayout_3.setObjectName("gridLayout_3")

        ## ARRAY mas_GPA_budget9
        ############################################################
        self.mas_GPA_budget9 = []

        for i in range(self.SIZE_GRADE_POINT_AVERAG):
            self.mas_GPA_budget9.append(QtWidgets.QLineEdit(self.scrollAreaWidget_budget9))
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.mas_GPA_budget9[i].sizePolicy().hasHeightForWidth())
            self.mas_GPA_budget9[i].setSizePolicy(sizePolicy)
            self.mas_GPA_budget9[i].setMinimumSize(QtCore.QSize(70, 35))
            self.mas_GPA_budget9[i].setMaximumSize(QtCore.QSize(70, 16777215))

            font.setPointSize(13)
            self.mas_GPA_budget9[i].setFont(font)
            self.mas_GPA_budget9[i].setStyleSheet("background-color: rgb(238, 238, 236);\n"
                                                  "border: 1px solid;")
            self.mas_GPA_budget9[i].setMaxLength(4)
            self.mas_GPA_budget9[i].setAlignment(QtCore.Qt.AlignCenter)
            self.mas_GPA_budget9[i].setObjectName(f"mas_GPA_budget9_{i}")
            self.gridLayout_3.addWidget(self.mas_GPA_budget9[i], i, 1, 1, 1)

        ## LABEL

        for i in range(self.SIZE_GRADE_POINT_AVERAG):
            self.lst_label_GPA_budget9.append(QtWidgets.QLabel(self.scrollAreaWidget_budget9))
            self.lst_label_GPA_budget9[i].setEnabled(True)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.lst_label_GPA_budget9[i].sizePolicy().hasHeightForWidth())
            self.lst_label_GPA_budget9[i].setSizePolicy(sizePolicy)
            self.lst_label_GPA_budget9[i].setMinimumSize(QtCore.QSize(850, 35))
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(11)
            self.lst_label_GPA_budget9[i].setFont(font)
            self.lst_label_GPA_budget9[i].setStyleSheet("background-color: rgb(211, 215, 207);")
            self.lst_label_GPA_budget9[i].setFrameShape(QtWidgets.QFrame.Box)
            self.lst_label_GPA_budget9[i].setObjectName(f"lst_label_GPA_budget9_{i}")
            self.gridLayout_3.addWidget(self.lst_label_GPA_budget9[i], i, 0, 1, 1)

        self.scrollArea_lbl_grade_point_averag_budget9.setWidget(self.scrollAreaWidget_budget9)
        self.gridLayout.addWidget(self.scrollArea_lbl_grade_point_averag_budget9, 11, 1, 1, 1)
        self.le_grade_point_averag_paid11 = QtWidgets.QLineEdit(self.scrollAreaInput)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_grade_point_averag_paid11.sizePolicy().hasHeightForWidth())
        self.le_grade_point_averag_paid11.setSizePolicy(sizePolicy)
        self.le_grade_point_averag_paid11.setMinimumSize(QtCore.QSize(0, 50))
        self.le_grade_point_averag_paid11.setMaximumSize(QtCore.QSize(65, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.le_grade_point_averag_paid11.setFont(font)
        self.le_grade_point_averag_paid11.setStyleSheet("background-color: rgb(238, 238, 236);\n"
                                                        "border: 1px solid;")
        self.le_grade_point_averag_paid11.setInputMask("")
        self.le_grade_point_averag_paid11.setMaxLength(4)
        self.le_grade_point_averag_paid11.setAlignment(QtCore.Qt.AlignCenter)
        self.le_grade_point_averag_paid11.setObjectName("le_grade_point_averag_paid11")
        self.gridLayout.addWidget(self.le_grade_point_averag_paid11, 16, 2, 1, 1)
        self.le_grade_point_averag_paid9 = QtWidgets.QLineEdit(self.scrollAreaInput)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_grade_point_averag_paid9.sizePolicy().hasHeightForWidth())
        self.le_grade_point_averag_paid9.setSizePolicy(sizePolicy)
        self.le_grade_point_averag_paid9.setMinimumSize(QtCore.QSize(0, 0))
        self.le_grade_point_averag_paid9.setMaximumSize(QtCore.QSize(65, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.le_grade_point_averag_paid9.setFont(font)
        self.le_grade_point_averag_paid9.setStyleSheet("background-color: rgb(238, 238, 236);\n"
                                                       "border: 1px solid;")
        self.le_grade_point_averag_paid9.setInputMask("")
        self.le_grade_point_averag_paid9.setMaxLength(4)
        self.le_grade_point_averag_paid9.setAlignment(QtCore.Qt.AlignCenter)
        self.le_grade_point_averag_paid9.setObjectName("le_grade_point_averag_paid9")
        self.gridLayout.addWidget(self.le_grade_point_averag_paid9, 12, 2, 1, 1)
        self.le_top50 = QtWidgets.QLineEdit(self.scrollAreaInput)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_top50.sizePolicy().hasHeightForWidth())
        self.le_top50.setSizePolicy(sizePolicy)
        self.le_top50.setMinimumSize(QtCore.QSize(0, 0))
        self.le_top50.setMaximumSize(QtCore.QSize(65, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.le_top50.setFont(font)
        self.le_top50.setStyleSheet("background-color: rgb(238, 238, 236);\n"
                                    "border: 1px solid;")
        self.le_top50.setInputMask("")
        self.le_top50.setMaxLength(4)
        self.le_top50.setAlignment(QtCore.Qt.AlignCenter)
        self.le_top50.setObjectName("le_top50")
        self.gridLayout.addWidget(self.le_top50, 7, 2, 1, 1)
        self.lbl_num_1_4 = QtWidgets.QLabel(self.scrollAreaInput)
        self.lbl_num_1_4.setMinimumSize(QtCore.QSize(0, 0))
        self.lbl_num_1_4.setMaximumSize(QtCore.QSize(50, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_num_1_4.setFont(font)
        self.lbl_num_1_4.setStyleSheet("background-color: rgb(191, 192, 192);\n"
                                       "border: 1px solid;\n"
                                       "")
        self.lbl_num_1_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_num_1_4.setObjectName("lbl_num_1_4")
        self.gridLayout.addWidget(self.lbl_num_1_4, 4, 0, 1, 1)
        self.le_count_stud_budget = QtWidgets.QLineEdit(self.scrollAreaInput)
        self.le_count_stud_budget.setMinimumSize(QtCore.QSize(0, 35))
        self.le_count_stud_budget.setMaximumSize(QtCore.QSize(65, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.le_count_stud_budget.setFont(font)
        self.le_count_stud_budget.setStyleSheet("background-color: rgb(238, 238, 236);\n"
                                                "border: 1px solid;")
        self.le_count_stud_budget.setInputMask("")
        self.le_count_stud_budget.setMaxLength(4)
        self.le_count_stud_budget.setAlignment(QtCore.Qt.AlignCenter)
        self.le_count_stud_budget.setObjectName("le_count_stud_budget")
        self.gridLayout.addWidget(self.le_count_stud_budget, 5, 2, 1, 1)
        self.scrollArea_lbl_grade_point_averag_paid9 = QtWidgets.QScrollArea(self.scrollAreaInput)
        self.scrollArea_lbl_grade_point_averag_paid9.setMinimumSize(QtCore.QSize(1000, 310))
        self.scrollArea_lbl_grade_point_averag_paid9.setMaximumSize(QtCore.QSize(16777215, 350))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.scrollArea_lbl_grade_point_averag_paid9.setFont(font)
        self.scrollArea_lbl_grade_point_averag_paid9.setFrameShape(QtWidgets.QFrame.Box)
        self.scrollArea_lbl_grade_point_averag_paid9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea_lbl_grade_point_averag_paid9.setWidgetResizable(True)
        self.scrollArea_lbl_grade_point_averag_paid9.setObjectName("scrollArea_lbl_grade_point_averag_paid9")
        self.scrollAreaWidget_paid9 = QtWidgets.QWidget()
        self.scrollAreaWidget_paid9.setGeometry(QtCore.QRect(0, 0, 1003, 348))
        self.scrollAreaWidget_paid9.setObjectName("scrollAreaWidget_paid9")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidget_paid9)
        self.gridLayout_4.setObjectName("gridLayout_4")

        ############################################################
        ## ARRAY GPA paid 9 classes
        ############################################################

        for i in range(self.SIZE_GRADE_POINT_AVERAG):
            self.mas_GPA_paid9.append(QtWidgets.QLineEdit(self.scrollAreaWidget_paid9))
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.mas_GPA_paid9[i].sizePolicy().hasHeightForWidth())
            self.mas_GPA_paid9[i].setSizePolicy(sizePolicy)
            self.mas_GPA_paid9[i].setMinimumSize(QtCore.QSize(70, 35))
            self.mas_GPA_paid9[i].setMaximumSize(QtCore.QSize(70, 16777215))
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(13)
            self.mas_GPA_paid9[i].setFont(font)
            self.mas_GPA_paid9[i].setStyleSheet("background-color: rgb(238, 238, 236);\n"
                                                "border: 1px solid;")
            self.mas_GPA_paid9[i].setInputMask("")
            self.mas_GPA_paid9[i].setMaxLength(4)
            self.mas_GPA_paid9[i].setAlignment(QtCore.Qt.AlignCenter)
            self.mas_GPA_paid9[i].setObjectName(f"mas_GPA_paid9_{i}")
            self.gridLayout_4.addWidget(self.mas_GPA_paid9[i], i, 1, 1, 1)

        ## LABEL

        for i in range(self.SIZE_GRADE_POINT_AVERAG):
            self.lst_label_GPA_paid9.append(QtWidgets.QLabel(self.scrollAreaWidget_paid9))
            self.lst_label_GPA_paid9[i].setEnabled(True)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.lst_label_GPA_paid9[i].sizePolicy().hasHeightForWidth())
            self.lst_label_GPA_paid9[i].setSizePolicy(sizePolicy)
            self.lst_label_GPA_paid9[i].setMinimumSize(QtCore.QSize(850, 35))
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(11)
            self.lst_label_GPA_paid9[i].setFont(font)
            self.lst_label_GPA_paid9[i].setStyleSheet("background-color: rgb(211, 215, 207);")
            self.lst_label_GPA_paid9[i].setFrameShape(QtWidgets.QFrame.Box)
            self.lst_label_GPA_paid9[i].setObjectName(f"lst_label_GPA_paid9_{i}")
            self.gridLayout_4.addWidget(self.lst_label_GPA_paid9[i], i, 0, 1, 1)

        self.scrollArea_lbl_grade_point_averag_paid9.setWidget(self.scrollAreaWidget_paid9)
        self.gridLayout.addWidget(self.scrollArea_lbl_grade_point_averag_paid9, 13, 1, 1, 1)
        self.lbl_num_8 = QtWidgets.QLabel(self.scrollAreaInput)
        self.lbl_num_8.setMinimumSize(QtCore.QSize(0, 0))
        self.lbl_num_8.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_num_8.setFont(font)
        self.lbl_num_8.setStyleSheet("background-color: rgb(191, 192, 192);\n"
                                     "border: 1px solid;\n"
                                     "")
        self.lbl_num_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbl_num_8.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_num_8.setObjectName("lbl_num_8")
        self.gridLayout.addWidget(self.lbl_num_8, 16, 0, 1, 1)
        self.lbl_num_1_2 = QtWidgets.QLabel(self.scrollAreaInput)
        self.lbl_num_1_2.setMinimumSize(QtCore.QSize(0, 0))
        self.lbl_num_1_2.setMaximumSize(QtCore.QSize(50, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_num_1_2.setFont(font)
        self.lbl_num_1_2.setStyleSheet("background-color: rgb(191, 192, 192);\n"
                                       "border: 1px solid;\n"
                                       "")
        self.lbl_num_1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_num_1_2.setObjectName("lbl_num_1_2")
        self.gridLayout.addWidget(self.lbl_num_1_2, 2, 0, 1, 1)
        self.lbl_num_4 = QtWidgets.QLabel(self.scrollAreaInput)
        self.lbl_num_4.setMinimumSize(QtCore.QSize(0, 0))
        self.lbl_num_4.setMaximumSize(QtCore.QSize(50, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_num_4.setFont(font)
        self.lbl_num_4.setStyleSheet("background-color: rgb(191, 192, 192);\n"
                                     "border: 1px solid;\n"
                                     "")
        self.lbl_num_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_num_4.setObjectName("lbl_num_4")
        self.gridLayout.addWidget(self.lbl_num_4, 7, 0, 1, 1)
        self.lbl_grade_point_averag_paid9 = QtWidgets.QLabel(self.scrollAreaInput)
        self.lbl_grade_point_averag_paid9.setMinimumSize(QtCore.QSize(1000, 50))
        self.lbl_grade_point_averag_paid9.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.lbl_grade_point_averag_paid9.setFont(font)
        self.lbl_grade_point_averag_paid9.setStyleSheet("background-color: rgb(198, 198, 255);")
        self.lbl_grade_point_averag_paid9.setFrameShape(QtWidgets.QFrame.Box)
        self.lbl_grade_point_averag_paid9.setScaledContents(False)
        self.lbl_grade_point_averag_paid9.setWordWrap(True)
        self.lbl_grade_point_averag_paid9.setObjectName("lbl_grade_point_averag_paid9")
        self.gridLayout.addWidget(self.lbl_grade_point_averag_paid9, 12, 1, 1, 1)
        self.lbl_count_stud_budget = QtWidgets.QLabel(self.scrollAreaInput)
        self.lbl_count_stud_budget.setMinimumSize(QtCore.QSize(1000, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.lbl_count_stud_budget.setFont(font)
        self.lbl_count_stud_budget.setStyleSheet("background-color: rgb(198, 198, 198);\n"
                                                 "border: 1px solid;")
        self.lbl_count_stud_budget.setObjectName("lbl_count_stud_budget")
        self.gridLayout.addWidget(self.lbl_count_stud_budget, 5, 1, 1, 1)
        self.scrollArea_lbl_grade_point_averag_budget11_2 = QtWidgets.QScrollArea(self.scrollAreaInput)
        self.scrollArea_lbl_grade_point_averag_budget11_2.setMinimumSize(QtCore.QSize(1000, 310))
        self.scrollArea_lbl_grade_point_averag_budget11_2.setMaximumSize(QtCore.QSize(16777215, 350))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.scrollArea_lbl_grade_point_averag_budget11_2.setFont(font)
        self.scrollArea_lbl_grade_point_averag_budget11_2.setFrameShape(QtWidgets.QFrame.Box)
        self.scrollArea_lbl_grade_point_averag_budget11_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea_lbl_grade_point_averag_budget11_2.setWidgetResizable(True)
        self.scrollArea_lbl_grade_point_averag_budget11_2.setObjectName("scrollArea_lbl_grade_point_averag_budget11_2")
        self.scrollAreaWidget_paid11 = QtWidgets.QWidget()
        self.scrollAreaWidget_paid11.setGeometry(QtCore.QRect(0, 0, 1003, 348))
        self.scrollAreaWidget_paid11.setObjectName("scrollAreaWidget_paid11")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.scrollAreaWidget_paid11)
        self.gridLayout_7.setObjectName("gridLayout_7")

        ############################################################
        ## ARRAY GPA paid 11 classes
        ############################################################

        for i in range(self.SIZE_GRADE_POINT_AVERAG):
            self.mas_GPA_paid11.append(QtWidgets.QLineEdit(self.scrollAreaWidget_paid11))
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.mas_GPA_paid11[i].sizePolicy().hasHeightForWidth())
            self.mas_GPA_paid11[i].setSizePolicy(sizePolicy)
            self.mas_GPA_paid11[i].setMinimumSize(QtCore.QSize(70, 35))
            self.mas_GPA_paid11[i].setMaximumSize(QtCore.QSize(70, 16777215))
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(13)
            self.mas_GPA_paid11[i].setFont(font)
            self.mas_GPA_paid11[i].setStyleSheet("background-color: rgb(238, 238, 236);\n"
                                                 "border: 1px solid;")
            self.mas_GPA_paid11[i].setInputMask("")
            self.mas_GPA_paid11[i].setMaxLength(4)
            self.mas_GPA_paid11[i].setAlignment(QtCore.Qt.AlignCenter)
            self.mas_GPA_paid11[i].setObjectName(f"mas_GPA_paid11_{i}")
            self.gridLayout_7.addWidget(self.mas_GPA_paid11[i], i, 1, 1, 1)

        ## Label

        for i in range(self.SIZE_GRADE_POINT_AVERAG):
            self.lst_label_GPA_paid11.append(QtWidgets.QLabel(self.scrollAreaWidget_paid11))
            self.lst_label_GPA_paid11[i].setEnabled(True)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.lst_label_GPA_paid11[i].sizePolicy().hasHeightForWidth())
            self.lst_label_GPA_paid11[i].setSizePolicy(sizePolicy)
            self.lst_label_GPA_paid11[i].setMinimumSize(QtCore.QSize(850, 35))
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(11)
            self.lst_label_GPA_paid11[i].setFont(font)
            self.lst_label_GPA_paid11[i].setStyleSheet("background-color: rgb(211, 215, 207);")
            self.lst_label_GPA_paid11[i].setFrameShape(QtWidgets.QFrame.Box)
            self.lst_label_GPA_paid11[i].setObjectName(f"lst_label_GPA_paid11_{i}")
            self.gridLayout_7.addWidget(self.lst_label_GPA_paid11[i], i, 0, 1, 1)

        self.scrollArea_lbl_grade_point_averag_budget11_2.setWidget(self.scrollAreaWidget_paid11)
        self.gridLayout.addWidget(self.scrollArea_lbl_grade_point_averag_budget11_2, 17, 1, 1, 1)
        self.lbl_num_7 = QtWidgets.QLabel(self.scrollAreaInput)
        self.lbl_num_7.setMinimumSize(QtCore.QSize(0, 0))
        self.lbl_num_7.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_num_7.setFont(font)
        self.lbl_num_7.setStyleSheet("background-color: rgb(191, 192, 192);\n"
                                     "border: 1px solid;\n"
                                     "")
        self.lbl_num_7.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_num_7.setObjectName("lbl_num_7")
        self.gridLayout.addWidget(self.lbl_num_7, 14, 0, 1, 1)
        self.lbl_absentia = QtWidgets.QLabel(self.scrollAreaInput)
        self.lbl_absentia.setMinimumSize(QtCore.QSize(1000, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.lbl_absentia.setFont(font)
        self.lbl_absentia.setStyleSheet("background-color: rgb(198, 198, 198);\n"
                                        "border: 1px solid;")
        self.lbl_absentia.setObjectName("lbl_absentia")
        self.gridLayout.addWidget(self.lbl_absentia, 4, 1, 1, 1)
        self.lbl_parttime = QtWidgets.QLabel(self.scrollAreaInput)
        self.lbl_parttime.setMinimumSize(QtCore.QSize(1000, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.lbl_parttime.setFont(font)
        self.lbl_parttime.setStyleSheet("background-color: rgb(198, 198, 198);\n"
                                        "border: 1px solid;")
        self.lbl_parttime.setObjectName("lbl_parttime")
        self.gridLayout.addWidget(self.lbl_parttime, 3, 1, 1, 1)
        self.le_count_stud_paid = QtWidgets.QLineEdit(self.scrollAreaInput)
        self.le_count_stud_paid.setMinimumSize(QtCore.QSize(0, 35))
        self.le_count_stud_paid.setMaximumSize(QtCore.QSize(65, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.le_count_stud_paid.setFont(font)
        self.le_count_stud_paid.setStyleSheet("background-color: rgb(238, 238, 236);\n"
                                              "border: 1px solid;")
        self.le_count_stud_paid.setInputMask("")
        self.le_count_stud_paid.setMaxLength(4)
        self.le_count_stud_paid.setAlignment(QtCore.Qt.AlignCenter)
        self.le_count_stud_paid.setObjectName("le_count_stud_paid")
        self.gridLayout.addWidget(self.le_count_stud_paid, 6, 2, 1, 1)
        self.le_count_stud = QtWidgets.QLineEdit(self.scrollAreaInput)
        self.le_count_stud.setMinimumSize(QtCore.QSize(0, 35))
        self.le_count_stud.setMaximumSize(QtCore.QSize(65, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.le_count_stud.setFont(font)
        self.le_count_stud.setStyleSheet("background-color: rgb(238, 238, 236);\n"
                                         "border: 1px solid;")
        self.le_count_stud.setInputMask("")
        self.le_count_stud.setMaxLength(4)
        self.le_count_stud.setAlignment(QtCore.Qt.AlignCenter)
        self.le_count_stud.setObjectName("le_count_stud")
        self.gridLayout.addWidget(self.le_count_stud, 1, 2, 1, 1)
        self.le_grade_point_averag_budget11 = QtWidgets.QLineEdit(self.scrollAreaInput)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_grade_point_averag_budget11.sizePolicy().hasHeightForWidth())
        self.le_grade_point_averag_budget11.setSizePolicy(sizePolicy)
        self.le_grade_point_averag_budget11.setMinimumSize(QtCore.QSize(0, 40))
        self.le_grade_point_averag_budget11.setMaximumSize(QtCore.QSize(65, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.le_grade_point_averag_budget11.setFont(font)
        self.le_grade_point_averag_budget11.setStyleSheet("background-color: rgb(238, 238, 236);\n"
                                                          "border: 1px solid;")
        self.le_grade_point_averag_budget11.setInputMask("")
        self.le_grade_point_averag_budget11.setMaxLength(4)
        self.le_grade_point_averag_budget11.setAlignment(QtCore.Qt.AlignCenter)
        self.le_grade_point_averag_budget11.setObjectName("le_grade_point_averag_budget11")
        self.gridLayout.addWidget(self.le_grade_point_averag_budget11, 14, 2, 1, 1)
        self.lbl_count_stud_paid = QtWidgets.QLabel(self.scrollAreaInput)
        self.lbl_count_stud_paid.setMinimumSize(QtCore.QSize(1000, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.lbl_count_stud_paid.setFont(font)
        self.lbl_count_stud_paid.setStyleSheet("background-color: rgb(198, 198, 198);\n"
                                               "border: 1px solid;")
        self.lbl_count_stud_paid.setObjectName("lbl_count_stud_paid")
        self.gridLayout.addWidget(self.lbl_count_stud_paid, 6, 1, 1, 1)
        self.scrollArea_top50 = QtWidgets.QScrollArea(self.scrollAreaInput)
        self.scrollArea_top50.setMinimumSize(QtCore.QSize(1000, 310))
        self.scrollArea_top50.setMaximumSize(QtCore.QSize(16777215, 310))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.scrollArea_top50.setFont(font)
        self.scrollArea_top50.setFrameShape(QtWidgets.QFrame.Box)
        self.scrollArea_top50.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea_top50.setWidgetResizable(True)
        self.scrollArea_top50.setObjectName("scrollArea_top50")
        self.scrollAreaWidget_top50 = QtWidgets.QWidget()
        self.scrollAreaWidget_top50.setGeometry(QtCore.QRect(0, 0, 1003, 308))
        self.scrollAreaWidget_top50.setObjectName("scrollAreaWidget_top50")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidget_top50)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_22 = QtWidgets.QLabel(self.scrollAreaWidget_top50)
        self.label_22.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        self.label_22.setMinimumSize(QtCore.QSize(850, 35))
        self.label_22.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("background-color: rgb(211, 215, 207);\n"
                                    "")
        self.label_22.setFrameShape(QtWidgets.QFrame.Box)
        self.label_22.setObjectName("label_22")
        self.gridLayout_2.addWidget(self.label_22, 0, 0, 1, 1)

        ## ARRAY TOP 50
        ############################################################
        for i in range(self.SIZE_TOP50):
            self.mas_top50.append(QtWidgets.QLineEdit(self.scrollAreaWidget_top50))
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.mas_top50[i].sizePolicy().hasHeightForWidth())
            self.mas_top50[i].setSizePolicy(sizePolicy)
            self.mas_top50[i].setMinimumSize(QtCore.QSize(70, 35))
            self.mas_top50[i].setMaximumSize(QtCore.QSize(70, 16777215))

            font.setPointSize(13)
            self.mas_top50[i].setFont(font)
            self.mas_top50[i].setStyleSheet("background-color: rgb(238, 238, 236);\n"
                                            "border: 1px solid;")
            self.mas_top50[i].setMaxLength(4)
            self.mas_top50[i].setAlignment(QtCore.Qt.AlignCenter)
            self.mas_top50[i].setObjectName(f"mas_top50_{i}")
            self.gridLayout_2.addWidget(self.mas_top50[i], i, 1, 1, 1)

            ## LABEL
            self.lst_label_top50 = [QtWidgets.QLabel(self.scrollAreaWidget_top50) for _ in
                                    range(self.SIZE_TOP50)]
            for i in range(self.SIZE_TOP50):
                self.lst_label_top50[i].setEnabled(True)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.lst_label_top50[i].sizePolicy().hasHeightForWidth())
                self.lst_label_top50[i].setSizePolicy(sizePolicy)
                self.lst_label_top50[i].setMinimumSize(QtCore.QSize(850, 35))
                self.lst_label_top50[i].setMaximumSize(QtCore.QSize(16777215, 16777215))

                font.setPointSize(11)
                self.lst_label_top50[i].setFont(font)
                self.lst_label_top50[i].setStyleSheet("background-color: rgb(211, 215, 207);\n"
                                                      "")

                self.lst_label_top50[i].setFrameShape(QtWidgets.QFrame.Box)
                self.lst_label_top50[i].setObjectName(f"lst_label_top50_{i}")
                self.gridLayout_2.addWidget(self.lst_label_top50[i], i, 0, 1, 1)

        self.scrollArea_top50.setWidget(self.scrollAreaWidget_top50)
        self.gridLayout.addWidget(self.scrollArea_top50, 8, 1, 1, 1)
        self.lbl_count_stud = QtWidgets.QLabel(self.scrollAreaInput)
        self.lbl_count_stud.setMinimumSize(QtCore.QSize(1000, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.lbl_count_stud.setFont(font)
        self.lbl_count_stud.setStyleSheet("background-color: rgb(198, 198, 198);\n"
                                          "border: 1px solid;")
        self.lbl_count_stud.setObjectName("lbl_count_stud")
        self.gridLayout.addWidget(self.lbl_count_stud, 1, 1, 1, 1)
        self.lbl_grade_point_averag_paid11 = QtWidgets.QLabel(self.scrollAreaInput)
        self.lbl_grade_point_averag_paid11.setMinimumSize(QtCore.QSize(1000, 50))
        self.lbl_grade_point_averag_paid11.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.lbl_grade_point_averag_paid11.setFont(font)
        self.lbl_grade_point_averag_paid11.setStyleSheet("background-color: rgb(198, 198, 255);")
        self.lbl_grade_point_averag_paid11.setFrameShape(QtWidgets.QFrame.Box)
        self.lbl_grade_point_averag_paid11.setScaledContents(False)
        self.lbl_grade_point_averag_paid11.setWordWrap(True)
        self.lbl_grade_point_averag_paid11.setObjectName("lbl_grade_point_averag_paid11")
        self.gridLayout.addWidget(self.lbl_grade_point_averag_paid11, 16, 1, 1, 1)
        self.lbl_title3 = QtWidgets.QLabel(self.scrollAreaInput)
        self.lbl_title3.setMinimumSize(QtCore.QSize(0, 40))
        self.lbl_title3.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_title3.setFont(font)
        self.lbl_title3.setStyleSheet("background-color: rgb(92, 92, 92);\n"
                                      "border: 1px solid;\n"
                                      "")
        self.lbl_title3.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_title3.setWordWrap(True)
        self.lbl_title3.setObjectName("lbl_title3")
        self.gridLayout.addWidget(self.lbl_title3, 0, 2, 1, 1)
        self.lbl_num_6 = QtWidgets.QLabel(self.scrollAreaInput)
        self.lbl_num_6.setMinimumSize(QtCore.QSize(0, 0))
        self.lbl_num_6.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_num_6.setFont(font)
        self.lbl_num_6.setStyleSheet("background-color: rgb(191, 192, 192);\n"
                                     "border: 1px solid;\n"
                                     "")
        self.lbl_num_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_num_6.setObjectName("lbl_num_6")
        self.gridLayout.addWidget(self.lbl_num_6, 12, 0, 1, 1)
        self.le_count_stud_absentia = QtWidgets.QLineEdit(self.scrollAreaInput)
        self.le_count_stud_absentia.setMinimumSize(QtCore.QSize(0, 35))
        self.le_count_stud_absentia.setMaximumSize(QtCore.QSize(65, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.le_count_stud_absentia.setFont(font)
        self.le_count_stud_absentia.setStyleSheet("background-color: rgb(238, 238, 236);\n"
                                                  "border: 1px solid;")
        self.le_count_stud_absentia.setInputMask("")
        self.le_count_stud_absentia.setMaxLength(4)
        self.le_count_stud_absentia.setAlignment(QtCore.Qt.AlignCenter)
        self.le_count_stud_absentia.setObjectName("le_count_stud_absentia")
        self.gridLayout.addWidget(self.le_count_stud_absentia, 3, 2, 1, 1)
        self.lbl_grade_point_averag_budget9 = QtWidgets.QLabel(self.scrollAreaInput)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_grade_point_averag_budget9.sizePolicy().hasHeightForWidth())
        self.lbl_grade_point_averag_budget9.setSizePolicy(sizePolicy)
        self.lbl_grade_point_averag_budget9.setMinimumSize(QtCore.QSize(1000, 50))
        self.lbl_grade_point_averag_budget9.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.lbl_grade_point_averag_budget9.setFont(font)
        self.lbl_grade_point_averag_budget9.setStyleSheet("background-color: rgb(198, 198, 255);")
        self.lbl_grade_point_averag_budget9.setFrameShape(QtWidgets.QFrame.Box)
        self.lbl_grade_point_averag_budget9.setScaledContents(False)
        self.lbl_grade_point_averag_budget9.setWordWrap(True)
        self.lbl_grade_point_averag_budget9.setObjectName("lbl_grade_point_averag_budget9")
        self.gridLayout.addWidget(self.lbl_grade_point_averag_budget9, 9, 1, 1, 1)
        self.lbl_num_1_3 = QtWidgets.QLabel(self.scrollAreaInput)
        self.lbl_num_1_3.setMinimumSize(QtCore.QSize(0, 0))
        self.lbl_num_1_3.setMaximumSize(QtCore.QSize(50, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_num_1_3.setFont(font)
        self.lbl_num_1_3.setStyleSheet("background-color: rgb(191, 192, 192);\n"
                                       "border: 1px solid;\n"
                                       "")
        self.lbl_num_1_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_num_1_3.setObjectName("lbl_num_1_3")
        self.gridLayout.addWidget(self.lbl_num_1_3, 3, 0, 1, 1)
        self.lbl_num_1_5 = QtWidgets.QLabel(self.scrollAreaInput)
        self.lbl_num_1_5.setMinimumSize(QtCore.QSize(0, 0))
        self.lbl_num_1_5.setMaximumSize(QtCore.QSize(50, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_num_1_5.setFont(font)
        self.lbl_num_1_5.setStyleSheet("background-color: rgb(191, 192, 192);\n"
                                       "border: 1px solid;\n"
                                       "")
        self.lbl_num_1_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_num_1_5.setObjectName("lbl_num_1_5")
        self.gridLayout.addWidget(self.lbl_num_1_5, 5, 0, 1, 1)
        self.lbl_num_1_1 = QtWidgets.QLabel(self.scrollAreaInput)
        self.lbl_num_1_1.setMinimumSize(QtCore.QSize(0, 0))
        self.lbl_num_1_1.setMaximumSize(QtCore.QSize(50, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_num_1_1.setFont(font)
        self.lbl_num_1_1.setStyleSheet("background-color: rgb(191, 192, 192);\n"
                                       "border: 1px solid;\n"
                                       "")
        self.lbl_num_1_1.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_num_1_1.setObjectName("lbl_num_1_1")
        self.gridLayout.addWidget(self.lbl_num_1_1, 1, 0, 1, 1)
        self.lbl_grade_point_averag_budget11 = QtWidgets.QLabel(self.scrollAreaInput)
        self.lbl_grade_point_averag_budget11.setMinimumSize(QtCore.QSize(1000, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.lbl_grade_point_averag_budget11.setFont(font)
        self.lbl_grade_point_averag_budget11.setStyleSheet("background-color: rgb(198, 198, 255);")
        self.lbl_grade_point_averag_budget11.setFrameShape(QtWidgets.QFrame.Box)
        self.lbl_grade_point_averag_budget11.setScaledContents(False)
        self.lbl_grade_point_averag_budget11.setWordWrap(True)
        self.lbl_grade_point_averag_budget11.setObjectName("lbl_grade_point_averag_budget11")
        self.gridLayout.addWidget(self.lbl_grade_point_averag_budget11, 14, 1, 1, 1)
        self.le_count_stud_fulltime = QtWidgets.QLineEdit(self.scrollAreaInput)
        self.le_count_stud_fulltime.setMinimumSize(QtCore.QSize(0, 35))
        self.le_count_stud_fulltime.setMaximumSize(QtCore.QSize(65, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.le_count_stud_fulltime.setFont(font)
        self.le_count_stud_fulltime.setStyleSheet("background-color: rgb(238, 238, 236);\n"
                                                  "border: 1px solid;")
        self.le_count_stud_fulltime.setInputMask("")
        self.le_count_stud_fulltime.setMaxLength(4)
        self.le_count_stud_fulltime.setAlignment(QtCore.Qt.AlignCenter)
        self.le_count_stud_fulltime.setObjectName("le_count_stud_fulltime")
        self.gridLayout.addWidget(self.le_count_stud_fulltime, 2, 2, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaInput)
        self.verticalLayout_7.addWidget(self.scrollArea)
        self.frame_btn = QtWidgets.QFrame(self.page_input)
        self.frame_btn.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.frame_btn.setFont(font)
        self.frame_btn.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_btn.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_btn.setObjectName("frame_btn")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_btn)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_input_save = QtWidgets.QPushButton(self.frame_btn)
        self.btn_input_save.setMinimumSize(QtCore.QSize(110, 45))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.btn_input_save.setFont(font)
        self.btn_input_save.setStyleSheet("QPushButton {\n"
                                          "    color: rgb(255, 255, 255);\n"
                                          "    background-color: rgb(35, 35, 35);\n"
                                          "    border: 0px solid;\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "    background-color: rgb(85, 170, 255);\n"
                                          "}")
        self.btn_input_save.setObjectName("btn_input_save")
        self.horizontalLayout_3.addWidget(self.btn_input_save)
        self.btn_input_next = QtWidgets.QPushButton(self.frame_btn)
        self.btn_input_next.setMinimumSize(QtCore.QSize(110, 45))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.btn_input_next.setFont(font)
        self.btn_input_next.setStyleSheet("QPushButton {\n"
                                          "    color: rgb(255, 255, 255);\n"
                                          "    background-color: rgb(35, 35, 35);\n"
                                          "    border: 0px solid;\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "    background-color: rgb(85, 170, 255);\n"
                                          "}")
        self.btn_input_next.setObjectName("btn_input_next")
        self.horizontalLayout_3.addWidget(self.btn_input_next)
        self.verticalLayout_7.addWidget(self.frame_btn, 0, QtCore.Qt.AlignRight)
        self.Pages_Widget.addWidget(self.page_input)
        self.page_output = QtWidgets.QWidget()
        self.page_output.setObjectName("page_output")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_output)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_top_output = QtWidgets.QFrame(self.page_output)
        self.frame_top_output.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_top_output.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_output.setObjectName("frame_top_output")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_top_output)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.lbl_title1_2 = QtWidgets.QLabel(self.frame_top_output)
        self.lbl_title1_2.setMinimumSize(QtCore.QSize(50, 40))
        self.lbl_title1_2.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_title1_2.setFont(font)
        self.lbl_title1_2.setStyleSheet("background-color: rgb(92, 92, 92);\n"
                                        "border: 1px solid;\n"
                                        "")
        self.lbl_title1_2.setFrameShape(QtWidgets.QFrame.Box)
        self.lbl_title1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_title1_2.setObjectName("lbl_title1_2")
        self.gridLayout_6.addWidget(self.lbl_title1_2, 0, 0, 1, 1)
        self.lbl_title2_2 = QtWidgets.QLabel(self.frame_top_output)
        self.lbl_title2_2.setMinimumSize(QtCore.QSize(1000, 40))
        self.lbl_title2_2.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_title2_2.setFont(font)
        self.lbl_title2_2.setStyleSheet("background-color: rgb(92, 92, 92);\n"
                                        "border: 1px solid;\n"
                                        "")
        self.lbl_title2_2.setFrameShape(QtWidgets.QFrame.Box)
        self.lbl_title2_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_title2_2.setObjectName("lbl_title2_2")
        self.gridLayout_6.addWidget(self.lbl_title2_2, 0, 1, 1, 1)
        self.lbl_title3_2 = QtWidgets.QLabel(self.frame_top_output)
        self.lbl_title3_2.setMinimumSize(QtCore.QSize(100, 40))
        self.lbl_title3_2.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_title3_2.setFont(font)
        self.lbl_title3_2.setStyleSheet("background-color: rgb(92, 92, 92);\n"
                                        "border: 1px solid;\n"
                                        "")
        self.lbl_title3_2.setFrameShape(QtWidgets.QFrame.Box)
        self.lbl_title3_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_title3_2.setWordWrap(True)
        self.lbl_title3_2.setObjectName("lbl_title3_2")
        self.gridLayout_6.addWidget(self.lbl_title3_2, 0, 2, 1, 1)
        self.lbl_num1_1 = QtWidgets.QLabel(self.frame_top_output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_num1_1.sizePolicy().hasHeightForWidth())
        self.lbl_num1_1.setSizePolicy(sizePolicy)
        self.lbl_num1_1.setMinimumSize(QtCore.QSize(50, 40))
        self.lbl_num1_1.setMaximumSize(QtCore.QSize(50, 45))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_num1_1.setFont(font)
        self.lbl_num1_1.setStyleSheet("background-color: rgb(191, 192, 192);\n"
                                      "border: 1px solid;\n"
                                      "")
        self.lbl_num1_1.setFrameShape(QtWidgets.QFrame.Box)
        self.lbl_num1_1.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_num1_1.setObjectName("lbl_num1_1")
        self.gridLayout_6.addWidget(self.lbl_num1_1, 1, 0, 1, 1)
        self.lbl_count_stud_2 = QtWidgets.QLabel(self.frame_top_output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_count_stud_2.sizePolicy().hasHeightForWidth())
        self.lbl_count_stud_2.setSizePolicy(sizePolicy)
        self.lbl_count_stud_2.setMinimumSize(QtCore.QSize(1000, 0))
        self.lbl_count_stud_2.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lbl_count_stud_2.setFont(font)
        self.lbl_count_stud_2.setStyleSheet("background-color: rgb(198, 198, 198);")
        self.lbl_count_stud_2.setFrameShape(QtWidgets.QFrame.Box)
        self.lbl_count_stud_2.setObjectName("lbl_count_stud_2")
        self.gridLayout_6.addWidget(self.lbl_count_stud_2, 1, 1, 1, 1)
        self.lo_count_stud = QtWidgets.QLabel(self.frame_top_output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lo_count_stud.sizePolicy().hasHeightForWidth())
        self.lo_count_stud.setSizePolicy(sizePolicy)
        self.lo_count_stud.setMinimumSize(QtCore.QSize(0, 0))
        self.lo_count_stud.setMaximumSize(QtCore.QSize(100, 45))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lo_count_stud.setFont(font)
        self.lo_count_stud.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.lo_count_stud.setFrameShape(QtWidgets.QFrame.Box)
        self.lo_count_stud.setAlignment(QtCore.Qt.AlignCenter)
        self.lo_count_stud.setObjectName("lo_count_stud")
        self.gridLayout_6.addWidget(self.lo_count_stud, 1, 2, 1, 1)
        self.lbl_num1_2 = QtWidgets.QLabel(self.frame_top_output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_num1_2.sizePolicy().hasHeightForWidth())
        self.lbl_num1_2.setSizePolicy(sizePolicy)
        self.lbl_num1_2.setMinimumSize(QtCore.QSize(50, 40))
        self.lbl_num1_2.setMaximumSize(QtCore.QSize(50, 45))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_num1_2.setFont(font)
        self.lbl_num1_2.setStyleSheet("background-color: rgb(191, 192, 192);\n"
                                      "border: 1px solid;\n"
                                      "")
        self.lbl_num1_2.setFrameShape(QtWidgets.QFrame.Box)
        self.lbl_num1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_num1_2.setObjectName("lbl_num1_2")
        self.gridLayout_6.addWidget(self.lbl_num1_2, 2, 0, 1, 1)
        self.lbl_proportion_stud_fulltime = QtWidgets.QLabel(self.frame_top_output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_proportion_stud_fulltime.sizePolicy().hasHeightForWidth())
        self.lbl_proportion_stud_fulltime.setSizePolicy(sizePolicy)
        self.lbl_proportion_stud_fulltime.setMinimumSize(QtCore.QSize(1000, 0))
        self.lbl_proportion_stud_fulltime.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lbl_proportion_stud_fulltime.setFont(font)
        self.lbl_proportion_stud_fulltime.setStyleSheet("background-color: rgb(198, 198, 198);")
        self.lbl_proportion_stud_fulltime.setFrameShape(QtWidgets.QFrame.Box)
        self.lbl_proportion_stud_fulltime.setObjectName("lbl_proportion_stud_fulltime")
        self.gridLayout_6.addWidget(self.lbl_proportion_stud_fulltime, 2, 1, 1, 1)
        self.lo_proportion_stud_fulltime = QtWidgets.QLabel(self.frame_top_output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lo_proportion_stud_fulltime.sizePolicy().hasHeightForWidth())
        self.lo_proportion_stud_fulltime.setSizePolicy(sizePolicy)
        self.lo_proportion_stud_fulltime.setMinimumSize(QtCore.QSize(0, 0))
        self.lo_proportion_stud_fulltime.setMaximumSize(QtCore.QSize(100, 45))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lo_proportion_stud_fulltime.setFont(font)
        self.lo_proportion_stud_fulltime.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.lo_proportion_stud_fulltime.setFrameShape(QtWidgets.QFrame.Box)
        self.lo_proportion_stud_fulltime.setAlignment(QtCore.Qt.AlignCenter)
        self.lo_proportion_stud_fulltime.setObjectName("lo_proportion_stud_fulltime")
        self.gridLayout_6.addWidget(self.lo_proportion_stud_fulltime, 2, 2, 1, 1)
        self.lbl_num1_3 = QtWidgets.QLabel(self.frame_top_output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_num1_3.sizePolicy().hasHeightForWidth())
        self.lbl_num1_3.setSizePolicy(sizePolicy)
        self.lbl_num1_3.setMinimumSize(QtCore.QSize(50, 40))
        self.lbl_num1_3.setMaximumSize(QtCore.QSize(50, 45))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_num1_3.setFont(font)
        self.lbl_num1_3.setStyleSheet("background-color: rgb(191, 192, 192);\n"
                                      "border: 1px solid;\n"
                                      "")
        self.lbl_num1_3.setFrameShape(QtWidgets.QFrame.Box)
        self.lbl_num1_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_num1_3.setObjectName("lbl_num1_3")
        self.gridLayout_6.addWidget(self.lbl_num1_3, 3, 0, 1, 1)
        self.lbl_proportion_stud_budget = QtWidgets.QLabel(self.frame_top_output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_proportion_stud_budget.sizePolicy().hasHeightForWidth())
        self.lbl_proportion_stud_budget.setSizePolicy(sizePolicy)
        self.lbl_proportion_stud_budget.setMinimumSize(QtCore.QSize(1000, 0))
        self.lbl_proportion_stud_budget.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lbl_proportion_stud_budget.setFont(font)
        self.lbl_proportion_stud_budget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lbl_proportion_stud_budget.setAcceptDrops(False)
        self.lbl_proportion_stud_budget.setAutoFillBackground(False)
        self.lbl_proportion_stud_budget.setStyleSheet("background-color: rgb(198, 198, 198);")
        self.lbl_proportion_stud_budget.setFrameShape(QtWidgets.QFrame.Box)
        self.lbl_proportion_stud_budget.setWordWrap(True)
        self.lbl_proportion_stud_budget.setObjectName("lbl_proportion_stud_budget")
        self.gridLayout_6.addWidget(self.lbl_proportion_stud_budget, 3, 1, 1, 1)
        self.lo_proportion_stud_budget = QtWidgets.QLabel(self.frame_top_output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lo_proportion_stud_budget.sizePolicy().hasHeightForWidth())
        self.lo_proportion_stud_budget.setSizePolicy(sizePolicy)
        self.lo_proportion_stud_budget.setMinimumSize(QtCore.QSize(0, 0))
        self.lo_proportion_stud_budget.setMaximumSize(QtCore.QSize(100, 45))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lo_proportion_stud_budget.setFont(font)
        self.lo_proportion_stud_budget.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.lo_proportion_stud_budget.setFrameShape(QtWidgets.QFrame.Box)
        self.lo_proportion_stud_budget.setAlignment(QtCore.Qt.AlignCenter)
        self.lo_proportion_stud_budget.setObjectName("lo_proportion_stud_budget")
        self.gridLayout_6.addWidget(self.lo_proportion_stud_budget, 3, 2, 1, 1)
        self.lbl_num1_4 = QtWidgets.QLabel(self.frame_top_output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_num1_4.sizePolicy().hasHeightForWidth())
        self.lbl_num1_4.setSizePolicy(sizePolicy)
        self.lbl_num1_4.setMinimumSize(QtCore.QSize(50, 40))
        self.lbl_num1_4.setMaximumSize(QtCore.QSize(50, 45))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_num1_4.setFont(font)
        self.lbl_num1_4.setStyleSheet("background-color: rgb(191, 192, 192);\n"
                                      "border: 1px solid;\n"
                                      "")
        self.lbl_num1_4.setFrameShape(QtWidgets.QFrame.Box)
        self.lbl_num1_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_num1_4.setObjectName("lbl_num1_4")
        self.gridLayout_6.addWidget(self.lbl_num1_4, 4, 0, 1, 1)
        self.lbl_count_stud_top50 = QtWidgets.QLabel(self.frame_top_output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_count_stud_top50.sizePolicy().hasHeightForWidth())
        self.lbl_count_stud_top50.setSizePolicy(sizePolicy)
        self.lbl_count_stud_top50.setMinimumSize(QtCore.QSize(1000, 0))
        self.lbl_count_stud_top50.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lbl_count_stud_top50.setFont(font)
        self.lbl_count_stud_top50.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lbl_count_stud_top50.setAcceptDrops(False)
        self.lbl_count_stud_top50.setAutoFillBackground(False)
        self.lbl_count_stud_top50.setStyleSheet("background-color: rgb(198, 198, 198);")
        self.lbl_count_stud_top50.setFrameShape(QtWidgets.QFrame.Box)
        self.lbl_count_stud_top50.setWordWrap(True)
        self.lbl_count_stud_top50.setObjectName("lbl_count_stud_top50")
        self.gridLayout_6.addWidget(self.lbl_count_stud_top50, 4, 1, 1, 1)
        self.lo_count_stud_top50 = QtWidgets.QLabel(self.frame_top_output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lo_count_stud_top50.sizePolicy().hasHeightForWidth())
        self.lo_count_stud_top50.setSizePolicy(sizePolicy)
        self.lo_count_stud_top50.setMinimumSize(QtCore.QSize(0, 0))
        self.lo_count_stud_top50.setMaximumSize(QtCore.QSize(100, 45))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lo_count_stud_top50.setFont(font)
        self.lo_count_stud_top50.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.lo_count_stud_top50.setFrameShape(QtWidgets.QFrame.Box)
        self.lo_count_stud_top50.setAlignment(QtCore.Qt.AlignCenter)
        self.lo_count_stud_top50.setObjectName("lo_count_stud_top50")
        self.gridLayout_6.addWidget(self.lo_count_stud_top50, 4, 2, 1, 1)
        self.lbl_num1_4_1 = QtWidgets.QLabel(self.frame_top_output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_num1_4_1.sizePolicy().hasHeightForWidth())
        self.lbl_num1_4_1.setSizePolicy(sizePolicy)
        self.lbl_num1_4_1.setMinimumSize(QtCore.QSize(50, 40))
        self.lbl_num1_4_1.setMaximumSize(QtCore.QSize(50, 45))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_num1_4_1.setFont(font)
        self.lbl_num1_4_1.setStyleSheet("background-color: rgb(191, 192, 192);\n"
                                        "border: 1px solid;\n"
                                        "")
        self.lbl_num1_4_1.setFrameShape(QtWidgets.QFrame.Box)
        self.lbl_num1_4_1.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_num1_4_1.setObjectName("lbl_num1_4_1")
        self.gridLayout_6.addWidget(self.lbl_num1_4_1, 5, 0, 1, 1)
        self.lbl_proportion_stud_top50 = QtWidgets.QLabel(self.frame_top_output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_proportion_stud_top50.sizePolicy().hasHeightForWidth())
        self.lbl_proportion_stud_top50.setSizePolicy(sizePolicy)
        self.lbl_proportion_stud_top50.setMinimumSize(QtCore.QSize(1000, 0))
        self.lbl_proportion_stud_top50.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lbl_proportion_stud_top50.setFont(font)
        self.lbl_proportion_stud_top50.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lbl_proportion_stud_top50.setAcceptDrops(False)
        self.lbl_proportion_stud_top50.setAutoFillBackground(False)
        self.lbl_proportion_stud_top50.setStyleSheet("background-color: rgb(198, 198, 198);")
        self.lbl_proportion_stud_top50.setFrameShape(QtWidgets.QFrame.Box)
        self.lbl_proportion_stud_top50.setWordWrap(True)
        self.lbl_proportion_stud_top50.setObjectName("lbl_proportion_stud_top50")
        self.gridLayout_6.addWidget(self.lbl_proportion_stud_top50, 5, 1, 1, 1)
        self.lo_proportion_stud_top50 = QtWidgets.QLabel(self.frame_top_output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lo_proportion_stud_top50.sizePolicy().hasHeightForWidth())
        self.lo_proportion_stud_top50.setSizePolicy(sizePolicy)
        self.lo_proportion_stud_top50.setMinimumSize(QtCore.QSize(0, 0))
        self.lo_proportion_stud_top50.setMaximumSize(QtCore.QSize(100, 45))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lo_proportion_stud_top50.setFont(font)
        self.lo_proportion_stud_top50.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.lo_proportion_stud_top50.setFrameShape(QtWidgets.QFrame.Box)
        self.lo_proportion_stud_top50.setAlignment(QtCore.Qt.AlignCenter)
        self.lo_proportion_stud_top50.setObjectName("lo_proportion_stud_top50")
        self.gridLayout_6.addWidget(self.lo_proportion_stud_top50, 5, 2, 1, 1)
        self.lbl_num1_5 = QtWidgets.QLabel(self.frame_top_output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_num1_5.sizePolicy().hasHeightForWidth())
        self.lbl_num1_5.setSizePolicy(sizePolicy)
        self.lbl_num1_5.setMinimumSize(QtCore.QSize(50, 40))
        self.lbl_num1_5.setMaximumSize(QtCore.QSize(50, 45))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_num1_5.setFont(font)
        self.lbl_num1_5.setStyleSheet("background-color: rgb(191, 192, 192);\n"
                                      "border: 1px solid;\n"
                                      "")
        self.lbl_num1_5.setFrameShape(QtWidgets.QFrame.Box)
        self.lbl_num1_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_num1_5.setObjectName("lbl_num1_5")
        self.gridLayout_6.addWidget(self.lbl_num1_5, 6, 0, 1, 1)
        self.lbl_GPA_budget9 = QtWidgets.QLabel(self.frame_top_output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_GPA_budget9.sizePolicy().hasHeightForWidth())
        self.lbl_GPA_budget9.setSizePolicy(sizePolicy)
        self.lbl_GPA_budget9.setMinimumSize(QtCore.QSize(1000, 0))
        self.lbl_GPA_budget9.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lbl_GPA_budget9.setFont(font)
        self.lbl_GPA_budget9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lbl_GPA_budget9.setAcceptDrops(False)
        self.lbl_GPA_budget9.setAutoFillBackground(False)
        self.lbl_GPA_budget9.setStyleSheet("background-color: rgb(198, 198, 198);")
        self.lbl_GPA_budget9.setFrameShape(QtWidgets.QFrame.Box)
        self.lbl_GPA_budget9.setWordWrap(True)
        self.lbl_GPA_budget9.setObjectName("lbl_GPA_budget9")
        self.gridLayout_6.addWidget(self.lbl_GPA_budget9, 6, 1, 1, 1)
        self.lo_GPA_budget9 = QtWidgets.QLabel(self.frame_top_output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lo_GPA_budget9.sizePolicy().hasHeightForWidth())
        self.lo_GPA_budget9.setSizePolicy(sizePolicy)
        self.lo_GPA_budget9.setMinimumSize(QtCore.QSize(0, 0))
        self.lo_GPA_budget9.setMaximumSize(QtCore.QSize(100, 45))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lo_GPA_budget9.setFont(font)
        self.lo_GPA_budget9.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.lo_GPA_budget9.setFrameShape(QtWidgets.QFrame.Box)
        self.lo_GPA_budget9.setAlignment(QtCore.Qt.AlignCenter)
        self.lo_GPA_budget9.setObjectName("lo_GPA_budget9")
        self.gridLayout_6.addWidget(self.lo_GPA_budget9, 6, 2, 1, 1)
        self.lbl_num1_5_1 = QtWidgets.QLabel(self.frame_top_output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_num1_5_1.sizePolicy().hasHeightForWidth())
        self.lbl_num1_5_1.setSizePolicy(sizePolicy)
        self.lbl_num1_5_1.setMinimumSize(QtCore.QSize(50, 40))
        self.lbl_num1_5_1.setMaximumSize(QtCore.QSize(50, 45))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_num1_5_1.setFont(font)
        self.lbl_num1_5_1.setStyleSheet("background-color: rgb(191, 192, 192);\n"
                                        "border: 1px solid;\n"
                                        "")
        self.lbl_num1_5_1.setFrameShape(QtWidgets.QFrame.Box)
        self.lbl_num1_5_1.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_num1_5_1.setObjectName("lbl_num1_5_1")
        self.gridLayout_6.addWidget(self.lbl_num1_5_1, 7, 0, 1, 1)
        self.lbl_GPA_paid9 = QtWidgets.QLabel(self.frame_top_output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_GPA_paid9.sizePolicy().hasHeightForWidth())
        self.lbl_GPA_paid9.setSizePolicy(sizePolicy)
        self.lbl_GPA_paid9.setMinimumSize(QtCore.QSize(1000, 0))
        self.lbl_GPA_paid9.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lbl_GPA_paid9.setFont(font)
        self.lbl_GPA_paid9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lbl_GPA_paid9.setAcceptDrops(False)
        self.lbl_GPA_paid9.setAutoFillBackground(False)
        self.lbl_GPA_paid9.setStyleSheet("background-color: rgb(198, 198, 198);")
        self.lbl_GPA_paid9.setFrameShape(QtWidgets.QFrame.Box)
        self.lbl_GPA_paid9.setWordWrap(True)
        self.lbl_GPA_paid9.setObjectName("lbl_GPA_paid9")
        self.gridLayout_6.addWidget(self.lbl_GPA_paid9, 7, 1, 1, 1)
        self.lo_GPA_paid9 = QtWidgets.QLabel(self.frame_top_output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lo_GPA_paid9.sizePolicy().hasHeightForWidth())
        self.lo_GPA_paid9.setSizePolicy(sizePolicy)
        self.lo_GPA_paid9.setMinimumSize(QtCore.QSize(0, 0))
        self.lo_GPA_paid9.setMaximumSize(QtCore.QSize(100, 45))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lo_GPA_paid9.setFont(font)
        self.lo_GPA_paid9.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.lo_GPA_paid9.setFrameShape(QtWidgets.QFrame.Box)
        self.lo_GPA_paid9.setAlignment(QtCore.Qt.AlignCenter)
        self.lo_GPA_paid9.setObjectName("lo_GPA_paid9")
        self.gridLayout_6.addWidget(self.lo_GPA_paid9, 7, 2, 1, 1)
        self.lbl_num1_6 = QtWidgets.QLabel(self.frame_top_output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_num1_6.sizePolicy().hasHeightForWidth())
        self.lbl_num1_6.setSizePolicy(sizePolicy)
        self.lbl_num1_6.setMinimumSize(QtCore.QSize(50, 40))
        self.lbl_num1_6.setMaximumSize(QtCore.QSize(50, 45))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_num1_6.setFont(font)
        self.lbl_num1_6.setStyleSheet("background-color: rgb(191, 192, 192);\n"
                                      "border: 1px solid;\n"
                                      "")
        self.lbl_num1_6.setFrameShape(QtWidgets.QFrame.Box)
        self.lbl_num1_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_num1_6.setObjectName("lbl_num1_6")
        self.gridLayout_6.addWidget(self.lbl_num1_6, 8, 0, 1, 1)
        self.lbl_GPA_budget11 = QtWidgets.QLabel(self.frame_top_output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_GPA_budget11.sizePolicy().hasHeightForWidth())
        self.lbl_GPA_budget11.setSizePolicy(sizePolicy)
        self.lbl_GPA_budget11.setMinimumSize(QtCore.QSize(1000, 0))
        self.lbl_GPA_budget11.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lbl_GPA_budget11.setFont(font)
        self.lbl_GPA_budget11.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lbl_GPA_budget11.setAcceptDrops(False)
        self.lbl_GPA_budget11.setAutoFillBackground(False)
        self.lbl_GPA_budget11.setStyleSheet("background-color: rgb(198, 198, 198);")
        self.lbl_GPA_budget11.setFrameShape(QtWidgets.QFrame.Box)
        self.lbl_GPA_budget11.setWordWrap(True)
        self.lbl_GPA_budget11.setObjectName("lbl_GPA_budget11")
        self.gridLayout_6.addWidget(self.lbl_GPA_budget11, 8, 1, 1, 1)
        self.lo_GPA_budget11 = QtWidgets.QLabel(self.frame_top_output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lo_GPA_budget11.sizePolicy().hasHeightForWidth())
        self.lo_GPA_budget11.setSizePolicy(sizePolicy)
        self.lo_GPA_budget11.setMinimumSize(QtCore.QSize(0, 0))
        self.lo_GPA_budget11.setMaximumSize(QtCore.QSize(100, 45))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lo_GPA_budget11.setFont(font)
        self.lo_GPA_budget11.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.lo_GPA_budget11.setFrameShape(QtWidgets.QFrame.Box)
        self.lo_GPA_budget11.setAlignment(QtCore.Qt.AlignCenter)
        self.lo_GPA_budget11.setObjectName("lo_GPA_budget11")
        self.gridLayout_6.addWidget(self.lo_GPA_budget11, 8, 2, 1, 1)
        self.lbl_num1_6_1 = QtWidgets.QLabel(self.frame_top_output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_num1_6_1.sizePolicy().hasHeightForWidth())
        self.lbl_num1_6_1.setSizePolicy(sizePolicy)
        self.lbl_num1_6_1.setMinimumSize(QtCore.QSize(50, 40))
        self.lbl_num1_6_1.setMaximumSize(QtCore.QSize(50, 45))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_num1_6_1.setFont(font)
        self.lbl_num1_6_1.setStyleSheet("background-color: rgb(191, 192, 192);\n"
                                        "border: 1px solid;\n"
                                        "")
        self.lbl_num1_6_1.setFrameShape(QtWidgets.QFrame.Box)
        self.lbl_num1_6_1.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_num1_6_1.setObjectName("lbl_num1_6_1")
        self.gridLayout_6.addWidget(self.lbl_num1_6_1, 9, 0, 1, 1)
        self.lbl_GPA_paid11 = QtWidgets.QLabel(self.frame_top_output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_GPA_paid11.sizePolicy().hasHeightForWidth())
        self.lbl_GPA_paid11.setSizePolicy(sizePolicy)
        self.lbl_GPA_paid11.setMinimumSize(QtCore.QSize(1000, 0))
        self.lbl_GPA_paid11.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lbl_GPA_paid11.setFont(font)
        self.lbl_GPA_paid11.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lbl_GPA_paid11.setAcceptDrops(False)
        self.lbl_GPA_paid11.setAutoFillBackground(False)
        self.lbl_GPA_paid11.setStyleSheet("background-color: rgb(198, 198, 198);")
        self.lbl_GPA_paid11.setFrameShape(QtWidgets.QFrame.Box)
        self.lbl_GPA_paid11.setWordWrap(True)
        self.lbl_GPA_paid11.setObjectName("lbl_GPA_paid11")
        self.gridLayout_6.addWidget(self.lbl_GPA_paid11, 9, 1, 1, 1)
        self.lo_GPA_paid11 = QtWidgets.QLabel(self.frame_top_output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lo_GPA_paid11.sizePolicy().hasHeightForWidth())
        self.lo_GPA_paid11.setSizePolicy(sizePolicy)
        self.lo_GPA_paid11.setMinimumSize(QtCore.QSize(0, 0))
        self.lo_GPA_paid11.setMaximumSize(QtCore.QSize(100, 45))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lo_GPA_paid11.setFont(font)
        self.lo_GPA_paid11.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.lo_GPA_paid11.setFrameShape(QtWidgets.QFrame.Box)
        self.lo_GPA_paid11.setAlignment(QtCore.Qt.AlignCenter)
        self.lo_GPA_paid11.setObjectName("lo_GPA_paid11")
        self.gridLayout_6.addWidget(self.lo_GPA_paid11, 9, 2, 1, 1)
        self.verticalLayout_6.addWidget(self.frame_top_output)
        self.frame_output_btn = QtWidgets.QFrame(self.page_output)
        self.frame_output_btn.setMinimumSize(QtCore.QSize(0, 100))
        self.frame_output_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_output_btn.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_output_btn.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_output_btn.setObjectName("frame_output_btn")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_output_btn)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.btn_output_back = QtWidgets.QPushButton(self.frame_output_btn)
        self.btn_output_back.setMinimumSize(QtCore.QSize(110, 45))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btn_output_back.setFont(font)
        self.btn_output_back.setStyleSheet("QPushButton {\n"
                                           "    color: rgb(255, 255, 255);\n"
                                           "    background-color: rgb(35, 35, 35);\n"
                                           "    border: 0px solid;\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "    background-color: rgb(85, 170, 255);\n"
                                           "}")
        self.btn_output_back.setObjectName("btn_output_back")
        self.horizontalLayout_11.addWidget(self.btn_output_back)
        self.btn_output_next = QtWidgets.QPushButton(self.frame_output_btn)
        self.btn_output_next.setMinimumSize(QtCore.QSize(110, 45))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btn_output_next.setFont(font)
        self.btn_output_next.setStyleSheet("QPushButton {\n"
                                           "    color: rgb(255, 255, 255);\n"
                                           "    background-color: rgb(35, 35, 35);\n"
                                           "    border: 0px solid;\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "    background-color: rgb(85, 170, 255);\n"
                                           "}")
        self.btn_output_next.setObjectName("btn_output_next")
        self.horizontalLayout_11.addWidget(self.btn_output_next)
        self.verticalLayout_6.addWidget(self.frame_output_btn, 0, QtCore.Qt.AlignRight)
        self.Pages_Widget.addWidget(self.page_output)

        ## Graphic Page

        self.page_graph = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page_graph.sizePolicy().hasHeightForWidth())
        self.page_graph.setSizePolicy(sizePolicy)
        self.page_graph.setObjectName("page_graph")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.page_graph)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")

        ## Окно графика

        self.frame_graphics = QtWidgets.QFrame(self.page_graph)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_graphics.sizePolicy().hasHeightForWidth())
        self.frame_graphics.setSizePolicy(sizePolicy)
        self.frame_graphics.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_graphics.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_graphics.setObjectName("frame_graphics")

        # Создаем пустой холст

        self.Layout_CHART = QtWidgets.QHBoxLayout(self.frame_graphics)
        self.Layout_CHART.setObjectName("Layout_CHART")
        self.Layout_CHART.setSpacing(0)

        self.sc = MplCanvas(self, width=9.55, height=4, dpi=100)

        self.Layout_CHART.addWidget(self.sc)

        self.horizontalLayout_graph_menu = QtWidgets.QVBoxLayout()
        self.horizontalLayout_graph_menu.setSpacing(0)
        self.horizontalLayout_graph_menu.setObjectName("horizontalLayout_graph_menu")
        self.label_indicator = QtWidgets.QLabel(self.frame_graphics)
        self.label_indicator.setMinimumSize(QtCore.QSize(0, 35))
        self.label_indicator.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_indicator.setStyleSheet("background-color: rgb(52, 101, 164);\n"
                                           "border: 1px solid;")
        self.label_indicator.setObjectName("label_indicator")
        self.horizontalLayout_graph_menu.addWidget(self.label_indicator)
        self.frame_graph_indicator = QtWidgets.QFrame(self.frame_graphics)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_graph_indicator.sizePolicy().hasHeightForWidth())
        self.frame_graph_indicator.setSizePolicy(sizePolicy)
        self.frame_graph_indicator.setStyleSheet("QFrame {\n"
                                                 "border: 1px solid;\n"
                                                 "}")
        self.frame_graph_indicator.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_graph_indicator.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_graph_indicator.setObjectName("frame_graph_indicator")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_graph_indicator)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.checkBox_main = QtWidgets.QCheckBox(self.frame_graph_indicator)
        self.checkBox_main.setObjectName("checkBox_main")
        self.verticalLayout_11.addWidget(self.checkBox_main)
        self.checkBox_budget = QtWidgets.QCheckBox(self.frame_graph_indicator)
        self.checkBox_budget.setObjectName("checkBox_budget")
        self.verticalLayout_11.addWidget(self.checkBox_budget)
        self.checkBox_paid = QtWidgets.QCheckBox(self.frame_graph_indicator)
        self.checkBox_paid.setObjectName("checkBox_paid")
        self.verticalLayout_11.addWidget(self.checkBox_paid)
        self.horizontalLayout_graph_menu.addWidget(self.frame_graph_indicator)

        # Таблица
        self.table_chart_info = QtWidgets.QTableWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_chart_info.sizePolicy().hasHeightForWidth())
        self.table_chart_info.setSizePolicy(sizePolicy)
        self.table_chart_info.setStyleSheet("background-color: rgb(238, 238, 236);\n"
                                       "")
        self.table_chart_info.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.table_chart_info.setAutoScroll(True)
        self.table_chart_info.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_chart_info.setDragEnabled(False)
        self.table_chart_info.setShowGrid(True)
        self.table_chart_info.setGridStyle(QtCore.Qt.SolidLine)
        self.table_chart_info.setWordWrap(True)
        self.table_chart_info.setCornerButtonEnabled(True)
        self.table_chart_info.setObjectName("table_chart_info")
        self.table_chart_info.setColumnCount(2)
        self.table_chart_info.setRowCount(21)

        self.horizontalLayout_graph_menu.addWidget(self.table_chart_info)




        self.lbl_update_GPA = QtWidgets.QLabel(self.frame_graphics)
        self.lbl_update_GPA.setMinimumSize(QtCore.QSize(0, 35))
        self.lbl_update_GPA.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lbl_update_GPA.setStyleSheet("background-color: rgb(52, 101, 164);\n"
                                          "border: 1px solid;\n"
                                          "")
        self.lbl_update_GPA.setObjectName("lbl_update_GPA")
        self.horizontalLayout_graph_menu.addWidget(self.lbl_update_GPA)
        self.btn_graph_update = QtWidgets.QPushButton(self.frame_graphics)
        self.btn_graph_update.setMinimumSize(QtCore.QSize(0, 35))
        self.btn_graph_update.setMaximumSize(QtCore.QSize(16777215, 35))
        self.btn_graph_update.setStyleSheet("QPushButton {\n"
                                            "    color: rgb(255, 255, 255);\n"
                                            "    background-color: rgb(35, 35, 35);\n"
                                            "    border: 0px solid;\n"
                                            "}\n"
                                            "QPushButton:hover {\n"
                                            "    background-color: rgb(85, 170, 255);\n"
                                            "}")
        self.btn_graph_update.setObjectName("btn_graph_update")
        self.horizontalLayout_graph_menu.addWidget(self.btn_graph_update)
        self.Layout_CHART.addLayout(self.horizontalLayout_graph_menu)
        self.verticalLayout_8.addWidget(self.frame_graphics)
        self.frame_graph_btn = QtWidgets.QFrame(self.page_graph)
        self.frame_graph_btn.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_graph_btn.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_graph_btn.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_graph_btn.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_graph_btn.setObjectName("frame_graph_btn")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_graph_btn)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btn_graph_back = QtWidgets.QPushButton(self.frame_graph_btn)
        self.btn_graph_back.setMinimumSize(QtCore.QSize(110, 45))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btn_graph_back.setFont(font)
        self.btn_graph_back.setStyleSheet("QPushButton {\n"
                                          "    color: rgb(255, 255, 255);\n"
                                          "    background-color: rgb(35, 35, 35);\n"
                                          "    border: 0px solid;\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "    background-color: rgb(85, 170, 255);\n"
                                          "}")
        self.btn_graph_back.setObjectName("btn_graph_back")
        self.horizontalLayout_5.addWidget(self.btn_graph_back)
        self.btn_graph_report = QtWidgets.QPushButton(self.frame_graph_btn)
        self.btn_graph_report.setMinimumSize(QtCore.QSize(110, 45))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btn_graph_report.setFont(font)
        self.btn_graph_report.setStyleSheet("QPushButton {\n"
                                            "    color: rgb(255, 255, 255);\n"
                                            "    background-color: rgb(35, 35, 35);\n"
                                            "    border: 0px solid;\n"
                                            "}\n"
                                            "QPushButton:hover {\n"
                                            "    background-color: rgb(85, 170, 255);\n"
                                            "}")
        self.btn_graph_report.setObjectName("btn_graph_report")
        self.horizontalLayout_5.addWidget(self.btn_graph_report)
        self.verticalLayout_8.addWidget(self.frame_graph_btn, 0, QtCore.Qt.AlignRight)
        self.Pages_Widget.addWidget(self.page_graph)

        self.verticalLayout_5.addWidget(self.Pages_Widget)
        self.horizontalLayout_2.addWidget(self.frame_pages)
        self.verticalLayout.addWidget(self.Content)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.Pages_Widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Образовательная деятельность СПО"))
        self.Btn_Toggle.setText(_translate("MainWindow", "Меню"))
        self.btn_page_input.setText(_translate("MainWindow", "Ввод"))
        self.btn_page_output.setText(_translate("MainWindow", "Вывод"))
        self.btn_page_gpraph.setText(_translate("MainWindow", "График"))
        self.btn_page_report.setText(_translate("MainWindow", "Отчет"))
        self.le_grade_point_averag_budget9.setPlaceholderText(_translate("MainWindow", "؊"))
        self.lbl_top50.setText(_translate("MainWindow",
                                          "Количество студентов, соответствующих списку топ 50 наиболее востребованных профессий"))
        self.lbl_title1.setText(_translate("MainWindow", "<b>№<br>п/п<b>"))
        self.lbl_count_stud_fulltime.setText(_translate("MainWindow", "Количество студентов очного отделения"))
        self.lbl_num_5.setText(_translate("MainWindow",
                                          "<html><head/><body><p><span style=\" font-weight:400;\">1.5</span></p></body></html>"))
        self.le_count_stud_parttime.setPlaceholderText(_translate("MainWindow", "100"))
        self.lbl_title2.setText(_translate("MainWindow", "<b>Наименвование показателя<b>"))
        self.lbl_num_1_6.setText(_translate("MainWindow",
                                            "<html><head/><body><p><span style=\" font-weight:400;\">1.1.6</span></p></body></html>"))
        self.le_grade_point_averag_paid11.setPlaceholderText(_translate("MainWindow", "؊"))
        self.le_grade_point_averag_paid9.setPlaceholderText(_translate("MainWindow", "؊"))
        self.le_top50.setPlaceholderText(_translate("MainWindow", "؊"))
        self.lbl_num_1_4.setText(_translate("MainWindow",
                                            "<html><head/><body><p><span style=\" font-weight:400;\">1.1.4</span></p></body></html>"))
        self.le_count_stud_budget.setPlaceholderText(_translate("MainWindow", "100"))
        self.lbl_num_8.setText(_translate("MainWindow",
                                          "<html><head/><body><p><span style=\" font-weight:400;\">1.6.1</span></p></body></html>"))
        self.lbl_num_1_2.setText(_translate("MainWindow",
                                            "<html><head/><body><p><span style=\" font-weight:400;\">1.1.2</span></p></body></html>"))
        self.lbl_num_4.setText(_translate("MainWindow",
                                          "<html><head/><body><p><span style=\" font-weight:400;\">1.4</span></p></body></html>"))
        self.lbl_grade_point_averag_paid9.setText(_translate("MainWindow",
                                                             "<html><head/><body><p>Средний балл аттестата об <span style=\" text-decoration: underline;\">основном</span> общем образовании и результатов отбора студентов, принятых на обучение по очной форме обучения(платники) </p></body></html>"))
        self.lbl_count_stud_budget.setText(_translate("MainWindow",
                                                      "Количество студентов, обучающихся за счет средств соотвествеющих бюджеттной системы РФ государства"))
        self.lbl_num_7.setText(_translate("MainWindow",
                                          "<html><head/><body><p><span style=\" font-weight:400;\">1.6</span></p></body></html>"))
        self.lbl_absentia.setText(_translate("MainWindow", "Количество студентов заочного отделения"))
        self.lbl_parttime.setText(_translate("MainWindow", "Количество студентов очно-заочного отделения"))
        self.le_count_stud_paid.setPlaceholderText(_translate("MainWindow", "100"))
        self.le_count_stud.setPlaceholderText(_translate("MainWindow", "100"))
        self.le_grade_point_averag_budget11.setPlaceholderText(_translate("MainWindow", "؊"))
        self.lbl_count_stud_paid.setText(
            _translate("MainWindow", "Количество студентов, обучающихся на платной основе"))
        self.label_22.setText(_translate("MainWindow", " 09.02.03 ПРОГРАММИРОВАНИЕ В КОМПЬЮТЕРНЫХ СИСТЕМАХ"))
        self.lbl_count_stud.setText(_translate("MainWindow", "Общая численность студентов"))
        self.lbl_grade_point_averag_paid11.setText(_translate("MainWindow",
                                                              "<html><head/><body><p>Средний балл аттестата об <span style=\" text-decoration: underline;\">среднем</span> общем образовании и результатов отбора студентов, принятых на обучение по очной форме обучения(платники) </p></body></html>"))
        self.lbl_title3.setText(_translate("MainWindow", "<b>Значение показателя<b>"))
        self.lbl_num_6.setText(_translate("MainWindow",
                                          "<html><head/><body><p><span style=\" font-weight:400;\">1.5.1</span></p></body></html>"))
        self.le_count_stud_absentia.setPlaceholderText(_translate("MainWindow", "100"))
        self.lbl_grade_point_averag_budget9.setText(_translate("MainWindow",
                                                               "<html><head/><body><p>Средний балл аттестата об <span style=\" text-decoration: underline;\">основном</span> общем образовании и результатов отбора студентов, принятых на обучение по очной форме обучения(бюджетники) </p></body></html>"))
        self.lbl_num_1_3.setText(_translate("MainWindow",
                                            "<html><head/><body><p><span style=\" font-weight:400;\">1.1.3</span></p></body></html>"))
        self.lbl_num_1_5.setText(_translate("MainWindow",
                                            "<html><head/><body><p><span style=\" font-weight:400;\">1.1.5</span></p></body></html>"))
        self.lbl_num_1_1.setText(_translate("MainWindow",
                                            "<html><head/><body><p><span style=\" font-weight:400;\">1.1</span></p></body></html>"))
        self.lbl_grade_point_averag_budget11.setText(_translate("MainWindow",
                                                                "<html><head/><body><p>Средний балл аттестата об <span style=\" text-decoration: underline;\">среднем</span> общем образовании и результатов отбора студентов, принятых на обучение по очной форме обучения(бюджетники) </p></body></html>"))
        self.le_count_stud_fulltime.setPlaceholderText(_translate("MainWindow", "100"))
        self.btn_input_save.setText(_translate("MainWindow", "Сохранить"))
        self.btn_input_next.setText(_translate("MainWindow", "Далее"))
        self.lbl_title1_2.setText(_translate("MainWindow", "<b>№<br>п/п<b>"))
        self.lbl_title2_2.setText(_translate("MainWindow", "<b>Наименвование показателя<b>"))
        self.lbl_title3_2.setText(_translate("MainWindow", "<b>Значение показателя<b>"))
        self.lbl_num1_1.setText(_translate("MainWindow",
                                           "<html><head/><body><p><span style=\" font-weight:400;\">1.1</span></p></body></html>"))
        self.lbl_count_stud_2.setText(_translate("MainWindow", "Общая численность студентов"))
        self.lo_count_stud.setText(_translate("MainWindow", "؊"))
        self.lbl_num1_2.setText(_translate("MainWindow",
                                           "<html><head/><body><p><span style=\" font-weight:400;\">1.2</span></p></body></html>"))
        self.lbl_proportion_stud_fulltime.setText(_translate("MainWindow",
                                                             "Удельный вес численности студентов, обучающихся по очной форме обучения в общей численности студентов"))
        self.lo_proportion_stud_fulltime.setText(_translate("MainWindow", "؊"))
        self.lbl_num1_3.setText(_translate("MainWindow",
                                           "<html><head/><body><p><span style=\" font-weight:400;\">1.3</span></p></body></html>"))
        self.lbl_proportion_stud_budget.setText(_translate("MainWindow",
                                                           "Удельный вес численности студентов, обучающихся за счет средств соответствующих бюджетов бюджетной системы РФ в общей численности студентов"))
        self.lo_proportion_stud_budget.setText(_translate("MainWindow", "؊"))
        self.lbl_num1_4.setText(_translate("MainWindow",
                                           "<html><head/><body><p><span style=\" font-weight:400;\">1.4</span></p></body></html>"))
        self.lbl_count_stud_top50.setText(_translate("MainWindow",
                                                     "Общая численность студентов, обучающихся по профессиям и специальностям, соответсвующим списку 50 наиболее востребованных на рынке труда"))
        self.lo_count_stud_top50.setText(_translate("MainWindow", "؊"))
        self.lbl_num1_4_1.setText(_translate("MainWindow",
                                             "<html><head/><body><p><span style=\" font-weight:400;\">1.4.1</span></p></body></html>"))
        self.lbl_proportion_stud_top50.setText(_translate("MainWindow",
                                                          "Удельный вес численности студентов, обучающихся по профессиям и специальностям, соответсвующим списку 50 наиболее востребованных на рынке труда, в общей численности студентов"))
        self.lo_proportion_stud_top50.setText(_translate("MainWindow", "؊"))
        self.lbl_num1_5.setText(_translate("MainWindow",
                                           "<html><head/><body><p><span style=\" font-weight:400;\">1.5</span></p></body></html>"))
        self.lbl_GPA_budget9.setText(_translate("MainWindow",
                                                "<html><head/><body><p>Средний балл аттестата об <span style=\" font-weight:600;\">основном</span> общем образовании и результатов отбора студентов, принятых на обучение по <span style=\" text-decoration: underline;\">очной</span> форме обучения(бюджетники) </p></body></html>"))
        self.lo_GPA_budget9.setText(_translate("MainWindow", "؊"))
        self.lbl_num1_5_1.setText(_translate("MainWindow",
                                             "<html><head/><body><p><span style=\" font-weight:400;\">1.5.1</span></p></body></html>"))
        self.lbl_GPA_paid9.setText(_translate("MainWindow",
                                              "<html><head/><body><p>Средний балл аттестата об <span style=\" font-weight:600;\">основном</span> общем образовании и результатов отбора студентов, принятых на обучение по <span style=\" text-decoration: underline;\">очной</span> форме обучения(платники) </p></body></html>"))
        self.lo_GPA_paid9.setText(_translate("MainWindow", "؊"))
        self.lbl_num1_6.setText(_translate("MainWindow",
                                           "<html><head/><body><p><span style=\" font-weight:400;\">1.6</span></p></body></html>"))
        self.lbl_GPA_budget11.setText(_translate("MainWindow",
                                                 "<html><head/><body><p>Средний балл аттестата об <span style=\" font-weight:600;\">среднем</span> общем образовании и результатов отбора студентов, принятых на обучение по очной форме обучения(бюджетники) </p></body></html>"))
        self.lo_GPA_budget11.setText(_translate("MainWindow", "؊"))
        self.lbl_num1_6_1.setText(_translate("MainWindow",
                                             "<html><head/><body><p><span style=\" font-weight:400;\">1.6.1</span></p></body></html>"))
        self.lbl_GPA_paid11.setText(_translate("MainWindow",
                                               "<html><head/><body><p>Средний балл аттестата об <span style=\" font-weight:600;\">среднем</span> общем образовании и результатов отбора студентов, принятых на обучение по очной форме обучения(платники) </p></body></html>"))
        self.lo_GPA_paid11.setText(_translate("MainWindow", "؊"))
        self.btn_output_back.setText(_translate("MainWindow", "Назад"))
        self.btn_output_next.setText(_translate("MainWindow", "Далее"))

        # Graphic Page
        self.label_indicator.setText(_translate("MainWindow", "<b>Показать на графике:<b>"))
        self.checkBox_main.setText(_translate("MainWindow", "Средний балл"))
        self.checkBox_budget.setText(_translate("MainWindow", "Бюджетники"))
        self.checkBox_paid.setText(_translate("MainWindow", "Платники"))
        self.lbl_update_GPA.setText(_translate("MainWindow", "Обовить средний балл"))
        self.btn_graph_update.setText(_translate("MainWindow", "Обновить"))
        self.btn_graph_back.setText(_translate("MainWindow", "Назад"))
        self.btn_graph_report.setText(_translate("MainWindow", "Отчет"))

        ###################################################################
        ## HOLDER
        ###################################################################

        # TOP 50
        for i in range(self.SIZE_TOP50):
            self.lst_label_top50[i].setText(_translate("MainWindow", self.lbl_text_top50[i]))
            self.mas_top50[i].setPlaceholderText(_translate("MainWindow", "100"))

        # GPA_BUDGET 9 classes
        for i in range(self.SIZE_GRADE_POINT_AVERAG):
            self.lst_label_GPA_budget9[i].setText(_translate("MainWindow", self.lbl_text_GPA[i]))
            self.mas_GPA_budget9[i].setPlaceholderText(_translate("MainWindow", "5.0"))

        # GPA_PAID 9 classes
        for i in range(self.SIZE_GRADE_POINT_AVERAG):
            self.lst_label_GPA_paid9[i].setText(_translate("MainWindow", self.lbl_text_GPA[i]))
            self.mas_GPA_paid9[i].setPlaceholderText(_translate("MainWindow", "5.0"))

        # GPA_BUDGET 11 classes
        for i in range(self.SIZE_GRADE_POINT_AVERAG):
            self.lst_label_GPA_budget11[i].setText(_translate("MainWindow", self.lbl_text_GPA[i]))
            self.mas_GPA_budget11[i].setPlaceholderText(_translate("MainWindow", "5.0"))

        # GPA_PAID 11 classes
        for i in range(self.SIZE_GRADE_POINT_AVERAG):
            self.lst_label_GPA_paid11[i].setText(_translate("MainWindow", self.lbl_text_GPA[i]))
            self.mas_GPA_paid11[i].setPlaceholderText(_translate("MainWindow", "5.0"))

        # Input Restriction
        self.setValidator()

    def setValidator(self):
        validator_int = QIntValidator(0, 1000)
        validator_double = QRegExpValidator(QRegExp(r'^(?:0|[2-5])\.[0-9]+$'))

        self.le_count_stud.setValidator(validator_int)
        self.le_count_stud_paid.setValidator(validator_int)
        self.le_count_stud_budget.setValidator(validator_int)
        self.le_count_stud_absentia.setValidator(validator_int)
        self.le_count_stud_fulltime.setValidator(validator_int)
        self.le_count_stud_parttime.setValidator(validator_int)

        for i in range(self.SIZE_TOP50):
            self.mas_top50[i].setValidator(validator_int)

        for i in range(self.SIZE_GRADE_POINT_AVERAG):
            self.mas_GPA_paid9[i].setValidator(validator_double)

        for i in range(self.SIZE_GRADE_POINT_AVERAG):
            self.mas_GPA_budget9[i].setValidator(validator_double)

        for i in range(self.SIZE_GRADE_POINT_AVERAG):
            self.mas_GPA_paid11[i].setValidator(validator_double)

        for i in range(self.SIZE_GRADE_POINT_AVERAG):
            self.mas_GPA_budget11[i].setValidator(validator_double)

        self.le_top50.setValidator(validator_int)
        self.le_grade_point_averag_paid9.setValidator(validator_double)
        self.le_grade_point_averag_budget9.setValidator(validator_double)
        self.le_grade_point_averag_paid11.setValidator(validator_double)
        self.le_grade_point_averag_budget11.setValidator(validator_double)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
