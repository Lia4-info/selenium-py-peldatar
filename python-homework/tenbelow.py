user_num = int()
total = int()
while user_num < 10:
    user_num = int(input("Enter an integer: "))
    total = total + user_num
    if user_num >= 10:
        total = total - user_num
print(total)