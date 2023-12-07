def findMidTime(time:int, distance:int, rate:int = 1 ):
    mid = findMaxDistance(time)

    r = mid
    while calcDistance(r,time) > distance and r <= time:
        r+=1
    l = mid
    while calcDistance(l,time) > distance and l >= 0:
        l -= 1
    return l,r

def findLengthTuple(input:tuple)-> int:
    return input[1]-input[0]-1

def calcDistance(press:int,time:int,rate:int=1)->int:
    speed = press*rate
    travelTime = time-press
    return speed*travelTime
    #press*rate (time-press) => time*pres*rate - press**2 *rate =d/dpress=> time*rate-2*press*rate 

def calcDdtDistance(press:int,time:int,rate:int=1)->int:
    return time*rate-2*press*rate

def findMaxDistance(time:int,rate:int=1)->int:
    l,r = 1, time

    while l < r:
        press = (r-1)//2 + l
        ddt = calcDdtDistance(press,time)

        if ddt == 0 or abs(ddt) == 1:
            return press
        elif ddt < 0:
            r = press -1
        else:
            l = press+1


    return press

def readlineNumbers(s:str)->list:
    import re
    return [int(n) for n in list(re.findall('\d+',s))]
def readlineNumbers2(s:str)->list:
    import re
    sol = ''
    for num in list(re.findall('\d+',s)):
        sol += num
    return int(sol)

def tests():
    time, distance = 7, 9
    assert(calcDistance(3,7)==12)

    assert(findMidTime(7,9)==(1,6))
    assert(findLengthTuple(findMidTime(7,9))==4)
    assert(findLengthTuple(findMidTime(15,40))==8)
    assert(findLengthTuple(findMidTime(30,200))==9)
    # for i in range(7):
        # print(i,calcDistance(i,7),calcDdtDistance(i,7))

    pass

def part1():
    with open('input.txt') as f:
        input = []
        for line in f:
            input.append(readlineNumbers(line))
        sol = 1
        for idx in range(len(input[0])):
            sol *= findLengthTuple(findMidTime(input[0][idx],input[1][idx]))
    return sol

def part2():
    with open('input.txt') as f:
        input = []
        for line in f:
            input.append(readlineNumbers2(line))
        sol = findLengthTuple(findMidTime(input[0],input[1]))
    return sol
def main():

    import timeit
    n = 100
    result = timeit.timeit(part1,globals=globals(), number = n)
    print("Part 1:",part1())
    print("Average Runtime:",result/n)

    n = 100
    result = timeit.timeit(part2,globals=globals(), number = n)
    print("Part 2:",part2())
    print("Average Runtime:",result/n)

if __name__ == "__main__":
    tests()
    main()