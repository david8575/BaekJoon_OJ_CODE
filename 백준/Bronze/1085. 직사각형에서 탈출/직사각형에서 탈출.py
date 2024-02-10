x, y, w, h = map(int, input().split())
list1 = [x, y, (h-y), (w-x)]
print(min(list1))