n = int(input())
subject_list = list(map(int, input().split()))
max = max(subject_list)

for i in range(n):
    subject_list[i] = subject_list[i]/max*100
print(sum(subject_list)/n)