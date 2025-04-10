import sys
input = sys.stdin.readline
s = set()

m = int(input())

for _ in range(m):
    temp = input().strip().split()

    if len(temp) == 1:
        if temp[0] == 'all':
            s = set(range(1, 21))
        else:  # empty
            s.clear()
    else:
        cmd, x = temp
        x = int(x)

        if cmd == 'add':
            s.add(x)
        elif cmd == 'remove':
            s.discard(x)
        elif cmd == 'check':
            print(1 if x in s else 0)
        elif cmd == 'toggle':
            if x in s:
                s.discard(x)
            else:
                s.add(x)