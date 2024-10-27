import re
import numpy as np

with open("aoc3.txt") as file:
    data = file.read().splitlines()

# Part I
special_chars = ["#","%","=","/","-","*","+","@","$","&"]

extra_line = ["."*len(data[0])]
data = extra_line + data + extra_line
data = ["."+line for line in data]
data = [line+"." for line in data]

sum_vals = 0
for i in range(len(data)):
    line = data[i]
    digits = re.finditer(r'\d+', line)
    for digit in digits:
        start = digit.start()
        end = digit.end()
        value = digit.group(0)
        value = int(value)
        upper_comp = data[i-1][(start-1):end+1]
        left_comp = line[start-1]
        right_comp = line[end]
        lower_comp = data[i+1][(start-1):end+1]

        all_chars = lower_comp+upper_comp+right_comp+left_comp
        if any(char in all_chars for char in special_chars):
            sum_vals += value

print(f"The sum of the part numbers is {sum_vals}.")

# Part II
sum_gears = 0
for i in range(len(data)):
    line = data[i]
    star_indices = [i for i, x in enumerate(line) if x == "*"]
    if star_indices:
        for star in star_indices:
            two = 0
            gear_vals = []
            digits_line = re.finditer(r'\d+', line)
            if digits_line:
                for digit in digits_line:
                    if digit.start() == star+1:
                        two += 1
                        gear_vals.append(int(digit.group(0)))
                    if digit.end() == star:
                        two += 1
                        gear_vals.append(int(digit.group(0)))

            digits_u = re.finditer(r'\d+', data[i-1])
            if digits_u:
                for digit in digits_u:
                    if digit.start() == star-1 or digit.start() == star or digit.start() == star+1 or digit.end()-1 == star-1 or digit.end()-1 == star or digit.end()-1 == star+1:
                        two += 1
                        gear_vals.append(int(digit.group(0)))
            digits_l = re.finditer(r'\d+', data[i+1])
            if digits_l:
                for digit in digits_l:
                    if digit.start() == star-1 or digit.start() == star or digit.start() == star+1 or digit.end()-1 == star-1 or digit.end()-1 == star or digit.end()-1 == star+1:
                        two += 1
                        gear_vals.append(int(digit.group(0)))
            if two == 2:
                product_gear = np.prod(gear_vals)
                sum_gears += product_gear

print(f"The sum of the gear ratios is {sum_gears}.")