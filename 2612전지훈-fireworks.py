import turtle as t
import random
class Firework:
    def __init__(self,num=0):
        self.num=num

    def DrawStar(self,side):
        t.right(54)
        for i in range(5):
            t.right(72)
            t.forward(side)
            t.left(144)
            t.forward(side)

    def ColorRandomChange(self):
        r,g,b=0,0,0
        r=random.random()
        g=random.random()
        b=random.random()
        t.pencolor(r,g,b)

    def FireworkRun(self,num):
        t.bgcolor("black")
        t.tracer(0)
        for i in range(num):
            self.ColorRandomChange()
            t.setheading(random.randint(1,360))
            t.forward(random.randint(1,400))
            side=random.gauss(4,1)
            self.DrawStar(side)
            t.goto(random.gauss(0,4),random.gauss(0,4))
        t.update()
        t.mainloop()

Firework1=Firework()
Firework1.FireworkRun(400)