def letterCombination(digit):
  mapping = {'2': 'abc', '3': 'def', '4':'ghi', '5':'jkl', '6':'mno', '7': 'pqrs', '8':'tuv', '9': 'wxyz'}

  if len(digit) == 0:
    return []

  elif len(digit) == 1:
    return list(mapping[digit])

  prev = letterCombination(digit[:-1])

  additional = mapping[digit[-1]]

  return [prev_char + additional_char for prev_char in prev for additional_char in additional]

print(letterCombination("234"))
# ['adg', 'adh', 'adi', 'aeg', 'aeh', 'aei', 'afg', 'afh', 'afi', 'bdg', 'bdh', 'bdi', 'beg', 'beh', 'bei', 'bfg', 'bfh', 'bfi', 'cdg', 'cdh', 'cdi', 'ceg', 'ceh', 'cei', 'cfg', 'cfh', 'cfi']
