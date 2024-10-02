a, b, c, m = map(int, input().split())

tired = 0
worked = 0
for _ in range(24):
    if tired + a > m:
        tired -= c
        tired = max(0, tired)
    else:
        tired += a
        worked += b

print(worked)