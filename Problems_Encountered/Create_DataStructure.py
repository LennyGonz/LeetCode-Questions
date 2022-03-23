'''
I was having an intervew at Twitter several months ago and I was asked to develop a data structure that have

add(key, value)

remove(key, value)

getLast()

Looks easy, but we need to make all operations in O(1)

OrderedDict: a dictionary variant that remembers the order the keys were last inserted.
'''
class newDS:
  def __init__(self):
    self.hmap = collections.OrderedDict()

  def get(self, key):
    if key in self.hmap:
      return self.hmap[key]
    return -1

  def add(self, key, val):
    self.hmap[key] = val

  def remove(self, key):        
    if key in self.hmap:
      self.hmap.move_to_end(key)
      self.hmap.popitem()

  def getLast(self):
    if not self.hmap:
      return -1        
    key,val = self.hmap.popitem()
    self.hmap[key] = val
    return val
