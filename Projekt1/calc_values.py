# Read file
import copy
import math

# Atrybuty wraz z liczbą wystąpień
def count_occur(n, m, data):
    data_t = copy.deepcopy(data)
    data_t = list(map(list, zip(*data_t)))
    #print(data_t)
    dict_of_words = {}
    for i in range(m):
        dict_of_words[i] = {}
        for j in range(n):
            key = data[j][i]
            dict_of_words[i][key] = data_t[i].count(key)

    return dict_of_words


# Prawdopodobieństwo wystąpienia
def occur_prob(n, m, dict_of_words):
    dict_of_chance = dict_of_words
    for i in range(m):
        for key in dict_of_chance[i]:
            dict_of_chance[i][key] = dict_of_chance[i][key]/n
    return dict_of_chance


# Wyliczenie entropii
def calc_entropy(dict_of_chance):
    entropy = 0
    for key in dict_of_chance:
        p = dict_of_chance[key]
        if p != 0:
            entropy += p * math.log2(p)
            #print(entropy)
    entropy = entropy * -1
    return entropy