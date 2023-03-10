from pathlib import Path
import pytest

langs = ['py','cpp']
#list all folders, check for answer files

days = []
for f in Path('./').iterdir():
    if f.is_dir() and f.name.startswith('day'):
        #print(f)
        days += [f]
days.sort()

tests = []
for d in days:
    for f in d.iterdir():
        if f.is_dir() and f.name in langs:
            print(f)
            tests += [(d.name,f.name)]

#print(tests)

@pytest.mark.parametrize('day,lang',tests)
def test_build(day,lang):
    p = Path(day + '/' + lang)
    afile = p / 'a.ans'
    bfile = p / 'b.ans'

    assert afile.exists()
    assert bfile.exists()
