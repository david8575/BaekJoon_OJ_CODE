while True:
    a = input()
    if a != "0":
        reverse_a = "".join(reversed(a))
        if reverse_a == a:
            print("yes")
        else:
            print("no")
    else:
        break