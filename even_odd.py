# program to check wether the number is even or odd.
count=10
while count>0:
    count=count-1
    num=int(input("Enter number: "))
    if num%2==0:
        print(f"{num} is even.")

    else:
        print(f"{num} is odd.")


