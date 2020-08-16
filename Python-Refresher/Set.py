'''
a Set object is a unordered collection of DISTINCT objects

Uses include:
* removing duplicates from a sequence
* computing mathematical operations such as:
    * intersection
    * union
    * difference
    * symmetric difference

set supports:
* x in set
* len(set)
* for x in set

Since sets are unordered collections, Sets DO NOT record 
element position or order of insertion

Sets DO NOT support:
* indexing
* slicing
* Or other sequence-like behavior

Sets are mutable -- contents can be changed using the following methods:
* add()
* remove()

len(s) = returns the cardinality of set s
x in s = Text x for membership in s
x not in s = Text x for non-membership in s

add(elem)     = Add element 'elem' to the set
remove(elem)  = Remove element 'elem' from the set
discard(elem) = Remove element 'elem' from the set IF it is present
pop()         = Remove and return an arbitrary element from the set
clear()       = Remove all elements from the set

'''

'''
Problem:

Return the longest substring with no repeating characters

example input: "abcdbef"
correct output: "cdbef" --> length is 5 so we return 5
'''
def substring(inputString):
    nonrepeating_substring = set()
    set_size = 0
    for letter in inputString:
        if letter not in nonrepeating_substring:
            nonrepeating_substring.add(letter)
        if letter in nonrepeating_substring:
            break
        if len(nonrepeating_substring) < set_size:
            nonrepeating_substring.clear()
    for word in nonrepeating_substring:
        print(word)
    return nonrepeating_substring

substring('abcdbef')