import math

# Wyliczenie entropii
def calc_entropy(dict_of_chance):
    entr = 0
    for key in dict_of_chance:
        p = dict_of_chance[key]
        if p != 0:
            entr += p * math.log2(p)
            #print(entropy)
    entr = entr * -1
    return entr

def calc_info():
    pass

