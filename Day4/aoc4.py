
with open("aoc4.txt") as file:
    data = file.read().splitlines()

data = [x.split(": ")[1] for x in data]
data = [x.split(" | ") for x in data]
data = [[x.split() for x in sides] for sides in data]

# Part I
sum_points = 0
for card in data:
    winning_numbers = card[0]
    elfs_numbers = card[1]
    number_of_matches = len(set(winning_numbers).intersection(elfs_numbers))
    if number_of_matches > 0:
        value = 2**(number_of_matches-1)
        sum_points += value

print(f"Sum of points: {sum_points}.")

# Part II
number_of_cards = [1]*len(data)
for c in range(len(data)):
    card = data[c]
    cards_exist = number_of_cards[c]
    winning_numbers = card[0]
    elfs_numbers = card[1]
    matching_numbers = len(list(set(winning_numbers).intersection(elfs_numbers)))
    if matching_numbers > 0:
        for n in range(1, matching_numbers+1):
            number_of_cards[c+n] += cards_exist

print(f"The total number of scratchcards is: {sum(number_of_cards)}.")
