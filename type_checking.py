import typing as T

count: int

count = "wombat"

print(f"{count = }")

def find_word(word: str, file_paths: T.Iterable[str]) -> list:
    found = []
    for file_path in file_paths:
        with open(file_path) as file_in:
            for line in file_in:
                if word in line:
                    found.append(line.rstrip())
    return found


found_lines: list = find_word("rabbit", ["DATA/words.txt", "DATA/alice.txt"])
print(found_lines)

# T.Dict[str, int]
# dict[str, int]
# set[int]
# set[str]
# list[int|float]

def spam(foo: T.Any) -> int:
    return 0


def ham(bar: T.Optional[float]):
    pass


class Animal:
    pass

class Mammal(Animal):
    pass

class Dog(Mammal):
    pass

class Mosquito(Animal):
    pass

def toast(pet: Mammal):
    pass











