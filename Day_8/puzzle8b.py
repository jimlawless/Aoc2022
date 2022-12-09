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
    best_row = -1
    best_col = -1
    best_score = -1
    for r in range(1,count-1):
        for c in range(1,len(trees[0])):
            up = 0
            down  = 0
            left = 0
            right = 0
            for r_pos in range(r-1,-1,-1):
                up+=1
                if trees[r_pos][c]>=trees[r][c]:
                    break
            for r_pos in range(r+1,count):
                down+=1
                if trees[r_pos][c]>=trees[r][c]:
                    break
            for c_pos in range(c-1,-1,-1):
                left+=1
                if trees[r][c_pos]>=trees[r][c]:
                    break
            for c_pos in range(c+1,len(trees[0])):
                right+=1
                if trees[r][c_pos]>=trees[r][c]:
                    break
            score=up*down*left*right
            #print(r,c,up,down,left,right)
            if score > best_score:
                best_score = score
                best_row=r
                best_col=c
    print(r,c,best_score)    
    
