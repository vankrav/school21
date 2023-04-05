s = 0
while(True):
    x = input()
    if x == "":
        break
    elif int(x) % 2 == 0:
        s += int(x)
        print(s)
    else:
        print(0)
