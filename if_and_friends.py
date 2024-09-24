value = 42

if value > 75: 
    print("kangaroo")
    print("kookaburra")
    if value > 85:
        print("wallaby")
elif value > 50:  # else if
    print("koala")
    print("crocodile")
else:
    print("platypus")

print("ALL DONE\n")

DEBUG = True

#  output_color = DEBUG?"red":"blue"
output_color = "red" if DEBUG else "blue"

print(f"{output_color = }")

#  == != > < >= <= 



