# Write a program to print 10 fibonacci numbers.

# num1 = 0
# num2 = 1
#
# for i in range(2, 12):
#     sum = num1+num2
#     print(sum)
#     num1 = num2
#     num2 = sum

def fibbo(num):
    """
    :param num: enter num ,upto num returns fibbonacci numbers.
    :return: return fibonacci numbers.
    """
    a = 0
    b = 1

    for i in range(2,num+1):
        sum = a + b
        print(sum)
        a = b
        b = sum
fibbo(20)