# Jim Lawless
# License: https://github.com/jimlawless/AoC2022/LICENSE

if __name__ == "__main__":
    total = 0
    count = 0
    infile = open("input3.txt","r")
    for line in infile:
        if count == 0:
            x1 = line
            count+=1
            continue
        if count == 1:
            x2 = line
            count+=1
            continue
        if count == 2:
            count = 0
            for c in line:
                if c.isalpha():
                    if (x1.find(c)>=0) and (x2.find(c)>=0):
                        o=ord(c)
                        if  (o >= ord('a')) and (o<=ord('z')):
                            total+=ord(c)-ord('a')+1
                        else:
                            total+=ord(c)-ord('A')+27
                        break    
    infile.close()
    print(total)