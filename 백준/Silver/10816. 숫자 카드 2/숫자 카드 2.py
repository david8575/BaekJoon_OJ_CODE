def binary_search_left(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left+right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid -1
    return left

def binary_search_right(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left+right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid -1
    return right

def cnt_num(arr, target):
    left_index = binary_search_left(arr, target)
    right_index = binary_search_right(arr, target)
    if left_index <= right_index:
        return right_index - left_index + 1
    else:
        return 0

n = int(input())
list1 = list(map(int,input().split())) 
list1.sort()
m = int(input())
list2 = list(map(int,input().split())) 

for target in list2:
    print(cnt_num(list1,target), end=" ")
