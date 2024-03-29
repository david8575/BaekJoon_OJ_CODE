n = int(input())
nums_1 = list(map(int, input().split()))
nums_2 = list(map(int, input().split()))

nums_1.sort()
nums_2.sort(reverse = True)

minSum = 0
for i in range(n):
    minSum += (nums_1[i]*nums_2[i])

print(minSum)