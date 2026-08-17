# 1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren bir fonksiyon yazınız.
def kelimeyazdir(kelime, kez):
    for i in range(kez):
        print(kelime)

kelimeyazdir("Merhaba", 3)
# 2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyonu yazınız.
def listeyap(*args):
    liste = []
    for arg in args:
        liste.append(arg)
    return liste

print(listeyap(1, 2, 3, 4, 5, "Armut", "Muz", "Elma", "Karpuz", True))

# 3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulun.
def asalSayilariBul(sayi1, sayi2):
    asal_sayilar = []
    for num in range(sayi1, sayi2 + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)

sayi1 = int(input("Birinci sayıyı giriniz: "))
sayi2 = int(input("İkinci sayıyı giriniz: "))

asalSayilariBul(sayi1, sayi2)

# 4- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren bir fonksiyon yazınız.
def tamBolenleriBul(sayi):
    tamBolenler = []

    for i in range(1, sayi + 1):
        if sayi % i == 0:
            tamBolenler.append(i)
    return tamBolenler

print(tamBolenleriBul(12))