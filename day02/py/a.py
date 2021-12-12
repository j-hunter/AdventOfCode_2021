from pathlib import Path

filename = '../input.txt'

def A(fname = filename):
    file = Path(fname)

    x = 0
    y = 0

    dx = {'forward': 1, 'up': 0, 'down': 0}
    dy = {'forward': 0, 'up': -1, 'down': 1}

    with open(file) as f:
        for l in f:
            s = l.split()
            x += dx[s[0]] * int(s[1])
            y += dy[s[0]] * int(s[1])

    return x * y

if __name__ == '__main__':
    print(A())