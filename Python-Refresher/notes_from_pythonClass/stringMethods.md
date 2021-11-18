# String Methods

| Methods | Description |
| :------ | :--------- |
| capitalize() | return a copy of the string with only its first character capitalized |
| center() | pads string with specified character |
| count(sub) | return the number of occurrences of substring `sub` in string S |
| endswith() | checks if string ends with the specified suffix |
| format() | formats the specified value(s) and insert them inside the string's placeholder. The placeholder is defined using curly brackets: `{}` |
| join() | returns a concatenated string with the elements of an iterable |
| slice() | returns a slice object that can be used to slice strings, lists, tuple, etc|
| strip([chars]) | return a copy of the string with the leading and trailing characters removed - `[chars]` specifies which `char` you want to remove |
| split() | splits the string at the specified `char`, returns a list |

## Examples

- `capitalize()`

```python
txt = "hello, and welcome to my world."

x = txt.capitalize()

print (x)
```

output: `"Hello, and welcome to my world."`

- `center()`

```python
txt = "banana"

x = txt.center(20)

print(x)
```

output: `"       banana"`

- `count()`

```python
txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple")

print(x)
```

Output: `2` because there are 2 instances of the string `apple` in the variable `txt`

- `endswith()`

```python
txt = "Hello, welcome to my world."

x = txt.endswith(".")

print(x)
```

Output: `True` Because the string stored in `txt` does end with a "."

- `format()`

```python
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))
```

Output: `"For only 49.00 dollars!"`

- `join()`

```python
myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)
```

Output: `"John#Peter#Vicky"` - in this example I joined the elements with a hash character, but I could've joined them with any character I want.

- `slice()`

`slice(start, stop, step)`
**start(optional)** - Starting integer where the slicing of the object starts. Defaults to none
**stop** - integer until which the slicing takes place
**step(optional)** - integer value which determines the increment between each index for slicing. Defaults to none if not specified

```python
# contains indices (0, 1, 2)
result1 = slice(3)
print(result1)

# contains indices (1, 3)
result2 = slice(1, 5, 2)
print(slice(1, 5, 2))

py_string = 'Python'

# contains indices 0, 1 and 2
print(py_string[0:3])  # Pyt
```

Output:

```python
slice(None, 3, None)
slice(1, 5, 2)
```

- `strip()`

```python
txt = "     banana     "

x = txt.strip()

print("of all fruits", x, "is my favorite")
```

Output: `"of all fruits banana is my favorite"`

- `split()`

```python
txt = "welcome+to+the+jungle"

x = txt.split('+')

print(x)

txt2 = "welcome to the jungle"

y = txt2.split() # this would output the same result
```

Output: `['welcome', 'to', 'the', 'jungle']`
