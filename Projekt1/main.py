from calc_values import count_occur, occur_prob
from functions import calc_entropy, calc_info_main, calc_gain
import copy
from tree import build_tree

f = open("gielda.txt", "r")
data = [[x for x in line.rstrip("\n").split(',')] for line in f]
build_tree(data)

