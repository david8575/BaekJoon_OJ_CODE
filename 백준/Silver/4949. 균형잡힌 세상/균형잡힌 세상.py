while(True):
    str = input()
    if str == '.':
        break
    stack = []
    balanced = True

    for char in str:
        if char in "([":
            stack.append(char)
        elif char == ")":
            if not stack or stack[-1] != "(":
                balanced = False
                break
            stack.pop()
        elif char == ']':
            if not stack or stack[-1] != "[":
                balanced = False
                break
            stack.pop()

    if stack:
        balanced = False
    if balanced:
        print("yes")
    else:
        print("no")