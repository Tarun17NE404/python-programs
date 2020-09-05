for i in range(101):
    result = 0
    n = len(str(i))
    while(i != 0):
        t = i % 10
        result = result + t**n
        i = i//10
        if i == result:
            print(i)



