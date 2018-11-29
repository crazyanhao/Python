# !/usr/bin/env python
# _*_ coding:utf-8 _*_
import random
class Game:
    def __init__(self):
        self.board_list = [
            ['', '', '', ''],
            ['', '', '', ''],
            ['', '', '', ''],
            ['', '', '', ''],
        ]

        self.score = 0
        # 空位 存储坐标 （行， 列）
        self.board_empty = []
    def start(self):
        self.restart()
        while True:
            self.print_board()
            code = input('请输入指令>>>:')
            if code == 'w':
                self.move_up()
            elif code == 's':
                self.move_down()
            elif code == 'a':
                self.move_left()
            elif code == 'd':
                self.move_right()
            elif code == 'r':
                self.restart()
                continue
            elif code == 'q':
                exit('退出')
            else:
                print('你的输入有误，请重新输入！')
                continue

            if self.is_win():
                print('YOU WIN! ')
                break
            if self.gameover():
                print('Game over!')
                break
            # 在空白的地方随机添加2,4
            self.add_piece()
    def print_board(self):
        print('''
        SCORE:{}
        +-----+-----+-----+-----+
        |{:^5}|{:^5}|{:^5}|{:^5}|
        +-----+-----+-----+-----+
        |{:^5}|{:^5}|{:^5}|{:^5}|
        +-----+-----+-----+-----+
        |{:^5}|{:^5}|{:^5}|{:^5}|
        +-----+-----+-----+-----+
        |{:^5}|{:^5}|{:^5}|{:^5}|
        +-----+-----+-----+-----+
        w(up),s(down),a(left),d(right)
        r(restart),q（exit）'''.format(self.score,
                                     *self.board_list[0],
                                     *self.board_list[1],
                                     *self.board_list[2],
                                     *self.board_list[3]))

    def is_win(self):
        # 判断是否获胜
        # 空位也要判断
        self.board_empty = []
        for i in range(len(self.board_list)):
            for j in range(len(self.board_list)):
                if self.board_list[i][j] == 2048:
                    return True
                if self.board_list[i][j] == '':
                    self.board_empty.append((i,j))

        return False
    def gameover(self):
        if not self.board_empty:
            # 每行每列没有相邻相等的元素
            # 判断每一行
            for i in range(len(self.board_list)):
                for j in range(len(self.board_list[i])-1):
                    if self.board_list[i][j] == self.board_list[i][j+1]:
                        return False
            #判断每一列
            self.turn_right()
            for i in range(len(self.board_list)):
                for j in range(len(self.board_list[i])-1):
                    if self.board_list[i][j] == self.board_list[i][j+1]:
                        self.turn_left()
                        return False
            return True
        return False

    def add_piece(self):
        # 在空白的位置随机添加2或者4
        # 先随机位置，再随机值
        if self.board_empty:
            # 随机位置， 并且删除
            p = self.board_empty.pop(random.randrange(len(self.board_empty)))  #长度以board_empty为准
            # 再随机值
            self.board_list[p[0]][p[1]] = random.randrange(2, 5, 2)

    def restart(self):
        self.board_list = [
            ['', '', '', ''],
            ['', '', '', ''],
            ['', '', '', ''],
            ['', '', '', ''],
        ]
        while True:
            t1 = (random.randrange(len(self.board_list[0]))), (random.randrange(len(self.board_list[0])))
            t2 = (random.randrange(len(self.board_list[0]))), (random.randrange(len(self.board_list[0])))
            if t1 != t2:
                break
        self.board_list[t1[0]][t1[1]] = random.randrange(2, 5, 2)
        self.board_list[t2[0]][t2[1]] = random.randrange(2, 5, 2)

    def move_up(self):
        self.turn_left()
        self.move_left()
        self.turn_right()

    def move_down(self):
        # 先顺时针旋转90°
        self.turn_right()
        # 向左操作
        self.move_left()
        # 左转90°回来
        self.turn_left()

    def move_left(self):
        for i in range(len(self.board_list)):
            self.board_list[i] = self.row_left_oper(self.board_list[i])

    def move_right(self):
        self.turn_left()
        self.move_up()
        self.turn_right()

    def row_left_oper(self, row):
        # 向左把一行列表进行2048操作
        # l1 = [2, '', 2, '']
        # 如何达成游戏效果   ①l1 = [2, '', 2, ''] => [2, 2] => [4] => [4, '', '', '']
        #                    ②......
        #                    ③......（头脑风暴）
        # 先挤到一起
        temp = []
        for item in row:
            if item:
                temp.append(item)
        new_row = []
        # 合并同类项    temp长度是不固定的 0,1,2,3,4
        flag = True
        for i in range(len(temp)):
            if flag:
                # 判断相邻的数是否相等
                if i + 1 < len(temp) and temp[i] == temp[i + 1]:
                    new_row.append(temp[i] * 2)
                    flag = False
                else:
                    new_row.append(temp[i])
            else:
                flag = True
        # 补齐
        n = len(row)
        for i in range(n - len(new_row)):
            new_row.append('')
        return new_row

    def turn_right(self):
        # 顺时针旋转90°
        self.board_list = [list(x[::-1]) for x in zip(*self.board_list)]
    def turn_left(self):
        # 逆时针旋转90°···相当于顺时针旋转270°···因此重复3次即可
        for i in range(3):
            self.turn_right()

if __name__ == '__main__':
    game = Game()
    game.start()