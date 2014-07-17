import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    key = record[0]
    value = record[1]
    mr.emit_intermediate(key, "in:"+value)
    mr.emit_intermediate(value, "out:"+key)

def reducer(key, list_of_values):
    inMap = {}
    outMap = {}
    for v in list_of_values:
        sp = v.split(":")
        if sp[0] == "in":
            inMap[sp[1]] = sp[1]
        else:
            outMap[sp[1]] = sp[1]

    for inKey in inMap.keys():
        if contain(outMap,inKey) == False:
            mr.emit((inKey, key))
            mr.emit((key, inKey))


def contain(map,key):
    if map.get(key,None) == key:
        return True
    else:
        return False

if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
