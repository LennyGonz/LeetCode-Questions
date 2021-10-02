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
'''


## Breadth-First Search (BFS)

Trees can also be travered in level-order, where we visit every node on a level before going to a lower lovel.

This search is referred to as BFS, as the search tree is broadened as mich as possible on each depth before going to the next depth
