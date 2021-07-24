def get_values(node):
  while node:
    yield node.val
    node = node.next


def is_palindrome(node):
  values = get_values(node)
  values_reversed = reversed(list(get_values(node))) # O(N) space

  return all(x == y for x, y in zip(values, values_reversed))
