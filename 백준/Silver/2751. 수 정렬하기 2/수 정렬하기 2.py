import sys
n = int(input())
list1 = []
for i in range(n):
    a = int(sys.stdin.readline())
    list1.append(a)
list1.sort()
for i in range(len(list1)):
    print(list1[i])