def pascalTriangle():
    n = int(input())
    matrix = [[] for x in range(n)]
    # In var loops

    for i in range(0, n):
        matrix[i] = [0 for x in range(0, (i + 1))]
        matrix[i][0] = matrix[i][i] = 1

        for j in range(1, i):
            matrix[i][j] = matrix[i - 1][j - 1] + matrix[i - 1][j]
    print(matrix)

pascalTriangle()\

    #adadkjadhasdhashjkd