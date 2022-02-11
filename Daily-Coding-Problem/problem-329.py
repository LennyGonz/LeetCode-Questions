def format_input(guy_preferences, gal_preferences):
  """
  Format preferences lists to improve the running time.
  - guy preferences are reversed, so popping the next most desired partner is O(1)
  - gal preferences are stored in a dict, so that comparing partner desirability is O(1)
  """
  guy_preferences = {guy: list(reversed(pref)) for guy, pref in guy_preferences.items()}

  for gal, pref in gal_preferences.items():
    gal_preferences.update({gal: {guy: i for i, guy in enumerate(pref)}})

  return guy_preferences, gal_preferences

def match(guy_preferences, gal_preferences):
  guy_preferences, gal_preferences = format_input(guy_preferences, gal_preferences)

  married_men = set()
  married_women = set()

  bachelors = list(guy_preferences.keys())
  pairs = {}

  while bachelors:
    m1 = bachelors.pop()
    while m1 not in married_men:
      woman = guy_preferences[m1].pop()

      if woman not in married_women:
        married_men.add(m1)
        married_women.add(woman)
        pairs[woman] = m1

      else:
        m2 = pairs[woman]
        if gal_preferences[woman][m1] < gal_preferences[woman][m2]:
          married_men.add(m1)
          married_men.remove(m2)
          bachelors.append(m2)
          pairs[woman] = m1

  return pairs
