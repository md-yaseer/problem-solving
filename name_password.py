n = input()
le = str(len(n))
lc = n[-1]
fc = n[0]
if len(n) % 2 == 0:
    print(lc+le+'@'+fc+'654'+lc)
else:
    print(lc+le+'!'+fc+'432'+lc)
