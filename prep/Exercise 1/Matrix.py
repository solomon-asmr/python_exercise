# rows=2
# cols=2
# Matrix=[[0 for _ in range(cols)] for _ in range(rows)]
# Matrix[0][0]=1
# Matrix[1][1]=4
#
# Matrix_sum=0
# for row in Matrix:
#     for col in row:
#         Matrix_sum+=col
#
# print(Matrix)
# print(Matrix_sum)

# row=3
# col=3
# matrix=[[0 for _ in range(col)] for _ in range(row)]
# dig=1
# for i in range(row):
#     for j in range(col):
#         if i==j:
#             matrix[i][j]=dig
#             dig+=1
# print(matrix)
# diagonal_sum=0
# for n in range(row):
#     diagonal_sum+=matrix[n][n]
#
# print(f"the sum of the diagonal is {diagonal_sum}")

row=5
col=5
matrix=[[0 for _ in range(col) ] for _ in range(row)]
diagonal_element=1
top_left=5
for i in range(row):
    for j in range(col):
        if i==j:
            matrix[i][j]=diagonal_element
            diagonal_element+=1
        if i+j==row-1:
            matrix[i][j]=top_left
            top_left-=1
print(matrix)