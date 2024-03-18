#Turtle Survive
#기존에 인터넷 상에 있던 Turtle Run은 PyCharm에서 잘 안 돌아가고,
#오류들이 꽤 있어 나만의 방식으로 살짝씩 바꿔 만들어 보았다.
import turtle as t
import random

score=0
playing=False

player=t.Turtle()
player.shape("turtle")
player.color("blue")
player.up()
player.speed(9)
player.goto(0,0)

enemy=t.Turtle()
enemy.shape("circle")
enemy.color("red")
enemy.up()
enemy.speed(5)
enemy.goto(-200,0)

food=t.Turtle()
food.shape("square")
food.up()
food.color("green")
food.speed(0)
food.goto(200,0)


def turn_right():
    player.setheading(0)
def turn_up():
    player.setheading(90)
def turn_left():
    player.setheading(180)
def turn_down():
    player.setheading(270)

def start():
    global playing
    if playing==False:
        playing=True
        player.clear()
        play()

def play():
    global score
    global playing
    enemy.forward(enemy.speed())
    ang=enemy.towards(player.pos())
    enemy.setheading(ang)
    player.forward(player.speed())
    if player.distance(enemy)<12:
        text="Score :"+str(score)
        message("Game Over",text)
        playing=False
        score=0
    if player.distance(food)<12:
        score+=1
        player.write(score)
        food_x=random.randint(-230,230)
        food_y=random.randint(-230,230)
        food.goto(food_x,food_y)
    if score%5==0:
        enemy.speed(5+score/5)
    if playing:
        t.ontimer(play,100)

def message(m1,m2):
    player.clear()
    player.goto(0,0)
    enemy.goto(0,200)
    player.write(m1,False,"center",("",20))
    player.home()
    enemy.goto(-200,0)
    food.goto(200,0)

t.title("Turtle Run")
t.setup(1000,600)
t.bgcolor("black")
t.onkeypress(turn_right,"Right")
t.onkeypress(turn_up,"Up")
t.onkeypress(turn_left,"Left")
t.onkeypress(turn_down,"Down")
t.onkeypress(start,"space")
t.listen()
t.mainloop()
message("Turtle Run","[space]")



