# rows = 6
# for i in range(rows, 0, -1):
#     for j in range(0, i + 1):
#         print("*", end=' ')
#     print()
# for k in range(rows):
#     for m in range(0, k + 1):
#         print("*", end=" ")
#     print()

rows=5
for i in range(1,rows+1):
    print(" *" * i)
for j in range(rows+1,0,-1):
    print(" *" *j)