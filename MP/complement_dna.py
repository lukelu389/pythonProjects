"""
Xiao Lu
420-SN1 Programming, Section #21
Winter 2025
J. Gullifer, instructor
Lab Assignment #8
"""


DNA = input("Enter a DNA sequence")

out = ""
for i in range(len(DNA)):
    if DNA[i] == "A": out+= "T"
    elif DNA[i] == "T": out += "A"
    elif DNA[i] == "C": out += "G"
    else: out += "C"

print("The complement is", out)