def solution(participant, completion):
    
    participant_dict = {}
    hash_sum = 0
    
    for p in participant:
        participant_dict[hash(p)] = p
        hash_sum += hash(p)
        
    for c in completion:
        hash_sum -= hash(c)
        
    answer = participant_dict[hash_sum]
    
    return answer