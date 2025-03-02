def hesap_makinesi():
    while True:
        print("\n Basit Hesap Makinesi")
        print("1. Toplama")
        print("2. Çikarma")
        print("3. Çarpma")
        print("4. Bölme")
        print("5. Cikis")
        
        secim = input("Seciminizi yapin(1/2/3/4/5):")
        if secim == "5":
            print("cikis yapiliyor...")

            break
        if secim in ("1", "2", "3","4"):

         try:
                sayi1 = float(input("Birinci sayiyi girin:"))
                sayi2 = float(input("ikinci sayiyi girin:"))

         except ValueError:
            print("Lutfen gecerli bir sayi girin")

            continue

        if secim =="1":
            print(f"sonuc:{sayi1} + {sayi2} = {sayi1 + sayi2}")
        elif secim == "2":
            print(f"sonuc:{sayi1} - {sayi2} = {sayi1 - sayi2}")
        elif secim =="3":
            print(f"sonuc:{sayi1} * {sayi2} = {sayi1 * sayi2}")
        elif secim == "4":
             if sayi2 == 0:
                print("hata! bir sayi sifira bölünmez")
             else:
                print(f"sonuc:{sayi1} + {sayi2} = {sayi1 + sayi2}")
        else:
            print("geçersiz seçim,lütfen tekrar deeyin.")
hesap_makinesi()

            








