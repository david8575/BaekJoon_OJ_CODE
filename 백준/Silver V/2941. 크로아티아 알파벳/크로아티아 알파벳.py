word = input()
croa_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for alpha in croa_list:
    if alpha in word:
        word = word.replace(alpha, "1")

print(len(word))