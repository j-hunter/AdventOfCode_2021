from pathlib import Path
import pytest

# Use truths to generate tests

days = []

with open("truths.txt") as f:
    for l in f:
        days += [l.split(',')[0]] 

#print(days)
tests = []
langs = ['py','cpp']
for d in days:
    tests += [(d,'ans')]
    for l in langs:
        if Path('./' + d + '/' + l).is_dir():
            tests += [(d,l)]
#print(tests)

@pytest.mark.parametrize("day, lang",tests)
def test_ans(day,lang):
    ansA = './' + day + '/a.ans'
    ansB = './' + day + '/b.ans'

    if lang == 'ans':
        print("Testing answer")
        assert Path(ansA).exists()
        assert Path(ansB).exists()
    else:
        print("Testing " + lang)
        langA = './' + day + '/' + lang + '/a.ans'
        langB = './' + day + '/' + lang + '/b.ans'
        #Still verify files exist
        assert Path(ansA).exists()
        assert Path(ansB).exists()
        assert Path(langA).exists()
        assert Path(langB).exists()

        #Read in and compare
        sAnsA = open(ansA).readline()
        sLangA = open(langA).readline()
        assert sAnsA == sLangA

        sAnsB = open(ansB).readline()
        sLangB = open(langB).readline()
        assert sAnsB == sLangB
