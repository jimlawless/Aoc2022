# Jim Lawless
# License: https://github.com/jimlawless/AoC2022/LICENSE

if __name__ == "__main__":
    infile = open("input6.txt","r")
    for line in infile:
        for i in range(3,len(line)):
            tmp="".join(sorted(line[i-3:i+1]))
            found=False
            for j in range(1,len(tmp)):
                if tmp[j]==tmp[j-1]:
                    found=True
            if found:
                continue            
            print(i+1)
            break                     
    infile.close()
 