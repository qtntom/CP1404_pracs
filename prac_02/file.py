'''
FILENAME = 'name'
output_file = open(FILENAME, 'w')

input_name = input("What's your name: ")
print(input_name, file=output_file)
output_file.close()

output_file = open(FILENAME)
output_name = output_file.read()
print("Your name is {}".format(output_name))
output_file.close()
'''

output_file = open('numbers', 'r')
lines = output_file.readlines()
numbers = []

for line in lines:
    numbers.append(int(line))


print("{}".format(sum(numbers)))

output_file.close()
