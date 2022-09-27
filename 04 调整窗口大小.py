import sys

from PyQt5.QtWidgets import QApplication, QWidget


def set_window_size():

    app = QApplication(sys.argv)

    w = QWidget()

    # 设置窗口标题
    w.setWindowTitle("演示窗口")

    # 窗口的大小
    w.resize(800, 500)

    # 展示窗口
    w.show()

    # 程序进行循环等待状态
    app.exec()


if __name__ == '__main__':
    set_window_size()