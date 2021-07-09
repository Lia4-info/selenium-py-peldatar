# soronként másik file-ba
with open("adat.txt", "r", encoding="utf8") as adat:
    with open("adat4.txt", "w", encoding="utf8") as adat4:
        adat_list = []
        for line in adat:
            adat_list.append(line)
        adat4.write("".join(map(str, adat_list)))
