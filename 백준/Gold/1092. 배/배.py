n = int(input())
hr = list(map(int, input().split()))
m = int(input())
h = list(map(int, input().split()))

hr.sort(reverse=True)
h.sort(reverse=True)

count = 0

if hr[0] < h[0]:
    print(-1)
    exit()
while len(h) > 0:
    for i in hr:
        if len(h) > 0 and i < h[-1]:
            break

        for j in h:
            if j <= i:
                h.remove(j)
                break

    count += 1

print(count)