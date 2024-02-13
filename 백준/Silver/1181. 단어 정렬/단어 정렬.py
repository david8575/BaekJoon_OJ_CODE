n = int(input())
word_list = []
for i in range(n):
    word = input()
    if word not in word_list:
        word_list.append(word)
word_list.sort()
word_list = sorted(word_list, key = len)
for i in range(len(word_list)):
    print(word_list[i])