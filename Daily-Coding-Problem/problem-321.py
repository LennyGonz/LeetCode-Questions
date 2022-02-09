def steps(n):
  distance = [i - 1 for i in range(n + 1)]

  for i in range(1, n + 1):
    for j in range(int(i ** 0.5), 1, -1):
      if i % j == 0:
        distance[i] = min(distance[i], distance[i // j] + 1)
    distance[i] = min(distance[i], distance[i - 1] + 1)

  return distance[-1]

'''
The time complexity of this algorithm is worse, but mercifully simpler to calculate.
Our outer loop iterates through values 1 to N, while our inner loop goes up to the square root of the element being looked at.
Therefore, this algorithm will run in O(N^(3/2)) time and O(N) space.
'''
