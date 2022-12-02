# Jim Lawless
# License: https://github.com/jimlawless/AoC2022/LICENSE

m={ "A" : 1, "B" : 2, "C" : 3, "X" : 1, "Y" : 2, "Z" : 3}

if __name__ == "__main__":
    total = 0
    infile = open("input2.txt","r")
    for line in infile:
        pair=line.split()
        if (pair[0]=="A")and(pair[1]=="X"):
            total=total+m["Z"]
        elif (pair[0]=="A")and(pair[1]=="Y"):
            total=total+3
            total=total+m["X"]
        elif (pair[0]=="A")and(pair[1]=="Z"):
            total=total+6
            total=total+m["Y"]
        elif (pair[0]=="B")and(pair[1]=="X"):
            total=total+m["X"]
        elif (pair[0]=="B")and(pair[1]=="Y"):
            total=total+3
            total=total+m["Y"]
        elif (pair[0]=="B")and(pair[1]=="Z"):
            total=total+6
            total=total+m["Z"]       
        elif (pair[0]=="C")and(pair[1]=="X"):
            total=total+m["Y"]
        elif (pair[0]=="C")and(pair[1]=="Y"):
            total=total+3
            total=total+m["Z"]
        elif (pair[0]=="C")and(pair[1]=="Z"):
            total=total+6
            total=total+m["X"]
    infile.close()
    print(total)