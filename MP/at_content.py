"""
Xiao Lu
420-SN1 Programming, Section #21
Winter 2025
J. Gullifer, instructor
Lab Assignment #8
"""

DNA = input("Enter a DNA sequence")

t = 0
for i in range(len(DNA)):
    if DNA[i] in "AT":
        t += 1
print("The AT content is", t/len(DNA))