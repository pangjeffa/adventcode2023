def getNum(s:str)-> tuple:

    for l in range(len(s)):
        if s[l].isnumeric():
            l = l
            break
    for r in range(len(s)-1,-1,-1):
        if s[r].isnumeric():
            r = r
            break
    return (s[l],s[r])
    return 1,2

def getNumIndex(s:str)-> tuple:

    left = right = None
    for l in range(len(s)):
        if s[l].isnumeric():
            left = l
            break
    for r in range(len(s)-1,-1,-1):
        if s[r].isnumeric():
            right = r
            break

    return (left,right)

def getAlphaNumber(s:str) -> tuple:
    import heapq
    import re

    mapNumbers = {'one':'1',
                  'two':'2',
                  'three':'3',
                  'four':'4',
                  'five':'5',
                  'six':'6',
                  'seven':'7',
                  'eight':'8',
                  'nine':'9'}
    leftHeap = []
    rightHeap = []

    reCompiled = []
    #precompile
    for num in mapNumbers:
        reCompiled.append((re.compile(num),mapNumbers[num]))

    left,right = getNumIndex(s)

    if left != None:
        heapq.heappush(leftHeap,(left, s[left]))
    if right != None:
        heapq.heappush(rightHeap,(-right,s[right]))
    
    for reExp in reCompiled:
        matches = list(re.finditer(reExp[0],s))
        if matches:
            heapq.heappush(leftHeap,(matches[0].span()[0],reExp[1]))
            heapq.heappush(rightHeap,(-matches[-1].span()[1]+1,reExp[1]))

    
    return leftHeap[0][1],rightHeap[0][1]



        
import timeit
f1 = '''with open('input.txt') as f:
    output = 0
    lines = f.readlines()
    for line in lines:
        l,r = getNum(line)
        output += int(l+r)
    '''
n = 100
result = timeit.timeit(f1,globals=globals(), number = n)
print(result/n)


f2 = '''with open('input2.txt') as f:
    output = 0
    lines = f.readlines()
    for line in lines:
        l,r = getAlphaNumber(line)

        output += int(l+r)
    # print(output)'''
n = 100
result = timeit.timeit(f2,globals=globals(), number = n)
print(result/n)

# import re

# print(re.findall('one','onetwoonetwo'))
# # for item in list(re.finditer('one','onetwoonetwo')):
# #     print(item)
# print(list(re.finditer('one','onetwoonetwo'))[0].span())

