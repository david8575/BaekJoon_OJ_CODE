def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left+right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid -1
    return False

n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

arr1.sort()

for target in arr2:
    if binary_search(arr1, target):
        print(1)
    else:
        print(0)