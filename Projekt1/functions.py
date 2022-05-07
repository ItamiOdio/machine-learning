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
        #print(attr_indexes)
        info_temp = create_decision_table(attr_indexes, data, prob_count, i)
        info.append(info_temp)


    return info
    pass

def calc_gain(attr_info, entropy):
    gain = entropy - attr_info
    return gain

def clac_gain_ratio(gain, split_info):
    ratio = 0
    if split_info != 0:
        ratio = gain/split_info
    return ratio

def find_attributes(data, key_list, index):
    index_list = []
    #print(key_list)
    for key in key_list[index]:
        value = [i for i, x in enumerate(data[index]) if x == key]
        index_list.append(value)
    return index_list

def create_decision_table(attr_indexes, data, prob_count, ind):
    info = 0
    probs_temp = []
    decision_temp = []
    for k in prob_count[ind]:
        probs_temp.append(prob_count[ind][k])

    for i in (attr_indexes):
        tab_of_decision = dict.fromkeys(prob_count[len(data[0]) - 1].keys(), 0.0)
        for j in i:
            tab_of_decision[data[j][len(data[0]) - 1]] += 1

        for key in tab_of_decision:
            tab_of_decision[key] = tab_of_decision[key] / len(i)

        decision_temp.append(tab_of_decision)

    #print(decision_temp)
    #print(probs_temp)
    info = sum([(probs_temp[i] * calc_entropy(decision_temp[i])) for i in range(len(probs_temp))])
    return info



def calc_info2(attr_indexes, data, prob_count, ind):
    info = 0
    temp_entr = []

    for i in (attr_indexes):
        temp = []
        for j in i:
            temp.append(data[j])
            temp_occ = count_occur(len(temp), len(temp[0]), temp)
            temp_prob = occur_prob(len(temp), len(temp[0]), temp_occ)

        temp_entr.append(calc_entropy(temp_prob[len(temp[0])-1]))
    #print(temp_entr)

    k = 0
    for key in prob_count[ind]:
        prob = prob_count[ind][key]
        ent = temp_entr[k]
        info += prob * ent
        k += 1

    # print(info)
    return info





