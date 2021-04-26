lst = []
while True:
    x = float(input("Enter a num: "))
    lst.append(x)
    print(lst)
    q_ask = input("'y' for more inputs or 'n' to quit:\n")
    if q_ask=="y":
        continue
    if q_ask == "n":
        print(lst)
        break