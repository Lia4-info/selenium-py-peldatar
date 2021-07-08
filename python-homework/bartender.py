guest_age = int(input("Életkor: "))
guest_drink = input("Választott ital: ")

if guest_age < 18 and guest_drink == "sör":
    print("Kiskorúaknak nem adhatunk sört!")
elif guest_age > 60 and guest_drink == "kóla":
    print("A koffein megemelheti a vérnyomását.")
elif guest_drink == "sör":
    print("Parancsoljon, a söre.")
elif guest_drink == "kóla":
    print("Parancsoljon,a kólája.")
else:
    print("Csak sör és kóla van.")