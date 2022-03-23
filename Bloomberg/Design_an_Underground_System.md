# Design an Underground System
*Leetcode #1396*

<hr>

An underground railway system is keeping track of customer travel times between different stations.

They are using this data to calculate the average time it takes to travel from one station to another.

Implement the UndergroundSystem class:

- `void checkIn(int id, string stationName, int t)`
  - A customer with a card ID equal to id, checks in at the station stationName at time t.
  - A customer can only be checked into one place at a time.

- `void checkOut(int id, string stationName, int t)`
  - A customer with a card ID equal to id, checks out from the station stationName at time t.

- `double getAverageTime(string startStation, string endStation)`
  - Returns the average time it takes to travel from startStation to endStation.
  - The average time is computed from all the previous traveling times from startStation to endStation that happened directly, meaning a check in at startStation followed by a check out from endStation.
  - The time it takes to travel from startStation to endStation may be different from the time it takes to travel from endStation to startStation.
  - There will be at least one customer that has traveled from startStation to endStation before getAverageTime is called.

You may assume all calls to the `checkIn` and `checkOut` methods are consistent.
If a customer checks in at time t1 then checks out at time t2, then t1 < t2.
All events happen in chronological order.

<hr>

**Solution**:

* We have several persons, defined by id, which 
  - check-in at some station at some time and then 
  - check-out from some other station at some other time.

We need to calculate times this person spent to go from one station to another **and then** 
  calculate average time for all persons. Let us keep 3 pieces of information:

- `self.ids` is dictionary, where for each person(id) we will keep pair (station, time)
  - if the last action this person did is **check-in** and
  - **empty** if it was check out
- `self.pairs` is a counter, where for each pair of stations we keep total time spend between two stations.
- `self.freqs` is a counter, where for each pair of stations we keep how many trips we have between these two stations.

`self.pairs` and `self.freqs` will help us calculate the average time it takes to travel from station1 to station2

Now, let us discuss, what our functions will do:

1. `checkIn(self, id, stationName, t)`: we just put pair (stationName, t) into self.ids[id].

2. `checkOut(self, id, stationName, t)`: Here we look at person id, extract information about his last station visited (pop it from self.ids[id] and update self.pairs, self.freqs for these pairs of stations.
3. `getAverageTime(self, startStation, endStation)`: here we just look at dictionaries self.pairs and self.freqs and directly return result.

**Complexity**: 

**Time compexlty**: is O(1) for all 3 operations
**Space complexity**: potentially is O(N), where N is total number of queries.

<hr>

```py
# A Counter is a dict subclass for counting hashable objects.
# It is a collection where elements are stored as dictionary keys and
# their counts are stored as dictionary values
# counters are just frequency maps
from collections import Counter

class UndergroundSystem:
  def __init__(self):
    self.ids = {}
    self.pairs = Counter()
    self.freqs = Counter()

  def checkIn(self, id, stationName, t):
    self.ids[id] = (stationName, t)

  def checkOut(self, id, stationName, t):
    # we update the information of the traveler that checked out
    Name2, t2 = self.ids.pop(id)

    # we record where that traveler started, ended AND time spent between both stations
    self.pairs[(Name2, stationName)] += t-t2
    self.freqs[(Name2, stationName)] += 1

  def getAverageTime(self, startStation, endStation):
    return self.pairs[startStation, endStation]/self.freqs[startStation, endStation]
```

Example Testcase:
```
Input
["UndergroundSystem","checkIn","checkIn","checkIn","checkOut","checkOut","checkOut","getAverageTime","getAverageTime","checkIn","getAverageTime","checkOut","getAverageTime"]

[[],[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22],["Paradise","Cambridge"],["Leyton","Waterloo"],[10,"Leyton",24],["Leyton","Waterloo"],[10,"Waterloo",38],["Leyton","Waterloo"]]

Output
[null,null,null,null,null,null,null,14.00000,11.00000,null,11.00000,null,12.00000]

Explanation
UndergroundSystem undergroundSystem = new UndergroundSystem();
undergroundSystem.checkIn(45, "Leyton", 3);
undergroundSystem.checkIn(32, "Paradise", 8);
undergroundSystem.checkIn(27, "Leyton", 10);

self.ids will look like:
{45: ('Leyton', 3)}
{45: ('Leyton', 3), 32: ('Paradise', 8)}
{45: ('Leyton', 3), 32: ('Paradise', 8), 27: ('Leyton', 10)}



undergroundSystem.checkOut(45, "Waterloo", 15);  // Customer 45 "Leyton" -> "Waterloo" in 15-3 = 12

self.ids:  {32: ('Paradise', 8), 27: ('Leyton', 10)} // 2 customers left on the train
self.pairs:  Counter({('Leyton', 'Waterloo'): 12})
self.freqs:  Counter({('Leyton', 'Waterloo'): 1})

undergroundSystem.checkOut(27, "Waterloo", 20);  // Customer 27 "Leyton" -> "Waterloo" in 20-10 = 10

self.ids:  {32: ('Paradise', 8)} // 1 customer left on the train
self.pairs:  Counter({('Leyton', 'Waterloo'): 22}) // Customer 27 "Leyton" -> "Waterloo" in 20-10 = 10
self.freqs:  Counter({('Leyton', 'Waterloo'): 2}) // there have been 2 trips from Leyton -> Waterloo

undergroundSystem.checkOut(32, "Cambridge", 22); // Customer 32 "Paradise" -> "Cambridge" in 22-8 = 14

self.ids:  {}
self.pairs:  Counter({('Leyton', 'Waterloo'): 22, ('Paradise', 'Cambridge'): 14})
self.freqs:  Counter({('Leyton', 'Waterloo'): 2, ('Paradise', 'Cambridge'): 1})

undergroundSystem.getAverageTime("Paradise", "Cambridge"); // return 14.00000. One trip "Paradise" -> "Cambridge", (14) / 1 = 14
undergroundSystem.getAverageTime("Leyton", "Waterloo");    // return 11.00000. Two trips "Leyton" -> "Waterloo", (10 + 12) / 2 = 11
undergroundSystem.checkIn(10, "Leyton", 24);

self.ids will look like:
{10: ('Leyton', 24)}

undergroundSystem.getAverageTime("Leyton", "Waterloo");    // return 11.00000
undergroundSystem.checkOut(10, "Waterloo", 38);  // Customer 10 "Leyton" -> "Waterloo" in 38-24 = 14

self.ids:  {}
self.pairs:  Counter({('Leyton', 'Waterloo'): 36, ('Paradise', 'Cambridge'): 14})
self.freqs:  Counter({('Leyton', 'Waterloo'): 3, ('Paradise', 'Cambridge'): 1})


undergroundSystem.getAverageTime("Leyton", "Waterloo");    // return 12.00000. Three trips "Leyton" -> "Waterloo", (10 + 12 + 14) / 3 = 12
```
