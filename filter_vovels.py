lst = ['v', 'i', 'k', 'a', 's']
lst1 = ['k', 'a', 'l', 'e']


def filter_vovels(variables):
    vovels = ['a', 'e', 'i', 'o', 'u']

    if variables not in vovels:
        return False

    else:
        return True


result = filter(filter_vovels, lst1)

for vovel in result:
    print(vovel)
