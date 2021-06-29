def check_alpha(counter):
    if chr(counter).isalpha():
        return chr(counter)
    else:
        return ""


def check_last_column(counter):
    if chr(counter).isalpha():
        return counter
    else:
        return ""


counter = 97
for i in range(10):
    print(chr(counter), counter,
          chr(counter + 10), counter + 10,
          check_alpha(counter + 20), check_last_column(counter + 20))
    counter += 1