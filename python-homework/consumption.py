consumption_highway = int(input("Mennyit fogyaszt az autód országúton? "))
consumption_city = int(input("Mennyit fogyaszt az autód városban? "))
km_highway = int(input("Hány km-t utazol országúton? "))
km_city = int(input("Hány km-t utazol városban? "))
fuel_price = int(input("Mennyibe kerül a beznin? "))

one_way = (consumption_highway * km_highway + consumption_city * km_city)/100
print(one_way)
return_way = one_way * 2
print(return_way)
full_price = return_way * fuel_price
print(full_price)
