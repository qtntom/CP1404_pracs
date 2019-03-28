MIN_LEN = 5

pw = input('what is ur password?')
while len(pw) < MIN_LEN:
    print('Invalid password!')
    pw = input('what is ur password?')

masked_pw = ''
for i in range(len(pw)):
    masked_pw += '*'

print(masked_pw)