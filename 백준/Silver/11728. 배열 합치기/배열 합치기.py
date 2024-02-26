m, n = map(int, input().split())

list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))
list_c = list_a + list_b
list_c.sort()

for i in range(m+n):
    print(list_c[i], end=" ")