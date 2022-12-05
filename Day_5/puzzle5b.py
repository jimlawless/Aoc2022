# Jim Lawless
# License: https://github.com/jimlawless/AoC2022/LICENSE

if __name__ == "__main__":
    count=0
    tab=[]
    for i in range(0,10):
        tab.insert(i,[])
    infile = open("input5.txt","r")
    lines = infile.readlines()
    infile.close()
    while count < len(lines):
        if(len(lines[count])<2):
            break
        for i in range(1,len(lines[count]),4):
            if lines[count][i].isalpha():      
                tab[int(i/4)].append(lines[count][i])
        count+=1
    count+=1
    while count < len(lines):
        words = lines[count].split()
        num = int(words[1])
        frm = int(words[3])-1
        to = int(words[5])-1
        for i in range(0,num):
            tmp=tab[frm].pop(num-(i+1))
            tab[to].insert(0,tmp)
        count+=1
    for i in range(0,10):
        if(len(tab[i])>0):
            tmp=tab[i].pop(0)
            print(tmp,end="")
        