a, b, c = list(map(int, input().split()))
number = (a / 40000 + b / 60000 + c / 70000) * 60
print(format(number, ".2f"))
