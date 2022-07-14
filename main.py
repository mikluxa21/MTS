import sys

from Interface import Inter

from PySide6.QtWidgets import QApplication
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Inter()
    window.show()
    sys.exit(app.exec())