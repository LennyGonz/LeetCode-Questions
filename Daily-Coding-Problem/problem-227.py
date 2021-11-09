def get_neighbors(location, grid_size=4):
  i, j = location
  neighbors = [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1), (i, j + 1), (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]
  return [n for n in neighbors if 0 <= n[0] < grid_size and 0 <= n[1] < grid_size]

def make_trie(words):
  root = {}
  for word in words:
    current_dict = root
    for letter in word:
      current_dict = current_dict.setdefault(letter, {})
    current_dict['#'] = '#'
  return root

def search(location, grid, trie, visited, word, result):
  visited.add(location)
  letter = grid[location[0]][location[1]]
  if '#' in trie[letter]:
    result.add(''.join(word))

  for neighbor in get_neighbors(location):
    if neighbor not in visited:
      row, col = neighbor
      if grid[row][col] in trie[letter]:
        subtrie = trie[letter]
        word.append(grid[row][col])
        search(neighbor, grid, subtrie, visited, word, result)
        word.pop()
        visited.remove(neighbor)

def boggle(grid, trie):
  visited = set()
  result = set()

  for row in range(len(grid)):
    for col in range(len(grid)):
      if grid[row][col] in trie:
        word = [grid[row][col]]
        search((row, col), grid, trie, visited, word, result)

  return list(result)
