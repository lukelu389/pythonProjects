import turtle
import random
import time

score_display = 0

snake = turtle.Turtle()
wn = turtle.Screen()
wn.title("SNAKE GAME")
wn.bgcolor("black")

wn.setup(width=600, height=600)
wn.tracer(0)

snake.shape("square")
snake.color("white")
snake.penup()
snake.goto(0, 0)
snake.direction = "Stop"

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 250)
score.write("Score :0 ", align="center", font=("candara", 24, "bold"))


def group():
    snake.direction = "up"


def go_down():
    snake.direction = "down"


def go_left():
    snake.direction = "left"


def go_right():
    snake.direction = "right"


def move():
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
        # Move segment 0 to the head
    if len(segments) > 0:
        x = snake.xcor()
        y = snake.ycor()
        segments[0].goto(x, y)

    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 1.5)
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 1.5)
    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 1.5)
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 1.5)


def collision():
    snake.goto(0, 0)
    snake.direction = 'stop'

    for segment in segments:
        segment.hideturtle()

    segments.clear()
    score.clear()
    score.write("Score :" + str(score_display), align="center", font=("candara", 24, "bold"))
    message = turtle.Turtle()
    message.color("white")
    message.penup()
    message.write("NICE TRY!", align = "center", font=("candara", 40, "bold"))
    time.sleep(0.5)


wn.listen()
wn.onkeypress(group, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

segments = []

while True:
    wn.update()

    # Check for collision with border
    if snake.xcor() > 290 or snake.xcor() < -290 or snake.ycor() > 290 or snake.ycor() < -290:
        collision()

    move()

    if snake.distance(food) < 20:
        food.goto(random.randint(-290, 290), random.randint(-290, 290))
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color("white")
        new_segment.penup()
        segments.append(new_segment)
        segments.append(new_segment)
        segments.append(new_segment)
        segments.append(new_segment)
        score_display += 1
        score.clear()
        score.write("Score :" + str(score_display), align="center", font=("candara", 24, "bold"))