import sys
from PyQt5.QtWidgets import *


if __name__ == '__main__':
    # 创建对象
    app = QApplication(sys.argv)
    w = QWidget()
    # 设置窗口标题
    w.setWindowTitle('第一个PyQt程序')
    # 在窗口中添加文本
    label = QLabel('账号：', w)
    # 显示位置与大小: x, y, w, h
    label.setGeometry(20, 20, 30, 20)

    # 输入框
    edit = QLineEdit(w)
    edit.setPlaceholderText('请输入账号')
    edit.setGeometry(55, 20, 200, 20)

    # 在窗口中添加控件
    # btn = QPushButton('按钮')
    # 设置按钮的父亲是当前窗口，等于是添加到窗口中显示
    # btn.setParent(w)

    # 展示窗口
    w.show()
    # 程序进行循环等待状态
    app.exec()
