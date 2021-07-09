with open("adat.txt", "r", encoding="utf8") as adat:
    for line in adat:
        line = line.rstrip('\n')
        print(line, end=" ")
