"""Task1"""
"""Web-site was visited by N-number of visitors"""
"""For each visitor we know TimeIn, TimeOut. We suppose that visitor was at the web-site from TimeIn till TimeOut inclusively"""
"""Lets count max number of visitors that were online simultaneously"""

"""Solution"""
"""For each visitor we create two events - enter(in) and exit(out)"""
"""Every event is a pair, where the first number is time of the event, second one is the type of the event"""

def maxvisitorsonline(n, tin, tout):
    events = []
    for i in range(n):
        events.append((tin[i], -1))# man in, and -1 is lower(< 1) - (priority 1)
        events.append((tout[i], 1))# man out, and 1 is greater(> -1) - (priority 2)
    events.sort()
    online = 0
    maxonline = 0
    for event in events:
        if event[1] == -1: # if priority of event is 1(lowest number here)
            online += 1
        elif event[1] == 1:
            online -= 1
        maxonline = max(online, maxonline)
    return maxonline

print(maxvisitorsonline(5,[7.15,7.20,9.00,11.00,11.30],[9.00,9.17,11.25,16.00,17.00]))

"""Task2"""
"""Web-site was visited by N-number of visitors"""
"""For each visitor we know TimeIn, TimeOut. We suppose that visitor was at the web-site from TimeIn till TimeOut inclusively"""
"""We should define time interval when at least one visitor were online"""

"""Solution"""
"""If we came to the event with a positive counter of people number, then there was someone online before current event and previous one"""
"""We will add a time interval between these events to the answer"""

def timewithvisitors(n, tin, tout):
    events = []
    for i in range(n):
        events.append((tin[i], -1))# man in, and -1 is lower(< 1) - (priority 1)
        events.append((tout[i], 1))# man out, and 1 is greater(> -1) - (priority 2)
    events.sort()
    online = 0
    notemptytime = 0
    for i in range(len(events)):
        if online > 0:
            notemptytime += events[i][0] - events[i-1][0]
        elif events[i][1] == -1:
            online += 1
        else:
            online -= 1
    return notemptytime

print(timewithvisitors(5,[7.15,7.20,9.00,11.00,11.30],[9.00,9.17,11.25,16.00,17.00]))

"""Task3"""
"""Web-site was visited by N-number of visitors"""
"""For each visitor we know TimeIn, TimeOut. We suppose that visitor was at the web-site from TimeIn till TimeOut inclusively"""
"""Boss visited the web-site M-times, at time-moments "Boss" and watched how many people were online. Boss visits are sorted by time"""
"""We should define which values of the counter of people online he saw."""

"""Solution"""
"""Lets create a new event - entrance of the Boss and if this event happens we will save a current number of visitors online"""

def bosscounters(n, tin, tout, m, tboss):
    events = []
    for i in range(n):
        events.append((tin[i], -1))# man in, and -1 is lower(< 1) - (priority 1)
        events.append((tout[i], 1))# man out, and 1 is greater(> -1) - (priority 3)
    for i in range(m):
        events.append((tboss[i], 0))# boss in, and 0 is before man out and after man in - (priority 2)
    events.sort()
    online = 0
    bossans = []
    for i in range(len(events)):
        if events[i][1] == -1:
            online += 1
        elif events[i][1] == 1:
            online -= 1
        else:
            bossans.append(online)
    return bossans

print(bosscounters(5,[7.15,7.20,9.00,11.00,11.30],[9.00,9.17,11.25,16.00,17.00],3,[7.45,11.27,14.00]))



"""Task 4"""
"""There are N-number of parking places on the parking in the shopping center(numbered from 1 to N)"""
"""There were M-number of cars during the day. Some of them are long-one and they occupied some of the parking places which are next to each other"""
"""For each car we know TimeIn and TimeOut, and two numbers - start number and the last number of parking place which were occupied"""
"""If in some moment in time one car moved from the parking place, than we suggest that parking place is empty and at the same moment in time it can be occupied by another car"""
"""We should define if there was a time moment when all of the parking places were occupied"""

"""Solution"""
"""Our events are - car arrival and car departure. Departure should be before arrival! We will hold an occupied parking places. And if after some event counter is equal to N, then there were such moments when all of the parking places were occupied """

def isparkingfull(cars, n):
    events = []
    for car in cars:
        timein, timeout, placefrom, placeto = car
        events.append((timein, 1, placeto - placefrom +1))
        events.append((timeout, -1, placeto - placefrom +1))
    events.sort()
    occupied = 0
    for i in range(len(events)):
        if events[i][1] == -1:
            occupied -= events[i][2]
        elif events[i][1] == 1:
            occupied += events[i][2]
        if occupied == n:
            return True
    return False


print(isparkingfull(([7.15,18.00,1,2],[11.00,11.45,3,3],[11.30,14.00,4,5],[7.00,9.15,5,5],[16.00,18.45,4,4]),5))

