# Jim Lawless
# License: https://github.com/jimlawless/AoC2022/LICENSE

if __name__ == "__main__":
    total = 0
    
    infile = open("input3.txt","r")
    for line in infile:
        keep={}
        for i in range(0,int(len(line)/2)):
            c=line[i]
            if c.isalpha():
                keep[c]=1;
        for i in range((int(len(line)/2)),len(line)):
            c=line[i]
            if c.isalpha():
                if keep.get(c,0)==1:
                    o=ord(c)
                    if  (o >= ord('a')) and (o<=ord('z')):
                        total+=ord(c)-ord('a')+1
                    else:
                        total+=ord(c)-ord('A')+27
                    break    
    infile.close()
    print(total)