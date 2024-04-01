import turtle
import turtle as t
class baduk:
    def __init__(self,turn=0,x=0,y=0):
        self.turn=turn
        self.x=x
        self.y=y
        t.ht()

    def DrawPlate(self):
        t.bgcolor("tan2")
        t.tracer(0)
        for i in range(-9,10):
            t.pu()
            t.goto(-270,i*30)
            t.pd()
            t.forward(540)
        t.right(90)
        for i in range(-9,10):
            t.pu()
            t.goto(i*30,270)
            t.pd()
            t.forward(540)
        t.update()

    def PlaceStone(self,x,y):
        t.pu()
        for i in range(-9,10):
            for j in range(-9,10):
                if 30*i-15<=x<=30*i+15 and 30*j-15<=y<=30*j+15:
                    t.goto(30*i,30*j)
        t.pd()
        t.dot(30,self.DotColor(self.turn))
        print(self.turn)

    def DotColor(self,turn):
        if turn%2==0:
            self.turn+=1
            return "black"
        else:
            self.turn+=1
            return "white"

screen=turtle.Screen()
Baduk=baduk()
Baduk.DrawPlate()

screen.onscreenclick(Baduk.PlaceStone)
t.mainloop()