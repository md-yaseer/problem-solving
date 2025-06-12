items = int(input())
price = int(input())

if items >= 50 and items <= 100:
    items = items - 10
elif items >= 51 and items <= 200:
    items = items - 20
elif items >= 201:
    items = items - 30

total_amount = price * items

if total_amount >= 1 and total_amount <= 1000:
    discount_percent = 10
elif total_amount >= 1001 and total_amount <= 10000:
    discount_percent = 15
elif total_amount >= 10001:
    discount_percent = 20

discounted_price = total_amount - (total_amount * discount_percent / 100)
print(discounted_price)
