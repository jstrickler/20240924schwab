import alpha.mathlib.geometry as geometry   # find geometry.py and execute its code
import sys

a1 = geometry.circle_area(8)
a2 = geometry.rectangle_area(10, 12)
a3 = geometry.square_area(7.9)
print(a1, a2, a3)

# module search algorithm
# 1. Current dir/folder
# 2. Folders in PYTHONPATH env variable
# 3. Standard Python library location (depends on installation)
print(f"{sys.prefix = }")
print()
for path in sys.path:
    print(path)
