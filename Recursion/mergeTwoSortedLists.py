def mergeSortedLists(l1,l2):
  if not l1 or not l2:
    return l1 or l2
  
  elif l1.val < l2.val:
    l1.next = mergeSortedLists(l1.next, l2)
    return l1
  
  else:
    l2.next = mergeSortedLists(l1, l2.next)
    return l2
