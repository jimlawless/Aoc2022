# Jim Lawless
# License: https://github.com/jimlawless/AoC2020/LICENSE

if __name__ == "__main__":
    infile = open("input1.txt","r")
    elf_count = 1
    total=0
    elves=[]
    elf_count = 0
    for line in infile:
        if(len(line)>1):
            total = total + int(line)
        else:
            elves.insert(0,total)
            elf_count = elf_count + 1
            total = 0
    infile.close()
    elves.sort()
    last_three = elves[elf_count-1]+elves[elf_count-2]+elves[elf_count-3]
    print(last_three)
