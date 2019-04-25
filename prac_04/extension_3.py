texts = []
duplicate_text = ''
text = input('Enter any text: (blank to quite) ')
while text != '':
    if text in texts:
        duplicate_text += text + ','
    else:
        texts.append(text)
    text = input('Enter next text: ')

if duplicate_text != '':
    print('Strings repeated:', duplicate_text)
else:
    print('No repeated strings entered')