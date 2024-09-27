
person = "Abraham Lincoln"

def spam():
    word = "SPAM"
    print(f"{word} {word} {word} {word} ")

spam()
print(person)

g = globals()
print(g)
print('-' * 60)

variable_name = "person"

print(f"{g[variable_name] = }")

g['color'] = "blue"
print(f"{color = }")


