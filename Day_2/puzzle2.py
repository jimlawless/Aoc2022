# Jim Lawless
# License: https://github.com/jimlawless/AoC2022/LICENSE

m={ "A" : 1, "B" : 2, "C" : 3, "X" : 1, "Y" : 2, "Z" : 3}

if __name__ == "__main__":
    total = 0
    infile = open("input2.txt","r")
    for line in infile:
        pair=line.split()
        if (pair[0]=="A")and(pair[1]=="X"):
            total=total+3
        elif (pair[0]=="A")and(pair[1]=="Y"):
            total=total+6
        elif (pair[0]=="B")and(pair[1]=="Y"):
            total=total+3
        elif (pair[0]=="B")and(pair[1]=="Z"):
            total=total+6
        elif (pair[0]=="C")and(pair[1]=="X"):
            total=total+6
        elif (pair[0]=="C")and(pair[1]=="Z"):
            total=total+3
        total=total+m[pair[1]]
    infile.close()
    print(total)