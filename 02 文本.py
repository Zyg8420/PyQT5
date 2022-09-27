import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel


def set_window_size():

    app = QApplication(sys.argv)

    w = QWidget()

    # 设置窗口标题
    w.setWindowTitle("第一个PyQt")

    # # 下面创建一个Label，然后调用方法指定父类
    # label = QLabel("账号: ", w)
    # # 设置父对象
    # label.setParent(w)

    # 下面创建一个Label（纯文本），在创建的时候指定了父对象
    label = QLabel("账号: ", w)

    # 显示位置与大小 ： x, y , w, h
    label.setGeometry(20, 20, 300, 40)

    # 展示窗口
    w.show()

    # 程序进行循环等待状态
    app.exec()


if __name__ == '__main__':
    set_window_size()