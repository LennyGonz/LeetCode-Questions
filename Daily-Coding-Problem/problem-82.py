class Reader:
  def __init__(self):
    self.remainder = ''

  def readN(self, n):
    result = self.remainder
    text = None

    while len(result) < n and (text is None or len(text) >= 5):
      text = read7()
      result += text

    self.remainder = result[n:]

    return result[:n]
