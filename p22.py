import os
with open('0022_names.txt', 'r') as file:
    content = file.read()

names = content.replace('"', '')
names = names.split(',')
names.sort()
name_scores = []
letter_values = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
name_score_sum = 0
for pos, name in enumerate(names):
    letters_in_name = list(name)
    alphabetical_value = 0
    for letter in letters_in_name:
        # alphabetical_value += letter_values[letter]
        alphabetical_value += ord(letter) - 64
    name_score = alphabetical_value * (pos + 1)
    name_score_sum += name_score
    name_scores.append([name, alphabetical_value, name_score, pos])
print(name_score_sum)

# short solution from preseren 
with open("0022_names.txt", "r") as names:
    names = sorted(names.read().replace('"', ""). split(","))
    result = sum(sum(ord(j) - 64 for j in name) * i for i, name in enumerate(names, 1))
    print(result)
