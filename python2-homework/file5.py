with open("adat.txt", "r", encoding="utf8") as adat:
    with open("adat5.txt", "w", encoding="utf8") as adat5:
        adat5.write(adat.read())