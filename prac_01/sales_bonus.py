"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sale = float(input("Enter sales ($): "))

while sale >= 0:
    if sale < 1000:
        bonus = sale * .1
    else:
        bonus = sale * .15
    print("Your bonus is {:.2f}".format(bonus))
    sale = float(input("Enter sales ($): "))
