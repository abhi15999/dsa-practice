# Set Matrix Zero Solution
def setValues(matrix, rowIndex, colIndex):
  if matrix[rowIndex][colIndex] != 0:
    matrix[rowIndex][colIndex] = -1

def printMatrix(matrix):
      print(matrix)

def bruteForceSolution():
  matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
  row, col = len(matrix), len(matrix[0])
  for i in range(0, row):
    for j in range(0, col):
      if (matrix[i][j] == 0):
        ind = i - 1;
        while (ind >= 0):
          setValues(matrix, ind, j)
          ind -= 1
        ind = i + 1
        while (ind < row):
          setValues(matrix, ind, j)
          ind += 1
        ind = j - 1
        while (ind >= 0):
          setValues(matrix, i, ind)
          ind -= 1
        ind = j + 1
        while (ind < col):
          setValues(matrix, i, ind)
          ind += 1
  for i in range(0, row):
    for j in range(0, col):
      if matrix[i][j] <= 0:
        matrix[i][j] = 0
  printMatrix(matrix)
  print(bruteForceSolution.__name__);

def semiOptimizedSolution():
  matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
  row, col = len(matrix), len(matrix[0])
  dummyRow = [-1] * row
  dummyCol = [-1] * col
  for i in range(0, row):
    for j in range(0, col):
       if (matrix[i][j] == 0):
         dummyRow[i] = 0
         dummyCol[j] = 0
  for i in range(0, row):
    for j in range(0, col):
      if dummyRow[i] == 0 or dummyCol[j] == 0:
        matrix[i][j] = 0
  printMatrix(matrix)
  print(semiOptimizedSolution.__name__);


# bruteForceSolution()
semiOptimizedSolution();


#asjdjkahdjas