u = int(input())
if u >= 1 and u <= 25:
    print('$', 1.25*u)
elif u >= 26 and u < 50:
    print('$', 1.45*u)
elif u >= 51 and u <= 75:
    print('$', 1.65*u)
elif u >= 76 and u <= 95:
    print('$', 1.95*u)
elif u > 95:
    print('$', 2.00*u)
