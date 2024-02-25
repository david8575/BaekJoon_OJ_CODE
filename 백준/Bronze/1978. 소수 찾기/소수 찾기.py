def is_prime_num(num) :
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

n = int(input())
count = 0
num_list = list(map(int, input().split()))

for i in range(len(num_list)):
    if num_list[i] != 1:
        if is_prime_num(num_list[i]):
            count+=1

print(count)