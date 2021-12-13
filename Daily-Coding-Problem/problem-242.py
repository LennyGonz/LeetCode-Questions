class BIT:
  def __init__(self, nums: int):
    self.tree = [0 for _ in range(len(nums) + 1)]
    for i, num in enumerate(nums):
      self.update(i + 1, num)

  def update(self, index: int, value: int):
    while index < len(self.tree):
      self.tree[index] += value
      index += index & -index

  def query(self, index: int):
    total = 0
    while index > 0:
      total += self.tree[index]
      index -= index & -index
    return total

class Subscribers:
  def __init__(self, nums: int):
    self.bit = BIT(nums)
    self.nums = nums

  def update(self, hour: int, value: int):
    self.bit.update(hour, value - self.nums[hour])
    self.nums[hour] = value

  def query(self, start: int, end: int):
    return self.bit.query(end + 1) - self.bit.query(start)
