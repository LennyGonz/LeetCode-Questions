from random import random

BIAS = 0.66

def toss_biased():
  return random() > BIAS

def toss_fair():
  t1, t2 = toss_biased(), toss_biased()
  if t1 and not t2:
    return True
  elif not t1 and t2:
    return False
  else:
    return toss_fair()
