level = int(input())

for i in range(level):
    print(" " * (level-1-i), end="")
    print("*" * (2*i+1))

for i in range(level-1):
    print(" " * (i+1),end="")
    print("*" * ((2*(level-1-i))-1))