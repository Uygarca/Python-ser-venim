"""
Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.
"""
# birinci yöntem if koşullarını kullanarak

print("Girilen 3 sayı içerisinde en büyük sayıyı bulan program")

sayi1: int = int(input("İlk sayıyı giriniz : "))
sayi2 = int(input("İkinci sayıyı giriniz : "))
sayi3 = int(input("Üçüncü sayıyı giriniz = "))

print("Giridiğiniz sayılar\n"
      "ilk sayı = {}\n"
      "İkinci sayı ={}\n"
      " Üçüncü sayı = {}".format(sayi1, sayi2, sayi3))

buyuk = None
orta = None
kucuk = None

#birinci if yöntemi
# ilk önce en büyük sayıyı bulalım en dıştaki koşullu durum ile
# sonra iç koşulsa orta ve küçük sayıyı bulalım


if sayi1 > sayi2 and sayi1 > sayi3:
    buyuk = sayi1
    if sayi2 > sayi3:
        orta = sayi2
        kucuk = sayi3
    else:
        orta = sayi3
        kucuk = sayi2
elif sayi2 > sayi1 and sayi2 > sayi3:
    buyuk = sayi2
    if sayi1 > sayi3:
        orta = sayi1
        kucuk = sayi3
    else:
        orta = sayi3
        kucuk = sayi1
elif sayi3 > sayi2 and sayi3 > sayi1:
    buyuk = sayi3
    if sayi2 > sayi1 :
        orta = sayi2
        kucuk = sayi1
    else:
        orta = sayi1
        kucuk = sayi2

print("Sayıların sıralaması\n"
      "Büyük = {}\n"
      "Orta = {}\n"
      "Küçük = {}".format(buyuk,orta,kucuk))