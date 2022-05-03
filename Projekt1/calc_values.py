# Read file

# Atrybuty wraz z liczbą wystąpień
def count_occur(n, m, data):
    data_merged = sum(data, [])
    dict_of_words = {}
    for i in range(m):
        dict_of_words[i] = {}
        for j in range(n):
            key = data[j][i]
            dict_of_words[i][key] = data_merged.count(key)

    return dict_of_words


# Prawdopodobieństwo wystąpienia
def occur_prob(n, m, dict_of_words):
    dict_of_chance = dict_of_words
    for i in range(m):
        for key in dict_of_chance[i]:
            dict_of_chance[i][key] = dict_of_chance[i][key]/n
    return dict_of_chance


