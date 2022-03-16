'''
Leetcode #297

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree.
There is no restriction on how your serialization/deserialization algorithm should work.
You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

        1
      /   \
     2     3
          / \
         4   5
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This seems like a standard tree problem

- We want to iterate the entire tree -> as we reach each node we want to stringify each node
- We also need to think about a delimiter to sperate the nodes from each other, useful for when we deserialize

This DFS implementation is basically the standard, and is also known as PreOrder Traversal (root -> left subtree -> right subtree)

So the way our traversal will work is Preorder Traversal

* As we taverse, and reach a null on the left most path -> that's our signal to move to the right (standard)
* when we reach a null on the right most path -> that's our signal to move to the right substree (standard)

BUT when we reach the nulls, we also add them to our string, bc when we deserialize the nulls will act as flags to create the binary tree correctly

That's how we serialize the Binary Tree

To DESERIALIZE the tree
We use the serialized string + preorder traversal to reconstruct the tree

Well we know that the first node of this string is the root, BUT
  how do we know when the left subtree STOPS
    AND the right subtree STARTS
  
  * well the value after 2 is Null that means we can't continue 2's left subtree
    * so any value after that Null will go in the right subtree

That's how we deserialize the serialized string
'''
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Codec:
  def serialize(self, root):
    # res will be a list where we store our stringified tree
    res = []
    
    # we start out preorder traversal
    def dfs(node):
      # base case -> if the current node we're on IS NULL -> we append "Null" to the stringified tree
      if not node:
        res.append("Null")
        return
      
      # if the node we're on IS NOT NULL
      # we stringify the value of the node and append it to our list
      res.append(str(node.val))
      
      # then continue traversing
      dfs(node.left)
      dfs(node.right)
      
      # once the function is done recursing - it'll return by default
      # then we can join everything in our res list, using a comma as our delimiter
    
    dfs(root)
    
    return ",".join(res)
  
  # the input is the serialized tree
  def deserialize(self, data):
    # we want to split our string and store it in a list - hence why we use split
    vals = data.split(',')
    
    # we want to create a global pointer (i) b/c it's easier to use when we declare the nested dfs function (we won't have to pass it in)
    self.i = 0
    
    def dfs():
      # base case: if we reach a Null in the serialized string
      # we return a null node
      if vals[self.i] == "Null":
        self.i += 1
        return None

      # if the node is not a Null we create the node
      node = TreeNode(int(vals[self.i]))
      
      # if we created a node -> we still need to move along through the input
      # so we increment the pointer
      self.i += 1
      
      # once we're done with the root, we begin "traversing" and properly building the tree
      node.left = dfs()
      node.right = dfs()
      
      # once the recursion is done, node will be our root
      return node
    
    # the dfs function builds the tree and returns the root node - we just return and excute the function in the same line
    return dfs()

def main():
  root = TreeNode(1)

  root.left = TreeNode(2)
  root.right = TreeNode(3)

  root.left.left = TreeNode(4)
  root.left.right = TreeNode(5)

  root.right.left = TreeNode(6)
  root.right.right = TreeNode(7)
  
  # driver code
  serialize = Codec()
  deserialize = Codec()

  ans = deserialize.deserialize(serialize.serialize(root))
  
  print(ans)

main()
