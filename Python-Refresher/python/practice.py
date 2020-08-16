# presidents = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson"]
# for president in range(len(presidents)):
#   print("President {}: {}".format(president+1, presidents[president]))

# presidents = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson"]
# for num, name in enumerate(presidents, start=1):
#   print("President {}: {}".format(num, name))

# colors = ["red", "green", "blue", "purple"]
# ratios = [0.2, 0.3, 0.1, 0.4]
# for i, color in enumerate(colors):
#   ratio = ratios[i]
#   print("{}% {}".format(ratio * 100, color))

# colors = ["red", "green", "blue", "purple"]
# ratios = [0.2, 0.3, 0.1, 0.4]

# result = zip(colors, ratios)
# result_list = list(result)
# print("ratios: ", result_list)

# for color, ratio in zip(colors, ratios):
#   print("{}% {}".format(ratio * 100, color))

# txt = "welcome+to+the+jungle"

# x = txt.split('+')

# print(x)

# languages = ["Python", "C Programming", "Java", "JavaScript"]
# largest_string = max(languages);

# print("The largest string is:", largest_string)

import heapq
H = [21,1,45,78,3,5]
# Use heapify to rearrange the elements
heapq.heapify(H)
print(H)
