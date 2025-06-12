num = int(input())
if num < 10 and num > 0:
    print(num*num)
else:
    digits = []
    temp = num
    while temp > 0:
        rem = temp % 10
        digits.append(rem)
        temp = temp // 10
    if digits[-2] % 2 == 0 and digits[-2] % 4 == 0:
        print('24')
    elif num % 2 == 0:
        print('2')
    else:
        print('1')
