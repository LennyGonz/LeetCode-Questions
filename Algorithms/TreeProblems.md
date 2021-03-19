# How to Formulaically Solve Tree Interview Questions

**ex)** Given the root to a binary tree, count the total number of nodes there are

*First Impressions*: If given this question, the first idea that comes to mind is recursively traversing the tree and adding each node to a set
If the node is already in the set don't add it. When finished traversing the entire tree return the length of the set

Solving any binary tree question invovles just **2 steps:**

1. Solving the base case
   > This usually means solving the leaf node case ( a lead node has no left or right children) or the null case
   > For the above problem, we can see that a null should represent 0 nodes while a leaf node should represent 1 node
2. The recursive step
   > Assuming you knew the solution to the left subtree and the right subtree, how could you combine the two results to give you the final solution?
   > It's important to not get caught up on this works and just have faith that it works.
   > If you start tracing the recursion, you're going to needlessly use up time and energy during the interview
   > Intuitively though, it works for similar reasons as why regular induction works
   > P(0) or the base case works which cause P(1) or the leaf node to work which causes P(2) to work and so on
   > For this problem, it's easy to combine the results of the left and right subtrees. Just add the two numbers and then another 1 for the root

```python
def count(node):
  return count(node.left) + count(node.right) + 1 if node else 0
```

You definitely won't get a question this easy but the process is the same for trickier problems

**ex)** Given the root to a binary tree, return the deepest node

Base case - for this question actually can't be null, because it's not a real result that can be combined (null is not a node).
Here we should use the leaf node as the base case and return itself

The recursive step - for this problem is different because we can't actually see the results of the left and right subtrees directly.
So we need to ask, what other information do we need to solve this question?
It turns out if we tagged with each subresult node their depths, we could get the final solution by picking the higher depth leaf and then incrementing it:

```python
def deepest(node):
  if node and not node.left and not node.right:
    return (node, 1) # leaf and its depth
  
  if not node.left:
    return increment_depth(deepest(node.right))
  
  elif not node.right:
    return increment_depth(deepest(node.left))
  
  return increment_depth(max(deepest(node.left), deepest(node.right), key=lambda x: x[1]))

def increment_depth(node_depth_tuple):
  node, depth = node_depth_tuple
  return (node, depth+1)
```
