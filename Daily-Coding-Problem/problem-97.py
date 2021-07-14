class TimeMap:
  def __init__(self):
    self.keys = []
    self.values = []

  def get(self, key):
    if self.keys is None:
      return None
    i = bisect.bisect_left(self.keys, key)
    if len(self.keys) == i:
      return self.values[i - 1]
    elif self.keys[i] == key:
      return self.values[i]
    elif i == 0:
      return None
    else:
      return self.values[i - 1]

  def set(self, key, value):
    i = bisect.bisect_left(self.keys, key)
    if len(self.keys) == i:
      self.keys.append(key)
      self.values.append(value)
    elif self.keys[i] == key:
      self.values[i] = value
    else:
      self.keys.insert(i + 1, key)
      self.values.insert(i + 1, value)

class MultiTimeMap:
  def __init__(self):
    self.map = defaultdict(TimeMap)

  def set(self, key, value, time):
    self.map[key].set(time, value)

  def get(self, key, time):
    time_map = self.map.get(key)
    if time_map is None:
      return None
    else:
      return time_map.get(time)
