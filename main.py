from PyQt5.QtWidgets import QApplication
import sys
from gui import ChessApp

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ChessApp()
    window.show()
    sys.exit(app.exec_())