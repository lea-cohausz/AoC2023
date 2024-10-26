import re

with open("aoc1.txt") as file:
    data = file.read().splitlines()

### Part I
digits_only = [re.findall(r"\d+", s) for s in data]
digits_only = ["".join(s) for s in digits_only]
first_and_last_digit = [d[0] + d[-1] for d in digits_only]
first_and_last_digit = [int(d) for d in first_and_last_digit]

print(f"The sum of the calibration values is: {sum(first_and_last_digit)}")


### Part II
replacer = {'one': 'one1one','two': 'two2two','three': 'three3three','four': 'four4four', 'five': 'five5five','six': 'six6six','seven': 'seven7sevenn','eight': 'eight8eight','nine': 'nine9nine'}
replaced = []
for s in data:
    for word, digit in replacer.items():
        s = s.replace(word, digit)
    replaced.append(s)
digits_only = [re.findall(r"\d+", s) for s in replaced]
digits_only = ["".join(s) for s in digits_only]
first_and_last_digit = [d[0] + d[-1] for d in digits_only]
first_and_last_digit = [int(d) for d in first_and_last_digit]
print(replaced)
print(f"The sum of the calibration values for Part II is: {sum(first_and_last_digit)}")