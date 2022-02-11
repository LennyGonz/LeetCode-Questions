class Elo:
  def __init__(self, k=32, n=400, d=1000):
    self.ratings = {}
    self.k = k 
    self.n = n
    self.default = d

  def add_player(self, name):
    self.ratings[name] = self.default

  def expected(self, r1, r2):
    return 1 / (1 + 10 ** ((r2 - r1) / self.n))

  def update(self, p1, p2, outcome):
    e1 = self.expected(self.ratings[p1], self.ratings[p2])
    e2 = self.expected(self.ratings[p2], self.ratings[p1])

    o1, o2 = 1 - outcome, outcome

    self.ratings[p1] += self.k * (o1 - e1)
    self.ratings[p2] += self.k * (o2 - e2)
