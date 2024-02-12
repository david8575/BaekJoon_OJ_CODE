n = int(input())
group_word = 0
for i in range(n):
    word = input().lower()
    word_dic = {}
    check = True
    for j in range(len(word)):
        if word[j] not in word_dic:
            word_dic.setdefault(word[j])
        else:
            if word[j-1] != word[j]:
                check = False
    if check:
        group_word += 1
print(group_word)