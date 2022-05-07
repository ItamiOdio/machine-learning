from calc_values import count_occur, occur_prob
from functions import calc_entropy, calc_info_main, calc_gain, clac_gain_ratio
import copy

def build_tree(data, margin='', poprzedni=-1):
    rows = len(data)
    columns = len(data[0])
    #print(data)

    # Oblicz 1) wystąpienia, 2) prawdopodobieństwa, 3) entropię, 4) f. informacji, 5) przyrost,
    #
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

    ratio_indexes = [i for i in range(len(gain_ratio)) if gain_ratio[i] == max(gain_ratio)]
    #print(ratio_indexes)

    w_index = 0
    for w in ratio_indexes:
        if w != poprzedni:
            w_index = w
            break
    
    if max(gain_ratio) > 0:
        if poprzedni != -1:
            print(f'{margin}:{list(occurances[poprzedni].keys())[0]} A{w_index + 1}')
        else:
    
            print(f'{margin}A{w_index + 1}')
        poprzedni = w_index
        margin += '\t'
        new_data = [[a1 for a1 in data if a1[w_index] == key] for key in occurances[w_index]]
        # print(new_data)
        for lisc in new_data:
            # print('----')
            build_tree(lisc, margin, poprzedni)
    else:
        print(f'{margin}:{list(occurances[poprzedni].keys())[0]} -> {list(occurances[columns - 1].keys())[0]}')

