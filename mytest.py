def histogram(s):
    d = dict()
    for c in s:
        d[c] = 1 + d.get(c,0)
    return d

h = histogram('windows')
h
