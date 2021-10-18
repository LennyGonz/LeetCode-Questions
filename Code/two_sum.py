def twoSum(numarr, target):
  processedInts = {}

  for index, value in enumerate(numarr):
    if target - value in processedInts:
      return [processedInts[target-value], index]
    else:
      processedInts[value] = index
    
  return 0

ex1 = [2, 7, 11, 15]
print(twoSum(ex1, 26))


def formatSongs(songDuration):
  songs = []
  for i in range(len(songDuration)):
    songs.append([songDuration[i], i])
  return songs



def findSongs(rideDuration, songDurations):
  # Write your code here
  rideDuration -= 30
  map = {}
  maximum = -1
  ans = [-1, -1]
  
  for i in range(len(songDurations)):
    if songDurations[i] not in map:
      map[rideDuration - songDurations[i]] = i
    else:
      if songDurations[i] > maximum or rideDuration - songDurations[i] > maximum:
        ans[0] = map[songDurations[i]]
        ans[1] = i
        maximum = max(songDurations[i], rideDuration-songDurations[i])
  
  if ans != [-1, -1]:
    return ans
  else:
    return [-1, -1]
