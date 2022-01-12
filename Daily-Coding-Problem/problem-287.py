def compute_similarity(a, b, visitors):
  return len(visitors[a] & visitors[b]) / len(visitors[a] | visitors[b])

def top_pairs(log, k):
  visitors = defaultdict(set)
  for site, user in log:
    visitors[site].add(user)

  pairs = []
  sites = list(visitors.keys())

  for _ in range(k):
    heapq.heappush(pairs, (0, ('', '')))

  for i in range(len(sites) - 1):
    for j in range(i + 1, len(sites)):
      score = compute_similarity(sites[i], sites[j], visitors)
      heapq.heappushpop(pairs, (score, (sites[i], sites[j])))

  return [pair[1] for pair in pairs]

'''
For each pair of websites, we must compute the union of its users. 
As a result, this part of our algorithm will take O(N2* M), where N is number of sites and M is the number of users. Inserting into and deletion from the heap is logarithmic in the size of the heap, so if we assume k < M, our heap operations will be dominated by the calculation above.
Therefore, our time complexity will be O(N2* M).

As for space complexity, our hash table will require N2 keys, and our heap will have at most k elements. Assuming k < N2, then, the space required by this program will be O(N2).
'''
