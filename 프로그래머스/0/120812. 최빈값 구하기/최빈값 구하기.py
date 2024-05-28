from collections import Counter

def solution(array):
    counter = Counter(array)
    elements = counter.most_common()
    freq = elements[0][1]
    max = [item[0] for item in elements if item[1] == freq]
    if len(max) > 1:
        return -1
    else:
        return max[0]
    