# Jim Lawless
# License: https://github.com/jimlawless/AoC2020/LICENSE

if __name__ == "__main__":
    infile = open("input1.txt","r")
    elf_count = 1
    total=0
    most=0
    most_count=0
    for line in infile:
        if(len(line)>1):
            total = total + int(line)
        else:
            if total > most:
                most = total
                most_count = elf_count
            total=0
            elf_count = elf_count + 1
    infile.close()
    print(most," ",most_count)
