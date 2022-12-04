# Jim Lawless
# License: https://github.com/jimlawless/AoC2022/LICENSE

if __name__ == "__main__":
    count=0

    infile = open("input4.txt","r")
    for line in infile:
        line = line.replace("-"," ")
        line = line.replace(","," ")
        words = line.split()
        r1_1=int(words[0])
        r1_2=int(words[1])
        r2_1=int(words[2])
        r2_2=int(words[3])
        found=False
        for i in range( r1_1, r1_2 + 1):
            for j in range(r2_1, r2_2 + 1):
                if i == j:
                    found=True
                    count+=1
                    break
                if found:
                    break
            if found:
                break            
    infile.close()
    print(count)