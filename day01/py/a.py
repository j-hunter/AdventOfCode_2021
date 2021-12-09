
from pathlib import Path

filename = '../input.txt'

def A(fname = filename):
    file = Path(fname)

    inc = 0
    with open(file) as f:
        last = int(f.readline())
        for l in f:
            i = int(l)
            if(i > last):
                inc = inc + 1
            last = i

    return inc

if __name__ == '__main__':
    print(A())
