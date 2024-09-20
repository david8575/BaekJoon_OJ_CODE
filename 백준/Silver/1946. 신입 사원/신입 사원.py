test = int(input())

for _ in range(test):
    n = int(input())
    people = []
    for _ in range(n):
        document, interview = map(int, input().split())
        people.append((document, interview))
        
    people.sort()
    
    rank = 1000000
    count = 0
    for i in range(n):
        if people[i][1] < rank:
            count += 1
            rank = people[i][1]
    print(count)