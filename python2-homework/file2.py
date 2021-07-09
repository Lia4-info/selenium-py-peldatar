with open("adat.txt", "r", encoding="utf8") as adat:
    adat_list = []
    for line in adat:
        line = line.rstrip('\n')
        adat_list.append(line)
text_line = " ".join(map(str, adat_list))
print(text_line)
