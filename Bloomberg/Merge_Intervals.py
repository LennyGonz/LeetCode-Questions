'''
LeetCode #56

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and 
return an array of the non-overlapping intervals that cover all the intervals in the input.

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Immediately we want to think of sorting... that way we know which intervals are overlapping

the way I see we have about 4 scenarios

1) interval a and interval b DO NOT overlap
2) some part of interval b - overlaps - with interval a
3) interval a FULLY overlaps interval b
4) interval b fully overlaps interval a, BUT both have the same start time

Now for scenarios 2-4 -> this is how we'd want to merge the intervals
1) if some part of interval b overlaps with interval a
    -> we use interval a's start time and interval b's end time

2) if interval a fully overlaps interval b
    -> we use interval a's start AND end time

3) if interval b fully overlaps interval a
    -> we use interval a's start time and interval b's end time

So based on this approach we'll want to sort the intervals using start time
'''
def merge(intervals):
  # sort the input array based on start time
  intervals.sort(key=lambda x: x[0])
  
  # result list
  merged = []
  
  for interval in intervals:
    
		# if the list of merged intervals is empty 
		# or if the current interval does not overlap with the previous interval, append it.
    if not merged or merged[-1][1] < interval[0]:
      merged.append(interval)
    
    # otherwise, there is overlap, so we merge the current and previous intervals
    else:
      merged[-1][1] = max(merged[-1][1], interval[1])

  return merged

'''
Time: O(NlogN) - the most costly action is sorting (NlogN), other than that we do a linear scan of the input list
Space: O(N) - in the worst case, we're given an input array of no overlapping intervals so our output array holds all the elements

Quick Walk-Through
intervals [[1, 3], [2, 6], [8, 10], [15, 18]]
intervals.sort [[1, 3], [2, 6], [8, 10], [15, 18]]

interval = [1,3]
merged =[]
not merged:
	merged =[ [1,3] ]

interval =[2,6]
merged = [ [1,3] ]
merged[-1][-1] = 3 > interval[0] = 2:
	merged[-1][-1] = max(merged[-1][-1] = 3 ,interval[-1] = 6) =6
merged = [[1,6]]
'''

'''
If intervals is a specific class
'''
class Interval:
  def __init__(self, start, end):
    self.start = start
    self.end = end

def merge(intervals):
  # base case -> if our input list has less than 2 intervals - no need to merge
  if len(intervals) < 2:
    return intervals

  merged = []
  
  # we iterate through the sorted input array (sorted by start time)
  for i in sorted(intervals, key=lambda i: i.start):
    # combine the current interval with the previous one if they overlap
    if merged and i.start <= merged[-1].end:
      merged[-1].end = max(merged[-1].end, i.end)
    
    # otherwise add it to the result array by itself if the current interval does not overlap with any other interval
    else:
      merged += i,

  return out
