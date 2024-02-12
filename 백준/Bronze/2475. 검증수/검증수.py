check_list = list(map(int, input().split()))
check_num = 0
for i in check_list:
    check_num += i*i
print(check_num%10)