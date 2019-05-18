"""
Clean up files by formatting file names
By Q.T
"""
import shutil
import os


def main():
    """Walk through all directories and change file names as it goes"""
    os.chdir('lyrics/christmas')
    print("Starting directory is: {}".format(os.getcwd()))

    for directory_name, subdirectories, filenames in os.walk('.'):
        for filename in filenames:
            new_name = get_fixed_filename(filename)
            os.rename(os.path.join(directory_name, filename), os.path.join(directory_name, new_name))
            print('{:30} renamed to {}'.format(filename, new_name))


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    filename = filename.replace(" ", "_").replace(".TXT", ".txt")
    new_name = ''
    for i, character in enumerate(filename):
        try:
            if filename[i-1] == '_':
                new_name += character.upper()
            elif character.isupper() and filename[i-1].islower():
                new_name += '_' + character
            else:
                new_name += character
        except IndexError:
            pass
    return new_name[1:]


main()
