"""RSQ Solution"""
def makeprefixsum(nums):
    prefixsum = [0] *(len(nums) + 1)
    for i in range(1, len(nums) + 1):
        prefixsum[i] = prefixsum[i-1] + nums[i-1]
    return prefixsum

print(makeprefixsum([2,3,6,8,9]))

def rsq(prefixsum, l, r):
    return prefixsum[r]-prefixsum[l]

print(rsq(makeprefixsum([2,3,6,8,9]),3,5))

"""Task1"""
"""Here is a sequence with len N and M-number of queries"""
"""Queries are - How many zeroes(0) on half-interval [L,R)"""

"""Solution 1 O(NM) difficulty"""
"""For each query run through numbers from L to R(not inclusive) and count a number of zeroes"""
def countzeroes(nums, l, r):
    cnt = 0
    for i in range(l,r):
        if nums[i] == 0:
            cnt +=1
    return cnt


"""Solution 2 O(N+M) difficulty"""
"""For each prefix we count number of zeroes on it(prefixzeroes)"""
"""That way, an answer for half-interval [L,R) will be: prefixzeroes[R] - prefixzeroes[L]"""
def makeprefixzeroes(nums):
    prefixzeroes =[0] *(len(nums) +1)
    for i in range(2, len(nums) +1):
        if nums[i-1] == 0:
            prefixzeroes[i] = prefixzeroes[i-1] + 1
        else:
            prefixzeroes[i] = prefixzeroes[i-1]
        return prefixzeroes
    
def countzeroes1(prefixzeroes, l, r):
    return prefixzeroes[r] - prefixzeroes[l]

"""Task2"""
"""Here is a sequence with len N. We need to find a number of intervals with 0-sum"""

"""Solution 1 O(N^3) difficulty"""
"""Search for all of the Beginnings and Endings for an interval and count a sum of its elements"""
def countzerosumranges(nums):
    cntranges = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums) +1):
            rangesum = 0
            for k in range(i,j):
                rangesum += nums[k]
            if rangesum == 0:
                cntranges +=1
    return cntranges


"""Solution 2 O(N^2) difficulty"""
"""Search for all of the Beginnings and will move and Ending for an inteval and count a sum of its elements"""
def countzerosumranges2(nums):
    cntranges = 0
    for i in range(len(nums)):
        rangesum = 0
        for j in range(i, len(nums)):
                rangesum += nums[j]
                if rangesum == 0:
                    cntranges +=1
    return cntranges

"""Solution 3 O(N) difficulty"""
"""Lets count a prefixsums. Same prefixsums means that the sum of the elements on interval with beginning and ending
 on positions where prefixsums is the same will be equal to zero"""
def countprefixsums(nums):
    prefixsumbyvalue = {0 : 1} # it means that sequence with sum 0 we met 1 time 
    nowsum = 0
    for now in nums:
        nowsum += now
        if nowsum not in prefixsumbyvalue:
            prefixsumbyvalue[nowsum] = 0
        prefixsumbyvalue[nowsum] +=1 # for an element in our dict with current prefixsum we raise a number of appearances by 1
    return prefixsumbyvalue

def countzerosumranges3(prefixsumbyvalue):
    cntranges = 0
    for nowsum in prefixsumbyvalue: # run through all of the prefixsums
        cntsum = prefixsumbyvalue[nowsum]
        cntranges += cntsum * (cntsum -1) // 2 # count a number of pairs with formula
    return cntranges


"""Task3"""
"""Here are sorted sequence with len N and number K. We need to find a number of pairs A,B. B-A > K"""

"""Solution 1 O(N^2) difficulty"""
"""Run through all of the pairs of numbers and check the condition"""
def cntpairswithdiffgtk(sortednums, k):
    cntpairs = 0
    for first in range(len(sortednums)):
        for last in range(first, len(sortednums)):
            if sortednums[last] - sortednums[first] > k:
                cntpairs +=1
    return cntpairs

"""Solution 2 O(N) difficulty"""
"""Take a min number and find a first suitable greater one. All of the numbers which are greater than the first suitable are suitable too.
Take as a min number the next number, and lets move a pointer of the first suitable greater one from the position where it is"""
def cntpairswithdiffgtk2(sortednums, k):
    cntpairs = 0
    last = 0
    for first in range(len(sortednums)):
        while last < len(sortednums) and sortednums[last] - sortednums[first] <=k: # conditions check goes from left to right, so if the first statement isn't true the second one won't be called
            last +=1
        cntpairs += len(sortednums) - last
    return cntpairs

"""Task4"""
"""Football player has one numerical characteristic - professionalism. A team called solid if the professionalism of one player is not greater than the sum of
professionalism of any two other players. A team consists of any number of players.
We have a sorted sequence with len N - professionalism of players. We need to find a maximum sum of professionalism for solid team"""

"""Solution 1"""
def bestteamsum(players):
    bestsum =0
    nowsum = 0
    last = 0
    for first in range(len(players)):
        while last < len(players) and (last == first or players[first] + players [first + 1] >= players[last]):
            nowsum += players[last]
            last +=1
        bestsum = max(bestsum, nowsum)
        nowsum -= players[first]
    return bestsum


"""Task5, Merge!"""
 
"""Here are two sorted sequences with len N and len M"""
"""We need to make one sorted sequence of these two"""

"""Solution 1"""
"""Lets set a pointers to the beginning of each of the sequences. Choose the one which pointed on the lower number, put this number to the result and move the pointer"""
def merge(nums1, nums2):
    merged = [0] * (len(nums1) + len(nums2))
    first1 = first2 = 0
    inf = max(nums1[-1], nums2[-1] +1)
    nums1.append(inf)
    nums2.append(inf)
    for k in range(len(nums1) + len(nums2) -2):
        if nums1[first1] <= nums2[first2]:
            merged[k] = nums1[first1]
            first1 += 1
        else:
            merged[k] = nums2[first2]
            first2 += 1
    nums1.pop()
    nums2.pop()
    
    return merged


print(merge([2,3,15,99,100,101,102,102],[66,77,78,78,79,200]))

"""Solution 2 O(N+M) difficulty"""
def merge2(nums1, nums2):
    merged = [0] * (len(nums1) + len(nums2))
    first1 = first2 = 0
    for k in range(len(nums1) + len(nums2)):
        if first1 != len(nums1) and (first2 == len(nums2) or nums1[first1] <= nums2[first2]):
            merged[k] = nums1[first1]
            first1 += 1
        else:
            merged[k] = nums2[first2]
            first2 += 1
    return merged


print(merge2([2,3,15,99,100,101,102,102],[66,77,78,78,79,200]))











