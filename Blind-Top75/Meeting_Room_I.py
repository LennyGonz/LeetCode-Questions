'''
LeetCode 252
'''


def canAttendMeetings(intervals):
  intervals.sort(key = lambda i : i[0])

  for i in range(len(intervals) - 1):
    if intervals[i][1] > intervals[i + 1][0]:
      return False
  return True

print(canAttendMeetings([[0,30],[5,10],[15,20]])) # False
print(canAttendMeetings([[7,10],[2,4]])) # True
