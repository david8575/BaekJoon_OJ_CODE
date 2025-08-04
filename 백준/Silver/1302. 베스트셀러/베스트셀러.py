n = int(input())

sell = {}

for _ in range(n):
    book = input()

    if book not in sell:
        sell[book] = 1
    
    sell[book] += 1

max_count = 0
max_book = ""

for k, v in sell.items():
    if max_count < v:
        max_count = v
        max_book = k
        
    elif max_count == v:
        if max_book > k:
            max_book = k

print(max_book)