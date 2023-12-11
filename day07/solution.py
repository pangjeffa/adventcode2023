def parseLine(input: str)->tuple:
    hand,value = input.split(' ')
    return (hand,int(value))

def countHand(handStr:str,part2:bool = False):
    import heapq
    hand = [[] for _ in range(6)]

    countCards = {}
    
    if not part2:
        for letter in handStr:
            card = getValue(letter)
            countCards[card] = countCards.get(card, 0)+1
    
        for card, count in countCards.items():
            # heapq.heappush(hand[count],-card)
            hand[count].append(-card)
    else:
        j = 0
        for letter in handStr:
            if letter == "J":
                j+=1
            else:
                card = getValue(letter)
                countCards[card] = countCards.get(card, 0)+1
        
        

    return hand
    # return [sorted(n)if n else [] for n in hand ]

def getValue(input:str)->int:
    cardToInt = {l: v for v, l in enumerate('123456789TJQKA', 1)}
                # {'2': 2,
                #  '3': 3,
                #  '4': 4,
                #  '5': 5,
                #  '6': 6,
                #  '7': 7,
                #  '8': 8,
                #  '9': 9,
                #  'T': 10,
                #  'J': 11,
                #  'Q': 12,
                #  'K': 13,
                #  'A': 14}
    return cardToInt[input]

def getHandPower(listHand:str)-> int:
    if (listHand[5]): #five of a kind
        return 6
    if (listHand[4]): #four of kind
        return 5
    if listHand[3] and listHand[2]: #full house
        return 4
    if listHand[3]:#three kind
        return 3
    if len(listHand[2]) == 2: #two pair
        return 2
    if listHand[2]: #pair
        return 1
    return 0
def getHandValue(listHand: list,hand:str,part2:bool = False) -> tuple:
    #uses there logic
    if not part2:
        return  (100000000*getValue(hand[0])+1000000*getValue(hand[1])+10000*getValue(hand[2])+100*getValue(hand[3])+1*getValue(hand[4]),getHandPower(listHand))
    newHand = hand.replace('J','1')
    return  (100000000*getValue(newHand[0])+1000000*getValue(newHand[1])+10000*getValue(newHand[2])+100*getValue(newHand[3])+1*getValue(newHand[4]),getHandPower(listHand))


def getHandValueNormal(listHand: list) -> int:
    #calcualtes handvalue like nomral poker
    if (listHand[5]): #five of a kind
        return ((-1*listHand[5][0]),6)
    if (listHand[4]): #four of kind
        return (10000*(-1*listHand[4][0]) + 10*(-1*listHand[1][0]),5)
    if listHand[3] and listHand[2]: #full house
        return (10000*(-1*listHand[3][0]) + 10*(-1*listHand[2][0]),4)
    if listHand[3]:#three kind
        return (10000*(-1*listHand[3][0]) + 100*(-1*listHand[1][0])+(-1*listHand[1][1]),3)
    if len(listHand[2]) == 2: #two pair

        return (100000*(-1*listHand[2][0]) + 1000*(-1*listHand[2][1])  + (-1*listHand[1][0]),2)
    if listHand[2]: #pair
        return (1000000*(-1*listHand[2][0]) + 10000*(-1*listHand[1][0])+ 100*(-1*listHand[1][1])+ (-1*listHand[1][2]),1)
    #high card
    return  (100000000*(-1*listHand[1][0]) +1000000*(-1*listHand[1][1]) +10000*(-1*listHand[1][2]) +100*(-1*listHand[1][3]) + (-1*listHand[1][4]),0)

def tests():
    assert(parseLine('32T3K 765') == ('32T3K',765))
    assert(parseLine('T55J5 684') == ('T55J5',684))
    assert(getValue('2')==2)
    assert(getValue('T')==10)
    # assert(countHand('32T3K')==[[], [-13, -2, -10], [-3], [], [], []])
    # assert(getHandValue(countHand('55555'))==100000025)
    # assert(getHandValue(countHand('55557'))==10000032)

    # print(countHand('32T3K'))
    print("Tests Complete")

def part1():
    import heapq
    rank = [[] for _ in range(7)]
    numberHands = 0
    
    with open('input.txt') as f:
        for line in f:
            hand, value = parseLine(line)
            hand1 = countHand(hand)
            
            hand2,idx = getHandValue(hand1,hand)
            # print(hand,hand1,hand2,value)
            heapq.heappush(rank[idx],(hand2,value,hand,hand1))
            numberHands+=1
    sol = 0
    iter = 1

    for hands in rank:

        while hands:
            val, bet, h,h1 = heapq.heappop(hands)
            # print(f"{iter};{val}; {bet}; {h};{h1}")
            sol += iter*bet
            iter +=1
    return sol

def main():
    print("Part 1:",part1())
if __name__ == "__main__":
    tests()
    main()

