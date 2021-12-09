def canFinish(numCourses, prerequisites):
  preMap = { i : [] for i in range(numCourses) }
  
  for course, prereq in prerequisites:
    preMap[course].append(prereq)


  visitSet = set()
  
  def dfs(crs):
    if crs in visitSet:
      return False
    
    if preMap[crs] == []:
      return True
    
    visitSet.add(crs)
    
    for pre in preMap[crs]:
      if not dfs(pre):
        return False
    
    visitSet.remove(crs)
    preMap[crs] = []
    
    return True
  
  for crs in range(numCourses):
    if not dfs(crs):
      return False
  
  return True

def main():
  numCourses = 5
  prerequisites = [[0,1],[0,2],[1,3],[1,4],[3,4]]
  print(canFinish(numCourses, prerequisites))

main()

