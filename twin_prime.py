a = input()  # '2,3,5,11,13,17,19'
num_list = a.split(',')
for i in range(len(num_list)):
    num_list[i] = int(num_list[i])


def is_prime(number):
    is_prime = True
    for j in range(2, number):
        if number % j == 0:
            is_prime = False
            break
    return is_prime


# num [2,3,5,11,13]
count = 0
for i in range(len(num_list)):
    if is_prime(num_list[i]):
        next_prime = num_list[i] + 2
        if is_prime(next_prime) and next_prime in num_list:
            count = count + 1
print(count)
