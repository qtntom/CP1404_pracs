words_counts = {}

text = input('Please enter your text:')
text_list = text.split()
for word in text_list:
    if word in words_counts:
        words_counts[word] += 1
    else:
        words_counts[word] = 1

sorted_keys = sorted(words_counts)

max_length = len(sorted_keys[0])
for key in sorted_keys:
    if max_length < len(key):
        max_length = len(key)

for key in sorted_keys:
    print('{:{}} : {}'.format(key, max_length, words_counts[key]))
