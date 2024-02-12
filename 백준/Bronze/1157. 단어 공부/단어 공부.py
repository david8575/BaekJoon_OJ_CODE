str = input().upper()
word_count = {}

for i in range(len(str)):
    if str[i] in word_count:
        word_count[str[i]] += 1
    else:
        word_count[str[i]] = 1

many_word = ""
max_count = 0
for key, value in word_count.items():
    if value > max_count:
        many_word = key
        max_count = value
    elif value == max_count:
        many_word = "?" 
        
print(many_word)