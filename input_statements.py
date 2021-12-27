#  1) split()
#  2) list comprehension
#  3) list unpacking

# a,b=[int(x) for x in input("Enter 2 elements: ").split()]
# print(a,b)

# s="Hello*world"
# a=s.split('*')
# print(a)

# List comprehension

fruits=['apple','orange','mango','grapes']
# new_lst=[]
# for ele in fruits:
#     if 'p' in ele:
#         new_lst.append(ele)
# print(new_lst)

# result=[x for x in fruits if 'n' in x]
# print(result)
# lst=[ i**2 for i in range(21) if i > 10]
# lst1=[ i for i in range(1,20) if i%2==0]
# print(lst1)

# a=input("Enter 5 numbers: ").split('----')
# print(a)
# b=input("Enter 5 numbers: ").split(',')
# print(b)
# for j in b:
#     print(j)
# c=[int(x) for x in b]
# print(c)

# **List Unpacking**
# List unpacking means extract the values in list back to the variables.

lst=[1,2,3,4,5,6,7,8]
a,b,*c=lst
print(a)
print(b)
print(c)

