class DisjointSet:
  def __init__(self, n):
    self.sets = list(range(n))
    self.sizes = [1] * n
    self.count = n

  def union(self, x, y):
    x, y = self.find(x), self.find(y)
    if x != y:
      if self.sizes[x] < self.sizes[y]: # union by size
        x, y = y, x
      self.sets[y] = x
      self.sizes[x] += self.sizes[y] 
      self.count -= 1

  def find(self, x):
    group = self.sets[x]

    while group != self.sets[group]:
      group = self.sets[group]
    self.sets[x] = group # path compression

    return group

def friend_groups(students):
  groups = DisjointSet(len(students))

  for student, friends in students.items():
    for friend in friends:
      groups.union(student, friend)

  return groups.count
