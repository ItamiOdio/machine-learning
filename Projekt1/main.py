from tree import build_tree

f = open("car.data", "r")
data = [[x for x in line.rstrip("\n").split(',')] for line in f]
build_tree(data)
