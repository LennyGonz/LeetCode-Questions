PAIRS = {
  'CM': 900,
  'CD': 400,
  'XC': 90,
  'XL': 40,
  'IX': 9,
  'IV': 4
}

SINGLES = {
  'M': 1000,
  'D': 500,
  'C': 100,
  'L': 50,
  'X': 10,
  'V': 5,
  'I': 1
}

def decimate(s):
  decimal_map = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

  total = 0
  for i in range(len(s) - 1):
    if decimal_map[s[i]] >= decimal_map[s[i + 1]]:
      total += decimal_map[s[i]]
    else:
      total -= decimal_map[s[i]]
  total += decimal_map[s[-1]]

  return total
