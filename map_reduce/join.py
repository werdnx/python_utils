from map_reduce import MapReduce
import sys


mr = MapReduce.MapReduce()


def mapper(record):
    key = record[1]
    value = record
    mr.emit_intermediate(key, value)


def reducer(key, list_of_values):
    order = None
    for v in list_of_values:
        if v[0] == "order":
            order = v

    for v in list_of_values:
        if v[0] != "order":
            mr.emit(order + v)


if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
