with open("adat.txt", "r", encoding="utf8") as adat:
    with open("adat2.txt", "w", encoding="utf8") as adat2:
        adat2.write(adat.read())