hour, minute, second = map(int, input().split())
cooking_second = int(input())

total_seconds = hour * 3600 + minute * 60 + second + cooking_second

total_seconds %= 24 * 3600

hour = total_seconds // 3600
minute = (total_seconds % 3600) // 60
second = total_seconds % 60

print(hour, minute, second)