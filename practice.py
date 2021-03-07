# def convert(string, numRows):
#   if numRows == 1:
#     return string

#   row_arr = [""] * numRows
#   row_index = 1
#   going_up = True

#   for char in string:
#     row_arr[row_index - 1] += char  #remember array indexes start at 0... so we add a character at index 0
    
#     if row_index == numRows:
#       going_up = False  #remember once we reach numRow that means we switch direction (in this case down)
    
#     elif row_index == 1:
#       going_up = True  #Once we start going down the point of inflection is 1 (thus we must go back up)
    
#     if going_up:
#       # now if the direction we're going is up that means we must increase our row_index
#       row_index += 1
#     else:
#       # if we reached numRow that means we must return back to 1
#       row_index -= 1
    
#     print("#################")
#     print(row_arr)
#     print("#################")
  
#   # read up on join -- but basically we join an empty string with all the characters in the array
#   return "".join(row_arr)


# input1 = 'PAYPALISHIRING'
# print(convert(input1, 4))

# def get_suggestions(wordlist, prefix):
#   return [word for word in wordlist if word[:len(prefix)] == prefix]

# print(get_suggestions(['dog','deer','deal'], 'de'))
# print(get_suggestions(['cat','car','cer'], 'ca'))
# print(get_suggestions(['cat','car','cer'], 'ae'))


def add_to_trie(s, trie):
  if not s:
    return trie
  print("****")
  print("string:", s)
  print("trie at the beginning", trie)
  character = s[0]
  print("char",character)
  if character not in trie:
    trie[character] = dict()
  
  print("trie before the recursion", trie)
  print("s[1:]", s[1:])
  print("character",character)
  print("trie[character]",trie[character])
  trie[character] = add_to_trie(s[1:], trie[character])
  
  print("done with word trie:", trie)
  return trie
trie[character]
def get_dictionary_trie(dictionary):
  trie = dict()
  for word in dictionary:
    trie = add_to_trie(word, trie)
    print("trie inside of get_dictionary_trie", trie)
  
  print("this gets returned \n", trie)

  print()
  return trie

print(get_dictionary_trie(['dog','deer','deal']))

####################################################
'''
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''


def multiplyArray(numlist):
  right_prod_array = list()
  cumulative_product = 1

  for num in numlist:
    cumulative_product *= num
    right_prod_array.append(cumulative_product)
  print("right prod array - cumulativeProduct", cumulative_product)
  print("right product array", right_prod_array)
  
  cumulative_product = 1
  left_prod_array = list()
  for num in numlist[::-1]:
    print("printing backwards", num)
    cumulative_product *= num
    left_prod_array.append(cumulative_product)
  print("left prod array - cumulativeProduct", cumulative_product)

  left_prod_array = left_prod_array[::-1]
  print('left_prod_array[::-1]:', left_prod_array)

  output_array = list()

  for i in range(len(numlist)):
    print("i",i)
    num = None
    print("num:",num)
    
    if i == 0:
      num = left_prod_array[i + 1]
    
    elif i == len(numlist) - 1:
      num = right_prod_array[i - 1]
    
    else:
      num = right_prod_array[i - 1] * left_prod_array[i + 1]

    print("num being added", num)
    output_array.append(num)
  
  return output_array

print(multiplyArray([1,2,3,4,5]))
