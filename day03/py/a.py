from pathlib import Path
import numpy as np

filename = '../input.txt'

def A(fname = filename):
    file = Path(fname)

    tot = np.zeros(12, np.int32)
    c = 0
    ans = 0

    with open(file) as f:
        for l in f:
            c = c + 1
            tot += np.asarray(list(l[:-1])).astype(np.int32)

    print(tot,c)
    for i in range(12):
        if tot[i] > c/2:
            ans = ans + 1
        ans = ans << 1

    ans = ans >> 1
    ans = ans * (int('111111111111',2) ^ ans)
    return ans

if __name__ == '__main__':
    print(A())