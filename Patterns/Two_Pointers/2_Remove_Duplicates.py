def remove_duplicates(arr):
  # index of the NEXT non-duplicate element
  next_non_duplicate = 1
  
  i = 1
  while (i < len(arr)):
    if arr[next_non_duplicate - 1] != arr[i]:
      arr[next_non_duplicate] = arr[i]
      next_non_duplicate += 1
    i += 1
  
  return next_non_duplicate
# we use next_non_duplicate to count unique elements

# --------------------------------------------------- #

def remove_duplicates_(arr):
  index = 1
  
  while index < len(arr):
    if arr[index] == arr[index-1]:
      arr.pop(index)
    else:
      index += 1
  
  return len(arr)
  
def main():
  print(remove_duplicates([2,3,3,3,6,9,9])) # 4
  print(remove_duplicates([2,2,2,11])) # 2
  
  print()
  
  print(remove_duplicates_([2,3,3,3,6,9,9])) # 4
  print(remove_duplicates_([2,2,2,11])) # 2

main()
