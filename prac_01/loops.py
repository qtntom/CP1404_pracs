for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(21):
    print(str(20-i), end=' ')
print()

star_number = int(input("Number of stars: "))
for i in range(star_number):
    print('*', end=' ')
print()

for i in range(star_number):
    for j in range(i+1):
        print('*', end=' ')
    print()