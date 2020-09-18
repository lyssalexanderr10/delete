FILE_NAME = './local_copy.log'

from collections import Counter

total_count = 0

for line in open(FILE_NAME):
    total_count = total_count + 1

print(f"There was {total_count} requests made in the time period represented by the log.")
