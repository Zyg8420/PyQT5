import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


def set_window_size():
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle('验证例子')
    # 在窗口添加控件
    btn = QPushButton('登录按钮')
    btn.setParent(w)
    w.show()
    app.exec()


if __name__ == '__main__':
    set_window_size()