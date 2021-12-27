# a=list(range(10))
# print(a)
# print(a[::2])
# print(a[1::3])
# print(a[3::-1])
# Multiple space seperated inputs in a list.
# We can use map function to convert input value to an integer value and then add those integer value to list.

# x=list(map(int,input("Enter numbers: ").split()))
# print(x)
# 2] Sum of digit of a number.
# num=1234   here we find sum of digit
# output should be 10.
# Method 1:
# sum_of_digit=lambda x:sum(map(int,str(x)))
# output=sum_of_digit(1234)
# print(f"Sum of digit is {output}")
# Method 2:
num=1234
sum=0
while num>0:
    result=num%10
    sum=sum+result
    num=num//10
print(sum)
