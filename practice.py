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
  
  print("trie before the recursion",trie)
  trie[character] = add_to_trie(s[1:], trie[character])
  
  print("done with word trie:", trie)
  return trie

def get_dictionary_trie(dictionary):
  trie = dict()
  for word in dictionary:
    trie = add_to_trie(word, trie)
    print("trie inside of get_dictionary_trie", trie)
  
  print("this gets returned \n", trie)

  print()
  return trie

print(get_dictionary_trie(['dog','deer','deal']))
