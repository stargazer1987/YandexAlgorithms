seq1 = [2,7,8,0,3,5,15,7,0,5,15,10,11]
print ("The length of a seq: ", len(seq1))
 
for i in range(len(seq1)-1,-1,-1):
    print ("pos:", i, "number:", seq1[i])
    if seq1[i] == 2:
        print ("Bingo!")
    else:
        print ("There is no such number!")

"""Linear Search"""

"""Task1"""
"""Here is a sequence with length N, find a first(left)
 position of x in it"""
 
def findx(seq, x):
    for i in range(0,len(seq)-1): # run through the indexes from 0! till the end
        ans = -1 # put some value to make a check (to be sure that we meet an element first time)
        if ans == -1 and seq[i] == x: # if we meet it first time and the element is the one we search for
            ans = i # put an index of the element into the answer
            return ("pos:", ans) # return position

print(findx([2,7,8,0,3,5,15,7,0,5,15,10,11],5))


"""Task2"""
"""Here is a sequence with length N, find a last(right)
 position of x in it"""
 
def findrightx(seq, x):
    for i in range(len(seq)-1, 0, -1):# run through the indexes from the end to 0!
        ans = -1 # put some value to make a check (to be sure that we meet an element first time)
        if ans == -1 and seq[i] == x: # if we meet it first time and the element is the one we search for
            ans = i # put an index of the element into the answer
            return ("pos:", ans) # return position
        

print(findrightx([2,7,8,0,3,5,15,7,0,5,15,10,11],7))

"""Task3"""
"""Find a maximum in a sequence with length N(N>0)"""

def findmax(seq):
    ans = 0 # put an index of max element
    for i in range(1,len(seq)): # run through the indexes from 1 till the end
        if seq[i] > seq[ans]: # compare current element and best(max)
            ans = i # put an index of new max element(rewrite)
    return seq[ans] # return a max element

print(findmax([2,7,8,0,3,5,15,7,0,5,15,10,11]))

"""Task4"""
"""Here is a sequence with length N(N>1)"""
"""Find a second maximum(which will be a maximum if we delete one maximum!)"""

def findmax2(seq):
    max1 = max(seq[0],seq[1]) # find a max from elements on indexes 0,1 and set a value to variable max1
    max2 = min(seq[0],seq[1]) # find a min from elements on indexes 0,1 and set a value to variable max2
    for i in range(2,len(seq)): # run through the indexes from 2 till the end
        if seq[i] > max1: # compare current element with value of max1, and if it is greater (>) than max1
            max2 = max1 # set a value of max1 to variable max2 then
            max1 = seq[i] # set a value of current element to variable max1
        elif seq[i] > max2: # also if value of current element is greater (>) than value of variable max2
                max2 = seq[i] # set a value of current element to variable max2
    return max2 # return value of variable max2
    
print(findmax2([2,7,8,0,3,5,15,16,16,7,0,5,15,10,11]))    
    
"""Task5"""
"""Here is a sequence with length N"""
"""Find a minimum even number or return -1 if there is no such number"""

def findmineven(seq):
    ans = -1 # put some value to make a check (to be sure that we meet an element first time)
    """flag = False""" # also possible and better way, create a boolean variable
    for i in range(len(seq)): # run through the elements
        if seq[i]%2 == 0 and (ans == -1 or seq[i] < ans): # or use this statement - (not flag or seq[i] < ans): # if modulo = 0 and also if we meet an element first time or value of element is lower (<) than value in variable ans
            ans = seq[i] # set a value of element to variable ans
            #and also this statement - (flag = True) # change a value of boolean variable to True
    return ans # return value of variable ans
    
print(findmineven([7,1,3,5,15,7,16,1,5,15,11]))    

"""Task6"""
"""Here is a sequence of words"""
"""Return all the shortest ones via space"""
def shortwords(words):
    minlen = len(words[0]) # set a value of length of first element(0 index) to variable minlen
    for word in words: # run through elements
        if len(word) < minlen: # if length of current element is lower (<) than value of variable minlen then
            minlen = len(word) # set a value of length of current element to variable minlen
            ans = [] # set a value of empty list[] to variable ans
    for word in words: # run through elements second time
        if len(word) == minlen: #if length of current element is equal to the value of variable minlen then
            ans.append(word) # append(add) current element to the list[] ans
    return " ".join(ans) # return the list[] ans with elements join via space

