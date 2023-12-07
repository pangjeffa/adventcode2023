# a = range(1,5)

# b = {}
# b[a] = "hello world"
# print(1 in list(b.keys())[0])
# print(b)

# for i in range(50,52):
#     print(i)

# print(a[0])
# print(a[0])

def parseInput(filename:str,part1 = True)->tuple:
    with open(filename) as f:
        numberOfMaps = 7 #set to seven for input
        #get Seeds!!!
        if part1:
            seeds = getSeeds(f.readline())
        else:
            seeds = getSeedsIter(f.readline())
        # soilToSoil = {}
        # soilToFert = {}
        # fertToWater ={}
        # waterTolight = {}
        # lightToTemp = {}
        # tempToHumidity = {}
        # humidityToLoc = {}
        maps = [{} for _ in range(numberOfMaps)]
        mapCount = -1 #set to -1 because logic
        while True:
            line = f.readline()
            if not line:
                break
            if line[0].isalpha():
                mapCount+=1
                continue
            if line[0].isnumeric():
                source,destination,rng = getMappingValues(line)
                maps[mapCount][range(source,source+rng)] = destination
        return (seeds, maps)
    # return (seeds, soilToSoil, soilToFert, fertToWater,waterTolight,lightToTemp,tempToHumidity,humidityToLoc)
def getMappingValues(s:str) -> tuple:
    if not s[0].isnumeric():
        s = s.strip()
    try:
        destination,source, rng = s.split(' ')
        return (int(source),int(destination),int(rng))
    except Exception as e:
        #do logging things
        print(e)

def getSeeds(s: str) -> list:
    if not s.startswith('seed'):
        raise Exception('Input not correct')

    s = s.split(':')[1].strip() #
    return [int(n) for n in s.split(' ')]

def getSeedsIter(s:str):
    if not s.startswith('seed'):
        raise Exception('Input not correct')

    s = s.split(':')[1].strip() #
    s = [int(n) for n in s.split(' ')]
    rngs = []
    for i in range(0,len(s),2):
        rngs.append(range(s[i],s[i]+s[i+1]))
    return rngs

def getLocation(seed:int,maps:list) ->int:
    pass
    for map in maps:
        # print(seed,map)
        for rng in map:
            if seed in rng:
                seed = map[rng] + abs(seed - rng[0]) 
                break
    return seed

def part1():
    seeds, maps = parseInput("input.txt")
    location = float('inf')
    # print(seeds,maps)
    for seed in seeds:
        newLocation = getLocation(seed, maps)
        if newLocation < location:
            location = newLocation
    return location
def part2():
    from tqdm import tqdm
    from multiprocessing import Pool

    seeds, maps = parseInput("input.txt",False)
    location = float('inf')
    # print(seeds,maps)

    def task(ceed):
        for ceed in tqdm(seed):
            newLocation = getLocation(ceed, maps)
            if newLocation < location:
                location = newLocation
    # print(seeds)

    for seed in seeds:
        for ceed in tqdm(seed):
            newLocation = getLocation(ceed, maps)
            if newLocation < location:
                location = newLocation
    return location


def task(maps,seed):
    from tqdm import tqdm
    location = float('inf')
    for ceed in tqdm(seed):
        newLocation = getLocation(ceed, maps)
        if newLocation < location:
            location = newLocation
    return location

def part2multi():
    from tqdm import tqdm
    
    import multiprocessing
    from multiprocessing import Pool
    from itertools import repeat
    from functools import partial
    seeds, maps = parseInput("input.txt",False)


    from tqdm import tqdm
    with Pool(processes=14) as pool:
        res = list(tqdm(pool.imap(partial(task,maps),seeds),total = len(seeds)))

    print(res)
    # for seed in seeds:
    #     p = multiprocessing.Process(target=task ,args=(seed,maps))
    #     processes.append(p)

    # for p in processes:
    #     p.start()

    return min(res)
def main():
    print("Part 1:",part1())
    print("Part 2:",part2multi())


def tests():
    assert(getSeeds('seeds: 79 14 55 13') == [79,14,55,13])
    assert( parseInput('input.txt')[0]==[1367444651, 99920667, 3319921504, 153335682, 67832336, 139859832, 2322838536, 666063790, 1591621692, 111959634, 442852010, 119609663, 733590868, 56288233, 2035874278, 85269124, 4145746192, 55841637, 864476811, 347179760])

if __name__ == "__main__":
    tests()
    main()
    

    