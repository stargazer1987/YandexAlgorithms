def countsort(seq):
    minval = min(seq) # find minimum in our seq
    maxval = max(seq) # find maximum in our seq
    k = (maxval - minval + 1) # find k as a result of subtraction between max and min in our seq +1
    count = [0] * k # create an array with 0's multiply k-times
    for now in seq: # for each element in our seq
        count[now - minval] +=1 # we add 1 to the block in our array with number equal to the result of subtraction between current element and minimum
    nowpos = 0 # set a new variable with value 0
    for val in range(0, k): # run through values of our blocks in array
        for i in range(count[val]): # run through indexes of blocks with values
            seq[nowpos] = val + minval # sort an elements, add a value of the block to the minimum
            nowpos += 1 # change position +1
    return seq
            
print (countsort([23,15,8,99,155,6,7,11,7]))
 
            
"""Task 1"""
"""Here are two numbers X, Y without 0 at first position"""
""" We need to check is it possible to get a second number from the first one, making changes of num positions"""


def isdigitpermutation(x,y):
    def countdigits(num):
        digitcount = [0] *10 # we make an array with 10 zeros
        while num > 0: # while our num is greater (>1) than 0
            lastdigit = num % 10 # we save a last number of it in the the variable (modulo) 
            digitcount[lastdigit] +=1 # add an 1 to to the box in the array with index of our variable
            num //=10 # an a new number will be a result of the float division by 10
        return digitcount # we return an array
    
    digitsx = countdigits(x) # count a number of occurrences for each digit in our first number
    digitsy = countdigits(y) # count a number of occurrences for each digit in our second number
    for digit in range(10): # run through each box in our array
        if digitsx[digit] != digitsy[digit]: # if number of occurrences for each digit in two numbers is not equal
            return False # we return false
    return True # else we return true


print (isdigitpermutation(2021,1220))  

"""Task 2"""
"""We've got a chess board with len NxN with M-number of rooks (rook can beat all squares horizontally or vertically till the nearest occupied)"""
""" We need to define how many pairs of rooks can beat each other. Rooks are set with two numbers I and J which are their coordinates"""
""" 1 <= N <= 10**9, 0 <= M <= 2 * 10**5"""

"""Solution"""
"""For each occupied horizontally and vertically square we will save a number of rooks on them"""
"""Number of pairs in horizontal or vertical is equal to the number of rooks - 1"""  
"""Count a total sum by adding all pairs in horizontal and vertical""" 

def countbeatingrooks(rookcoords):
    def addrook(roworcol, key):
        if key not in roworcol:
            roworcol[key] = 0
        roworcol[key] +=1
    
    def countpairs(roworcol):
        pairs = 0
        for key in roworcol:
            pairs += roworcol[key] -1
        return pairs
    
    rooksinrow = {}
    rooksincol = {}
    for row, col in rookcoords:
        addrook(rooksinrow, row)
        addrook(rooksincol, col)
    return countpairs(rooksinrow) +countpairs(rooksincol)

print (countbeatingrooks([(3,4),(3,5),(4,3),(6,8),(10,10)]))
        
""" If we need to count a number of queens, their coordinates can be set by I+J and I-J in diagonal""" 

"""Task 3"""
"""Here is a string S"""
"""We need to receive a histogram as an output""" """Codes of symbols are sorted"""
""" S = Hello, world! -->""" 

"""     #"""
"""     ##"""
"""##########"""
""" !,Hdelorw """

"""Solution"""
"""For each symbol in the dictionary we count how many times it meets"""
"""Find the most most frequent one and run through the amount from this number till the 1"""
"""Run through all sorted keys and if the number of keys is greater than our counter - output an #"""

def printchart(s):
    symcount = {}
    maxsymcount = 0
    for sym in s:
        if sym not in symcount:
            symcount[sym] = 0
        symcount[sym] += 1
        maxsymcount = max(maxsymcount, symcount[sym])
    sorteduniqsyms = sorted(symcount.keys())
    for row in range(maxsymcount, 0, -1):
        for sym in sorteduniqsyms:
            if symcount[sym] >= row:
                print('#', end ='')
            else:
                print(' ', end ='')
            print()
    print(''.join(sorteduniqsyms))

printchart("Hello world!")

"""Task 4"""
"""Group a words by the same letters"""
"""Sample Input: ["eat", "tea", "tan", "ate", "nat", "bat"]"""
"""Sample Output: [["ate", "eat", "tea",], ["nat", "tan"], ["bat"]]"""
  
"""Solution 1"""    
def groupwords(words):
    groups = {}
    for word in words:
        sortedword = "".join(sorted(word)) ### see below
        if sortedword not in groups:
            groups[sortedword] = []
        groups[sortedword].append(word)
    ans = []
    for sortedword in groups:
        ans.append(groups[sortedword])
    return ans

print(groupwords(["eat", "tea", "tan", "ate", "nat", "bat"]))

#  We suppose if len of word will be greater than N, sort will take O(NlogN)
#  Amount of different chars in  word is K <=N, We can count amount of each one for O(N) difficulty
#  And then sort for O(KlogK), theoretically...

"""Solution2"""
def groupwords2(words):
    def keybyword(word):
        return "".join(sorted(word)) # it could work slow on practice
    
    groups = {}
    for word in words:
        groupkey = keybyword(word)
        if groupkey not in groups:
            groups[groupkey] = []
        groups[groupkey].append(word)
    ans = []
    for groupkey in groups:
        ans.append(groups[groupkey])
    return ans

print(groupwords2(["eat", "tea", "tan", "ate", "nat", "bat"]))

"""Solution3"""
# Works slow. Kind of weird optimization ;))
def groupwords3(words):
    def keybyword(word):
        symcnt = {}
        for sym in word:
            if sym not in symcnt:
                symcnt[sym] = 0
            symcnt[sym] += 1
        lst = []
        for sym in sorted(symcnt.keys()):
            lst.append(sym)
            lst.append(str(symcnt[sym]))
        return "".join(lst)  # here we have a list like a3b1 from aaba
    
    groups = {}
    for word in words:
        groupkey = keybyword(word)
        if groupkey not in groups:
            groups[groupkey] = []
        groups[groupkey].append(word)
    ans = []
    for groupkey in groups:
        ans.append(groups[groupkey])
    return ans
    
print(groupwords3(["eat", "tea", "tan", "ate", "nat", "bat"]))