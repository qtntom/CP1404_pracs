"""
practice with wikipedia API
"""

import wikipedia

search_phrase = input('Please enter a search phrase:')
while search_phrase != '':
    try:
        wikipedia.search(search_phrase)
    except wikipedia.exceptions.PageError:
        print('No result found. Please try a different phrase: ')
    else:
        print('Page title:', wikipedia.page(search_phrase))
        print('Summary:', wikipedia.summary(search_phrase))
        # print(wikipedia.)
    search_phrase = input('Please enter a search phrase:')
