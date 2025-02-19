ps = input("Enter your password for validity")
satisfy = 0
if " " in ps or len(ps) < 10:
    print('Invalid')
elif len(ps) < 16:
    for i in ps:
        if i in "$*&%#." or i.isnumeric():
            satisfy += 1
        if satisfy >= 2:
            break

    if satisfy >= 2:
        print('Valid')
    else: print('Invalid')
else:
    print('Valid')