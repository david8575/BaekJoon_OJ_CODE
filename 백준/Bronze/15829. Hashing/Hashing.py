n = int(input())
word = list(input())

word = [ord(char) for char in word]

answer = 0
for i in range(n):
    answer += ((word[i]-96) * (31 ** i))

print(answer%1234567891)