def inOrder(list_1, list_2, root):
    if root <1 or 2**n <= root or list_1[root] != 0:
        return
    inOrder(list_1, list_2, root*2)
    list_1[root] = list_2.pop()
    inOrder(list_1, list_2, root*2+1)


n = int(input())
building_list = list(map(int, input().split()))
building_list.reverse()
tree_list = [0] * 2**n

inOrder(tree_list, building_list, 1)
del tree_list[0]

i = 0
while i < n:
    for j in range((2**i)-1,(2**(i+1))-1):
        print(tree_list[j], end=" ")
    print()
    i+=1