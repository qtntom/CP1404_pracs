import os
import shutil


def main():
    os.chdir('FilesToSort')
    print('Current directory: {}'.format(os.getcwd()))

    extensions = []
    filenames = os.listdir('.')
    for filename in filenames:
        name_and_extension = os.path.splitext(filename)
        if name_and_extension[1] not in extensions:
            os.mkdir(name_and_extension[1][1:])
            extensions.append(name_and_extension[1])
        # shutil.move(filename, '/' + name_and_extension[1][1:] + '/' + filename)


main()
