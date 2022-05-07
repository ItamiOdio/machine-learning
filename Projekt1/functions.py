from calc_values import count_occur, occur_prob
import math
import copy

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

def calc_info_main(data, prob_count, columns):
    info = []
    data_t = copy.deepcopy(data)
    data_t = list(map(list, zip(*data_t)))
    for i in range(columns-1):
        attr_indexes = (find_attributes(data_t,prob_count, i))
        print(attr_indexes)
        info_temp = calc_info(attr_indexes, data, prob_count, i)
        info.append(info_temp)

    return info
    pass

def calc_gain(attr_info, entropy):
    gain = entropy - attr_info
    return gain

def find_attributes(data, key_list, index):
    index_list = []
    #print(key_list)
    for key in key_list[index]:
        value = [i for i, x in enumerate(data[index]) if x == key]
        index_list.append(value)
    return index_list

def calc_info(attr_indexes, data, prob_count, ind):
    info = 0
    print('Poczatek')
    temp_entr = []

    for i in (attr_indexes):
        temp = []
        for j in i:
            temp.append(data[j])
            temp_occ = count_occur(len(temp), len(temp[0]), temp)
            temp_prob = occur_prob(len(temp), len(temp[0]), temp_occ)

        temp_entr.append(calc_entropy(temp_prob[len(temp[0])-1]))
    print(temp_entr)

    k = 0
    for key in prob_count[ind]:
        prob = prob_count[ind][key]
        ent = temp_entr[k]
        info += prob * ent
        k += 1

    print()
    print(info)
    print('Koniec')
    return info









