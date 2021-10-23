lengths = {}

def get_collatz_length(n):
  if n not in lengths:
    if n == 1:
      lengths[n] = 1
    elif n % 2 == 0:
      lengths[n] = get_collatz_length(n / 2) + 1
    else:
      lengths[n] = get_collatz_length(3 * n + 1) + 1
  return lengths[n]

for i in range(1, 1000000):
  get_collatz_length(i)

print(max(lengths, key=lengths.get)) # 837799
