def calc_gain(attr_info, entropy):
    gain = entropy - attr_info
    return gain

def clac_gain_ratio(gain, split_info):
    ratio = 0
    if split_info != 0:
        ratio = gain/split_info
    return ratio