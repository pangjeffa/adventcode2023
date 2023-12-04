# def removeNums(s:str,pos:int) -> None:
#     idx = pos
#     while idx >=0 and s[idx].isnumeric():
#         s[idx] = '.'
#         idx -= 1
    
#     idx = pos+1
#     while idx < len(s) and s[idx].isnumeric():
#         s[idx] = '.'
#         idx += 1

import re
import heapq
compileDigits = re.compile(r'(\d+)')
compileSymbolNoDot = re.compile("[^\w.\\n]|_")
def findNums(s:str,minheap: list, digits = compileDigits):
    for match in re.finditer(digits,s):
        l,r = match.span()
        heapq.heappush(minheap,(l,r-1,match[0]))

def findSymbols(s:str, symbols = compileSymbolNoDot)->iter:
    return re.finditer(symbols,s)

def getBounds(row:int,col:int,maxRow:int,maxCol:int)->tuple:
    if row == 0: #top row
        #  #.....#
        #  .......
        if col == 0: #left col
            return ((row,(col+1,col+1)),((row+1),(col,col+1)))
        elif col == maxCol: # right col
            return ((row,(col-1,col-1)),((row+1),(col-1,col)))
        else:
            return ((row,(col-1,col-1)),(row,(col+1,col+1)),
                    ((row+1),(col-1,col+1)))
    elif row == maxRow: # bottom row
        #  .......
        #  #.....#
        if col == 0: #left col
            return ((row,(col+1,col+1)),((row-1),(col,col+1)))
        elif col == maxCol: # right col
            return ((row,(col-1,col-1)),((row-1),(col-1,col)))
        else:
            return ((row,(col-1,col-1)),(row,(col+1,col+1)),
                    ((row-1),(col-1,col+1)))
    elif col == 0:
        return ((row,(col,col)), (row,(col+1,col+1)),
                (row+1,(col,col+1)),
                (row-1,(col,col+1))) 
    elif col == maxCol:
        return ((row,(col-1,col-1)), (row,(col,col)),
                (row+1,(col-1,col)),
                (row-1,(col-1,col)))
    else:
        #  ...
        #  .#.
        #  ...
        return ((row,(col-1,col-1)), (row,(col+1,col+1)),
                (row+1,(col-1,col+1)),
                (row-1,(col-1,col+1)))

def insertItem(minheap:list,newItems)->None:
    if not minheap or not newItems:
        return
    for item in newItems:
        l,r = item[1]
        heapq.heappush(minheap[item[0]],(l,r,''))

def getIntersections(minheap:list)->int:
    # heapq.heapify(minheap)

    total = 0
    l,r,val = heapq.heappop(minheap)
    visited = set()
    # print(l,r,val,minheap[0])
    while minheap:
        l2,r2,val2 = heapq.heappop(minheap)
        # print(l2,r2,val2)
        if l2 <= r:
            if val2 == '':
                if val != '' and (l,r,val) not in visited:
                    total += int(val)
                    visited.add((l,r,val))
                
            elif (l2,r2,val2) not in visited:
                    total += int(val2)
                    visited.add((l2,r2,val2))
        l,r,val = l2,r2,val2
    return total

testinput = [(0, 3, '467'), (2, 4, ''), (5, 8, '114')]

assert(getIntersections(testinput)==467)


filename = 'input.txt'
lengthFile = 0
with open(filename, "rb") as f:
    lengthFile = sum(1 for _ in f)
with open(filename) as f:
    nums = [[] for _ in range(lengthFile)]
    
    row = 0
    while True:
        line = f.readline()
        if not line:
            break
        findNums(line,nums[row])
        
        for symbol in findSymbols(line):
            bounds = getBounds(row,symbol.span()[0],len(nums)-1,len(line)-1)
            insertItem(nums,bounds)
        #increment counter
        row += 1
    total = 0

    for idx,line in enumerate(nums):
        l = line.copy()
        part = getIntersections(line)
        # print(idx,part, l)
        total += part
    print(total)







############
#     print(nums[0])
#     # print(heapq.heapify(nums[0]))
#     # heapq.heappush(nums[0],(2,4,'sdf'))
#     while nums[0]:
#         print(nums[0])
#         print(heapq.heappop(nums[0]))

    


# # print(list(findNums('12...23.1.4.1')))

# h = []
# s = '233...233..2.3.'
# findNums(s,h)
# print(h)
# heapq.heappush(h,(2,4,'sdf'))
# print(h)