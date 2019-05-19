"""
create folders for each extension type and move files into
By Q.T
"""

import os
import shutil


def main():
    """Main function"""
    os.chdir('FilesToSort')
    print('Current directory: {}'.format(os.getcwd()))

    extensions = []
    filenames = os.listdir('.')
    # Loop through every filename, split the extension from the name, and check if extension already been found
    for filename in filenames:
        extension = os.path.splitext(filename)[1]
        if extension not in extensions:
            os.mkdir(extension[1:])
            extensions.append(extension)
        shutil.move(filename, extension[1:] + '/' + filename)


main()
