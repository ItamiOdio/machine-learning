from calc_values import count_occur, occur_prob
from info import calc_entropy, calc_info_main
from gain import calc_gain, clac_gain_ratio
import copy

def build_tree(data, margin='', prev=-1):
    rows = len(data)
    columns = len(data[0])
    data_t = [list(i) for i in zip(*data)]
    #print(data)

    # Oblicz 1) wystąpienia, 2) prawdopodobieństwa, 3) entropię, 4) f. informacji, 5) przyrost,
    occurances = count_occur(rows, columns, data)
    #print(occurances)
    probabilities = occur_prob(rows, columns, copy.deepcopy(occurances))

    #print(probabilities)

    ent = calc_entropy(probabilities[columns - 1])
    #print(ent)

    info = calc_info_main(data, probabilities, columns)
    #print(info)

    gain = [(calc_gain(info[i], ent)) for i in range(len(info))]
    #print(gain)

    split_info = [(calc_entropy(probabilities[i])) for i in range(columns - 1)]
    #print(split_info)

    gain_ratio = [clac_gain_ratio(gain[i],split_info[i]) for i in range(len(gain))]
    #print(gain_ratio)

    max_gain_ratio = max(gain_ratio)
    index_max_gain_ratio = gain_ratio.index(max_gain_ratio)

    # Warunek stopu
    if max_gain_ratio > 0:

        # Wypisz dla liści
        if prev != -1:
            print(f'{margin}{list(occurances[prev].keys())[0]} -> Atrybut: {index_max_gain_ratio + 1}')

        # Wypisz dla korzenia
        else:
            print(f'{margin}Atrybut: {index_max_gain_ratio + 1}')

        # Przygotuj dane do rozgałęzienia
        prev = index_max_gain_ratio
        margin += '\t'
        new_data = [[x for x in data if x[index_max_gain_ratio] == key] for key in occurances[index_max_gain_ratio]]
        #print(new_data)


        for x in new_data:
            build_tree(x, margin, prev)
            
    #Decyzja
    else:
        print(f'{margin}{list(occurances[prev].keys())[0]} -> D: {list(occurances[columns - 1].keys())[0]}')

