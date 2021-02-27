def convert(string, numRows):
  if numRows == 1:
    return string

  row_arr = [""] * numRows
  row_index = 1
  going_up = True

  for char in string:
    row_arr[row_index - 1] += char  #remember array indexes start at 0... so we add a character at index 0
    
    if row_index == numRows:
      going_up = False  #remember once we reach numRow that means we switch direction (in this case down)
    
    elif row_index == 1:
      going_up = True  #Once we start going down the point of inflection is 1 (thus we must go back up)
    
    if going_up:
      # now if the direction we're going is up that means we must increase our row_index
      row_index += 1
    else:
      # if we reached numRow that means we must return back to 1
      row_index -= 1
    
    print("#################")
    print(row_arr)
    print("#################")
  
  # read up on join -- but basically we join an empty string with all the characters in the array
  return "".join(row_arr)


input1 = 'PAYPALISHIRING'
print(convert(input1, 4))
