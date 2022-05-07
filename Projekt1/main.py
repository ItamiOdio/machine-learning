from calc_values import count_occur, occur_prob
from functions import calc_entropy, calc_info_main, calc_gain
import copy

f = open("gielda.txt", "r")
data = [[x for x in line.rstrip("\n").split(',')] for line in f]
rows = len(data)
columns = len(data[0])
print(rows)

occurances = count_occur(rows, columns, data)
print(occurances)
probabilities = occur_prob(rows, columns, copy.deepcopy(occurances))

print(probabilities)

# Oblicz entropię dla atrybutu decyzyjnego
ent = calc_entropy(probabilities[columns-1])
print(ent)

info = calc_info_main(data, probabilities, columns)
print(info)

gain = [(calc_gain(info[i], ent)) for i in range(len(info))]
print(gain)

split_info = [(calc_entropy(probabilities[i])) for i in range(columns-1)]
print(split_info)
