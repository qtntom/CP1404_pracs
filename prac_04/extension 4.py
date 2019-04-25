def main():
    a = [1, 2, 3]
    b = [5, 6, 7]
    print(add_memberwise(a, b))


def add_memberwise(a, b):
    return [x + b[i] for i, x in enumerate(a)]


main()
