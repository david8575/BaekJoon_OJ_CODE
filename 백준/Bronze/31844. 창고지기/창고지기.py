pos = list(input())

robot_pos = pos.index('@')
target_pos = pos.index('!')
box_pos = pos.index('#')

if robot_pos < box_pos < target_pos or target_pos < box_pos < robot_pos:
    print(abs(robot_pos - target_pos)-1)
else:
    print(-1)