# Sample Space with Parenthesis (not inclusive)
from permutation import *

# num = [1,4,5,6]

print("type in numbers with space: ex. 1 2 3 4")
num = input().split()
op = ['+','-','*','/']

numList = permute([str(n) for n in num])
opList = permute_with_repetition(op,3)

sampleSpace = []

for p in numList:
    for o in opList:
        sampleSpace.append(f"{p[0]} {o[0]} {p[1]} {o[1]} {p[2]} {o[2]} {p[3]}")
        sampleSpace.append(f"({p[0]} {o[0]} {p[1]}) {o[1]} {p[2]} {o[2]} {p[3]}")
        sampleSpace.append(f"({p[0]} {o[0]} {p[1]} {o[1]} {p[2]}) {o[2]} {p[3]}")
        sampleSpace.append(f"{p[0]} {o[0]} ({p[1]} {o[1]} {p[2]}) {o[2]} {p[3]}")
        sampleSpace.append(f"{p[0]} {o[0]} ({p[1]} {o[1]} {p[2]} {o[2]} {p[3]})")
        sampleSpace.append(f"{p[0]} {o[0]} {p[1]} {o[1]} ({p[2]} {o[2]} {p[3]})")
        sampleSpace.append(f"({p[0]} {o[0]} {p[1]}) {o[1]} ({p[2]} {o[2]} {p[3]})")
        sampleSpace.append(f"(({p[0]} {o[0]} {p[1]}) {o[1]} {p[2]}) {o[2]} {p[3]}")
        
for ss in sampleSpace:
    try:
        value = eval(ss)
        if value == 24:
            print(f"{ss} = {value}")
    except ZeroDivisionError:
        continue