'''
Validate A Binary search tree

Time: O(n)
Space: O(n)
-------------------------------

Let's start with a simple definition of the nodes of a binary search tree!
A parent node is greater than its left child but smaller than its right.

    2
   / \
  1   3 // valid tree!

    5
   / \
  1   4  // not valid here!
     / \
    3   6

One solution would be to check every parent as we work down the tree but it creates a lot 
of complicated logic. So why don't we check every child on the way up! All we have to do 
is keep track of the mininum and maximum valid values on the way down.

To prevent some extra checks let's start with -infinity and infinity.

def isValidBST(self, root):
    return check_bst(root, float("-inf"), float("inf"))

    2 
   / \
  1   3 
	
1 // -inf < 1 < 2, so it's still valid
3 //  2 < 3 < inf, so it's still a valid tree
2 // -inf < 2 < inf, so it's a valid tree!

And what about an invalid tree?

    5 
   / \
  1   4 
	
1 // -inf < 1 < 5, so it's still a valid tree
4 // 5 > 4 < inf, this tree is not a valid binary tree!	

So here's one way we could implement this logic!
'''
def isValidBST(self, root):
    return check_bst(root, float("-inf"), float("inf"))
	
def check_bst(self, node, left, right):
    if not node:
        return True

    if not left < node.val < right:
        return False

    return (check_bst(node.left, left, node.val)
            and check_bst(node.right, node.val, right))
