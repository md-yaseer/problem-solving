a = input()
absent_count = 0
con_late = False
for i in range(len(a)):
    if a[i] == 'A':
        absent_count = absent_count + 1
    if a[i] == 'L' and a[i-1] == 'L' and a[i-2] == 'L':
        con_late = True
        break

if absent_count > 1 or con_late:
    print(False)
else:
    print(True)
