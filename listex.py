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

#------------------Exercise 8 --- START

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

#------------------Exercise 8 --- END
