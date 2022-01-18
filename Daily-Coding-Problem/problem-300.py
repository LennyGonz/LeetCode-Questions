import heapq
import threading
import time

from collections import defaultdict

class VoteReporter:
  def __init__(self, data, k=3, poll_interval=10):
    self.data = data
    self.k = k
    self.poll_interval = poll_interval
    self.voters = {}
    self.tally = defaultdict(int)
    self.frauds = []
    self.stream_done = False
    self.run()

  def run(self):
    t1 = threading.Thread(target=self.read_data)
    t2 = threading.Thread(target=self.get_top_candidates)

    for thread in (t1, t2):
      thread.start()

  def read_data(self):
    for voter, candidate in self.data:
      if voter not in self.voters:
        self.voters[voter] = candidate
        self.tally[candidate] += 1
      else:
        self.report_fraud(voter)

    self.stream_done = True

  def report_fraud(self, voter):
    self.frauds.append(voter)

  def get_top_candidates(self):
    while not self.stream_done:
      time.sleep(self.poll_interval)

      heap = []
      for candidate, votes in self.tally.items():
        heapq.heappush(heap, (-votes, candidate))

      for i in range(1, self.k + 1):
        candidate = heapq.heappop(heap)[1]
        print("#{} candidate:".format(i), candidate)
