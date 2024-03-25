n, m = map(int, input().split())

not_seen = set()
not_heard = set()

for i in range(n):
    not_seen.add(input())
for i in range(m):
    not_heard.add(input())

not_seen_heard = sorted(list(not_seen & not_heard))

print(len(not_seen_heard))
for name in not_seen_heard:
    print(name)