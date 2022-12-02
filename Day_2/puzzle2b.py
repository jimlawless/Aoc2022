# Jim Lawless
# License: https://github.com/jimlawless/AoC2022/LICENSE

tab={ "AX":3,"AY":4,"AZ":8,"BX":1,"BY":5,"BZ":9,"CX":2,"CY":6,"CZ":7 } 

if __name__ == "__main__":
    total = 0
    infile = open("input2.txt","r")
    for line in infile:
        them,me=line.split()
        total+=tab[them+me]
    infile.close()
    print(total)