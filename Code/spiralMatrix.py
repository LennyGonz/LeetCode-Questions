def spiralMatrix(matrix):
  if not matrix:
    return []
  
  rowbegin = 0
  rowend = len(matrix)
  columnbegin = 0
  columnend = len(matrix[0])
  res = []

  while rowend > rowbegin and columnend > columnbegin:
    # deals with the first row [1,2,3]
    for i in range(columnbegin, columnend):
      res.append(matrix[rowbegin][i])
    
    # deals with the elements between the end of row 1 and the end of the last row of the matrix
    for j in range(rowbegin+1, rowend-1):
      res.append(matrix[j][columnend - 1])
    
    if (rowend != rowbegin + 1):
      for i in range(columnend - 1, columnbegin - 1, -1):
        res.append(matrix[rowend-1][i])
    
    if (columnbegin != columnend - 1):
      for j in range(rowend - 2, rowbegin, -1):
        res.append(matrix[j][columnbegin])
  
    rowbegin += 1
    rowend -= 1
    columnbegin += 1
    columnend -= 1
  
  return res
    
m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(spiralMatrix(m1))
