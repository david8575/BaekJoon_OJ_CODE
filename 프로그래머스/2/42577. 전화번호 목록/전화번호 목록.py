def solution(phone_book):
    phone_book.sort()

    answer = True    
    
    for i in range(1, len(phone_book)):
        if phone_book[i].startswith(phone_book[i-1]):
            answer = False
            
    return answer