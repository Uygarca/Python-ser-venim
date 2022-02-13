"""Şimdi de geometrik şekil hesaplama işlemi yapalım. İlk olarak kullanıcıdan üçgenin mi dörtgenin mi tipini bulmak istediğini sorun.

Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi ,
dikdörtgen mi yoksa sıradan bir dörtgen mi olduğunu bulmaya çalışın.

Eğer kullanıcı "Üçgen" cevabını verirse , 3 tane kenar isteyip bu üçgenin ikizkenar mı ,
eşkenar mı yoksa sıradan bir üçgen mi olduğunu bulmaya çalışın.
Eğer verilen kenarlar bir üçgen belirtmiyorsa, ekrana "Üçgen belirtmiyor" şeklinde bir yazı yazın.o

Üçgen belirtme şartını bilmiyorsunuz internetten bakabilirsiniz.

Ayrıca , bu problemde mutlak değer bulmaya ihtiyacınız olacak.
 Bunun için, Pythonda hazır bir fonksiyon olan abs()
 fonksiyonunu kullanabilirsiniz. Kullanımı şu şekildedir ;"""

print("\n**********************************\n"
      "Geometrik şekil hesaplama programı\n"
      "**********************************")

secim = input("Üçgen için : 1\n"
              "Dörtgen için : 2\n"
              "Şekli seçin : ")

if secim == "1":
    print("Üçgen seçtiniz.")
    a = abs(int(input("a kenarını girin : ")))
    b = abs(int(input("b kenarını girin : ")))
    c = abs(int(input("c kenarını girin : ")))

    siralama = [a,b,c]
    siralama.sort()
    kosul = bool(siralama[1] + siralama[0] <= siralama[2])
    kosul2 = bool(a == 0 or b == 0 or c == 0)

    if kosul == True or kosul2 == True:
        print("Girdiğiniz değerler ile Üçgen oluşturulamaz...")
    else:
        if a == b and b == c:
            print("Eş kenar üçgen.")
        elif a == b or b == c or c == a:
            print("İkiz kenar ücgen.")
        else:
            print("Sıradan üçgen.")
elif secim == "2":
    print("Dörtgen seçtiniz")
    a = int(input("a kenarını girin : "))
    b = int(input("b kenarını girin : "))
    c = int(input("c kenarını girin : "))
    d = int(input("d kenarını girin : "))
# üçgen olabilmesi i
    siralama = [a,b,c,d]
    siralama.sort()
    kosul = bool((siralama[0] + siralama[1] + siralama[2]) <= siralama[3])
    kosul2 = bool(a == 0 or b == 0 or c == 0 or d == 0)

    if kosul == True or kosul2 == True:
        print("Girdiğiniz değerler ile Dörtgen çizilemez.")
    elif (a or b or c or d) == 0 :
        print("0' dan büyük bir değer girmelisiniz. Dörtgen çizilemez.")
    else:
        if a == b and b == c and c == d:
            print("Kare.")
        elif a == c and b == d:
            print("Dikdörtgen.")
        else:
            print("Sıradan dörtgen.")
else:
    print("Geçersiz seçim yaptınız.")