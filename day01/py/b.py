
from pathlib import Path

filename = '../input.txt'

def B(fname = filename):
    file = Path(fname)

    inc = 0
    ser = []

    with open(file) as f:
        for i in range(3):
            ser.insert(0,int(f.readline()))

        last = sum(ser)
        
        for l in f:
            i = int(l)

            ser.insert(0,i)
            ser.pop()
            if(sum(ser) > last):
                inc = inc + 1
            last = sum(ser)

    return inc

if __name__ == '__main__':
    print(B())
