n = int(input())
colors = input()

merge_colors = ""

for i in range(n):
    if i == 0 or colors[i] != colors[i-1]:
        merge_colors += colors[i]
        
blue = merge_colors.count('B')
red = merge_colors.count('R')

print(1 + min(red, blue))