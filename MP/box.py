"""
Xiao Lu
420-SN1 Programming, Section #21
Winter 2025
J. Gullifer, instructor
Lab Assignment #7
"""

from math import *
m = float(input("Enter the box's mass in kilogram: "))
kCoefficient = float(input('Enter the coefficient of kinetic friction: '))
g = 9.8
T = 30
lis = [0]*900
for i in range(900):
    degree = radians(i/10)
    lis[i] = (T * cos(degree) - kCoefficient*(m*g-T*sin(degree)))/m

maximum = max(lis)
i =  lis.index(maximum)
if maximum <= 0:
    print('Box does not move')
else:
    print("The maximum acceleration is", round(maximum, 2), "at angle", i/10 ,"degrees.")

"""
let the penguins stand in a line
take out your pen and paper to ready to note down many information
go to the first penguin of the line
assign this penguin as the tallest and the shortest of the entire colony
go the the next one penguin until there is no penguin left:
    is this penguin shorter than the data of the shortest penguin on your paper
    if so, assign this one as the shortest
    if not just pass to the next
    
    is this penguin taller than the data of the tallest penguin on your paper
    if so, assign this one as the tallest
    if not just pass to the next

now you traversed the entire colony and found the tallest and the shortest penguin
their data are recorded in your data of the tallest and shortest respectively
"""