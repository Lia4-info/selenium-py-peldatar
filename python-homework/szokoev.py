def szokoev(n):
    if n % 400 == 0:
        print(n, "szökőév")
    elif n % 100 == 0:
        print(n, "nem szökőév")
    elif n % 4 == 0:
        print(n, "szökőév")
    else:
        print(n, "nem szökőév")

year = int(input("Írj be egy évszámot: "))
szokoev(year)