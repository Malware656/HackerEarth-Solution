def symmetric(matrix,n):
    for i in range(n):
        for j in range(n):
            if int(matrix[i][0][j]) != int(matrix[n-1-i][0][j]):
                return 'NO'
            if int(matrix[i][0][j]) != int(matrix[i][0][n-1-j]):
                return 'NO'
    return 'YES'
t = int(input())
for _ in range(t):
    n = int(input())
    matrix = []
    for i in range(n):
        temp = list((input().split()))
        matrix.append(temp)
    print(symmetric(matrix,n))
    
# ALTER
# def symmetric(matrix,n):
# for m, i in enumerate(range(n), 1):
#     for k, j in enumerate(range(n), 1):
#         if int(matrix[i][0][j]) != int(matrix[i][0][-k]):
#             return 'NO'
#         if int(matrix[i][0][j]) != int(matrix[-m][0][j]):
#             return 'NO'
#     return 'YES'
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     matrix = []
#     for i in range(n):
#         temp = list((input().split()))
#         matrix.append(temp)
#     print(symmetric(matrix,n))
