start = int(input("voer een begin waarde in: "))
eind = int(input("voer een eindwaarde in: "))


for i in range(start, eind):
    if i%7 ==0  and  i % 5 != 0:
        print(i)

