from collections import Counter

while True:
    print("Available Years and Registrar Name \n1974,1976,1980,1983,1987,1991 \nschmidt , kohl\n")
    x = input("Enter the Registrar Name or Year: ")

    years = ['1974', '1976', '1980', '1983', '1987', '1991']
    registrar_name = ['schmidt', 'kohl']

    if x in registrar_name:
        if x == 'kohl':
            print('kohl')

        elif x == 'schmidt':
            print('schmidt')
    elif x in years:
        if x == '1974':
            file = open('1974-Schmidt-SPD.nostop', 'r', )
            string = file.read()
            li = list(string.split(" "))
            c = Counter(li)
            c.most_common(10)
            print(c)

            print("1974")
        elif x == '1976':
            print("1976")
        elif x == '1980':
            print("1980")
        elif x == '1983':
            print("1983")
        elif x == '1987':
            print("1987")
        elif x == '1991':
            print("1991")
    else:
        print("Incorrect Registrar Name or Year ")
