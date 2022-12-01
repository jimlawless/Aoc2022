# Jim Lawless
# License: https://github.com/jimlawless/AoC2020/LICENSE

if __name__ == "__main__":
    infile = open("input1.txt","r")
    total=0
    elves=[]
    for line in infile:
        if(len(line)>1):
            total = total + int(line)
        else:
            elves.insert(0,total)
            total = 0
    infile.close()
    elves.sort(reverse=True)
    print(elves[0]+elves[1]+elves[2])