#SquareSpiral1.py
import turtle as t

def polygon():
    try:
        t.speed(0)
        # t = turtle.Pen()
        t.bgcolor("black")
        t.hideturtle()
        # sides=eval(input("输入要绘制的边的数目，请输入2-6的数字！"))
        sides=6
        colors=["red","yellow","green","blue","orange","purple"]
        for x in range(300):
            t.pencolor(colors[x%sides])
            t.forward(x*3/sides+x)
            t.left(360/sides+1)
            t.width(x*sides/200)
        t.exitonclick()
    except:
        t.reset()
