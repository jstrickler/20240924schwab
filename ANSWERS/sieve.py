import sys

limit = 101
if len(sys.argv) > 1:
    limit = int(sys.argv[1]) + 1

flags = [True] * limit

prime_count = 0
for num in range(2, limit):
    if flags[num]:
        prime_count += 1
        for multiple_of_num in range(2 * num, limit, num):
            flags[multiple_of_num] = False
    