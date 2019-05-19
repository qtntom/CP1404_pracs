"""
Let user categorise files extension then move files to directories with category name
"""

import os
import shutil


def main():
    os.chdir('filestosort')
    print('Current directory:')
    print(os.getcwd())

    extensions_to_categories = {}
    categories = []
    filenames = os.listdir('.')
    # Loop through every filenames, get extension, check if extension already found
    for filename in filenames:
        extension = os.path.splitext(filename)[1]
        if extension not in extensions_to_categories:
            category = input('What category would you like to sort {} files into? '.format(extension[1:]))
            extensions_to_categories[extension] = category
            # If new category then add to categories list and creat new folder
            if category not in categories:
                categories.append(category)
                os.mkdir(category)
        # Move file to folder whether old or just created
        shutil.move(filename, category + '/' + filename)


main()
