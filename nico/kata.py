# https://www.codewars.com/kata/basic-nico-variation/train/python
import math


def nico(key, message):
    # crazy {2:[], 3:[], 1:[], 5:[], 4[]}
    d = {key: [] for key in list(map(lambda x: sorted(key).index(x) + 1, list(key)))}

    # secretinformation
    # {2:[s,t,r,o], 3:[e,i,m,n], 1:[c,n,a,''], 5:[r,f,t,''], 4[e,o,i,'']}
    counter = 0
    for i in range(0, int(math.ceil(len(message) / len(key)))):
        for _, v in d.items():
            if counter < len(message):
                v.append(message[counter])
            else:
                v.append(" ")
            counter += 1

    res = []
    for i in range(0, int(math.ceil(len(message) / len(key)))):
        res.extend([d[k][i] for k in sorted(d.keys())])
    return "".join(res)
