# I want to create a matrix which looks like below:
#
# matrix = [[0, 1, 2, 3, 4],
#           [0, 1, 2, 3, 4],
#           [0, 1, 2, 3, 4],
#           [0, 1, 2, 3, 4],
#           [0, 1, 2, 3, 4]]

# matrix=[]
# for i in range(5):
#     matrix.append([])
#
#     for j in range(5):
#         matrix[i].append(j)
# print(* matrix,sep='\n')

x=[[i for i in range(5)] for j in range(5)]

print(*x,sep='\n')
