"""
Xiao Lu
420-SN1 Programming, Section #21
Winter 2025
J. Gullifer, instructor
Lab Assignment #9
"""

s = input("Enter the last 4 digits:")
if s[0] in "89" and s[-1] in"89" and s[1] == s[2] and (int(s[0]) + int(s[1]) + int(s[2]) + int(s[-1])) % 2 == 1:
    print("BLOCK")
else:
    print("ALLOW")

