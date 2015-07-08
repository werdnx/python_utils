__author__ = 'Dmitrenko'
import re
import collections
import numpy
import sys
from matplotlib import pyplot


def groupByKey(l, agg):
    res = {}
    for i in l:
        v = res.get(i[0], None)
        if v == None:
            res[i[0]] = i[1]
        else:
            res[i[0]] = agg(v, i[1])
    return res


def histInfo(ordered):
    x = []
    y = []
    for k, v in ordered.iteritems():
        x.append(k)
        y.append(v)
    return (x, y)


if __name__ == '__main__':
    times = []
    args = sys.argv
    colorDict = {0: 'Red', 1: 'Blue', 2: 'Green', 3: 'Black'}
    i = 0
    for file in args[1:]:
        times = []
        print 'file=' + file
        ins = open(file, "r")
        for line in ins:
            m = re.search("^.*?GET.*?transactionCheck.*?REQUEST_BODY.*?:7009\" \"200\" \"(.*?)\"", line)
            if m:
                times.append(m.groups()[0])

        grouped = groupByKey(map(lambda x: (x, 1), map(lambda x: float("{0:.2f}".format(float(x))), times)),
                             lambda x, y: x + y)

        ordered = collections.OrderedDict(sorted(grouped.items()))

        info = histInfo(ordered)

        bins = numpy.linspace(0, 1, 100)
        pyplot.hist(info[0], bins, alpha=0.25, label='file'+str(i), weights=info[1], color=colorDict[i])
        # pyplot.hist(y, bins, alpha=0.25, label='y',weights=[3,1])
        pyplot.legend(loc='upper right')
        i = i + 1
        # f = open('E:\\temp\\rbs\\logs\\py-ord.csv', 'w')
        # f.write('time;count\n')
        # for k,v in ordered.iteritems():
        #    f.write(str(k))
        #    f.write(";")
        #    f.write(str(v))
        #    f.write('\n')
        # f.close()
    pyplot.show()

