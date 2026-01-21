import turtle as t
import random

# -----------------------------
# Setup
# -----------------------------
screen = t.Screen()
screen.setup(1000, 800)
screen.bgcolor("gray")

t.speed(0)
t.color("cyan")
t.pensize(2)

# -----------------------------
# Utility Functions
# -----------------------------
def ask_int(prompt):
    """Safely ask for an integer."""
    while True:
        value = screen.textinput("Input Required", prompt)
        if value is None:
            return None
        try:
            return int(value)
        except ValueError:
            pass

def ask_color():
    """Ask for a valid turtle color."""
    while True:
        color = screen.textinput("Fill Color", "Enter a color name:")
        if color is None:
            return None
        try:
            t.color(color)
            return color
        except t.TurtleGraphicsError:
            pass

# -----------------------------
# Fill System
# -----------------------------
def start_fill():
    color = ask_color()
    if color:
        t.begin_fill()

def end_fill():
    try:
        t.end_fill()
    except:
        pass

# -----------------------------
# Shape Drawing
# -----------------------------
def draw_polygon(sides=None, length=None):
    if sides is None:
        sides = ask_int("Number of sides:")
    if length is None:
        length = ask_int("Side length:")

    if sides and length:
        for _ in range(sides):
            t.forward(length)
            t.right(360 / sides)

def draw_circle():
    radius = ask_int("Circle radius:")
    if radius:
        t.circle(radius)

# Preset shapes
def draw_triangle():
    draw_polygon(3, 100)

def draw_square():
    draw_polygon(4, 100)

def draw_hexagon():
    draw_polygon(6, 80)

# -----------------------------
# Teleport
# -----------------------------
def teleport():
    x = ask_int("Teleport X:")
    y = ask_int("Teleport Y:")
    if x is not None and y is not None:
        t.penup()
        t.goto(x, y)
        t.pendown()

# -----------------------------
# Movement Controls
# -----------------------------
def move_up():
    t.setheading(90)
    t.forward(20)

def move_down():
    t.setheading(270)
    t.forward(20)

def move_left():
    t.setheading(180)
    t.forward(20)

def move_right():
    t.setheading(0)
    t.forward(20)

def pen_up():
    t.penup()

def pen_down():
    t.pendown()

def undo():
    t.undo()

def clear_screen():
    t.clear()

# -----------------------------
# Brush & Speed Controls
# -----------------------------
def increase_brush():
    t.pensize(t.pensize() + 1)

def decrease_brush():
    size = t.pensize()
    if size > 1:
        t.pensize(size - 1)

def faster():
    t.speed(min(t.speed() + 1, 10))

def slower():
    t.speed(max(t.speed() - 1, 1))

# -----------------------------
# Random Color Mode
# -----------------------------
def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    t.color(r, g, b)

# -----------------------------
# MENU (SPACEBAR ACTIVATED)
# -----------------------------
def open_menu():
    choice = screen.textinput(
        "Turtle Menu",
        "1. Draw Polygon\n"
        "2. Draw Circle\n"
        "3. Start Fill\n"
        "4. End Fill\n"
        "5. Teleport\n"
        "6. Triangle\n"
        "7. Square\n"
        "8. Hexagon\n"
        "9. Exit Menu\n\n"
        "Choose an option:"
    )

    if choice == "1":
        draw_polygon()
    elif choice == "2":
        draw_circle()
    elif choice == "3":
        start_fill()
    elif choice == "4":
        end_fill()
    elif choice == "5":
        teleport()
    elif choice == "6":
        draw_triangle()
    elif choice == "7":
        draw_square()
    elif choice == "8":
        draw_hexagon()
    elif choice == "9":
        return  # stop showing menu

    # Reopen menu after action
    screen.ontimer(open_menu, 100)

# -----------------------------
# Key Bindings
# -----------------------------
def bind_keys():
    screen.listen()

    # Movement
    screen.onkey(move_up, "Up")
    screen.onkey(move_down, "Down")
    screen.onkey(move_left, "Left")
    screen.onkey(move_right, "Right")

    # Pen control
    screen.onkey(pen_up, "s")
    screen.onkey(pen_down, "d")

    # Brush size
    screen.onkey(increase_brush, "+")
    screen.onkey(decrease_brush, "-")

    # Speed
    screen.onkey(faster, "]")
    screen.onkey(slower, "[")

    # Undo & clear
    screen.onkey(undo, "f")
    screen.onkey(clear_screen, "a")

    # Random color
    screen.onkey(random_color, "r")

    # SPACEBAR opens menu
    screen.onkey(open_menu, "space")

bind_keys()

screen.mainloop()
