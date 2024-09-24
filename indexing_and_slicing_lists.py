fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

print(f"{len(fruits) = }")
print(f"{fruits[0] = }")
print(f"{fruits[9] = }")
print(f"{fruits[21] = }")
print(f"{fruits[-1] = }")  # len(fruits) - 1
print()
print(f"{fruits[2:6] = }")
#  LIST[start-at:stop-before:count-by]
print(f"{fruits[0:3] = }")
print(f"{fruits[:3] = }")
print(f"{fruits[-4:] = }")
print(f"{fruits[1:-1] = }")

s = '"Kentucky"'
print(s)
print(s[1:-1])

# slicing works on lists, tuples, strings, and bytes

print(f"{fruits[5:11] = }")

start = 5
print(f"{fruits[start:start+6] = }")

fruits_copy = list(fruits)
fruits_copy = fruits[::]

