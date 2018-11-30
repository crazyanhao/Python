# !/usr/bin/env python



from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget,QLCDNumber,QApplication,QVBoxLayout
import sys,time
'''
编程思想
面向对象/面向过程。

'''
class MyTime(QWidget):
    # 构造方法
    def __init__(self):     # self代表当前实例对象的本身 ps：不是类本身
        super().__init__()
        self.initUI()
        self.init_timer()
    def update_time(self):
        # 获取当前的系统时间
        self.lcd.display(time.strftime('%X',time.localtime()))
    def init_timer(self):
        # 定时器
        self.timer = QTimer()
        # 间隔0.5s发送一次信号
        self.timer.setInterval(500)
        # 启动定时器
        self.timer.start()
                # 信号 和 槽函数
        self.timer.timeout.connect(self.update_time)
    def initUI(self):
        # 窗口组件的大小   251px * 150
        self.resize(251,150)
        # 窗口组件的名称
        self.setWindowTitle('不完美时钟')
        # 设置窗口图标
        self.setWindowIcon(QIcon('微信图片_20180706210835.jpg'))
        # 颜色调色板
        self.pa = QPalette()
        # 设置背景颜色为深黄色
        self.pa.setColor(QPalette.Background,Qt.darkCyan)
        self.setAutoFillBackground(True)
        self.setPalette(self.pa)

        self.lcd = QLCDNumber()
        # 设置数字的个数为10个
        self.lcd.setDigitCount(10)
        # 设置显示的数字模式为10进制
        self.lcd.setMode(QLCDNumber.Dec)
        # 设置展示的模式为水平
        self.lcd.setSegmentStyle(QLCDNumber.Flat)
        # 获取当前的系统时间
        self.lcd.display(time.strftime('%X',time.localtime()))
        # 初始化一个盒子布局
        self.main_layout = QVBoxLayout()
        # 把时间添加到布局中
        self.main_layout.addWidget(self.lcd)
        # 设置组件到布局的中间
        self.main_layout.setAlignment(Qt.AlignCenter)
        # 将子布局 设置到 顶层布局
        self.setLayout(self.main_layout)


        # 显示布局
        self.show()


# 程序入口
if __name__ == '__main__':
    # 构建一个应用程序
    app = QApplication(sys.argv)
    my_tt = MyTime()
    # 不留残留垃圾的退出
    sys.exit(app.exec_())