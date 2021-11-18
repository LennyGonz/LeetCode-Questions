# Python List Methods

| Methods | Description |
| :------ | :---------- |
| append() | method adds an item to the end of the list |
| extend() | method modifies the original list. It doesn't return any value |
| insert() | method takes 2 parameters - `index` and `element` ... doesn't return anything only updates current list |
| remove() | doesn't return any value (returns `None`) |
| index() | method returns the index of the given element in the list |
| count() | method returns the number of items `element` appears in the list |
| pop() | method removes the item at the given index from the list and returns the removed item |
| reverse() | method doesn't return any value. It updates the existing list |
| sort() | method sorts the elements the elements of a given list |
| copy() | method returns a shallow copy of the list |
| enumerate() | method adds counter to an iterable and returns it |
| filter() | method filters the given iterable with the help of a function that tests each element in the iterable to be `true` or `false` |
| list() | constructor returns a list in Python |
| len() | function returns the number of items (length) in an object |
| max() | function returns the largest item in an iterable. It can also be used to find the largest item between two or more parameters |
| min() | function returns the smallest item in an iterable. It can also be used to find the smallest item between two or more parameters |
| map() | applies a given function to **each** item of an iterable (list, tuple, etc) and returns a **list** of the results |
| slice() | returns a slice object that can be used to slice strings, lists, tuples, etc |
| sum() | adds the items of the given iterable from left to right |
| zip() | The zip function returns an iterator of tuples based on the iterable objects. Suppose, two iterables are passed to `zip()`; one iterable containing three and other containing five elements. Then, the returned iterator will contain three tuples. It's because iterator stops when the shortest iterable is exhausted |

- `append()`

```python
# animals list
animals = ['cat', 'dog', 'rabbit']

# 'guinea pig' is appended to the animals list
animals.append('guinea pig')

# Updated animals list
print('Updated animals list: ', animals)
```

Output: `Updated animals list:  ['cat', 'dog', 'rabbit', 'guinea pig']`

- `extend()`

```python
# language list
language = ['French', 'English']

# another list of language
language1 = ['Spanish', 'Portuguese']

# appending language1 elements to language
language.extend(language1)

print('Language List:', language)
```

Output: `Language List: ['French', 'English', 'Spanish', 'Portuguese']`

- `insert()`

```python
# vowel list
vowel = ['a', 'e', 'i', 'u']

# 'o' is inserted at index 3
# the position of 'o' will be 4th
vowel.insert(3, 'o')

print('Updated List:', vowel)
```

Output: `Updated List: ['a', 'e', 'i', 'o', 'u']`

- `remove()`

```python
# animals list
animals = ['cat', 'dog', 'rabbit', 'guinea pig']

# 'rabbit' is removed
animals.remove('rabbit')

# Updated animals List
print('Updated animals list: ', animals)
```

Output: `Updated animals list:  ['cat', 'dog', 'guinea pig']`

- `index()`

```python
# vowels list
vowels = ['a', 'e', 'i', 'o', 'i', 'u']

# index of 'e' in vowels
index = vowels.index('e')
print('The index of e:', index)

# element 'i' is searched
# index of the first 'i' is returned
index = vowels.index('i')

print('The index of i:', index)
```

Output: `The index of e: 1` & `The index of e: 2`

- `count()`

```python
# vowels list
vowels = ['a', 'e', 'i', 'o', 'i', 'u']

# count element 'i'
count = vowels.count('i')

# print count
print('The count of i is:', count)

# count element 'p'
count = vowels.count('p')

# print count
print('The count of p is:', count)
```

Output: `The count of i is: 2` & `The count of p is: 0`

- `pop()`

```python
# programming languages list
languages = ['Python', 'Java', 'C++', 'French', 'C']

# remove and return the 4th item
return_value = languages.pop(3)
print('Return Value:', return_value)

# Updated List
print('Updated List:', languages)
```

Output: `Return Value: French` & `Updated List: ['Python', 'Java', 'C++', 'C']`

- `reverse()`

```python
# Operating System List
systems = ['Windows', 'macOS', 'Linux']
print('Original List:', systems)

# List Reverse
systems.reverse()

# updated list
print('Updated List:', systems)
```

