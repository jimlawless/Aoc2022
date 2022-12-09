# Jim Lawless
# License: https://github.com/jimlawless/AoC2022/LICENSE

if __name__ == "__main__":
    trees=[]
    count=0
    infile = open("input8.txt","r")
    for line in infile:
        line=line.rstrip("\n")
        trees.insert(count,[])
        for i in range(0,len(line)):
            trees[count].insert(i,line[i])
        count+=1            
    infile.close()
    total=len(trees[0])*2+(count-2)
    for r in range(1,count-1):
        for c in range(1,len(trees[0])):
            found = True
            for r_pos in range(r-1,-1,-1):
                if trees[r_pos][c]>=trees[r][c]:
                    found = False
                    break
            if found:
                total+=1
                continue
            found = True
            for r_pos in range(r+1,count):
                if trees[r_pos][c]>=trees[r][c]:
                    found = False
                    break
            if found:
                total+=1
                continue
            found = True
            for c_pos in range(c-1,-1,-1):            
                if trees[r][c_pos]>=trees[r][c]:
                    found = False
                    break
            if found:
                total+=1
                continue   
            found = True
            for c_pos in range(c+1,len(trees[0])):
                if trees[r][c_pos]>=trees[r][c]:
                    found = False
                    break
            if found:
                total+=1
    print(total)                    
    
