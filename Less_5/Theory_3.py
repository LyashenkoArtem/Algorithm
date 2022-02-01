from collections import ChainMap

d_1 = {'a': 2, 'b': 4, 'c': 20}
d_2 = {'a': 10, 'b': 20, 'd': 40}

d_map = ChainMap(d_1, d_2)

print(d_map)

x = d_map.new_child({'a': 11, 'f': 30})

print(x)
print(x.maps[0])
print(x.maps[-1])
print(x.parents)