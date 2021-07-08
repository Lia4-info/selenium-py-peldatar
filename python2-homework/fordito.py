num_list = []
user_num = 1
while user_num != 0:
    user_num = int(input("Enter a non negative integer: "))
    num_list.append(user_num)
num_list.remove(0)
num_list.reverse()
print(num_list)