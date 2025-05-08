import sys
from GUI import QApplication, MainWindow

if  __name__ == '__main__':
    app = QApplication(sys.argv)

    main_window = MainWindow()

    main_window.show()

    sys.exit(app.exec())
