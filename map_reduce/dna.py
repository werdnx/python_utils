from map_reduce import MapReduce
import sys

mr = MapReduce.MapReduce()


def mapper(record):
    value = record[1]
    mr.emit_intermediate(1, value[:(len(value) - 10)])


def reducer(key, list_of_values):
    map = {}
    for v in list_of_values:
        map[v] = v
    for mapKey in map.keys():
        mr.emit(mapKey)

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
