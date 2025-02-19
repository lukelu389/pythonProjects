"""
Xiao Lu
420-SN1 Programming, Section #21
Winter 2025
J. Gullifer, instructor
Lab Assignment #7
"""

from turtle import *
from random import *

speed(0)
pencolor("Cyan")
pensize(5)
steps = int(input("How many steps do you think it will take"))
for _ in range(steps):

    directions = randint(0, 369)
    right(directions)
    forward(randint(-50, 50))


exitonclick()
