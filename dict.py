def histogram(s):
    d = dict()
    for c in s:
        d[c] += 1
    return d

known = {0:0, 1:1}

def fibonacci(n):
    if n in known:
        return known[n]

    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res

#------------------Exercise 1:

def creat_dic():
    fin = open('g:\py\words.txt')

    dwordlist = dict()

    for line in fin:
        dwordlist[line.strip()] = ''

    return dwordlist

"""


for word in ['aa', 'alien', 'allen', 'haa', 'zymurgy']: # try find word
    if word in dwordlist:
        print(word, 'in list', 'True')
    else:
        print(word, 'in list', 'False')

def find_rp(wordlist): # try find reverse word
    for word in wordlist:
        if word[::-1] in wordlist:
            print(word)

find_rp(dwordlist)
"""

#------------------Exercise 2:

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        inverse.setdefault(val,[]).append(key)
    return inverse
