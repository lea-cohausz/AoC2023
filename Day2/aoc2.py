import re

with open("aoc2.txt") as file:
    data = file.read().splitlines()

def get_maximum(pattern, game):
    match = re.findall(pattern, game)
    match = [int(x) for x in match]
    max_match = max(match)
    return(max_match)

### Part I
red_allowed = 12
blue_allowed = 14
green_allowed = 13

counter = 1
sum_games = 0
for game in data:
    max_red = get_maximum('(\d+) red', game)
    max_blue = get_maximum('(\d+) blue', game)
    max_green = get_maximum('(\d+) green', game)
    if max_red <= red_allowed and max_blue <= blue_allowed and max_green <= green_allowed:
        sum_games += counter
    counter += 1

print(f"The sum of the IDs of the allowed games is {sum_games}.")


### Part II
powers_of_cubes = 0
for game in data:
    max_red = get_maximum('(\d+) red', game)
    max_blue = get_maximum('(\d+) blue', game)
    max_green = get_maximum('(\d+) green', game)
    powers_of_cubes += max_red*max_blue*max_green
print(f"The sum of the power of cubes is {powers_of_cubes}.")