from PyQt5 import QtWidgets

from ui_main import Ui_MainWindow
import sys


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## PAGES
        ########################################################################

        # PAGE 1
        self.ui.Btn_Menu_Input.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_input))

        # PAGE 2
        self.ui.Btn_Menu_Output.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_output))

        # PAGE 3
        self.ui.Btn_Menu_Graph.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_output))



def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
