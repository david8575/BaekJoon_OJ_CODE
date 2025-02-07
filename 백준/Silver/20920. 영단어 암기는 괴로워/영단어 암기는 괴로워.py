from collections import Counter
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
words = []

for _ in range(n):
    words.append(input().rstrip())

memories = []
for word in words:
    if len(word) >= m:
        memories.append(word)

counter = Counter(memories)

sorted_words = sorted(counter.keys(), key=lambda x:(-counter[x], -len(x), x))

for word in sorted_words:
    print(word)