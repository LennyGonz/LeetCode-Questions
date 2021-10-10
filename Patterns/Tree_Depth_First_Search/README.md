# Tree Traversal Techniques

Tree Traversal: Also known as tree search and walking the tree, refers to the process of isiting (checking/updating) each node in a tree data structure, exactly once. Such traversals are classified by the order in which the nodes are visited

## Depth-First Search (DFS)

1. Pre-Order (NLR)
2. In-Order (LNR)
3. Post-Order (LRN)

*Node, Left Child, Right Child*

These searches are referred to as depth-first search, since the search tree is deepend as much as possible on each child before going to the next sibling

> Post Order Traversal

```python
visited = set()

def dfs(visited, graph, node):
  if node not in visited:
    print(node)
    visited.add(node)
    for neighbour in graph[node]:
      dfs(visited, graph, neighbour)
```

Notice that after adding the root node, we begin to traverse the tree by focusing on the left child. Once there are no more left children, we absolve all the recursive calls till we reach a point where we can visit the right child of a node.

3 Types of Depth First Search

### PreOrder Traversal

```python
def preOrder(root):
  stack = [root]
  path = []

  curr = root

  while stack:
    if curr:
      path.append(curr.val)

      if curr.right():
        stack.append(curr.right)

      curr = curr.left

    else:
      curr = stack.pop()
  
  return path
```

### InOrder Traversal

```python
def inOrder(root):
  stack = []
  path = []

  curr = root

  while stack or curr:
    if curr:
      stack.append(curr)
      curr = curr.left
    else:
      curr = stack.pop()
      path.append(curr.data)
      curr = curr.right
  
  return path
```

### PostOrder Traversal

```python
def postOrder(root):
  stack = [root]
  output = []

  while stack:
    curr = stack.pop()
    output.append(curr.val)

    if curr.left:
      stack.append(curr.left)
    
    if curr.right:
      stack.append(curr.right)
  
  return [elem for elem in reversed(output)]
```

DFS is a good searching algorithm to know when dealing with Tree problems, for example:

Binary Tree Path Sum:
Given a binary tree and a number ‘S’, find if the tree has a path from root-to-leaf such that the sum of all the node values of that path equals ‘S’.

> The objective is to find out whether the binary tree contains a path that the value of the nodes add up to the target
> We clearly need to traverse all paths from root to leaf, and the best way to do that is by using DFS with some extra conditions
> So on the way from root to leaf, we subtract the node value from the target, and when we finally reach a leaf we do a check
> if leaf value == target and if the leaf is a leaf, then we can return true, bc there's a path in the tree that when added equals the target

All Paths for a Sum:
Given a binary tree and a number ‘S’, find all paths from root-to-leaf such that the sum of all the node values of each path equals ‘S’.
> The objective is to return a list with all the paths from root-to-leaf s.t the sum of all the node vlaues of each path equals the target
> So similar to the previous problem except instead of returning a boolean, we return a list of lists
> This still requires DFS, but with more conditions and more variables
>
> I thought it best to keep 2 lists, currentPath and result
> With currentPath, this list collects all the nodes from root to leaf, when we reach a leaf we do the same condition: if leaf value == target and if the leaf is a leaf, then we can append this path to our result list
> Now since we're at a leaf node we need to pop the leaf from our list and backtrack to the parent and visit the right subtree
> So we're basically doing a preorder traversal of our tree, and when we hit our condition we simply add the currentPath to our result

All Paths:
Given a binary tree, return all root-to-leaf paths
> Basically the same question as All Paths for a Sum, but without the restriction of the path having to equal the sum
> So our strategy stays the same, but the condition needs to be altered so that we don't check for the leaf==target 

Path with Maximum Sum:
Given a binary tree, find the root-to-leaf path with the maximum sum.
> This is similar to All Paths for a Sum, but instead of having a result list, we keep track of a maximum sum
> So we traverse the tree using DFS and whenever we reach a leaf we simply enter an if statement and update our maximum variable

Sum of Paths:
Given a binary tree where each node can only have a digit (0-9) value, each root-to-leaf path will represent a number. Find the total sum of all the numbers represented by all paths.
> There are multiple objectives with this question, first we have to construct the number created when traversing each path and then adding the numbers together and returning the summation.
> But it's important to recognize that the problem requires us to explore all paths, therefore we need to use DFS and incoporate the necessary logic to achieve each of our objectives

## Breadth-First Search (BFS)

Trees can also be travered in level-order, where we visit every node on a level before going to a lower lovel.

This search is referred to as BFS, as the search tree is broadened as mich as possible on each depth before going to the next depth
