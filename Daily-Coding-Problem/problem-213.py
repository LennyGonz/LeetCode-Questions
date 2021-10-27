def generate_IP_addresses(s, parts=[]):
  addresses = []

  if len(parts) > 4:
    return []

  if not s:
    if len(parts) == 4:
      return [".".join(parts)]
    else:
      return []

  addresses += generate_IP_addresses(s[1:], parts + [s[:1]])

  if len(s) > 1 and 10 <= int(s[:2]) <= 99:
    addresses += generate_IP_addresses(s[2:], parts + [s[:2]])

  if len(s) > 2 and 100 <= int(s[:3]) <= 255:
    addresses += generate_IP_addresses(s[3:], parts + [s[:3]])

  return addresses
