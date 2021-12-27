# write a program to remove all special characters from given string.

# def removeAll(Input):
#     """
#     :param Input: Accept string with special characters.
#     :return: only characters.
#     """
#     x = [char for char in Input if
#          ord(char) in range(ord('a'), ord('z'), 1) or ord(char) in range(ord('A'), ord('Z'), 1)]
#
#     return ''.join(x)
#
#
# Input = 'V@i%&k@a&$#S '
#
# print(removeAll(Input))


def removeAll(Input):
    """
    :param Input: Accept string with special characters.
    :return: only characters.
    """
    x = []
    for char in Input:
        if ord(char) in range(ord('a'), ord('z'), 1) or ord(char) in range(ord('A'), ord('Z'), 1):
            x.append(char)

    return ''.join(x)


Input = 'V@i%&k@a&$#S '

print(removeAll(Input))