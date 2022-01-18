from itertools import combinations

def satisfies(option, preferences):
  return all(set(c).intersection(option) for c in preferences.values())

def make_drinks(preferences):
  customers = preferences.keys()
  drinks = set([x for y in preferences.values() for x in y])

  for i in range(1, len(customers) + 1):
    options = combinations(drinks, i)
    for option in options:
      if satisfies(option, preferences):
        return i

'''
Checking each option will take O(N2) time in the worst case, as we must check whether there is a matching element in our candidate solution for each set of preferences.

And since there are 2N ways of forming combinations from a set, the overall time complexity will be O(N2 * 2N).
'''
