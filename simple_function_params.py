import os

def show_file_contents(search_term, file_path):
    with open(file_path) as file_in:
        for line in file_in:
            if search_term in line:
                print(line.rstrip())

show_file_contents("lamb", "DATA/mary.txt")
print('-' * 60)
show_file_contents("bird", "DATA/parrot.txt")
print("=" * 60)

def show_file_contents_multi(search_term, *file_paths):
    for file_path in file_paths:
        with open(file_path) as file_in:
            for line in file_in:
                if search_term in line:
                    file_name = os.path.basename(file_path)
                    print(file_name, line.rstrip())

show_file_contents_multi("bird", "DATA/alice.txt", "DATA/parrot.txt")

print("=" * 60)

def show_file_contents_ic(search_term, *file_paths, ignore_case=False):
    if ignore_case:
        search_term = search_term.lower()
    for file_path in file_paths:
        with open(file_path) as file_in:
            for original_line in file_in:
                if ignore_case:
                    search_line = original_line.lower()
                else:
                    search_line = original_line

                if search_term in search_line:
                    file_name = os.path.basename(file_path)
                    print(file_name, original_line.rstrip())

show_file_contents_ic("lizard", "DATA/words.txt", "DATA/alice.txt", "DATA/parrot.txt")
print('-' * 60)
show_file_contents_ic("lizard", "DATA/words.txt", "DATA/alice.txt", "DATA/parrot.txt", ignore_case=True)
