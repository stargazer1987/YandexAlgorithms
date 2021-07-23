"""Task1"""
"""Here is a string (UTF-8 format). We should find the most repeatable symbol."""
"""If we have more then one symbol which has the same number of replays we can return any of them"""

"""Solution 0"""

s = input()
print(max(map(lambda x: (s.count(x), x), s))[1])

"""Solution 1 O(N**2) difficulty and O(N) memory"""
s = input() # read a line
ans ="" # empty variable
anscnt = 0 # value 0
for i in range(len(s)): # run through the positions in string
    nowcnt = 0 # counter = 0
    for j in range(len(s)): # for each position run through the positions in string once again
        if s[i] == s[j]: # if we meet the same symbol
            nowcnt +=1 # we add 1 to our counter
    if nowcnt > anscnt: # if the value of our counter is greater than previous result
        ans =s[i] # we put our symbol to the variable
        anscnt = nowcnt # and save the number of replays for it
print(ans) # print our symbol

"""Solution 2 O(NK) difficulty and O(N+K)=O(N) memory"""
s = input() # read a line
ans ="" # empty variable
anscnt = 0 # value 0
for now in set(s): # run through the symbols in the set (no replays)
    nowcnt = 0 # counter = 0
    for j in range(len(s)): # for each symbol run through the positions in string
        if now == s[j]: # if we meet the same symbol
            nowcnt +=1 # we add 1 to our counter
    if nowcnt > anscnt: # if the value of our counter is greater than previous result
        ans = now # we put our symbol to the variable
        anscnt = nowcnt # and save the number of replays for it
print(ans) # print our symbol

"""Solution 3 O(N+K) = O(N) difficulty and O(K) memory"""
s = input() # read a line
ans ="" # empty variable
anscnt = 0 # value 0
dct = {} # create an empty dict
for now in s: # run through the symbols in the string
    if now not in dct: # if symbol is not in the dict
        dct[now] = 0 # we add this symbol to the dict with key -0
    dct[now] +=1 # we add 1 for each replay
#for key in dct: # run through the keys in dict - not necessary
    if dct[now] > anscnt: # if the value is greater then previous result
        anscnt = dct[now] # we put our symbol to the variable
        ans = now # and save the number of replays for it
print(ans) # print our symbol


"""Task2""" 
"""Sum of the sequence"""

"""Solution1"""
seq = list(map(int, input().split()))
if len(seq) == 0: # Here we don't need this special case, our program will work correctly
    print(0)
else:
    seqsum = seq[0]
    for i in range(1, len(seq)):
        seqsum +=seq[i]
    print(seqsum)
    
"""Solution2""" 
seq = list(map(int, input().split()))
seqsum = 0
for i in range(1, len(seq)):
    seqsum +=seq[i]
print(seqsum)

"""Task3""" 
"""Maximum of the sequence"""

"""Solution1"""
seq = list(map(int, input().split()))
seqmax = 0
for i in range(len(seq)):
    if seq[i]> seqmax:
        seqmax =seq[i]
print(seqmax)

"""Solution2"""
seq = list(map(int, input().split()))
seqmax = 0
if len(seq) == 0: # Here we need this special case, otherwise our program crush with empty seq
    print("-inf")
else:
    seqmax = seq[0]
    for i in range(1,len(seq)):
        if seq[i]> seqmax:
            seqmax =seq[i]
    print(seqmax)
   
   
"""Task4"""
"""Quadratic equation"""
from math import sqrt
a,b,c = list(map(int, input().split()))
if a == 0:
    if b != 0:
        print(-c/b)
    if b == 0 and c == 0:
        print("Infinite number of solutions")
else:
    d = b**2  - 4*a*c
    print(sqrt(d))
    if d == 0:
        x1 = - b/(2*a)
        print(x1)
    elif d > 0:
        x1 = (-b -sqrt(d))/(2*a)
        x2 = (-b +sqrt(d))/(2*a)
        if x1 < x2:
            print(x1,x2)
        else:
            print(x2,x1)
           
