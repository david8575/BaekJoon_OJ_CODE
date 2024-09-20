total_video, blue_ray = map(int, input().split()) 
videos = list(map(int, input().split()))
# 탐색 범위 = [영상 길이의 최댓값, 영상 길이의 합]
lower_capacity = max(videos)
upper_capacity = sum(videos)
answer = -1
while lower_capacity <= upper_capacity:
    mid = (lower_capacity + upper_capacity) // 2
    count = 1
    cur_sum = 0
    for video in videos:
        if cur_sum + video > mid:
            count+=1
            cur_sum = video
        else:
            cur_sum += video
    
    if count <= blue_ray:
        answer = mid
        upper_capacity = mid - 1
    else:
        lower_capacity = mid + 1
        
print(answer)