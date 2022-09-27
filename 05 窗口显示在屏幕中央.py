import sys

from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget



def set_window_size():
    app = QApplication(sys.argv)

    w = QWidget()

    # 设置窗口标题
    w.setWindowTitle("演示窗口")

    # 窗口的大小
    w.resize(500, 300)

    # 将窗口设置在屏幕的左上角
    # w.move(0, 0)

    # 调整窗口在屏幕中央显示
    center_pointer = QDesktopWidget().availableGeometry().center()
    x = center_pointer.x()
    y = center_pointer.y()
    # w.move(x, y)
    # w.move(x-150, y-150)
    print(w.frameGeometry())
    print(w.frameGeometry().getRect())
    print(type(w.frameGeometry().getRect()))
    old_x, old_y, width, height = w.frameGeometry().getRect()
    w.move(x - width / 2, y - height / 2)

    # 展示窗口
    w.show()

    # 程序进行循环等待状态
    app.exec()



if __name__ == '__main__':
    set_window_size()