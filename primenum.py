for num in range(100, 301): 
    flag = True
    if num < 2:
        flag = False
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                flag = False
                break
    if flag :
        print(num)