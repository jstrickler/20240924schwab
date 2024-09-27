from president import President

p = President(26)

print(p.first_name, p.last_name)
print()

for field in 'first_name', 'last_name', 'party':
    print(getattr(p, field))
print()

def get_fn(self):
    return f"{self.first_name} {self.last_name}"

setattr(President, "get_full_name", get_fn)

print(f"{p.get_full_name() = }")
