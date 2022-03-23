# Design an Ordered Stream

*LeetCode 1656*

There is a stream of `n` `(idKey, value)` pairs arriving in an arbitrary order, where `idKey` is an integer between 1 and `n` and value is a string.
No two pairs have the same id.

Design a stream that returns the values in increasing order of their IDs by returning a chunk (list) of values after each insertion.

The concatenation of all the chunks should result in a list of the sorted values.

Implement the OrderedStream class:

* `OrderedStream(int n)` - Constructs the stream to take n values.
* `String[] insert(int idKey, String value)` - Inserts the pair (idKey, value) into the stream, then returns the largest possible chunk of currently inserted values that appear next in the order.

*Example:*

*Input*: ["OrderedStream", "insert", "insert", "insert", "insert", "insert"]
         [[5], [3, "ccccc"], [1, "aaaaa"], [2, "bbbbb"], [5, "eeeee"], [4, "ddddd"]]

*Output*:
[null, [], ["aaaaa"], ["bbbbb", "ccccc"], [], ["ddddd", "eeeee"]]

**Explanation**:
// Note that the values ordered by ID is ["aaaaa", "bbbbb", "ccccc", "ddddd", "eeeee"].
OrderedStream os = new OrderedStream(5);
os.insert(3, "ccccc"); // Inserts (3, "ccccc"), returns [].
os.insert(1, "aaaaa"); // Inserts (1, "aaaaa"), returns ["aaaaa"].
os.insert(2, "bbbbb"); // Inserts (2, "bbbbb"), returns ["bbbbb", "ccccc"].
os.insert(5, "eeeee"); // Inserts (5, "eeeee"), returns [].
os.insert(4, "ddddd"); // Inserts (4, "ddddd"), returns ["ddddd", "eeeee"].
// Concatentating all the chunks returned:
// [] + ["aaaaa"] + ["bbbbb", "ccccc"] + [] + ["ddddd", "eeeee"] = ["aaaaa", "bbbbb", "ccccc", "ddddd", "eeeee"]
// The resulting order is the same as the order above.

**Further Explanation**:

Basically , we need to store every incoming value at the given index.
The idea is that you need to return a longest list that start at index of ptr. if ptr is not pointing an element, you need to return a empty list.

  * If the current index is less than the incoming index, the we have to return an empty list
  * Else , we have to return a sliced list from the incoming index to the first index where there is no insertion till yet.

Solution:

* Initialize a list of size n with None
* Maintain the current index with self.ptr
* For every insert call, with idKey, value
  - Assign the list[idKey-1] to the value # Since array is 0-index reduce 1
  - Check if the current index is less than incoming index(idKey-1) and return []
  - Else return sliced list from incoming index(idKey-1) till we do not encounter None.

```py
class OrderedStream:
  def __init__(self, n):
    # we initialize the list with size n
    self.stream = [None]*n

    # we'll use this pointer to maintain the current undex
    self.ptr = 0

  def insert(self, idKey, value):
    # adjust for the 0-based index
    idKey -= 1

    # insert the value for the corresponding index
    self.stream[idKey] = value

    # if the current index is LESS THAN the incoming index
    # we want to return an empty list
    if self.ptr < idKey:
      return []
    
    # otherwise, we'll return a list from the incoming index till 
    # an id that has a value of None (exclusive)
    else:
      while self.ptr < len(self.stream) and self.stream[self.ptr] is not None:
        self.ptr += 1
      return self.stream[idKey:self.ptr]
```

<hr>

```js
class OrderedStream {
  // Define a construction function and set some values as object properties to keep our data persistent between invocations
  constructor(n) {
    this.pointer = 0
    // this will create an array of length (n) and set all values to 'undefined'
    this.list = []
  }

  insert(id, value) {
    // will be used to store values that pass the condition and to be returned
    let chunk = []
    // since array indices start from zero and id in this problem from 1 we need to decrement it
    this.list[id - 1] = value
    // every time we insert a value we have to look if there is a value at the index (pointer) that should be returned
    // if there is any we copy it and then iterate to the next element until the condition is no longer true
    while(this.list[this.pointer]) {
      chunk.push(this.list[this.pointer])
      this.pointer++
    }
    return chunk
  }
}
```
