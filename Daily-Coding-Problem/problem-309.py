def move(seats):
  people = [i for i, x in enumerate(seats) if x == 1]
  n = len(people)
  median = people[n // 2]
  cost = 0

  # Move left seats closer to median.
  i = median - 1; j = n // 2 - 1
  while i >= 0 and j >= 0:
    if seats[i] == 0:
      cost += abs(people[j] - i)
      seats[i], seats[people[j]] = seats[people[j]], seats[i]
      j -= 1 
    i -= 1

  # Move right seats closer to median.
  i = median + 1; j = n // 2 + 1
  while i < len(seats) and j < n:
    if seats[i] == 0:
      cost += abs(people[j] - i)
      seats[i], seats[people[j]] = seats[people[j]], seats[i]
      j += 1
    i += 1

  return seats, cost

'''
This algorithm requires two passes over the input: one from the median to the left end, and one from the median to the right end.

Since in each pass we only perform constant-time operations, the time complexity will be O(N).

The space required will also be O(N), since we are using a helper array to store the occupied positions.
'''
