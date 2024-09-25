colors = ['red', 'green', 'purple', 'orange', 'brown',
'black', 'olive', 'navy', 'white', 'black',
'pink', 'chartreuse']

for color in colors:
    print(color)
print('-' * 60)

enum_colors = enumerate(colors)
print(f"{enum_colors = }")

for i, color in enum_colors:
    print(i, color)
print()

print(f"{colors = }")
rev_colors = reversed(colors)
print(f"{rev_colors = }")
for color in rev_colors:
    print(color)

states = ["NC", "AZ", "TX"]
cities = ['Durham', 'Tempe', 'Fredericksburg']

states_zip = zip(cities, states)

for city, state in states_zip:
    print(city, state)
print()

states_zip = zip(cities, states)
print(f"{list(states_zip) = }\n")

# range(stop-before)  range(start-at, stop-before)  range(start, stop, count-by)

for _ in range(3):
    print("Python is the best!")
print()
