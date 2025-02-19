"""
Xiao Lu
420-SN1 Programming, Section #21
Winter 2025
J. Gullifer, instructor
Lab Assignment #8
"""

DNA = input("Enter a DNA sequence")
n = int(input("Enter the value n:"))
m = int(input("Enter the value m:"))
out = ""
for i in range(len(DNA)):
    if i <= n or i >= m:
        out += DNA[i]

print("The transcribed DNA is", out)
