'''
    1-100 arasında rastgele üretilecek bir sayıyıyı aşağı yukarı ifadeleri ile buldurmaya çalışın. (hak = 5)
    ** "random modülü" için "python random" şeklinde arama yapın.
    ** 100 üzerinden puanlama yapın. Her soru 20 puan.
    ** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı üzerinden hesaplansın.
'''
import random

sayi = random.randint(1, 100)

print(sayi)

hak = 5
sayac = 0

while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input("1-100 arasında bir sayı tahmin edin: "))


    if sayi == tahmin:
        print("Tebrikler! Doğru tahmin ettiniz. Puanınız :", 100 - (sayac - 1) * 20)
        print(f"{sayac}. denemede bildiniz.")
        break
    elif sayi > tahmin:
        print("Daha büyük bir sayı tahmin edin.")
        print(f"Kalan hakkınız: {hak}")
    else:
        print("Daha küçük bir sayı tahmin edin.")
        print(f"Kalan hakkınız: {hak}")

    if hak == 0:
        print(f"Üzgünüm, hakkınız kalmadı. Doğru sayı {sayi} idi.")