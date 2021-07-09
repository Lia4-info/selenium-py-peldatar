# egy sor másik file-ba
with open("adat.txt", "r", encoding="utf8") as adat:
    with open("adat3.txt", "w", encoding="utf8") as adat3:
        adat_list = []
        for line in adat:
            line = line.rstrip('\n')
            adat_list.append(line)
        adat3.write(" ".join(map(str, adat_list)))
