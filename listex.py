from random import *

t = [[1, 2], [3], [4, 5, 6]]
t1 = [1,2,3,4,5,6,7,8,9,10]
t2 = [1,2,3,4,5,5]

word1 = 'asdf'
word2 = 'asddddsdaf'

def nested_sum(t):
    s = 0
    for n in t:
        if isinstance(n, list):
            for n1 in n:
                s = s + n1
        else:

            s = s + n
    return s

def middle(t):
    t1 = []
    t1 = t[1:len(t)-1]
    return t1

def chop(t):
    del t[0]
    del t[len(t)-1]

def is_sorted(t):
    x = 0
    while x < len(t) - 1:
        if t[x] > t[x+1]:
            return False
        x = x + 1
    return True

def is_anagram(w1, w2):

    n = 0

    for l1 in w1:
        p = 0
        for l2 in w2:
            if l1 == l2:
                n += 1
            else:
                p += 1
        if p == len(w2):
            return False

    if n == len(w2):
        return True
    else:
        return False

def has_duplicates(t):
    for n1 in t:
        x = 0
        p = 0
        while x < len(t):
            print(x)
            if n1 == t[x]:
                p += 1
            x += 1
        if p >=2:
            return False
    return True

#------------------Exercise 8:

def initialization_bd(bd, t):
    x = 0
    while x < t:
        bd.append(randint(1,366))
        x += 1

def odd_samebd():
    bd = []
    initialization_bd(bd, 23)
    for n in bd:
        x = 0
        p = 0
        while x < len(bd):
            if n == bd[x]:
                p += 1
            x += 1
        if p >= 2:
            return True
    return False

def bd_paradox(t):
    n = 0
    x = 0
    while n < t:
        if odd_samebd():
            x += 1
        n += 1
    print(x)

#------------------Exercise 9:
def creat_wlist():
    fin = open('g:\py\words.txt')

    wordlist = []

    for line in fin:
        wordlist.append(line.strip())

    return wordlist
    #    wordlist = wordlist + [line.strip()]

#------------------Exercise 10:
"""
def in_bisect(w):
    quot = 0
    rem = 0
    startp = 0
    endp = 0
    n = 0 #debug
    sect = len(wordlist)

    print(len(wordlist))

    while quot != 1:
        quot, rem = divmod(sect, 2)
        endp = endp + quot + rem
        sect = sect - quot - rem
        exit = 0
        n = n + 1 #debug
        print(startp, endp, sect, n) #debug
    #    search_list = wordlist[startp:endp]
        if w <= wordlist[endp]:
            for x in range(startp,endp):
                print(x) #debug
                if w == wordlist[x]:
                    print(wordlist[x])
                    print(x)
                    exit = 1
                    break
        if exit == 1:
            break
        startp = endp
    return False

in_bisect('ice')
"""

word_list = creat_wlist()

def in_bisect(word, word_list):

    i = len(word_list) // 2

    if i == 0:
        return False

    if word == word_list[i]:
        return True

    if word < word_list[i]:
        return in_bisect(word,word_list[:i])

    if word > word_list[i]:
        return in_bisect(word,word_list[i+1:])
    
for word in ['aa', 'alien', 'allen', 'zymurgy']:
        print(word, 'in list', in_bisect(word_list, word))
