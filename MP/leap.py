year = int(input())

if year < 1582:
    print('Invalid year')

elif year % 4 == 0:
    if year % 100 == 0 and year % 400 !=0:
        print('Not leap')
    else:
        print('Leap')
else:
    print('Not leap')
