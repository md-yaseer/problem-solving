a = input()  # '5,10,3,5,3,2,1'
amount_list = a.split(',')
for i in range(len(amount_list)):
    amount_list[i] = int(amount_list[i])

# [5,10,3,5,3,2,1]
money = amount_list.pop(0)
# money = 5
# amount_list = [10,3,5,3,2,1]

result = ''
for i in range(len(amount_list)):
    balance = money - amount_list[i]  # 5-10 ==> -5; 5-3 =2
    if balance >= 0:
        money = money - amount_list[i]
        result = result + '1'
    else:
        result = result + '0'
print(result)
