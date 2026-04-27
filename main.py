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
        screen.onkey(self.fire, fire_key) # Bind to a specific event handler

    def turn_left(self):
        self.left(10)

    def turn_right(self):
        self.right(10)

    def move(self):
        if self.alive:
            self.forward(4)
            if self.xcor() > 230 or self.xcor() < -230:
                self.setheading(180 - self.heading())
            if self.ycor() > 230 or self.ycor() < -230:
                self.setheading(-self.heading())

    def fire(self):
        if self.alive: # Only fire if the player is alive
            # Try to reuse a "ready" bullet
            fired = False
            for bullet in self.bullets:
                if bullet.state == "ready":
                    bullet.fire(self.xcor(), self.ycor(), self.heading())
                    fired = True
                    break
            if not fired:
                new_bullet = Bullet()
                new_bullet.fire(self.xcor(), self.ycor(), self.heading())
                self.bullets.append(new_bullet)

    def update_bullets(self):
        if self.alive:
            for bullet in self.bullets:
                bullet.move()

    def die(self):
        self.alive = False
        self.hideturtle()
        for bullet in self.bullets:
            bullet.hideturtle()
            bullet.state = "ready"

class Bullet(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.speed = 15
        self.state = "ready"
        self.hideturtle()

    def fire(self, start_x, start_y, start_heading):
        if self.state == "ready":
            self.goto(start_x, start_y)
            self.setheading(start_heading)
            self.showturtle()
            self.state = "fire"

    def move(self):
        if self.state == "fire":
            self.forward(self.speed)
            if not (-250 < self.xcor() < 250 and -250 < self.ycor() < 250):
                self.hideturtle()
                self.state = "ready"
    
    def is_collided_with(self, other):
        if self.state == "fire" and other.alive:
            return self.distance(other) < 15 # Adjust collision distance as needed
        return False

# --- Game Setup ---
screen = Screen()
screen.setup(520, 520)
screen.bgcolor("black")
screen.tracer(0) # Turn off screen updates for smoother animation

# Key Binding. Connects key presses and mouse clicks with function calls
screen.listen()

playing_area() # Draw the playing area

p1 = Player(-100, 0, "red", screen, "d", "a", "w")
p2 = Player(100, 0, "blue", screen, "Right", "Left", "Up")

def game_loop():
    screen.update() # Update the screen once at the start of each frame

    # Removed: if not (p1.alive and p2.alive): return # Allows game to continue if one player is dead

    p1.move()
    p1.update_bullets()

    p2.move()
    p2.update_bullets()

    # Collision Detection
    for bullet in p1.bullets:
        if bullet.is_collided_with(p2):
            p2.die()
            bullet.hideturtle()
            bullet.state = "ready"
      
    for bullet in p2.bullets:
        if bullet.is_collided_with(p1):
            p1.die()
            bullet.hideturtle()
            bullet.state = "ready"
            
    # Re-schedule the game loop to run again after 20 milliseconds
    screen.ontimer(game_loop, 20)

# Start the game loop
game_loop()

screen.exitonclick()

















































# from turtle import *
# import random

# def generate_color():
#     return f"#{random.randint(0, 0xFFFFFF):06x}"

# def playing_area():
#     pen = Turtle()
#     pen.ht()
#     pen.speed(0)
#     pen.color('teal')
#     pen.begin_fill()
#     pen.goto(-240,240)
#     pen.goto(240,240)
#     pen.goto(240,-240)
#     pen.goto(-240,-240)
#     pen.goto(-240,240)
#     pen.end_fill()
    
# class Player(Turtle):
#     def __init__(self, x, y, color, screen, right_key, left_key, fire_key):
#         super().__init__()
#         self.ht()
#         self.speed(0)
#         self.hue = color
#         self.color(color)
#         self.penup()
#         self.goto(x,y)
#         self.setheading(90)
#         self.shape("turtle")
#         self.bullets = []
#         self.alive = True
#         self.st()

#         screen.onkeypress(self.turn_left, left_key)
#         screen.onkeypress(self.turn_right, right_key)
#         screen.onkey(self.fire, fire_key)

#     def turn_left(self):
#         self.left(10)

#     def turn_right(self):
#         self.right(10)

#     def move(self):
#         self.forward(4)
#         if self.xcor() > 230 or self.xcor() < -230:
#             self.setheading(180 - self.heading())
#         if self.ycor() > 230 or self.ycor() < -230:
#             self.setheading(-self.heading())

#     def fire(self):
#         self.bullets.append(Bullet(bullets))
#         self.forward(10)
# class Bullet(Turtle):
#     def __init__(self, fire_key):
#         super().__init__()
#         self.penup()
#         self.color("green")
#         self.speed(0)
#         self.hideturtle()
#         self.forward(20)
#         self.bullets = []
#         screen.onkey(self.fire, fire_key)
#     def fire(self):
#         self.bullets.append(Bullet(bullets))
#         self.forward(10)
#     def move(self):
#         self.forward(4)
#         if self.xcor() > 230 or self.xcor() < -230:
#             self.setheading(180 - self.heading())
#         if self.ycor() > 230 or self.ycor() < -230:
#             self.setheading(-self.heading())
    
    

# screen = Screen()
# screen.bgcolor("black")
# screen.setup(520,520)
# # Key Binding. Connects key presses and mouse clicks with function calls
# screen.listen()

# playing_area()

# p1 = Player(-100, 0, "red",screen, "d", "a", "w")
# p2 = Player(100,0,"blue",screen, "Right","Left", "Up")
# bullets = Bullet("Up")
# while p1.alive and p2.alive:
#     p1.move()
#     p2.move()
    
# screen.exitonclick()