def getNum(s:str)-> tuple:
    # l, r = 0, len(s)-1
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

with open('input.txt') as f:
    output = 0
    lines = f.readlines()
    for line in lines:
        l,r = getNum(line)
        output += int(l+r)
    print(output)
        

