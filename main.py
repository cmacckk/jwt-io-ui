from modules.ui_jwt import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QWidget


if __name__ == '__main__':
    app = QApplication()
    window = QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    app.exec()