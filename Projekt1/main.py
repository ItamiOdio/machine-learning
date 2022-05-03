from calc_values import count_occur, occur_prob
from functions import calc_entropy, calc_info

f = open("gielda.txt", "r")
data = [[x for x in line.rstrip("\n").split(',')] for line in f]
data_t = list(map(list, zip(*data)))

rows = len(data)
columns = len(data[0])
print(rows)

occurances = count_occur(rows, columns, data)
print(occurances)

probabilities = occur_prob(rows, columns, occurances)
print(probabilities)

# Oblicz entropię dla atrybutu decyzyjnego
ent = calc_entropy(probabilities[columns-1])
print(ent)