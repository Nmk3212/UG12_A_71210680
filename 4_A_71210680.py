inputan = int(input("Input : "))
print("Output :")
sel=2 
for kol in range (1,inputan+1):
    for bar in range (1,2*inputan) :
        if kol+bar==inputan+1 or bar-kol==inputan-1:
            print ("*", end="")
        elif kol==inputan and bar!=sel:
            print ("*",end="")
            sel=sel+2
        else:
            print (end=" ")
    print ()
