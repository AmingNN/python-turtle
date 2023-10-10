import turtle as t
import math

def people(x, y, size):
    """画火柴人

    :param x: x坐标
    :param y: y坐标
    :param size: 大小
    :return: None
    """
    half_size = size / 2
    t.penup()
    t.goto((x, y))
    t.pendown()
    t.seth(0)
    t.circle(half_size, 360)
    t.goto((x, y - half_size))
    t.forward(half_size)
    t.seth(45)
    t.forward(half_size)
    t.backward(half_size)
    t.seth(-45)
    t.forward(half_size)
    t.backward(half_size)
    t.seth(0)
    t.backward(half_size)

    t.goto((x, y - size))
    t.seth(-135)
    t.forward(size)
    t.backward(size)
    t.seth(-45)
    t.forward(size)


def draw_love(x, y, size, color=("red", "red"), fill=True):
    """

    :param x:画心的x坐标
    :param y: 画心的y坐标
    :param size: 中心到上下两点的距离
    :param color: 颜色()
    :param fill: 是否填充
    :return: None
    """
    t.color(*color)
    t.penup()
    t.goto((x, y - size))
    if fill:
        t.begin_fill()
    t.pendown()
    t.goto((x + size, y))

    # 原图https://blog.csdn.net/weixin_43716048/article/details/97385969末尾
    r = math.sqrt(math.pow(size, 2) * 2) / 2
    t.seth(45)
    t.circle(r, 180)
    t.seth(135)
    t.circle(r, 180)
    t.seth(-45)
    t.goto(x, y - size)
    if fill:
        t.end_fill()

def write(x, y, message):
    t.penup()
    t.goto(x, y)
    t.write(message, move=True, align="left", font=("楷体", 20, "normal"))

def init(x, y, color):
    t.screensize(x, y, color)
    t.ht()
    t.speed(0)

def love():
    try:
        init(SCREEN_X, SCREEN_Y, COLOR)
        print(t.pos())
        people(-300, 50, 100)
        # 心心位置
        draw_love(-150, 0, 25)
        draw_love(0, 0, 50)
        draw_love(250, 0, 100)
        write(200, -300, message=message)
        t.done()
    except t.Terminator:
        t.reset()    

SCREEN_X, SCREEN_Y, COLOR = (1000, 1000, None)
message = "TO: 阿铭"

if __name__ == '__main__':
    love()
