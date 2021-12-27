def PrimeNumbers(lower,upper):
    """
    This function returns prime numbers between given range.
    :param lower:Enter lower value of range.
    :param upper:Enter upper value of range.
    :return:prime numbers between range.
    """

    for num in range(lower,upper+1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                print(num)

        else:
            return "Invalid range."

PrimeNumbers(5,20)
print(help(PrimeNumbers))
