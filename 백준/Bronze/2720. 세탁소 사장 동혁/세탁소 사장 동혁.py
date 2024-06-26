for _ in range(int(input())):
    money = int(input())
    for i in [25,10,5,1]:
        print(money//i, end=' ')
        money = money % i
    print()