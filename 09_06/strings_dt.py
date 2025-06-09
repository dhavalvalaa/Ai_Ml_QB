s = "python"

#reverse
print("reverse = ", s[::-1])

#skipping
print("skipping = ", s[::2])

a,b= 'hello i am mr.x' , 'hello to everyone'

print("modifing / rconstruct = ", a[:6] + " " + b[6:])

w="dhaval"

#palidrome
def palli(w):
    return w == w[::-1]

print(palli(w))
'''
Anagram
An anagram is when two different strings contain 
the same characters in a different order.
'''
a= 'abcd'
b='dcab'
def ana(a,b):
    # print("check this for undertandiiiingg",set(a))
    if set(a) == set(b):
        print("aana")
    # pass

ana(a,b)
'''
Isogram
An isogram is a word 
where no letter appears more than once.
'''
from collections import Counter
w = "aabcccdddddd"
# print(Counter(w))
w = 'newchar'
def iso(w):
    if len(w) == len(set(w)):
        print("isoo")
    pass

iso(w)
'''
Heterogram
A heterogram is similar to an isogram but 
applies to full sentences, meaning no letter repeats.
'''
print("----------------")
def hetero(s):
    print(len(s))
    print(len(set(s)))
    print(s.split())
    l = s.split()

    s = s.replace(" ", "")
    # w = ''
    # for i in range(len(l)):
    #     w +=  str(l[i])
    if len(s) == len(set(s)):
        print("hetero")
    pass
hetero("new strig q")
'''
Panagram
A pangram is a sentence that contains 
every letter in the alphabet at least once.'''

import string
def pana(s):
    return set(string.ascii_lowercase).issubset(set(s.lower()))
print(pana("The quick brown fox jumps over the lazy dog"))



# numeric and aplphanumeric strings

#hello