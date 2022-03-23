'''
Leetcode #253

Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

---------------------------------------------------------------------------------------------
Clarifying questions to ask:

- ex [(0,30),(5,10),(10,15)] -> do (5,10) and (10,15) overlap ? Bc they end and finish at the same time...

* Meeting Rooms I -> asks if a person can attend all meetings in the given array

Here we have to find the MINIMUM number of conference rooms

Since question asks for the minimum number of conference rooms, we can look at this from a different perspective:
  such as: What's the maximum number of overlapping meetings in the given time intervals?
  
With this new perspective what we can do is:

1) split the times into 2 lists:
  - start
  - end

2) we sort these lists

3) We use 2 pointers
  - pointer1 will be at the beginning of start
  - pointer 2 will be at the beginning of end

4) Between the 2 pointers, we're always going to pick the minimum value
  - if the minimum between the 2 is "start time"
    - we're going to increment our count variable (which is ultimately the minimum number of conference rooms needs)
    - AND we move the pointer1 up by 1

5) We could reach a point where the start array is empty -> so we stop and return the count

ex) [(0,30),(5,10),(10,15)]
start = [0,5,10]
end = [10,15,30]
count = 0

1) 0 < 10 -> we increase count to 1 and move up in the start array
2) 5 < 10 -> we increase count to 2 and move up in the start array
3) 10 !< 10 -> this is an edge case (a meeting is ending and starting)
  - In this scenario that this happens we visit the end time FIRST
    - so this action says, a meeting has to end before another meeting can start
  - So we shift our end pointer up by 1
  - AND decrement out count by 1 -> count = 1
4) 10 < 15 -> we increase count to 2
'''

def minMeetingRooms(intervals):
  # if there are no meetings - we don't need any rooms:
  if not intervals:
    return 0
  
  # separate the start and end timings
  # then sort them
  start = sorted(i[0] for i in intervals)
  end = sorted(i[1] for i in intervals)
  
  # holds the maximum number of overlapping meetings needed
  res = 0
  
  # pointers for the arrays
  startPointer, endPointer = 0,0
  
  # temp variable that will help determine the minimum number of rooms
  count = 0
  
  while startPointer < len(intervals):
    # if we have an overlapping meeting
    # we must increase the count -> move startPointer up
    if start[startPointer] < end[endPointer]:
      count += 1
      startPointer += 1
    
    # if a meeting is ending and starting at the same time
    # we reduce the count of rooms
    # and we increase the pointer position in the end list
    else:
      count -=1
      endPointer += 1
    
    # We take the max number of overlapping meetings through the entire interval of meetings
    res = max(res, count)
  
  return res

'''
Time: O(NlogN) - because all we are doing is sorting the two arrays for start timings and end timings individually, and then iterating through each list:O(N)
Space: O(N) - because we create two separate arrays of size N, one for recording the start times and one for the end times.
'''

def main():
  intervals = [[0,30],[5,10],[15,20]]
  print(minMeetingRooms(intervals)) # 2

  intervals = [[7,10],[2,4]]
  print(minMeetingRooms(intervals)) # 1

main()
