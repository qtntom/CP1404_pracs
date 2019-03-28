def main():
    MIN_LENGH = 5

    pw = get_password(MIN_LENGH)

    print_asterisks(pw)


def print_asterisks(pw):
    masked_pw = ''
    for i in range(len(pw)):
        masked_pw += '*'
    print(masked_pw)


def get_password(MIN_LEN):
    pw = input('what is ur password?')
    while len(pw) < MIN_LEN:
        print('Invalid password!')
        pw = input('what is ur password?')
    return pw


main()