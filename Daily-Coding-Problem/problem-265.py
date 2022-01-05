def assign_bonuses(lines):
  bonuses = [1 for _ in range(len(lines))]

  for i in range(1, len(lines)):
    if lines[i] > lines[i - 1]:
      bonuses[i] = bonuses[i - 1] + 1

  for i in range(len(lines) - 2, -1, -1):
    if lines[i] > lines[i + 1]:
      bonuses[i] = max(bonuses[i], bonuses[i + 1] + 1)

  return bonuses
