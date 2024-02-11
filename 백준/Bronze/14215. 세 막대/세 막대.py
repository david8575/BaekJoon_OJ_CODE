side_list = list((map(int, input().split())))
side_list.sort()
while(True):
    if side_list[2] >= side_list[1] + side_list[0]:
        a = side_list[2] - 1
        del side_list[2]
        side_list.append(a)
    else:
        print(sum(side_list))
        break