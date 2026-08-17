# 1-  "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.
arabalar = ["Bmw", "Mercedes", "Opel", "Mazda"]

# 2-  Liste Kaç elemanlıdır ?
result = len(arabalar)

# 3-  Listenin ilk ve son elemanı nedir ?
result = arabalar[0]
result = arabalar[-1]

# 4-  Mazda değerini Toyota ile değiştirin.
arabalar[3] = "Toyota"
result = arabalar

# 5-  Mercedes listenin bir elemanı mıdır ?
result = "Mercedes" in arabalar

# 6-  Listenin -2 indeksindeki değer nedir ?
result = arabalar[-2]

# 7-  Listenin ilk 3 elemanını alın.
result = arabalar[0:3]

# 8-  Listenin son 2 elemanı yerine "Toyota" ve "Renault" değerlerini ekleyin.
arabalar[-2:] = ["Toyota", "Renault"]
result = arabalar

# 9-  Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
arabalar = arabalar + ["Audi", "Nissan"]
result = arabalar

# 10- Listenin son elemanını silin.
del arabalar[-1]
result = arabalar

# # 11- Liste elemanlarını tersten yazdırınız.
arabalar = arabalar[::-1]
result = arabalar

# 12- Aşağıdaki verileri bir liste içinde saklayınız.
#     studentA: Yiğit Bilgi 2010, (70,60,70)
#     studentB: Sena Turan 1999, (80,80,70)
#     studentC: Ahmet Turan 1998, (60,60,70)
studentA = ("Yiğit Bilgi", 2010, (70, 60, 70))
studentB = ("Sena Turan", 1999, (80, 80, 70))
studentC = ("Ahmet Turan", 1998, (60, 60, 70))
students = [studentA, studentB, studentC]

# 13- Liste elemanlarını ekrana yazdırınız.
print(students)
print(result)