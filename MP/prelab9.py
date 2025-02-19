"""
Xiao Lu
420-SN1 Programming, Section #21
Winter 2025
J. Gullifer, instructor
Pre Lab Assignment 9
"""

# #1
# a, b = True , False
# c = not b
# print(a == True , b == True , c == True)
# print(a, b, c)
#
# """
# a = True, b = False
# c = True
# print(True == True, False == True, True == True)
# print(True, False, True)
# => True False True
# print(a, b, c)
# print(True, False, True)
# => True False True
# """
# #2
# a, b = True , False
# c = not b
# print(a != True , b == False , c == False )
# print(not a, not b, not c)
#
# """
# a = True, b = False
# c = True
# print(True != True, False == False, True == False)
# print(False, True, False)
# => False True False
# print(not True, not False, not True)
# print(False, True, False)
# => False True False
# """
# #3
#
# a, b = True , False
# c = not b
# print(a or b and not c)
# print(a or (b and (not c)))
# print ((a or b) and not c)
# """
# a = True, b = False
# c = True
# print(True or False and not True)
# print(True or False and False)
# print(True or False)
# print(True)
# => True
# print(a or (b and (not c)))
# exact the same step as the last line
# => True
# print((True or False) and not True)
# print(True and False)
# print(False)
# => False
# """

# a, b = True , False
# print(a or d)
# print(b and d)
# print(a and d)
# print(b or d)

"""
a = True, b = False
print(True or d)
=> True as even d is not defined, the statement will always be True

print(False and d)
=> False as even d is not defined, the statement will always be False

print(True and d)
=> Error because python will search for d and it cant find it, there for i haves a NameError

print(False or d)
=> Error because python will search for d and it cant find it, there for i haves a NameError
"""

print(bool ([]) , bool ([[]]))
print(bool (1e-324) , bool (1e-323))
print(bool (0) , bool (1))
print(bool(""), bool(" ")) # empty string vs. single space .

"""
print(bool([]), bool([[]])
print(False, True)
=> False True

print(bool(0.0), bool(1e-323))
print(False, True)
=> False True

print(bool(0), bool(1))
print(False, True)
=> False True

print(bool(""), bool(" ")
print(False, True)
=> False True
"""