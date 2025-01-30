iterations = int(input("Enter a positive integer:"))
counter = 1
s = 0 # renamed the sum to s since sum is a builtin function already, I don't want to mess with it
while counter <= iterations:
    if counter % 3 == 0 or counter % 5 == 0: # this if statement checks if the current number is either a multiple of
        # 3 or multiple of 5, if so, the sum "s" is incremented by the counter
        s += counter # s+= counter is a shorter way of writing s = s + counter

    counter += 1

print(s)
