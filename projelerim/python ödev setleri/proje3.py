list=[]
yeni=[]
a=int(input("Kac adet sayi gireceksiniz:"))
for i in range(a):
    sayi=int(input("Sayiyi giriniz:"))
    if sayi==0:
        yeni.append(sayi)
    else:
        list.append(sayi)
yenilist=[]
yenilist = yeni+list
print(yenilist)