"""Task 5"""
"""There are N-number of parking places on the parking in the shopping center(numbered from 1 to N)"""
"""There were M-number of cars during the day. Some of them are long-one and they occupied some of the parking places which are next to each other"""
"""For each car we know TimeIn and TimeOut, and two numbers - start number and the last number of parking place which were occupied"""
"""If in some moment in time one car moved from the parking place, than we suggest that parking place is empty and at the same moment in time it can be occupied by another car"""
"""We should define if there was a time moment when all of the parking places were occupied. Also we should define min number of cars which occupied all of the parking places"""
"""If there is no such moment - we should return M+1"""

"""Solution"""
"""Lets add one more counter for number of cars. And when all parking places are occupied we will refresh a min number of cars"""

def mincarsonfullparking(cars, n):
    events = []
    for car in cars:
        timein, timeout, placefrom, placeto = car
        events.append((timein, 1, placeto - placefrom +1))
        events.append((timeout, -1, placeto - placefrom +1))
       
    events.sort()
    print(events)
    occupied = 0
    nowcars = 0
    mincars = len(cars) + 1
    for i in range(len(events)):
        if events[i][1] == -1:
            occupied -= events[i][2]
            nowcars -= 1
        elif events[i][1] == 1:
            occupied += events[i][2]
            nowcars += 1
        if occupied == n:
            mincars = min(mincars,nowcars)
    return mincars


print(mincarsonfullparking(([7.15,18.00,1,2],[11.00,11.45,3,3],[11.30,14.00,4,5],[7.00,9.15,5,5],[16.00,18.45,4,4]),5))

"""Task 6"""
"""There are N-number of parking places on the parking in the shopping center(numbered from 1 to N)"""
"""There were M-number of cars during the day. Some of them are long-one and they occupied some of the parking places which are next to each other"""
"""For each car we know TimeIn and TimeOut, and two numbers - start number and the last number of parking place which were occupied"""
"""If in some moment in time one car moved from the parking place, than we suggest that parking place is empty and at the same moment in time it can be occupied by another car"""
"""We should define if there was a time moment when all of the parking places were occupied. Also we should define min number of cars which occupied all of the parking places"""
"""Also we should define numbers of these cars in a priority they were specified in the list. If there is no such moment when all parking spaces were occupied - we should return an empty list"""

"""Solution"""
"""Lets add a number of car to the events. If there is a new minimum, we just copy a current state to the answer """


def mincarsonfullparking2(cars, n):
    events = []
    for i in range(len(cars)):
        timein, timeout, placefrom, placeto = cars[i]
        events.append((timein, 1, placeto - placefrom +1, i))
        events.append((timeout, -1, placeto - placefrom +1, i))
    events.sort()
    occupied = 0
    nowcars = 0
    mincars = len(cars) + 1
    carnums = set()
    bestcarnums = set()
    for i in range(len(events)):
        if events[i][1] == -1:
            occupied -= events[i][2]
            nowcars -= 1
            carnums.remove(events[i][3])
        elif events[i][1] == 1:
            occupied += events[i][2]
            nowcars += 1
            carnums.add(events[i][3])
        if occupied == n and nowcars < mincars:
            bestcarnums = carnums.copy()
            mincars = nowcars
    return sorted(bestcarnums)


print(mincarsonfullparking2(([7.15,18.00,1,2],[11.00,11.45,3,3],[11.30,14.00,4,5],[7.00,9.15,5,5],[16.00,18.45,4,4]),5))

"""Solution 2, Effective"""

def mincarsonfullparking3(cars,n):
    events = []
    for i in range(len(cars)):
        timein, timeout, placefrom, placeto = cars[i]
        events.append((timein, 1, placeto - placefrom +1, i))
        events.append((timeout, -1, placeto - placefrom +1, i))
    events.sort()
    occupied = 0
    nowcars = 0
    mincars = len(cars) + 1
    for i in range(len(events)):
        if events[i][1] == -1:
            occupied -= events[i][2]
            nowcars -= 1
        elif events[i][1] == 1:
            occupied += events[i][2]
            nowcars += 1
        if occupied == n and nowcars < mincars:
            mincars = nowcars
    carnums = set()
    nowcars = 0
    for i in range(len(events)):
        if events[i][1] == -1:
            occupied -= events[i][2]
            nowcars -= 1
            carnums.remove(events[i][3])
        elif events[i][1] == 1:
            occupied += events[i][2]
            nowcars += 1
            carnums.add(events[i][3])
        if occupied == n and nowcars == mincars:
            return sorted(carnums)
    return set()

print(mincarsonfullparking3(([7.15,18.00,1,2],[11.00,11.45,3,3],[11.30,14.00,4,5],[7.00,9.15,5,5],[16.00,18.45,4,4]),5))
