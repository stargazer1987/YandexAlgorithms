"""Examples of left and right binsearch"""
def lbinsearch(l, r, check, checkparams):
    while l < r:
        m = (l + r)//2
        if check(m, checkparams):
            r = m
        else:
            l = m + 1
    return l

def rbinsearch(l, r, check, checkparams):
    while l < r:
        m = (l + r + 1)//2
        if check(m, checkparams):
            l = m
        else:
            r = m - 1
    return l

"""Task1"""
"""The board of school consists of parents, teachers and pupils. The number of parents should be not lower than 1/3 of total number of members.
At the current moment the board consists of N-number of people, and K-number parents are there"""
"""Define how many parents should we add to the board for our condition will be true(not lower 1/3)"""

"""Solution"""
def lbinsearch2(l, r, check, checkparams):
    while l < r:
        m = (l + r)//2
        if check(m, checkparams):
            r = m
        else:
            l = m + 1
    return l

def checkendownment(m,params):
    n,k = params
    return (k + m) *3 >= n + m

"""Task2"""
"""Yuriy is going to prepare for a job interview. He choose N-number of tasks. On the first day he solve K-number of task.
Each next day he solve one task more than previous day. Define how many days Yuriy will spend for preparation"""

"""Solution"""
def lbinsearch3(l, r, check, checkparams):
    while l < r:
        m = (l + r)//2
        if check(m, checkparams):
            r = m
        else:
            l = m + 1
    return l

def checkendownment2(days,params):
    n,k = params
    return (k + (k+ days - 1)) * days // 2 >= n

"""Task3"""
"""Mikhail gives lectures. There is a board size of W*H sentimeters. He need to place N-number of square stickers with cheat sheets on it. The len of sides should be int numbers"""
"""Define a max len of side for sticker, in the way that all stickers will placed on the board"""

"""Solution"""
def rbinsearch2(l, r, check, checkparams):
    while l < r:
        m = (l + r)//2
        if check(m, checkparams):
            r = m
        else:
            l = m + 1
    return l

def checkstickers(size,params):
    n,w,h = params
    return (w//size) * (h//size) >= n


"""Task4"""
"""Here are sorted and not descending sequence of N numbers and number X"""
"""We should define index of the first element which is greater or equal to X. 
If there is no such number we should return number N"""

"""Solution"""
def checkisge(index,params):
    seq, x = params
    return seq[index] >=x

def findfirstge(seq,x):
    ans = lbinsearch(0, len(seq) -1, checkisge,(seq,x))
    if seq[ans] < x:
        return len(seq)
    return ans

"""Task5"""
"""Here are sorted and not descending sequence of N numbers and number X"""
"""We should define how many times we meet the number X in the sequence"""

"""Solution"""

def checkisgt2(index,params):
    seq, x = params
    return seq[index] >x

def checkisge2(index,params):
    seq, x = params
    return seq[index] >=x

def findfirst2(seq,x,check):
    ans = lbinsearch(0, len(seq) -1, check,(seq,x))
    if not check(ans, (seq, x)):
        return len(seq)
    return ans

def countx2(seq, x):
    indexgt = findfirst2(seq, x, checkisgt2)
    indexge = findfirst2(seq, x, checkisge2)
    return indexgt - indexge

"""Task6"""
"""We have the interest rate on a loan (X% per year). Credit period - N-months and Loan sum - M-rubles"""
"""Define a sum of annuity monthly payment """

"""Solution"""
"""At first lets find a monthly perc"""
def checkmonthlyperc(mperc, yperc):
    msum = 1 + mperc / 100
    ysum = 1 + yperc / 100
    return msum ** 12 >= ysum

def fbinsearch(l, r, eps, check, checkparams):
    while l + eps < r:
        m = (l + r) / 2
        if check(m, checkparams):
            r = m
        else:
            l =m
    return l

x = 12
eps = 0.0001
mperc = fbinsearch(0, x, eps, checkmonthlyperc,x)

"""Lets find a loan sum with binsearch, and as a check we will simulate a process of payment. And reduce the loan body by the result of subtraction between loan payment sum and monthly percentage """
def checkcredit(mpay, params):
    periods, creditsum, mperc = params
    for i in range(periods):
        percay = creditsum * (mperc / 100)
        creditsum -= mpay - percay
    return creditsum <=0

def fbinsearch2(l, r, eps, check, checkparams):
    while l + eps < r:
        m = (l + r) / 2
        if check(m, checkparams):
            r = m
        else:
            l =m
    return l


eps = 0.01
m = 10000000
n = 300 # 25 years
monthlypay = fbinsearch2(0, m, eps, checkcredit,(n, m, mperc))
print(monthlypay)


"""Task 7"""
"""Cyclists which are participate in the bicycle race at some moment in time which called primary found their selves in some places which far from the start position on x1,x2,...xn meters (n - total number of cyclists, not greater than 100 000)
Each cyclist has his own constant speed V1, V2, .... Vn meters per second. All cyclists move into the one direction. We need to define the moment of time when the distance between the leader and the last one will be the shortest"""

"""Solution"""
"""Define a function dist(t) which with O(N) difficulty will define a distance between the leader and the last cyclist at the moment of time t.
If dist(t+eps)>dist(t), than our function is rasing and we need to move our left border of the search, otherwise - move right border"""

def dist(t,params):
    x, v = params
    minpos = maxpos = x[0] +v[0]*t
    for i in range(1,len(x)):
        nowpos = x[i] +v[i]*t
        minpos = min(minpos,nowpos)
        maxpos = max(maxpos,nowpos)
    return maxpos - minpos

def checkasc(t,eps,params):
    return dist(t + eps,params) >= dist(t, params)

def fbinsearch3(l,r,eps,checkasc,params):
    while l+ eps < r:
        m =(l + r)/2
        if checkasc(m,eps,params):
            r=m
        else:
            l =m
    return l












