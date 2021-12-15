def find_max_xor(array):
  k = max(array).bit_length()
  trie = Trie(k)

  for i in array:
      trie.insert(i)

  xor = 0
  for i in array:
    xor = max(xor, trie.find_max_xor(i))

  return xor

'''
The complexity of each insert and find_max_xor operation is O(k), where k is the number of bits in the maximum element of the array.
Since we must perform these operations for every element, this algorithm takes O(N * k) time overall.
Similarly, because our trie holds N words of size k, this uses O(N * k) space.
'''
