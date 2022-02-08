'''
LeetCode #588 - Design In-Memory File System - Amazon & Google & Microsoft & Airbnb & Tesla & Salesforce & ByteDance & Uber

Design a data structure that simulates an in-memory file system.

Implement the FileSystem class:

- FileSystem() Initializes the object of the system.
- List<String> ls(String path)
  - If path is a file path, returns a list that only contains this file's name.
  - If path is a directory path, returns the list of file and directory names in this directory.
**The answer should in lexicographic order.**
- void mkdir(String path) Makes a new directory according to the given path.
  - The given directory path does not exist. 
  - If the middle directories in the path do not exist, you should create them as well.

- void addContentToFile(String filePath, String content)
  - If filePath does not exist, creates that file containing given content.
  - If filePath already exists, appends the given content to original content.
- String readContentFromFile(String filePath) Returns the content in the file at filePath.

Input:
["FileSystem", "ls", "mkdir", "addContentToFile", "ls", "readContentFromFile"]
[[], ["/"], ["/a/b/c"], ["/a/b/c/d", "hello"], ["/"], ["/a/b/c/d"]]

Output:
[null, [], null, null, ["a"], "hello"]

Explanation
FileSystem fileSystem = new FileSystem();
fileSystem.ls("/");                         // return []
fileSystem.mkdir("/a/b/c");
fileSystem.addContentToFile("/a/b/c/d", "hello");
fileSystem.ls("/");                         // return ["a"]
fileSystem.readContentFromFile("/a/b/c/d"); // return "hello"

----------------------------------------------------------------

I prefer use Trie to solve this question.
To build a Trie, the core content area: 1) insert function, 2) search function. Please prepare the template for this kind of problem.

Similary quesiton: https://leetcode.com/problems/implement-trie-prefix-tree/ and https://leetcode.com/problems/design-search-autocomplete-system/ which are use the template to build Trie

Time complexity: O(mn) https://www.quora.com/What-is-the-complexity-of-Trie# and https://stackoverflow.com/questions/13032116/trie-complexity-and-searching
Space complexity: O(mn)
'''
class TrieNode(object):
  def __init__(self):
    self.next = {}
    self.word = ''

class FileSystem(object):
  def __init__(self):
    """
    Initialize your data structure here.
    """
    
    self.value_trie = TrieNode()

  def insert(self, path):
    root_temp = self.value_trie
    
    for char in path.split('/')[1:]:
      if not char in root_temp.next:
        root_temp.next[char] = TrieNode()

      root_temp = root_temp.next[char]

    return root_temp

  def search(self, path):
    root_temp = self.value_trie
    
    for char in path.split('/')[1:]:
      if not char in root_temp.next:
        return root_temp

      root_temp = root_temp.next[char]
    
    return root_temp

  def ls(self, path):
    temp_list = [path.split('/')[-1]]
    root_temp = self.search(path)
    
    if root_temp.word:
      return temp_list
    
    temp_list = sorted(root_temp.next.keys())
    
    return temp_list

  def mkdir(self, path):
    """
    :type path: str
    :rtype: None
    """
    self.insert(path)

  def addContentToFile(self, filePath, content):
    """
    :type filePath: str
    :type content: str
    :rtype: None
    """
    
    root_temp = self.insert(filePath)
    root_temp.word += content

  def readContentFromFile(self, filePath):
    """
    :type filePath: str
    :rtype: str
    """
    root_temp = self.search(filePath)
    temp_value = root_temp.word
    
    return temp_value


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)

# Implement Trie (Prefix Tree) solution, so you can see my template to solve same kind question.

'''
class TrieNode(object):
  def __init__(self):
    self.next = {}
    self.word = False

class Trie(object):
  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.value_trie = TrieNode()

  def insert(self, word):
    """
    Inserts a word into the trie.
    :type word: str
    :rtype: None
    """
    
    temp_root = self.value_trie
    
    for char in word:
      if not char in temp_root.next:
        temp_root.next[char] = TrieNode()

      temp_root = temp_root.next[char]
    
    temp_root.word = True

    def search(self, word):
      """
      Returns if the word is in the trie.
      :type word: str
      :rtype: bool
      """
      
      temp_root = self.value_trie
      
      for char in word:
        if not char in temp_root.next:
          return False

        temp_root = temp_root.next[char]
      
      if temp_root.word:
        return True
      else:
        return False

    def startsWith(self, prefix):
      """
      Returns if there is any word in the trie that starts with the given prefix.
      :type prefix: str
      :rtype: bool
      """
      
      temp_root = self.value_trie
      
      for char in prefix:
        if not char in temp_root.next:
          return False

        temp_root = temp_root.next[char]

      return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

'''
