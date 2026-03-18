# program i thjeshte per shpenzimet

exp = []

while True:
    print("\n1 shto")
    print("2 shiko")
    print("3 total")
    print("4 dil")
    
    z = input("zgjedh: ")

    if z == "1":
        a = input("sa lek shpenzove: ")
        a = float(a)
        exp.append(a)
        print("ok u shtua")

    elif z == "2":
        if len(exp) == 0:
            print("bosh")
        else:
            i = 1
            for e in exp:
                print(i, e)
                i = i + 1

    elif z == "3":
        t = 0
        for e in exp:
            t = t + e
        print("totali eshte", t)

    elif z == "4":
        print("po dal")
        break

    else:
        print("nuk eshte opsion")
