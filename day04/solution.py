
import logging
def parseGame(s:str)->tuple:
    try:
        game, numbers = s.split(':')
        winningNumbers,myNumbers = numbers.split('|')
        winningNumbers = set([int(n) for n in winningNumbers.strip().split(' ') if n != ''])
        myNumbers = [int(n) for n in myNumbers.strip().split(' ') if n != '']
        return (winningNumbers,myNumbers)
    except Exception as e:
        logging.error(e)
        print(e)
        return None

def countWins(winingNumbers:set,myNumbers:list)->int:
    matches = 0
    for n in myNumbers:
        if n in winingNumbers:
            matches+=1
    return matches

def calcScore(matches:int)->int:
    return int(2**(matches-1))

def getFileLength(filename:str)->int:
    with open(filename, "rb") as f:
        lengthFile = sum(1 for _ in f)
    return lengthFile

def part1(filename:str)-> int:
    solution = 0
    with open(filename) as f:
        for line in f:
            winningNumbers,myNumbers = parseGame(line)
            solution += calcScore(countWins(winningNumbers,myNumbers))
    return solution

def part2(filename:str)-> int:
    solution = 0
    fileLength = getFileLength(filename)
    with open(filename) as f:
        for line in f:
            winningNumbers,myNumbers = parseGame(line)
            solution += calcScore(countWins(winningNumbers,myNumbers))
    return solution

def main():
    logging.info("Program Start")
    filename = 'test.txt'
    assert(part1(filename)==13)
    # assert(part2(filename)==30)
    filename = 'input.txt'
    print(f"Part 1: {part1(filename)}")
    print(f"Part 2: {part2(filename)}")

if __name__ == "__main__":
    main()

    import timeit
    n = 100
    result = timeit.timeit('''main()''',globals=globals(), number = n)
    print(result/n)
