words_counted = {}

input_string = input('Please enter your text:')
words = input_string.split()
for word in words:
    if word in words_counted:
        words_counted[word] += 1
    else:
        words_counted[word] = 1

sorted_keys = sorted(words_counted)

max_length = len(sorted_keys[0])
for key in sorted_keys:
    if max_length < len(key):
        max_length = len(key)

for key in sorted_keys:
    print('{:{}} : {}'.format(key, max_length, words_counted[key]))
