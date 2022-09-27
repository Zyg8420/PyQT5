import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget



def set_window_icon():
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle('看看我好看吗？')
    # 设置图标
    w.setWindowIcon(QIcon('img_1.png'))
    w.show()
    app.exec()


if __name__ == '__main__':
    set_window_icon()