number_item = int(input("Number of item: "))
while number_item < 0:
    print("Invalid number of items!")
    number_item = int(input("Number of item: "))
total_price = 0

for i in range(number_item):
    item_price = float(input("Price of item: "))
    total_price += item_price

if total_price > 100:
    total_price = total_price * .9

print("Total price for {} item is ${:>10}".format(number_item,total_price))
