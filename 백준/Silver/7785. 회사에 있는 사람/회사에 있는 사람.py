import sys

input = sys.stdin.readline

n = int(input())
company = dict()

for _ in range(n):
    name, status = map(str, input().split())
    if status == "enter":
        company[name] = status
    if status == "leave":
        del company[name]

for key in sorted(company.keys(), reverse=True):
    print(key)