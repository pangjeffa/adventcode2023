# a = range(1,5)

# b = {}
# b[a] = "hello world"
# print(1 in list(b.keys())[0])
# print(b)

# for i in range(50,52):
#     print(i)

# print(a[0])
# print(a[0])

def parseInput(filename:str):
    with open(filename) as f:

def getMappingValues(s:str) -> tuple:
    if not s[0].isnumeric():
        s = s.strip()
    try:
        source, destination, rng = s.split(' ')
        return (int(source),int(destination),int(rng))
    except Exception as e:
        #do logging things
        print(e)

def getSeeds(s: str) -> list:
    if not s[0].isnumeric():
        s = s.strip()
    return [int(n) for n in s.split(' ')]

def main():
    parsed = parseInput()

if __name__ == "__main__":
    main()