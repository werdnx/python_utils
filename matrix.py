import MapReduce
import sys

mr = MapReduce.MapReduce()
L = 5
M = 5
N = 5


def mapper(record):
    name = record[0]
    i = record[1]
    j = record[2]
    v = record[3]
    if name == "a":
        for k in range(0, N):
            mr.emit_intermediate((i, k), (j, v))
    if name == "b":
        for k in range(0, L):
            mr.emit_intermediate((k, j), (i, v))


def reducer(key, list_of_values):
    map1 = {}
    map2 = {}
    for v in list_of_values:
        add_to_map(map1, map2, v[0], v[1])

    total = 0
    for mapKey in map1.keys():
        if (map2.__contains__(mapKey)):
            total += map1[mapKey] * map2[mapKey]
    mr.emit((key[0], key[1], total))


def add_to_map(map, map2, k, v):
    if map.get(k, None) is None:
        map[k] = v
    else:
        map2[k] = v


if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
