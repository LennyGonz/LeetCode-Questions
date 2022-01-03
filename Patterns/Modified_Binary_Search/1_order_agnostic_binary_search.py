def binary_search(arr, key):
  start = 0
  end = len(arr) - 1
  isAscending = arr[start] < arr[end]
  
  while start <= end:
    middle = start + (end-start) // 2
    
    if key == arr[middle]:
      return middle
    
    if isAscending:
      if key < arr[middle]:
        end = middle - 1
      else:
        start = middle + 1
    else:
      if key > arr[middle]:
        end = middle - 1
      else:
        start = middle + 1
  
  return -1

def main():
  print(binary_search([4, 6, 10], 10))
  print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
  print(binary_search([10, 6, 4], 10))
  print(binary_search([10, 6, 4], 4))

main()
