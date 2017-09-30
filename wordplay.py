def wlen(word):
    counter = 0
    for l in word:
        if l != ' ':
            counter += 1
    return counter

def w_no_e(word):
    for l in word:
        if l == 'e':
            return False
    return True

def has_no_e(fin):
    counter_all = 0.0
    counter_no_e = 0.0
    for line in fin:
        counter_all += 1
        word = line.strip()
        if w_no_e(word):
            counter_no_e += 1
            print(word)
    ratio = counter_no_e / counter_all
    print(counter_all)
    print(counter_no_e)
    print(ratio)

def avoids(word, string):
    for l_w in word:
        for l_s in string:
            if l_w == l_s:
                 return False
    return True

def is_in_string(letter, string):

    counter = 0

    for w in string:
        if letter == w:
            counter += 1

    if counter > 0:
        return True
    else:
        return False

def reduce_dup_letter(word):
    reduced = ''
    for l in word:
        if l not in reduced:
            reduced = reduced + l
    return reduced

def use_only(word, string):

    counter = 0

    for l_w in word:
        if is_in_string(l_w, string):
            counter += 1

    if counter == len(word):
        return True
    else:
        return False


def use_all(word, string):

    counter = 0

    p_word = reduce_dup_letter(word)

    for l_w in p_word:
        if is_in_string(l_w, string):
            counter += 1

    if counter == len(p_word) and counter >= len(string):
        return True
    else:
        return False

def is_abecedarian(word):

    index = 0


    while index < (len(word) - 1):
        if word[index] >= word[index+1]:
            return False

        index += 1

    return True

fin = open('words.txt')

for line in fin:
    file_word = line.strip()
    if is_abecedarian(file_word):
        print(file_word)

"""
f_string = input('Input forbidden letter(s):\n')

fin = open('words.txt')

for line in fin:
    file_word = line.strip()
    if use_only(file_word, f_string):
        print(file_word)
"""

"""
all_counter = 0

counter = 0

for line in fin:
    all_counter += 1
    word = line.strip()
    if avoids(word, my_s):
        counter += 1

print(counter, all_counter)
"""

#has_no_e(fin)

#    for line in fin:
#        word = line.strip()
#        if wlen(word) > 20:
#            print(word)

#def printwlen(fin):
#    print('in_printwlen')
#    for line in fin:
#        word = line
#        if wlen(word) > 20:
#            print(word)
