'''
LeetCode 252

Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: true

-------------------------------------------------------------------------------------------------------------------------------

A person cannot attend a meeting, if they are currently in a meeting
So what we can do is sort the input array by start time
With this sorted array
  - if the start time of the second interval is BEFORE the end time of the first interval
    - they overlap and we return False
  
  - if they don't overlap -> we continue to the next interval
    - we repeat the entire process until we reach the 2nd to last interval
      - because the last comparison we can do is the 2nd to last meeting WITH the last meeting
'''


def canAttendMeetings(intervals):
  # sort the intervals by start time
  intervals.sort(key = lambda i : i[0])

  # iterate through the sorted intervals
  for i in range(len(intervals) - 1):
    # if a meeting ends AFTER
    # the next meeting begins -> return False
    if intervals[i][1] > intervals[i + 1][0]:
      return False
  
  # if we iterate through all the intervals and there are no overlapping meetings
  # then we return True - bc a person can attend all the meetings
  return True

'''
Time: O(nlogn) - because we sort the input array
Space: O(1) - algorithm runs in constant space
'''

print(canAttendMeetings([[0,30],[5,10],[15,20]])) # False
print(canAttendMeetings([[7,10],[2,4]])) # True
