numbers = []
number = float(input('Enter any number: (negative number to quite) '))
while number >= 0:
    numbers.append(number)
    number = float(input('Enter next number: '))

for i in range(len(numbers)):
    print('Number', i, ': ', numbers[i])

# print('The first number is', numbers[0])
# print('The last number is', numbers[-1])
# print('The smallest number is', min(numbers))
# print('The largest number is', max(numbers))
# print('The average of the numbers is', sum(numbers) / len(numbers))
