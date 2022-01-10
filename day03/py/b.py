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
    least = np.round(1 - (np.sum(rep,axis = 0) / rep.shape[0]))
    least = least.astype(np.int32)

    print("Least: ", np.sum(rep,axis = 0) )

    o = rep == [most]
    c = rep == [least]
    ochk = 0
    cchk = 0
    oloc = 0
    cloc = 0

    for i in range(12):
        chk = o[:,:i+1]
        chk = np.all(chk, axis = 1)
        if np.any(chk):
            ochk = i
            oloc = np.nonzero(chk)
            #if len(oloc) < 5:
            #    print (oloc)
            

        chk = c[:,:i+1]
        chk = np.all(chk, axis = 1)
        if np.any(chk):
            cchk = i
            cloc = np.nonzero(chk)
            #if len(cloc) < 5:
            #    print(cloc)
        print(len(np.nonzero(chk)[0]))
        
        #print(np.any(chk),cchk)
        #print(np.any(o[:][,i]))
        #print(o[:,:i])
        #break
    oloc = oloc[0].tolist()
    cloc = cloc[0].tolist()
    print(f"Most is {ochk} at {oloc},\nleast is {cchk} at {cloc}")
    print(f"Mosts are:\n{ most }\n")
    for i in oloc:
        print(rep[i])

    print(f"Leasts are:\n{least}\n")
    for i in cloc:
        print(rep[i])


    #print(most,o[:,1])
    ans = ans >> 1
    ans = c * o
    return ans

if __name__ == '__main__':
    print(B())