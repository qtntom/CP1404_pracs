from random import randint

no_of_picks = int(input('How many quick pick? '))

for i in range(no_of_picks):
    temp_pick = []
    for j in range(6):
        temp_random = randint(1, 45)
        while temp_random in temp_pick:
            temp_random = randint(1, 45)
        temp_pick.append(temp_random)
    temp_pick.sort()
    temp_pick = str(temp_pick).replace(',', '', 5).strip(']').strip('[')

    print(temp_pick)
