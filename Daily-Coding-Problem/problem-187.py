def is_overlapping(rec1, rec2):
  if rec1["top_left"][0] >= rec2["top_left"][0] + rec2["dimensions"][0]:
    return False

  if rec1["top_left"][0] + rec1["dimensions"][0] <= rec2["top_left"][0]:
    return False

  if rec1["top_left"][1] <= rec2["top_left"][1] - rec2["dimensions"][1]:
    return False

  if rec1["top_left"][1] - rec1["dimensions"][1] >= rec2["top_left"][1]:
    return False

  return True
