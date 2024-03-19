def min_sugar_bags(n):
    _5kg_bags = n // 5
    remained_sugar = n % 5
    while _5kg_bags >= 0:  
        if remained_sugar % 3 == 0:  
            _3kg_bags = remained_sugar // 3
            return _5kg_bags + _3kg_bags
        else:  
            _5kg_bags -= 1  
            remained_sugar += 5  
    return -1  

n = int(input())

print(min_sugar_bags(n))