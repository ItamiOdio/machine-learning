from calc_values import calc_entropy
import copy

#Oblicz funkcję informacji
def calc_info_main(data, prob_count, columns):
    info = []
    data_t = copy.deepcopy(data)
    data_t = list(map(list, zip(*data_t)))
    for i in range(columns-1):
        attr_indexes = (find_attributes(data_t,prob_count, i))
        #print(attr_indexes)
        info_temp = calc_info(attr_indexes, data, prob_count, i)
        info.append(info_temp)
    return info
    pass

# Znajdź indeksy, dla poszczególnych kluczy
def find_attributes(data, key_list, index):
    index_list = []
    #print(key_list)
    for key in key_list[index]:
        value = [i for i, x in enumerate(data[index]) if x == key]
        index_list.append(value)
    return index_list

# Oblicz funkcję informacji dla jednej kolumny
def calc_info(attr_indexes, data, prob_count, ind):
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





