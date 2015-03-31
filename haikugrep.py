#!/usr/bin/python

#Paul Croft
#March 30, 2015

import string
from pprint import pprint, pformat

VOWELS = set("aeiouy")

def syllables(inword):
    inlist = list(inword.lower())
    invowels = False
    sylcount = 0
    if inlist[0] in VOWELS:
        invowels = True
        sylcount = 1
    while inlist:
        scanner = inlist.pop(0)
        if scanner in VOWELS and not invowels:
            sylcount += 1
            invowels = True
        elif scanner not in VOWELS and invowels:
            invowels = False

    #silent e sillyness
    if len(inword) > 2:
        if inword[-1] == 'e':
            if inword[-2] not in VOWELS:
                if inword[-3] in VOWELS:
                    sylcount -= 1

    #all consonant words sometimes arise (e.g. "Grr")
    if not sylcount:
        return 1
    return sylcount

def findhaiku(inlist):
    if not inlist:
        return
    startidx = 0
    endidx = 0
    sevenidx = 0
    fiveidx = 0
    finishidx = len(inlist) - 1
    foundhaiku = False
    while endidx != finishidx:
        if startidx == endidx:
            endidx += 1
        tempslys = sum(map(lambda x:x[1],inlist[startidx:endidx]))
        if tempslys < 5:
            endidx += 1
        elif tempslys > 5:
            startidx += 1
        else:#tempslys == 5
            sevenidx = endidx
            tempslys = sum(map(lambda x:x[1],inlist[endidx:sevenidx]))
            while tempslys < 6 and sevenidx != finishidx:
                sevenidx += 1
                tempslys = sum(map(lambda x:x[1],inlist[endidx:sevenidx]))
                if tempslys == 7:
                    fiveidx = sevenidx
                    tempslys = sum(map(lambda x:x[1],inlist[sevenidx:fiveidx]))
                    while tempslys < 4 and fiveidx != finishidx:
                        fiveidx += 1
                        tempslys = sum(map(lambda x:x[1],inlist[sevenidx:fiveidx]))
                        if tempslys == 5:
                            templist = []
                            templist.append(inlist[startidx:endidx])
                            templist.append(inlist[endidx:sevenidx])
                            templist.append(inlist[sevenidx:fiveidx])
                            templist = map(lambda x:' '.join(map(lambda y:y[0],x)),templist)#remove syllable counts and join with ' '
                            haiku = '\n'.join(map(string.capitalize,templist))
                            print "%s:" % string.capitalize(max(haiku.split(),key=len))
                            print haiku + '\n'

            startidx += 1

def main():
    line = raw_input()
    wordlist = []
    while True:
        line = line.strip().translate(None,(string.punctuation + '\t\r'))
        if line:
            map(lambda x:wordlist.append((x,syllables(x))),filter(None,line.split(' ')))
        try:
            line = raw_input()
        except EOFError:
            break

    findhaiku(wordlist)


if __name__ == '__main__':
    exit(main())
