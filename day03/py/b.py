from pathlib import Path
import numpy as np

filename = '../input.txt'

def B(fname = filename):
    file = Path(fname)

    rep = []#np.zeros((12,1), np.int32)
    c = 0
    o = 0
    ans = 0

    with open(file) as f:
        for l in f:
            rep += [np.asarray(list(l[:-1])).astype(np.int32)]

    rep = np.stack(rep)
    most = np.round(np.sum(rep,axis = 0) / rep.shape[0])
    most = most.astype(np.int32)
    least = 1 - np.round(np.sum(rep,axis = 0) / rep.shape[0])
    least = least.astype(np.int32)

    o = rep == [most]
    c = rep == [least]

    for i in range(12):
        print(np.any(o[:,:i]))
        #print(o[:,:i])

    #print(most,o[:,1])
    ans = ans >> 1
    ans = c * o
    return ans

if __name__ == '__main__':
    print(B())