Output:

```python
Original List: ['Windows', 'macOS', 'Linux']
Updated List: ['Linux', 'macOS', 'Windows']
```

- `sort()`

```python
# vowels list
vowels = ['e', 'a', 'u', 'o', 'i']

# sort the vowels
vowels.sort()

# print vowels
print('Sorted list:', vowels)
```

Output: `Sorted list: ['a', 'e', 'i', 'o', 'u']`

- `copy()`

```python
old_list = [1, 2, 3]
new_list = old_list

# add an element to list
new_list.append('a')

print('New List:', new_list)
print('Old List:', old_list)
```

Output:

```python
Old List: [1, 2, 3, 'a']
New List: [1, 2, 3, 'a']
```

- `enumerate()`

```python
grocery = ['bread', 'milk', 'butter']
enumerateGrocery = enumerate(grocery)

print(type(enumerateGrocery))

# converting to list
print(list(enumerateGrocery))

# changing the default counter
enumerateGrocery = enumerate(grocery, 10)
print(list(enumerateGrocery))
```

Output:

```python
<class 'enumerate'>
[(0, 'bread'), (1, 'milk'), (2, 'butter')]
[(10, 'bread'), (11, 'milk'), (12, 'butter')]
```

- `filter()`

```python
# list of letters
letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

# function that filters vowels
def filterVowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if(letter in vowels):
        return True
    else:
        return False

filteredVowels = filter(filterVowels, letters)

print('The filtered vowels are:')
for vowel in filteredVowels:
    print(vowel)
```

Output:

```python
The filtered vowels are:
a
e
i
o
```

- `list()`

```python
# vowel string
vowel_string = 'aeiou'
print(list(vowel_string))

# vowel tuple
vowel_tuple = ('a', 'e', 'i', 'o', 'u')
print(list(vowel_tuple))
```

Output: `['a', 'e', 'i', 'o', 'u']` & `['a', 'e', 'i', 'o', 'u']`

- `len()`

```python
testList = [1, 2, 3]
print(testList, 'length is', len(testList))

testTuple = (1, 2, 3)
print(testTuple, 'length is', len(testTuple))

testRange = range(1, 10)
print('Length of', testRange, 'is', len(testRange))
```

Output: `[1,2,3] length is 3` & `(1,2,3) length is 3` & `Length of range (1,10) is 9`

- `max()`

```python
languages = ["Python", "C Programming", "Java", "JavaScript"]
largest_string = max(languages);

print("The largest string is:", largest_string)
```

Output: `The largest string is: Python`

- `min()`

```python
number = [3, 2, 8, 5, 10, 6]
smallest_number = min(number);

print("The smallest number is:", smallest_number)
```

Output: `The smallest number is: 2`

- `map()`

```python
def calculateSquare(n):
  return n*n

numbers = (1, 2, 3, 4)
result = map(calculateSquare, numbers)
print(result)

# converting map object to set
numbersSquare = set(result)
print(numbersSquare)
```

Output: `<map object at 0x7f722da129e8>` & `{16, 1, 4, 9}`

- `slice()`

```python
py_list = ['P', 'y', 't', 'h', 'o', 'n']
py_tuple = ('P', 'y', 't', 'h', 'o', 'n')

# contains indices 0, 1 and 2
slice_object = slice(3)
print(py_list[slice_object]) # ['P', 'y', 't']

# contains indices 1 and 3
slice_object = slice(1, 5, 2)
print(py_tuple[slice_object]) # ('y', 'h')  
```

Output: `['P', 'y', 't']` & `('y', 'h')`

- `sum()`

```python
numbers = [2.5, 3, 4, -5]

# start parameter is not provided
numbers_sum = sum(numbers)
print(numbers_sum)

# start = 10
numbers_sum = sum(numbers, 10)
print(numbers_sum)
```

Output: `4.5` and `14.5`

- `zip()`

```python
number_list = [1, 2, 3]
str_list = ['one', 'two', 'three']

# Two iterables are passed
result = zip(number_list, str_list)

# Converting itertor to set
result_set = set(result)
print(result_set)
```

Output: `{(1, 'one'), (2, 'two'), (3, 'three')}`
