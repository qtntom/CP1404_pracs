'''
Electricity bill estimator using Dictionary
'''

TARIFF_DICT = {'11': 0.244618, '31': .136928, '21': .3, '41': .4, '51': .5}
print('Electricity bill estimator 2.0')

tariff_key_list = [key for key in TARIFF_DICT]
tariff_key_list = ','.join(tariff_key_list)
print('Please select a tariff:', tariff_key_list)
# print(tariff_key_list)
tariff = input()

while tariff not in TARIFF_DICT:
    print('Invalid tariff!')
    tariff = input('Which tariff? ')

daily_use = float(input('Enter daily use in kWh: '))
day = int(input('Enter no. of billing days: '))

print('Estimated bill: ${:.2f}'.format(day * daily_use * TARIFF_DICT[tariff]))
