def splitGameData(s:str) -> tuple:
    '''
        Game 1: 12 blue, 15 red, 2 green; 17 red, 8 green, 5 blue; 8 red, 17 blue; 9 green, 1 blue, 4 red
    '''
    try:
        name , data = s.split(':')
    except Exception as e:
        raise('unexpected input format')
    
    return (name,data.strip())
    
def extractGame(s:str) -> str:
    '''
        "Game 1","12 blue, 15 red, 2 green; 17 red, 8 green, 5 blue; 8 red, 17 blue; 9 green, 1 blue, 4 red"
    '''
    return s.split(" ")[1]

def checkRGB(s:str,limits:tuple) ->bool:
    '''
        "12 blue, 15 red, 2 green; 17 red, 8 green, 5 blue; 8 red, 17 blue; 9 green, 1 blue, 4 red"
    '''
    lines = s.replace(';',',').split(",")
    r,g,b = limits
    for line in lines:
        
        count, color = line.strip().split(' ')
        if color == 'blue' and int(count) > b:
            return False
        if color == 'red'and int(count) > r:
            return False
        if color == 'green' and int(count) > g:
            return False
    return True

def findMinPower(s:str) -> int:
    r=g=b = float("-inf")
    lines = s.replace(';',',').split(",")
    for line in lines:
        count, color = line.strip().split(' ')
        if color == 'blue' and int(count) > b:
            b = int(count)
        if color == 'red'and int(count) > r:
            r = int(count)
        if color == 'green' and int(count) > g:
            g = int(count)
    # print(r,g,b)
    return r*g*b


with open('input.txt') as f:
    idSum = 0
    red = 12
    green = 13
    blue = 14
    for line in f:
        game,data = splitGameData(line)
        if checkRGB(data,(red,green,blue)):
            idSum += int(extractGame(game))
print(idSum)
            
with open('input2.txt') as f:
    idSum = 0
    for line in f:
        game,data = splitGameData(line)

        idSum += findMinPower(data)
print(idSum)

# print(extractRGB('12 blue, 15 red, 2 green; 17 red, 8 green, 5 blue; 8 red, 17 blue; 9 green, 1 blue, 4 red')[0])


import timeit
f1 = '''with open('input.txt') as f:
    idSum = 0
    red = 12
    green = 13
    blue = 14
    for line in f:
        game,data = splitGameData(line)
        if checkRGB(data,(red,green,blue)):
            idSum += int(extractGame(game))'''

n = 1000
result = timeit.timeit(f1,globals=globals(), number = n)
print(result/n)

f2 = '''with open('input2.txt') as f:
    idSum = 0
    for line in f:
        game,data = splitGameData(line)

        idSum += findMinPower(data)'''
n = 1000
result = timeit.timeit(f2,globals=globals(), number = n)
print(result/n)