# Classes and Objects (Shooter and Bullets)



# Player Class 

## Overview

The `Player` class is an example of an **object-oriented design** in Python. It models a controllable player using the `turtle` graphics library.

Each `Player` object:

* Has its **own data (instance variables)**
* Has its **own behaviors (methods)**
* Responds to **user input (keyboard controls)**



## Class Definition

```python
class Player(Turtle):
```

* `Player` **inherits** from the `Turtle` class
* This means a `Player` automatically has access to built-in turtle methods like:

  * `forward()`, `left()`, `right()`, `goto()`, etc.


##  Constructor (`__init__`)

```python
def __init__(self, x, y, color, screen, right_key, left_key):
```

### When is this used?

* This method runs **automatically when a new Player object is created**

Example:

```python
p1 = Player(-100, 0, "red", screen, "d", "a")
```



## Instance Variables

Instance variables are **unique to each object**. Every player has its own copy.

### Defined inside `__init__`:

```python
self.color(color)
self.goto(x, y)
self.setheading(90)
self.alive = True
```

### Key Instance Variables:

| Variable     | Purpose                                          |
| ------------ | ------------------------------------------------ |
| `self.alive` | Tracks whether the player is still in the game   |
| Position     | Stored internally by Turtle (`xcor()`, `ycor()`) |
| Heading      | Direction the player is facing (`heading()`)     |
| Color        | Visual appearance of the player                  |

**Important**:
Even though we don’t explicitly write variables like `self.x`, the `Turtle` class is already storing that data internally.

---

##  Event Binding (User Input)

```python
screen.onkeypress(self.turn_left, left_key)
screen.onkeypress(self.turn_right, right_key)
```

###  When is this used?

* Runs during object creation (`__init__`)
* Connects **keyboard input to method calls**

### What happens?

* When the user presses a key:

  * The corresponding method runs automatically

---

## Methods (Behaviors)

Methods define what a `Player` can **do**.

---

### `turn_left`

```python
def turn_left(self):
    self.left(10)
```

* Turns the player 10 degrees left

 **When is it used?**

* Called when the user presses the assigned left key

---

### `turn_right`

```python
def turn_right(self):
    self.right(10)
```

* Turns the player 10 degrees right

 **When is it used?**

* Called when the user presses the assigned right key

---

###  `move`

```python
def move(self):
    self.forward(5)
```

* Moves the player forward continuously

 **When is it used?**

* Called repeatedly inside the game loop

Example:

```python
while p1.alive and p2.alive:
    p1.move()
    p2.move()
```



## Key Concepts

### 1. Objects

```python
p1 = Player(...)
p2 = Player(...)
```

* Each object is a **separate player**
* They share the same code but have different data

---

### 2. Instance Variables vs Methods

| Type              | Purpose         | Example      |
| ----------------- | --------------- | ------------ |
| Instance Variable | Stores data     | `self.alive` |
| Method            | Performs action | `move()`     |

---

### 3. When Things Happen

| Code Location     | When It Runs           |
| ----------------- | ---------------------- |
| `__init__`        | When object is created |
| `turn_left/right` | When key is pressed    |
| `move()`          | Every loop iteration   |

---

### 4. Game Loop Interaction

The game loop controls continuous movement:

```python
while p1.alive and p2.alive:
    p1.move()
    p2.move()
```

* Without this loop, nothing would move
* This is what makes the game “run”

---

## Summary

The `Player` class demonstrates:

* **Inheritance** → Extending `Turtle`
* **Encapsulation** → Each player stores its own data
* **Methods** → Define behavior
* **Event handling** → Reacting to user input
* **Game loops** → Continuous updates




