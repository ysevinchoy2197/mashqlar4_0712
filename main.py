#1-misol
masofa = float(input("Masofani kiriting (km): "))

if masofa < 2:
    print("Piyoda yuring!")
elif 2 <= masofa <= 10:
    print("Velosipedda boring!")
elif 10 < masofa <= 50:
    print("Avtobusda boring!")
else:
    print("Poyezd yoki mashina tanlang!")

#2-misol
kayfiyat = input("Kayfiyatingizni kiriting (xursand, xafa, zerikdim): ").lower()

if kayfiyat == "xursand":
    print("Komediya ko‘ring!")
elif kayfiyat == "xafa":
    print("Drama yoki romantika ko‘ring!")
elif kayfiyat == "zerikdim":
    print("Jangari yoki fantastika ko‘ring!")
else:
    print("Kayfiyatingizni aniqroq kiriting!")

#3-misol
sarflangan = int(input("Oyiga sarflangan elektr energiyasi (kVt): "))

if sarflangan < 100:
    print("To‘lov: 20 ming so‘m")
elif 100 <= sarflangan <= 300:
    print("To‘lov: 50 ming so‘m")
elif 300 < sarflangan <= 500:
    print("To‘lov: 100 ming so‘m")
else:
    print("To‘lov: 200 ming so‘m")
