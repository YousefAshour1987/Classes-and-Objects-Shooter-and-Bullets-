from turtle import *
import random

def generate_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"

def playing_area():
    pen = Turtle()
    pen.ht()
    pen.speed(0)
    pen.color('teal')
    pen.begin_fill()
    pen.goto(-240,240)
    pen.goto(240,240)
    pen.goto(240,-240)
    pen.goto(-240,-240)
    pen.goto(-240,240)
    pen.end_fill()

class Player(Turtle):
    def __init__(self, x, y, color, screen, right_key, left_key, fire_key):
        super().__init__()
        self.ht()
        self.speed(0)
        self.hue = color
        self.color(color)
        self.penup()
        self.goto(x,y)
        self.setheading(90)
        self.shape("turtle")
        self.bullets = []
        self.alive = True
        self.st()
        screen.onkeypress(self.turn_left, left_key)
        screen.onkeypress(self.turn_right, right_key)
        screen.onkey(self.fire, fire_key)

    def turn_left(self):
        self.left(10)

    def turn_right(self):
        self.right(10)

    def move(self):
        self.forward(4)
        if self.xcor() > 230 or self.xcor() < -230:
            self.setheading(180 - self.heading())
        if self.ycor() > 230 or self.ycor() < -230:
            self.setheading(-self.heading())

    def fire(self):
        self.bullets.append(Bullet(self))

    def die(self):
        self.alive = False
        self.hideturtle()
        for bullet in self.bullets:
            bullet.hideturtle()

class Bullet(Turtle):
    def __init__(self, player):
        super().__init__()
        self.ht()
        self.speed(0)
        self.penup()
        self.goto(player.xcor(), player.ycor())
        self.seth(player.heading())
        self.color("white")
        self.st()


    def move(self):
            self.forward(10)
            # if not (-250 < self.xcor() < 250 and -250 < self.ycor() < 250):
            #     self.hideturtle()

screen = Screen()
screen.setup(520, 520)
screen.bgcolor("black")

screen.listen()

playing_area()

p1 = Player(-100, 0, "red", screen, "d", "a", "w")
p2 = Player(100, 0, "blue", screen, "Right", "Left", "Up")

while True:
    p1.move()
    p2.move()
    for bullet in p1.bullets:
        bullet.move()
        if p2.distance(bullet) < 20:
            if p2.health == 2: 
                p2.color("yellow")
            if health == 1: 
                p2.color("red")
            else:
                p2.hideturtle()
    for bullet in p2.bullets:
        bullet.move()
        if p1.distance(bullet) < 20:
            if p1.health == 2: 
                p1.color("yellow")
            if health == 1: 
                p1.color("red")
            else:
                p1.hideturtle()
screen.exitonclick()