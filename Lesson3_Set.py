"""Define our multi-set. Working with hash functions"""
"""Basically we create a two-dimensional array or list of lists, list with 10 lists inside"""

setsize = 10
newset= [[] for _ in range(setsize)]

"""Add an element to our set"""
def add(x):
    # if not find (x) - better way to add. that way there will be no duplicates and we have a usual set
    newset[x % setsize].append(x)
    
"""Find an element in our set"""    
def find(x):
    for now in newset[x % setsize]:
        if now == x:
            return True
    return False

"""Delete an element in our set"""
def delete(x):
    xlist = newset[x % setsize]
    for i in range(len(xlist)):
        if xlist[i] == x:
            # a,b = b,a - swap(a,b) - usual for C++
            #xlist[i], xlist[len(xlist) - 1] = xlist[len(xlist) - 1], xlist[i]
            xlist[i] = xlist[len(xlist) - 1]
            xlist.pop()
            return
"""Task 1""" 
"""Here is a sequence with len N and a number X, all numbers all positive""" 
"""We need to find two different numbers A and B in our seq, A + B = X or return (0,0)
 if there are no such numbers""" 
      
"""Solution with O(N**2) difficulty"""
def twotermswithsumx(nums, x):
    for i in range(len(nums)): # run through indexes
        for j in range(i + 1, len(nums)): # run through indexes second time, starting from the next right element to i
            if nums[i] + nums[j] == x and nums[i] != nums[j]: # compare sum of our elements with indexes i,j with number X, also compare them to each other to define that they are not equal
                return nums[i],nums[j] # finally return a pair of numbers with i and j indexes if their sum is equal to X
    return 0, 0 # if there are no such numbers return 0,0

print(twotermswithsumx([2,3,3,4,5,7,1], 6))

"""Solution with O(N) difficulty"""    
def twotermswithsumx2(nums, x):
    prevnums = set() # define a set
    for nownum in nums: # run through the numbers
        if x - nownum in prevnums: # if result of subtraction between number X and current number is in our set
            return nownum, x - nownum # we return current number and result of previous subtraction
        prevnums.add(nownum) # otherwise we add current number to our set, and back to the loop
    return 0, 0   # we return 0,0 if there are no such pair of numbers

print(twotermswithsumx2([2,3,3,4,5,7,1], 6))        
        
"""Task 2"""
"""Here is a dictionary with N words, len of each word is not greater(>) than K""" 
"""For every word(total value of words - M) in the text(len < K) one letter can be skipped"""
"""We should say for every word(with a possible skipped letter) whether it is in our dictionary or not"""     

"""Solution with O(NK**2 + M) difficulty"""
def wordsindict(dictionary,text):
    goodwords = set(dictionary) # define a set of words which were in the dictionary
    for word in dictionary: # run through the words in the dictionary
        for delpos in range(len(word)): # run through the word 
            goodwords.add(word[:delpos] + word[delpos+1:]) # add to the set concatenation of slices without delpos
    
    ans = [] # create a new list
    for word in list(text.split()): # run through the words in our text
        ans.append(word in goodwords) # if current word is in our set we add it to our list
    return ans # we return our list with words which are both in the text and in the dictionary

print(wordsindict(("Hello","OK","Sure", "Mama","Papa", "dog"),"I love my dg"))