print(shortwords(["baba","ba","la","lollo","no","yes","go"]))


"""Task7"""
""" Pitecraft! We have got an island which is made of blocks 1x1 with different height of columns. Outside there is the sea."""
""" The rain fell down, and after it all of our lowlands are full of water. Excessive water flows directly to the sea, water level stays the same """
""" Find a number of blocks which consists of the water"""
def isleflood(h):
    maxpos = 0 # assume that height of the first element is max, and set it's index 0 to the variable maxpos
    for i in range(len(h)):# run through the indexes of all elements(blocks)
        if h[i] > h[maxpos]:# if value of the current element is greater (>) than value of element with index maxpos(0 index first turn):
            maxpos = i # rewrite the index of max element, and set to index of current element
    ans = 0 # set a value (0) to new variable answer (here we are collecting blocks of water)
    nowm = 0 # set a value (0) - to new variable nowm (new maximum)
    for i in range(maxpos): # run through the indexes of all elements from the left till our maxpos(index of max element)
        if h[i] > nowm: # if value of the current element is greater (>) than value of element nowm(0 - first turn):
            nowm = h[i] # set a value of current element to the variable nowm
        ans += nowm - h[i] # add to the total value of blocks of water(variable ans) the difference between nowm(new maximum) and current element
    nowm = 0 # once again set a value (0) - to new variable nowm (new maximum)
    for i in range(len(h)-1,maxpos,-1):# run through the indexes of all elements from right till our maxpos(index of max element)
        if h[i] > nowm: # if value of the current element is greater (>) than value of element nowm(0 - first turn):
            nowm = h[i] # set a value of current element to the variable nowm
        ans += nowm - h[i] # add to the total value of blocks of water(variable ans) the difference between nowm(new maximum) and current element
    return ans # return value of total blocks of water

print(isleflood([7,1,3,5,15,7,16,1,5,15,11]))

"""Task 8"""
""" RLE. Here is a string of letters A-Z. It can be empty"""
""" We need to write a function which will return the string without duplicates, and replace them with a values of total number of duplicates for each char!"""
""" At first, let's see how to solve an easier problem, We just want to replace duplicates"""
def easypeasy(s):
    lastsym = s[0] #set a char with index 0 to a variable lastsym
    ans = [] # set a value of empty list to a variable ans
    for i in range(1,len(s)): # run through the indexes of char
        if s[i] != lastsym: # if current char not equal to our last char saved in variable lastsym then
            ans.append(lastsym) # append(add) current char to the list[] ans
            lastsym = s[i] # set current char as lastsym
    ans.append(lastsym) # add lastsym to the result in list[] ans       
    return "".join(ans) #concatenate chars without space
            
print(easypeasy("AAAoooooEEEjjjKKlolOKoooKK")) 

"""This is our solution for general case"""

def rle(s):
    def pack(s, cnt):
        if cnt > 1:
            return s + str(cnt)
        return s
    lastsym = s[0] #set a char with index 0 to a variable lastsym
    lastpos = 0 #set a position of a char as 0
    ans= [] # set a value of empty list to a variable ans
    for i in range(1,len(s)):# run through the indexes of char
        if s[i] != lastsym: # if current char not equal to our last char saved in variable lastsym then
            ans.append(pack(lastsym,i-lastpos))# we call a function pack and add a result of it to the list[] ans
            lastpos = i # set an index of current char as lastpos
            lastsym = s[i] # set current char as lastsym
    ans.append(pack(s[lastpos],len(s)-lastpos)) # add call a function pack and add a result of it to list[] ans 
    return "".join(ans)  #concatenate chars without space
"""How pack function is working here. First time we put as arguments lastsym on first place and result of subtraction between current index(i)
 and index of last position as a second argument. If this result is greater (>) than 1 we return lastsym + string value of previous subtraction (this result). If it is not true, we return lastsym"""
"""Second time after the loop we call this function again. And put as arguments a char with index of lastpos at first place, and as a second argument we put the result of subtraction between value of len(s)
 and index of last position. That way we check if lastsym has duplicates and if it is so, we add a number of them to lastsym or just return lastsym"""    
    
print(rle("AAAoooooEEEjjjKKlolOKoooKK")) 
