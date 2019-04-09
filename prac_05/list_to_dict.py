names_dob = {}

def main():
    # for i in range(5):
    #     name = input('Person {} name:'.format(i + 1))
    #     dob = input('Person {} DOB:'.format(i + 1))
    #     dob = int(dob[-4:])
    #     names_dob[name] = dob
    #
    # for key, value in names_dob.items():
    #     print('{} is {} year old'.format(key, 2019 - value))

    print(create_dict_from_lists(['a', 'b', 'c'], [1,2,3]))


def create_dict_from_lists(list1, list2):
    return dict(zip(list1, list2))

main()