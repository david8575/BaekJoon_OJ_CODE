word = input()

unique_substrings = set()
for i in range(len(word)):
    for j in range(i + 1, len(word) + 1):
        unique_substrings.add(word[i:j])

print(len(unique_substrings))