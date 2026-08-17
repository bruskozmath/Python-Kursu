
# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
sayi = float(input('Sayı Giriniz: '))
aralik = (sayi > 0) and (sayi < 100)
print(aralik)

# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
pozCiftSayi = int(input('Bir tam sayı yazınız: '))
pozCift = pozCiftSayi > 0 and pozCiftSayi % 2 == 0
print(pozCift)

# 3- Email ve parola bilgileri ile giriş kontrolü yapınız.

# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
#    a-) Ortalama 50 olsa bile final notu en az 50 olmalıdır.
#    b-) Finalden 70 alındığında ortalamanın önemi olmasın.
# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#    Formül: (Kilo / boy uzunluğunun karesi)
#    Aşağıdaki tabloya göre kişi hangi gruba girmektedir:
#    0-18.4     => Zayıf
#    18.5-24.9  => Normal
#    25.0-29.9  => Fazla Kilolu
#    30.0-34.9  => Şişman (Obez)




