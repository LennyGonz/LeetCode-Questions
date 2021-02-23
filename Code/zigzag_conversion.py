'''
The string "PAYPALISHIRING" is written in zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string make this conversion given a number of rows:

string convert(string s, int numRows);

example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P         I      N
A      L  S   I  G
Y    A    H  R
P         I
'''


def convert(string, numRows):
  if numRows == 1:
    return string

  row_arr = [""] * numRows
  row_indx = 1
  going_up = True

  for char in string:
    row_arr[row_indx - 1] += char
    if row_indx == numRows:
      going_up = False
    
    elif row_indx == 1:
      going_up = True

    if going_up:
      row_indx += 1
    else:
      row_indx -= 1
  
  return "".join(row_arr)

string1 = "PAYPALISHIRING"
int1 = 3
print(convert(string1, int1))
