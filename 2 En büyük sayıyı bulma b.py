"""
Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.
"""
# İkinci yöntem liste ile sıralama (en kolayı)

print("Girilen 3 sayı içerisinde en büyük sayıyı bulan program")

liste = list()
# int fonksiyonu olmadan strig olarak atanıyor
liste.append(int(input("İlk sayıyı giriniz : ")))
liste.append(int(input("İkinci sayıyı giriniz : ")))
liste.append(int(input("Üçüncü sayıyı giriniz : ")))

listeSırali = liste

print("Giridiğiniz sayılar\n"
      "ilk sayı = {}\n"
      "İkinci sayı ={}\n"
      "Üçüncü sayı = {}".format(liste[0],liste[1],liste[2]))

#print(liste)

# sort metodu sırlamayı kalıcı olarak değiştiriyor bir değişkene atamaya gerak kalmıyor
# test etmek için yorum haline gelen printleri aktif etmek yeterli.

liste.sort(reverse=True)

print("Sayıların sıralaması\n"
      "Büyük = {}\n"
      "Orta = {}\n"
      "Küçük = {}".format(liste[0],liste[1],liste[2]))

#print(liste)