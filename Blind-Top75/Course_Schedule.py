'''
# LeetCode: 207 - Course Schedule

Clarification:

Some courses have pre-reqs: [[0,1]] -> There are a total of 2 courses -> But to take course 0, you need to have taken course 1
So if you want to take course 0, you need course 1 - 1 -> 0 - [0,1] is an edge

We could also have a cycle -> prereq = [[1,0],[0,1]] 
-> to take course 1, we need to have completed course 0
-> to take course 0, we need to have completed course 1
- This is a cycle

* so to take this problem, we implement DFS

ex) n = 5 - prereq: [[0,1],[0,2],[1,3],[1,4],[3,4]]

1) course0 has 2 prereqs: c1 and c2
- c2 has NO prereqs
- c1 has 2 prereqs

2) course1 has 2 prereqs: c3 and c4
- c4 has NO prereqs
- c3 has 1 prereq

3) c3 has 1 prereq: c4
- c4 has NO prereq

We can return True -> b/c we're allowed to take max of 5 courses and to complete all the courses we only need to take 4 courses

STRATEGY BEGINS HERE:

We USE an adjancency list to track the courses and their prereqs:

course | prereq
  0         [1,2]
  1         [3,4]
  2         []
  3         [4]
  4         []

* After we construct our adjacency list - we're going to run DFS on every single node
* We run DFS in the order of 0 to n-1
  -> so we start a course0 (node 0) -> DFS -> we see that it has 2 prereqs, so we run DFS on the first neighbor: course 1
    * we're at course1 -> DFS -> we see course1 has 2 neighbors, so we run DFS on the first neighbor: 3
      -> we're at course3 -> DFS -> we see course3 has 1 neighbor, so we run DFS on the first neighbor: 4
        * we're at course 4 -> no neighbors - so course 4 can be completed, which we can say b/c course 4 has NO neighbors == NO prereqs

We repeat this process till we've gone through all neighbors, OR
We've detected a cycle

* To detect a cycle, we MUST use a set
'''
def canFinish(numCourses, prerequisites):
  # we create the adjacency list -> key = course & value: list of prereqs for the respective course
  preMap = { i : [] for i in range(numCourses) }
  
  # we need to iterate through the 2D array (prereq) to populate the adjacency list
  for course, prereq in prerequisites:
    preMap[course].append(prereq)
  
  # we use this set to STORE all the courses along the DFS path we're on
  visitSet = set()
  
  # making dfs a nested function is easier for using global variables
  def dfs(crs):
    # if the current course we're on has ALREADY been visited, we can immediately return false
    if crs in visitSet:
      return False
    
    # our other base case - if the prereq of this course is an empty list
    # It means the current course has no prereq, and we can return True
    if preMap[crs] == []:
      return True
    
    # if neither conditions is satisfied - we can take this course and add it to the visitSet
    # b/c we're currently visiting it AND we're going to recursively run DFS on crs neighbors
    visitSet.add(crs)
    
    # we loop thru crs' prereqs and for each prereq run DFS on it
    for pre in preMap[crs]:
      # if dfs(pre) returns False -> it means that we found 1 course that couldn't be completed
      if not dfs(pre):
        return False
    
    # if the inner-if does not execute we have a course that can be taken
    # BUT we  need to remove this crs - AND since we know this course can be taken/visited
    # we can set it equal to an empty list
    visitSet.remove(crs)
    # we only do line 90 - IF we've visited each one of the current courses' prereq
    # And if we arrive at this line, it's okay to clear the prereqs
    preMap[crs] = [] # -> if we ever have to run dfs on this crs again, we save time and erase its former prereqs and we hit the base case
    
    return True
  
  # we want to call dfs on every single course
  # in the number of courses that we have
  # we loop this way in case we're given a disconnected graph
  for crs in range(numCourses):
    # if any of the courses return FALSE
    # we return FALSE immediately
    if not dfs(crs):
      return False

  # otherwise we can return True
  return True

# we look like this b/c our graph may not be fully connected
# 1 -> 2
# 3 -> 4
# so we have to manually iterate through every course and check:
# can 1 be completed?
# can 2 be completed?
# ...
# can 4 be completed?

def main():
  numCourses = 5
  prerequisites = [[0,1],[0,2],[1,3],[1,4],[3,4]]
  print(canFinish(numCourses, prerequisites))

main()

'''
Time: O(N) - N nodes in the tree that we visit
Space: O(N+M) - We use an adjancency list to store N courses and M prequeisites for those courses
'''
