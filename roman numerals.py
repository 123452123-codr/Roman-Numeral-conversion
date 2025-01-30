d = {"num":"",1:"I", 5:"V" ,10:"X" ,50:"L" ,100:"C" ,500:"D" ,1000:"M"}

num = int(input("Enter number (less than 4000) to convert to roman numerals:"))
c = len(str(num))

if type(num) == int:
    for i in range(c, 0, -1):
        x = num // (10 ** (i - 1))
        num -= x * (10 ** (i - 1))
        
        if i == 4:
            d["num"] = d["num"] + d[1000] * x
        elif i == 3:
            if x == 0:
                continue
            if 1 <= x <= 3:
                d["num"] = d["num"] + d[100] * x
            elif x == 4:
                d["num"] = d["num"] + d[100] + d[500]
            elif 5 <= x <= 8:
                d["num"] = d["num"] + d[500] + d[100] * (x - 5)
            elif x == 9:
                d["num"] = d["num"] + d[100] + d[1000]
        elif i == 2:
            if x == 0:
                continue
            if 1 <= x <= 3:
                d["num"] = d["num"] + d[10] * x
            elif x == 4:
                d["num"] = d["num"] + d[10] + d[50]
            elif 5 <= x <= 8:
                d["num"] = d["num"] + d[50] + d[10] * (x - 5)
            elif x == 9:
                d["num"] = d["num"] + d[10] + d[100]
        elif i == 1:
            if x == 0:
                continue
            if 1 <= x <= 3:
                d["num"] = d["num"] + d[1] * x
            elif x == 4:
                d["num"] = d["num"] + d[1] + d[5]
            elif 5 <= x <= 8:
                d["num"] = d["num"] + d[5] + d[1] * (x - 5)
            elif x == 9:
                d["num"] = d["num"] + d[1] + d[10]
    print("Roman numeral:",d["num"])
else:
    print("Error!")


        






    



