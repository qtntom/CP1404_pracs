import os
import shutil


def main():
    os.chdir('FilesToSort')
    print('Current directory: {}'.format(os.getcwd()))

    extensions = []
    filenames = os.listdir('.')
    for filename in filenames:
        extension = os.path.splitext(filename)[1]
        if extension not in extensions:
            os.mkdir(extension[1:])
            extensions.append(extension)
        shutil.move(filename, extension[1:] + '/' + filename)


main()
