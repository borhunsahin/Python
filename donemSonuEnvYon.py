import random

depo1   = 0
depo2   = 0
depo3   = 0
depo4   = 0
depo5   = 0
depo6   = 0
depo7   = 0
depo8   = 0
depo9   = 0
depo10  = 0

i = 0 # Sayaç

while i < 10: # i 10'dan küçük olduğu surece işleme devam eder.
    
    i += 1 # Her işlemden sonra i yi 1 arttırır.
    
    musteri = random.normalvariate(145, 50) # Ortalaması 145 standart sapması 50 olan rastgele müşteri sayısı üretir.
    yemek = random.normalvariate(145, 50) # Ortalaması 145 standart sapması 50 olan rastgele yemek sayısı üretir.
    
    musteri = abs(round(musteri)) # Rastgele çıkan ondalıklı sayıları yuvarlar, negatifse pozitife çevirir.
    yemek = abs(round(yemek))
    
    if i == 1: # 1. gün için
        
        musteri1 = musteri # Bunu 10. günün sonunda gelen tüm müşterileri toplayabilmek için oluşturdum.
        yemek1 = yemek # Toplam yemekler için
        acKalanMusteri1 = 0 # Bunu 10 günün sonunda yemek yiyemeyen müşterileri toplayabilmek için oluşturdum.
        
        kalanYemek1 = yemek1 - musteri1 # Kalan yemeklerin durumunu kontrol eder.
        
        print("            1. Gün            ")
        print("Müşteri ---------------------------- ",musteri1)
        print("Çıkan Yemek ------------------------ ",yemek1)
        
        if kalanYemek1 < 0: # Çıkan yemek sayısının gelen müşterilerden fazla olduğu durum.
            
            acKalanMusteri1 = abs(kalanYemek1) # Yemek yiyemeyen müşterilerin sayısını belirler.
            
            print("Kalan Yemek ------------------------  0")
            print("Depolanan Yemek --------------------  0")            
            print("Aç Kalan Müşteri ------------------- ",acKalanMusteri1)
            
        else: # Çıkan yemek sayısının gelen müşterilerden fazla olduğu durum.
            
            depo1 = kalanYemek1 # Kalan yemekleri depoya aktarır.
            
            print("Kalan Yemek ------------------------ ",kalanYemek1)
            print("Depolanan Yemek -------------------- ",depo1)
            
        print("                                          ")
        print("Pazartesi Deposu ------------------- ",depo1)
        print("//////////////////////////////////////// ")


    if i == 2: # 2. gün

        musteri2 = musteri
        yemek2 = yemek
        acKalanMusteri2 = 0
        
        cikanYemek2 = round(depo1*0.10) + yemek2 # Çıkan yemeklere depo1'deki yemeklerin yüzde 10'unu ekler.
        onceDepo1 = round(depo1*0.10) - musteri2 # depo1'e öncelik vermesi gereken durumu ve gelen müşetriyle arasındaki farkı kontrol eder.
        kalanYemek2 = cikanYemek2 - musteri2

        print("            2. Gün            ")
        print("Müşteri ---------------------------- ",musteri2)
        print("Dünden Kalan Yemek ----------------- ",depo1)
        print("Dünden Aktarılan Yemek ------------- ",round(depo1*0.10))
        print("Günlük Çıkan Yemek ----------------- ",yemek2)
        print("Toplam Çıkan Yemek ----------------- ",cikanYemek2)

        if depo1 == 0: # depo1'in boş olduğu durum.
            
            if kalanYemek2 < 0:
                
                acKalanMusteri2 = abs(kalanYemek2)
                
                print("Kalan Yemek ------------------------  0")
                print("Depolanan Yemek --------------------  0")   
                print("Aç Kalan Müşteri ------------------- ",acKalanMusteri2)
                
            else:
                
                depo2 = kalanYemek2
                
                print("Kalan Yemek ------------------------ ",kalanYemek2)
                print("Depolanan Yemek -------------------- ",depo2)
                
        else: # depo1'in dolu olduğu durum
            
            if onceDepo1 > 0: # Gelen müşterilerin depo1'in yüzde 10'undan az olduğu durum.
                
                depo1 = depo1 + onceDepo1 # depo1'deki kullanılan yemekleri depo1'den eksiltir.
                yemek2 = depo2 # Günlük çıkan yemeği olduğu gibi salı deposuna aktarır.
                
                print("Dünden Kalan Yemekten Kalan -------- ",depo1)
                print("Dünden Aktarılan Yemek ------------- ",round(depo1*0.10))
                print("Kalan Yemek ------------------------ ",yemek2)
                print("Toplam Kalan Yemek ----------------- ",depo1+yemek2)
                print("Depolana Yemek --------------------- ",yemek2+onceDepo1)
                
            else: # Gelen müşterilerin depo1'in yüzde 10'undan fazla Olduğu durum
                
                if kalanYemek2 < 0: # Toplam çıkan yemeklerin gelen müşterilerden az olduğu durum
                    
                    acKalanMusteri2 = abs(kalanYemek2)
                    depo1 = depo1 - round(depo1*0.10) # depo1'in kullanılan yemeklerini depo1' den çıkarır.
                
                    print("Kalan Yemek ------------------------  0")
                    print("Depolanan Yemek --------------------  0")   
                    print("Aç Kalan Müşteri ------------------- ",acKalanMusteri2)
                
                else: # Toplam çıkan yemeklerin gelen müşterilerden fazla olduğu durum
                    
                    depo1 = depo1 - round(depo1*0.10) # depo1'in kullanılan yemeklerini depo1'den eksiltir.
                    depo2 = kalanYemek2
                    
                    print("Kalan Yemek ------------------------ ",kalanYemek2)
                    print("Depolanan Yemek -------------------- ",depo2)
                    
        print("                                          ")
        print("Pazartesi Deposu ------------------- ",depo1)
        print("Salı Deposu ------------------------ ",depo2)
        print("//////////////////////////////////////// ")
        
    if i == 3: # 3. Gün
                    
        musteri3 = musteri
        yemek3 = yemek
        acKalanMusteri3 = 0
        
        cikanYemek3 = round(depo1*0.10) + round(depo2*0.10) + yemek3 # Çıkan yemeklere depo1'in ve depo2'nin yüzde 10'unu ekler.
        onceDepo1 = round(depo1*0.10) - musteri3 
        onceDepo2 = round(depo1*0.10) + round(depo2*0.10) - musteri3 # Eğer depo1 yeterli gelmez ise depo1 ile depo2 nin durumunu kontrol eder.
        kalanYemek3 = cikanYemek3 - musteri3
        
        print("            3. Gün            ")
        print("Müşteri ---------------------------- ",musteri3)
        print("Pazartesiden Kalan Yemek ----------- ",depo1)
        print("Pazartesiden Aktarılan Yemek ------- ",round(depo1*0.10))
        print("Dünden Kalan Yemek ----------------- ",depo2)
        print("Dünden Aktarılan Yemek ------------- ",round(depo2*0.10))
        print("Önceki Günlerden Aktarılan Yemek --- ",round(depo1*0.10)+round(depo2*0.10))
        print("Günlük Çıkan Yemek ----------------- ",yemek3)
        print("Toplam Çıkan Yemek ----------------- ",cikanYemek3)
        
        if depo1 == 0: # depo1'in 0,
            
            if depo2 == 0: #depo2'nin 0 olduğu durum.
                
                if kalanYemek3 < 0:
                    
                    acKalanMusteri3 = abs(kalanYemek3)
            
                    print("Kalan Yemek ------------------------  0")
                    print("Depolanan Yemek --------------------  0")   
                    print("Aç Kalan Müşteri ------------------- ",acKalanMusteri3)
                
                else:
                    
                    depo3 = kalanYemek3

                    print("Kalan Yemek ------------------------ ",kalanYemek3)
                    print("Depolanan Yemek -------------------- ",depo3)        
                
            else: # depo1'in 0 depo2'nin 1 olduğu durum
            
                if onceDepo2 > 0:
                    
                    depo2 = depo2 + onceDepo2
                    yemek3 = depo3
                
                    print("Dünden Kalan Yemekten Kalan -------- ",depo2)
                    print("Dünden Aktarılan Yemek ------------- ",round(depo2*0.10))
                    print("Kalan Yemek ------------------------ ",yemek3)
                    print("Toplam Kalan Yemek ----------------- ",depo2+yemek3)
                    print("Depolanan Yemek -------------------- ",yemek3+onceDepo2)
                    
                else:
                    
                    if kalanYemek3 < 0:
                        
                        acKalanMusteri3 = abs(kalanYemek3)
                        depo2 = depo2 - round(depo2*0.10) 
            
                        print("Kalan Yemek ------------------------  0")
                        print("Depolanan Yemek --------------------  0")   
                        print("Aç Kalan Müşteri ------------------- ",acKalanMusteri3)
                        
                    else:
                        
                        depo2 = depo2 - round(depo2*0.10)
                        depo3 = kalanYemek3
            
                        print("Kalan Yemek ------------------------ ",kalanYemek3)
                        print("Depolanan Yemek -------------------- ",depo3)
                        
        else: # depo1'in dolu,
            
            if depo2 == 0: # depo2'nin boş olduğu durum
                
                if onceDepo1 > 0:
                    
                    depo1 = depo1 + onceDepo1
                    yemek3 = depo3
                    
                    print("Dünden Kalan Yemekten Kalan -------- ",depo1)
                    print("Dünden Aktarılan Yemek ------------- ",round(depo1*0.10))
                    print("Kalan Yemek ------------------------ ",yemek3)
                    print("Toplam Kalan Yemek ----------------- ",depo1+yemek3)
                    print("Depolanan Yemek -------------------- ",onceDepo1+yemek3)
                    
                else:
                    
                    if kalanYemek3 < 0:
                        
                        acKalanMusteri3 = abs(kalanYemek3)
                        depo1 = depo1 - round(depo1*0.10)
                    
                        print("Kalan Yemek ------------------------  0")
                        print("Depolanan Yemek --------------------  0")   
                        print("Aç Kalan Müşteri ------------------- ",acKalanMusteri3)
                    
                    else:
                        
                        depo1 = depo1 - round(depo1*0.10)
                        depo3 = kalanYemek3
                        
                        print("Kalan Yemek ------------------------ ",kalanYemek3)
                        print("Depolanan Yemek -------------------- ",depo3)
                        
            else: # Tüm depoların dolu olduğu durum.
                
                if onceDepo1 > 0: # depo1'e öncelik verir ve durumunu kontrol eder.
                    
                    depo1 = depo1 + onceDepo1
                    yemek3 = depo3
                    
                    print("Pazartesiden Kalan Yemek ----------- ",depo1)
                    print("Pazartesiden Aktarılan Yemek ------- ",round(depo1*0.10))
                    print("Dünden Kalan Yemekten Kalan -------- ",depo2)
                    print("Dünden Aktarılan Yemek ------------- ",round(depo2*0.10))
                    print("Kalan Yemek ------------------------ ",yemek3)
                    print("Toplam Kalan Yemek ----------------- ",onceDepo1+depo2+yemek3)
                    print("Depolanan Yemek -------------------- ",onceDepo1+depo2+yemek3)
                          
                else: # Eğer depo1 yeterli değil ise depo2 ile birlikteki durumunu kontrol eder.
                    
                    if onceDepo2 > 0:

                        depo2 = depo2 + onceDepo2 # depo1'deki yemekler zaten kullanılacağından onceDepo2'nin içerisinde
                        yemek3 = depo3
                        
                        print("Pazartesiden Kalan Yemek ----------- ",depo1)
                        print("Pazartesiden Aktarılan Yemek ------- ",round(depo1*0.10))                    
                        print("Dünden Kalan Yemekten Kalan -------- ",depo2)
                        print("Dünden Aktarılan Yemek ------------- ",round(depo2*0.10))
                        print("Kalan Yemek ------------------------ ",yemek3)
                        print("Toplam Kalan Yemek ----------------- ",depo2+yemek3)
                        print("Depolanan Yemek -------------------- ",onceDepo2+yemek3)

                    else: # Eğer 2 depoda yeterli değilse toplam çıkan yemeğin durumunu kontrol eder.
                        
                        if kalanYemek3 < 0:
                            
                            acKalanMusteri3 = abs(kalanYemek3)
                            depo1 = depo1 - round(depo1*0.10)
                            depo2 = depo2 - round(depo2*0.10)
                        
                            print("Kalan Yemek ------------------------  0")
                            print("Depolanan Yemek --------------------  0")   
                            print("Aç Kalan Müşteri ------------------- ",acKalanMusteri3)

                        else: # Eğer toplam çıkan yemek fazla ise ;                          

                            depo1 = depo1 - round(depo1*0.10) # Kullanılan yemekleri depo1 den eksiltir.
                            depo2 = depo2 - round(depo2*0.10) # Kullanılan yemekleri depo2 den eksiltir.
                            depo3 = kalanYemek3
                            
                            print("Kalan Yemek ------------------------ ",kalanYemek3)
                            print("Depolanan Yemek -------------------- ",depo3)                                      
            
        print("                                          ")
        print("Pazartesi Deposu ------------------- ",depo1)
        print("Salı Deposu ------------------------ ",depo2)
        print("Carsamba Deposu -------------------- ",depo3)
        print("//////////////////////////////////////// ")
        
    if i == 4:
        
        musteri4 = musteri
        yemek4 = yemek
        acKalanMusteri4 = 0
        
        cikanYemek4 = round(depo1*0.10) + round(depo2*0.10) + round(depo3*0.10) + yemek4
        onceDepo1 = round(depo1*0.10) - musteri4
        onceDepo2 = round(depo1*0.10) + round(depo2*0.10) - musteri4
        onceDepo3 = round(depo1*0.10) + round(depo2*0.10) + round(depo3*0.10) - musteri4 # 3 deponunda gelen müşterilere yeterli gelip gelmediğini kontrol eder.
        
        kalanYemek4 = cikanYemek4 - musteri4
        
        print("            4. Gün            ")
        print("Müşteri ---------------------------- ",musteri4)
        print("Pazartesiden Kalan Yemek ----------- ",depo1)
        print("Pazartesiden Aktarılan Yemek ------- ",round(depo1*0.10))
        print("Salıdan Kalan Yemek ---------------- ",depo2)
        print("Salıdan Aktarılan Yemek ------------ ",round(depo2*0.10))
        print("Dünden Kalan Yemek ----------------- ",depo3)
        print("Dünden Aktarılan Yemek ------------- ",round(depo3*0.10))
        print("Önceki Günlerden Aktarılan Yemek --- ",round(depo1*0.10)+round(depo2*0.10)+round(depo3*0,10))
        print("Günlük Çıkan Yemek ----------------- ",yemek4)
        print("Toplam Çıkan Yemek ----------------- ",cikanYemek4)        
        
        if depo1 == 0:
            
            if depo2 == 0:
                
                if depo3 == 0:
                    
                    if kalanYemek4 < 0:
                        
                        acKalanMusteri4 = abs(kalanYemek4)
                
                        print("Kalan Yemek ------------------------  0")
                        print("Depolanan Yemek --------------------  0")   
                        print("Aç Kalan Müşteri ------------------- ",acKalanMusteri4)
                    
                    else:
                        
                        depo4 = kalanYemek4
    
                        print("Kalan Yemek ------------------------ ",kalanYemek4)
                        print("Depolanan Yemek -------------------- ",depo4)
                        
                else:
                    
                    if onceDepo3 > 0:
                        
                        depo3 = depo3 + onceDepo3
                        yemek4 = depo4
                    
                        print("Dünden Kalan Yemekten Kalan -------- ",depo3)
                        print("Dünden Aktarılan Yemek ------------- ",round(depo3*0.10))
                        print("Kalan Yemek ------------------------ ",yemek4)
                        print("Toplam Kalan Yemek ----------------- ",depo3+yemek4)
                        print("Depolanan Yemek -------------------- ",yemek4+onceDepo3)
                        
                    else:
                        
                        if kalanYemek4 < 0:
                            
                            acKalanMusteri4 = abs(kalanYemek4)
                            depo3 = depo3 - round(depo3*0.10) 
                
                            print("Kalan Yemek ------------------------  0")
                            print("Depolanan Yemek --------------------  0")   
                            print("Aç Kalan Müşteri ------------------- ",acKalanMusteri4)   
                        
                        else:
                            
                            depo3 = depo3 - round(depo3*0.10)
                            depo4 = kalanYemek4
                
                            print("Kalan Yemek ------------------------ ",kalanYemek4)
                            print("Depolanan Yemek -------------------- ",depo4)
                            
            else:
                
                if depo3 == 0:
                    
                    if onceDepo2 > 0:
                        
                        depo2 = depo2 + onceDepo2
                        yemek4 = depo4
                        
                        print("Salıdan Kalan Yemekten Kalan ------- ",depo2)
                        print("Salıdan Aktarılan Yemek ------------ ",round(depo2*0.10))
                        print("Kalan Yemek ------------------------ ",yemek4)
                        print("Toplam Kalan Yemek ----------------- ",depo2+yemek4)
                        print("Depolanan Yemek -------------------- ",onceDepo2+yemek4)
                        
                    else:
                        
                        if kalanYemek4 < 0:
                            
                            acKalanMusteri4 = abs(kalanYemek4)
                            depo2 = depo2 - round(depo2*0.10)
                        
                            print("Kalan Yemek ------------------------  0")
                            print("Depolanan Yemek --------------------  0")   
                            print("Aç Kalan Müşteri ------------------- ",acKalanMusteri4)
                        
                        else:
                            
                            depo2 = depo2 - round(depo2*0.10)
                            depo4 = kalanYemek4
                            
                            print("Kalan Yemek ------------------------ ",kalanYemek4)
                            print("Depolanan Yemek -------------------- ",depo4)
                            
                else:
                    
                    if onceDepo2 > 0:
                        
                        depo2 = depo2 + onceDepo2
                        yemek4 = depo4
                        
                        print("Salıdan Kalan Yemek ---------------- ",depo2)
                        print("Salıdan Aktarılan Yemek ------------ ",round(depo2*0.10))
                        print("Dünden Kalan Yemekten Kalan -------- ",depo3)
                        print("Dünden Aktarılan Yemek ------------- ",round(depo3*0.10))
                        print("Kalan Yemek ------------------------ ",yemek4)
                        print("Toplam Kalan Yemek ----------------- ",onceDepo2+depo3+yemek4)
                        print("Depolanan Yemek -------------------- ",onceDepo2+depo3+yemek4)
                              
                    else:
                        
                        if onceDepo3 > 0:
    
                            depo3 = depo3 + onceDepo3
                            yemek4 = depo4
                            
                            print("Salıdan Kalan Yemek ---------------- ",depo2)
                            print("Salıdan Aktarılan Yemek ------------ ",round(depo2*0.10))                    
                            print("Dünden Kalan Yemekten Kalan -------- ",depo3)
                            print("Dünden Aktarılan Yemek ------------- ",round(depo3*0.10))
                            print("Kalan Yemek ------------------------ ",yemek4)
                            print("Toplam Kalan Yemek ----------------- ",depo3+yemek4)
                            print("Depolanan Yemek -------------------- ",onceDepo3+yemek4)
    
                        else:
                            
                            if kalanYemek4 < 0:
                                
                                acKalanMusteri4 = abs(kalanYemek4)
                                depo2 = depo2 - round(depo2*0.10)
                                depo3 = depo3 - round(depo3*0.10)
                            
                                print("Kalan Yemek ------------------------  0")
                                print("Depolanan Yemek --------------------  0")   
                                print("Aç Kalan Müşteri ------------------- ",acKalanMusteri4)
    
                            else:                            
    
                                depo2 = depo2 - round(depo2*0.10)
                                depo3 = depo3 - round(depo3*0.10)
                                depo4 = kalanYemek4
                                
                                print("Kalan Yemek ------------------------ ",kalanYemek4)
                                print("Depolanan Yemek -------------------- ",depo4) 

        else:
            
            if depo2 == 0:
                
                if depo3 == 0:
                    
                    if onceDepo1 > 0:
                        
                        depo1 = depo1 + onceDepo1
                        yemek4 = depo4
                        
                        print("Pazartesiden Kalan Yemekten Kalan -- ",depo1)
                        print("Pazartesiden Aktarılan Yemek ------- ",round(depo1*0.10))
                        print("Kalan Yemek ------------------------ ",yemek4)
                        print("Toplam Kalan Yemek ----------------- ",depo1+yemek4)
                        print("Depolanan Yemek -------------------- ",onceDepo1+yemek4)
                        
                    else:
                        
                        if kalanYemek4 < 0:
                            
                            acKalanMusteri4 = abs(kalanYemek4)
                            depo1 = depo1 - round(depo1*0.10)
                        
                            print("Kalan Yemek ------------------------  0")
                            print("Depolanan Yemek --------------------  0")   
                            print("Aç Kalan Müşteri ------------------- ",acKalanMusteri4)
                        
                        else:
                            
                            depo1 = depo1 - round(depo2*0.10)
                            depo4 = kalanYemek4
                            
                            print("Kalan Yemek ------------------------ ",kalanYemek4)
                            print("Depolanan Yemek -------------------- ",depo4)
                            
                else:
                    
                    if onceDepo1 > 0:                    
                        
                        depo1 = depo1 + onceDepo1
                        yemek4 = depo4
                        
                        print("Pazartesiden Kalan Yemekten Kalan -- ",depo1)
                        print("Pazartesiden Aktarılan Yemek ------- ",round(depo1*0.10))
                        print("Kalan Yemek ------------------------ ",yemek4)
                        print("Toplam Kalan Yemek ----------------- ",depo1+yemek4)
                        print("Depolanan Yemek -------------------- ",onceDepo1+yemek4)
                    
                    else:
                        
                        if onceDepo3 > 0:
                            
                            depo3 = depo3 + onceDepo3
                            yemek4 = depo4
                            
                            print("Dünden Kalan Yemekten Kalan -------- ",depo3)
                            print("Dünden Aktarılan Yemek ------------- ",round(depo3*0.10))
                            print("Kalan Yemek ------------------------ ",yemek4)
                            print("Toplam Kalan Yemek ----------------- ",depo3+yemek4)
                            print("Depolanan Yemek -------------------- ",onceDepo3+yemek4)

                        else:
                            
                             if kalanYemek4 < 0:
                                
                                acKalanMusteri4 = abs(kalanYemek4)
                                depo1 = depo1 - round(depo1*0.10)
                                depo3 = depo3 - round(depo3*0.10)
                            
                                print("Kalan Yemek ------------------------  0")
                                print("Depolanan Yemek --------------------  0")   
                                print("Aç Kalan Müşteri ------------------- ",acKalanMusteri4)
    
                             else:                            
    
                                depo1 = depo1 - round(depo1*0.10)
                                depo3 = depo3 - round(depo3*0.10)
                                depo4 = kalanYemek4
                                
                                print("Kalan Yemek ------------------------ ",kalanYemek4)
                                print("Depolanan Yemek -------------------- ",depo4)
                                
            else:
                
                if depo3 == 0:
                    
                    if onceDepo1 > 0:
                        
                        depo1 = depo1 + onceDepo1
                        yemek4 = depo4
                        
                        print("Pazartesiden Kalan Yemekten Kalan -- ",depo1)
                        print("Pazartesiden Aktarılan Yemek ------- ",round(depo1*0.10))
                        print("Kalan Yemek ------------------------ ",yemek4)
                        print("Toplam Kalan Yemek ----------------- ",depo1+yemek4)
                        print("Depolanan Yemek -------------------- ",onceDepo1+yemek4)
                        
                    else:
                        
                        if kalanYemek4 < 0:
                            
                            acKalanMusteri4 = abs(kalanYemek4)
                            depo1 = depo1 - round(depo1*0.10)
                        
                            print("Kalan Yemek ------------------------  0")
                            print("Depolanan Yemek --------------------  0")   
                            print("Aç Kalan Müşteri ------------------- ",acKalanMusteri4)
                        
                        else:
                            
                            depo1 = depo1 - round(depo1*0.10)
                            depo4 = kalanYemek4
                            
                            print("Kalan Yemek ------------------------ ",kalanYemek4)
                            print("Depolanan Yemek -------------------- ",depo4)
                            
                else:
                    
                    if onceDepo2 > 0:                    
                        
                        depo2 = depo2 + onceDepo2
                        yemek4 = depo4
                        
                        print("Salıdan Kalan Yemekten Kalan ------- ",depo2)
                        print("Salıdan Aktarılan Yemek ------------ ",round(depo2*0.10))
                        print("Kalan Yemek ------------------------ ",yemek4)
                        print("Toplam Kalan Yemek ----------------- ",depo2+yemek4)
                        print("Depolanan Yemek -------------------- ",onceDepo2+yemek4)
                    
                    else:                        
                                                  
                        if kalanYemek4 < 0:
                                
                            acKalanMusteri4 = abs(kalanYemek4)
                            depo1 = depo1 - round(depo1*0.10)
                            depo2 = depo2 - round(depo2*0.10)
                            
                            print("Kalan Yemek ------------------------  0")
                            print("Depolanan Yemek --------------------  0")   
                            print("Aç Kalan Müşteri ------------------- ",acKalanMusteri4)
    
                        else:                            
    
                            depo1 = depo1 - round(depo1*0.10)
                            depo2 = depo2 - round(depo2*0.10)
                            depo4 = kalanYemek4
                                
                            print("Kalan Yemek ------------------------ ",kalanYemek4)
                            print("Depolanan Yemek -------------------- ",depo4)
                            
        print("                                          ")
        print("Pazartesi Deposu ------------------- ",depo1)
        print("Salı Deposu ------------------------ ",depo2)
        print("Carsamba Deposu -------------------- ",depo3)
        print("Perşembe Deposu -------------------- ",depo4)
        print("//////////////////////////////////////// ")
                                                    
                                                        
    if i == 5:
        
        musteri5 = musteri
        yemek5 = yemek
        acKalanMusteri5 = 0
        
        copeGiden1 = depo1
        depo1 = 0 # depo1'deki yemekler 3. günün sonunda çöpe gitti.
        
        cikanYemek5 = round(depo2*0.10) + round(depo3*0.10) + round(depo4*0.10) + yemek5
        onceDepo2 = round(depo2*0.10) - musteri5
        onceDepo3 = round(depo2*0.10) + round(depo3*0.10) - musteri5
        onceDepo4 = round(depo2*0.10) + round(depo3*0.10) + round(depo4*0.10) - musteri5
        
        kalanYemek5 = cikanYemek5 - musteri5
        
        print("            5. Gün            ")
        print("Müşteri ---------------------------- ",musteri5)
        print("Salıdan Kalan Yemek ---------------- ",depo2)
        print("Salıdan Aktarılan Yemek ------------ ",round(depo2*0.10))
        print("Çarşambadan Kalan Yemek ------------ ",depo3)
        print("Çarşambadan Aktarılan Yemek--------- ",round(depo3*0.10))
        print("Dünden Kalan Yemek ----------------- ",depo4)
        print("Dünden Aktarılan Yemek ------------- ",round(depo4*0.10))
        print("Önceki Günlerden Aktarılan Yemek --- ",round(depo2*0.10)+round(depo3*0.10)+round(depo4*0,10))
        print("Günlük Çıkan Yemek ----------------- ",yemek5)
        print("Toplam Çıkan Yemek ----------------- ",cikanYemek5)        
        
        if depo2 == 0:
            
            if depo3 == 0:
                
                if depo4 == 0:
                    
                    if kalanYemek5 < 0:
                        
                        acKalanMusteri5 = abs(kalanYemek5)
                
                        print("Kalan Yemek ------------------------  0")
                        print("Depolanan Yemek --------------------  0")   
                        print("Aç Kalan Müşteri ------------------- ",acKalanMusteri5)
                    
                    else:
                        
                        depo5 = kalanYemek5
    
                        print("Kalan Yemek ------------------------ ",kalanYemek5)
                        print("Depolanan Yemek -------------------- ",depo5)
                        
                else:
                    
                    if onceDepo4 > 0:
                        
                        depo4 = depo4 + onceDepo4
                        yemek5 = depo5
                    
                        print("Dünden Kalan Yemekten Kalan -------- ",depo4)
                        print("Dünden Aktarılan Yemek ------------- ",round(depo4*0.10))
                        print("Kalan Yemek ------------------------ ",yemek5)
                        print("Toplam Kalan Yemek ----------------- ",depo4+yemek5)
                        print("Depolanan Yemek -------------------- ",yemek5+onceDepo4)
                        
                    else:
                        
                        if kalanYemek5 < 0:
                            
                            acKalanMusteri5 = abs(kalanYemek5)
                            depo4 = depo4 - round(depo4*0.10) 
                
                            print("Kalan Yemek ------------------------  0")
                            print("Depolanan Yemek --------------------  0")   
                            print("Aç Kalan Müşteri ------------------- ",acKalanMusteri5)   
                        
                        else:
                            
                            depo4 = depo4 - round(depo4*0.10)
                            depo5 = kalanYemek5
                
                            print("Kalan Yemek ------------------------ ",kalanYemek5)
                            print("Depolanan Yemek -------------------- ",depo5)
                            
            else:
                
                if depo4 == 0:
                    
                    if onceDepo3 > 0:
                        
                        depo3 = depo3 + onceDepo3
                        yemek5 = depo5
                        
                        print("Çarşambadan Kalan Yemekten Kalan --- ",depo3)
                        print("Çarşambadan Aktarılan Yemek -------- ",round(depo3*0.10))
                        print("Kalan Yemek ------------------------ ",yemek5)
                        print("Toplam Kalan Yemek ----------------- ",depo3+yemek5)
                        print("Depolanan Yemek -------------------- ",onceDepo3+yemek5)
                        
                    else:
                        
                        if kalanYemek5 < 0:
                            
                            acKalanMusteri5 = abs(kalanYemek5)
                            depo3 = depo3 - round(depo3*0.10)
                        
                            print("Kalan Yemek ------------------------  0")
                            print("Depolanan Yemek --------------------  0")   
                            print("Aç Kalan Müşteri ------------------- ",acKalanMusteri5)
                        
                        else:
                            
                            depo3 = depo3 - round(depo3*0.10)
                            depo5 = kalanYemek5
                            
                            print("Kalan Yemek ------------------------ ",kalanYemek5)
                            print("Depolanan Yemek -------------------- ",depo5)
                            
                else:
                    
                    if onceDepo3 > 0:
                        
                        depo3 = depo3 + onceDepo3
                        yemek5 = depo5
                        
                        print("Çarşambadan Kalan Yemek ------------ ",depo3)
                        print("Çarşambadan Aktarılan Yemek -------- ",round(depo3*0.10))
                        print("Dünden Kalan Yemekten Kalan -------- ",depo4)
                        print("Dünden Aktarılan Yemek ------------- ",round(depo4*0.10))
                        print("Kalan Yemek ------------------------ ",yemek5)
                        print("Toplam Kalan Yemek ----------------- ",onceDepo3+depo4+yemek5)
                        print("Depolanan Yemek -------------------- ",onceDepo3+depo4+yemek5)
                              
                    else:
                        
                        if onceDepo4 > 0:
    
                            depo4 = depo4 + onceDepo4
                            yemek5 = depo5
                            
                            print("Çarşambadan Kalan Yemek ------------ ",depo3)
                            print("Çarşambadan Aktarılan Yemek -------- ",round(depo3*0.10))                    
                            print("Dünden Kalan Yemekten Kalan -------- ",depo4)
                            print("Dünden Aktarılan Yemek ------------- ",round(depo4*0.10))
                            print("Kalan Yemek ------------------------ ",yemek5)
                            print("Toplam Kalan Yemek ----------------- ",depo4+yemek5)
                            print("Depolanan Yemek -------------------- ",onceDepo4+yemek5)
    
                        else:
                            
                            if kalanYemek5 < 0:
                                
                                acKalanMusteri5 = abs(kalanYemek5)
                                depo3 = depo3 - round(depo3*0.10)
                                depo4 = depo4 - round(depo4*0.10)
                            
                                print("Kalan Yemek ------------------------  0")
                                print("Depolanan Yemek --------------------  0")   
                                print("Aç Kalan Müşteri ------------------- ",acKalanMusteri5)
    
                            else:                            
    
                                depo3 = depo3 - round(depo3*0.10)
                                depo4 = depo4 - round(depo4*0.10)
                                depo5 = kalanYemek5
                                
                                print("Kalan Yemek ------------------------ ",kalanYemek5)
                                print("Depolanan Yemek -------------------- ",depo5) 

        else:
            
            if depo3 == 0:
                
                if depo4 == 0:
                    
                    if onceDepo2 > 0:
                        
                        depo2 = depo2 + onceDepo2
                        yemek5 = depo5
                        
                        print("Salıdan Kalan Yemekten Kalan ------ ",depo2)
                        print("Salıdan Aktarılan Yemek ------------ ",round(depo2*0.10))
                        print("Kalan Yemek ------------------------ ",yemek5)
                        print("Toplam Kalan Yemek ----------------- ",depo2+yemek5)
                        print("Depolanan Yemek -------------------- ",onceDepo2+yemek5)
                        
                    else:
                        
                        if kalanYemek5 < 0:
                            
                            acKalanMusteri5 = abs(kalanYemek5)
                            depo2 = depo2 - round(depo2*0.10)
                        
                            print("Kalan Yemek ------------------------  0")
                            print("Depolanan Yemek --------------------  0")   
                            print("Aç Kalan Müşteri ------------------- ",acKalanMusteri5)
                        
                        else:
                            
                            depo2 = depo2 - round(depo2*0.10)
                            depo5 = kalanYemek5
                            
                            print("Kalan Yemek ------------------------ ",kalanYemek5)
                            print("Depolanan Yemek -------------------- ",depo5)
                            
                else:
                    
                    if onceDepo2 > 0:                    
                        
                        depo2 = depo2 + onceDepo2
                        yemek5 = depo5
                        
                        print("Salıdan Kalan Yemekten Kalan ------- ",depo2)
                        print("Salıdan Aktarılan Yemek ------------ ",round(depo2*0.10))
                        print("Kalan Yemek ------------------------ ",yemek5)
                        print("Toplam Kalan Yemek ----------------- ",depo2+yemek5)
                        print("Depolanan Yemek -------------------- ",onceDepo2+yemek5)
                    
                    else:
                        
                        if onceDepo4 > 0:
                            
                            depo4 = depo4 + onceDepo4
                            yemek5 = depo5
                            
                            print("Dünden Kalan Yemekten Kalan -------- ",depo4)
                            print("Dünden Aktarılan Yemek ------------- ",round(depo4*0.10))
                            print("Kalan Yemek ------------------------ ",yemek5)
                            print("Toplam Kalan Yemek ----------------- ",depo4+yemek5)
                            print("Depolanan Yemek -------------------- ",onceDepo4+yemek5)

                        else:
                            
                             if kalanYemek5 < 0:
                                
                                acKalanMusteri5 = abs(kalanYemek5)
                                depo2 = depo2 - round(depo2*0.10)
                                depo4 = depo4 - round(depo4*0.10)
                            
                                print("Kalan Yemek ------------------------  0")
                                print("Depolanan Yemek --------------------  0")   
                                print("Aç Kalan Müşteri ------------------- ",acKalanMusteri5)
    
                             else:                            
    
                                depo2 = depo2 - round(depo2*0.10)
                                depo4 = depo4 - round(depo4*0.10)
                                depo5 = kalanYemek5
                                
                                print("Kalan Yemek ------------------------ ",kalanYemek5)
                                print("Depolanan Yemek -------------------- ",depo5)
                                
            else:
                
                if depo4 == 0:
                    
                    if onceDepo2 > 0:
                        
                        depo2 = depo2 + onceDepo2
                        yemek5 = depo5
                        
                        print("Salıdan Kalan Yemekten Kalan ------- ",depo2)
                        print("Salıdan Aktarılan Yemek ------------ ",round(depo2*0.10))
                        print("Kalan Yemek ------------------------ ",yemek5)
                        print("Toplam Kalan Yemek ----------------- ",depo2+yemek5)
                        print("Depolanan Yemek -------------------- ",onceDepo2+yemek5)
                        
                    else:
                        
                        if kalanYemek5 < 0:
                            
                            acKalanMusteri5 = abs(kalanYemek5)
                            depo2 = depo2 - round(depo2*0.10)
                        
                            print("Kalan Yemek ------------------------  0")
                            print("Depolanan Yemek --------------------  0")   
                            print("Aç Kalan Müşteri ------------------- ",acKalanMusteri5)
                        
                        else:
                            
                            depo2 = depo2 - round(depo2*0.10)
                            depo5 = kalanYemek5
                            
                            print("Kalan Yemek ------------------------ ",kalanYemek5)
                            print("Depolanan Yemek -------------------- ",depo5)
                            
                else:
                    
                    if onceDepo2 > 0:                    
                        
                        depo2 = depo2 + onceDepo2
                        yemek5 = depo5
                        
                        print("Carsambadan Kalan Yemekten Kalan --- ",depo3)
                        print("Carsabadan Aktarılan Yemek --------- ",round(depo3*0.10))
                        print("Kalan Yemek ------------------------ ",yemek5)
                        print("Toplam Kalan Yemek ----------------- ",depo3+yemek5)
                        print("Depolanan Yemek -------------------- ",onceDepo3+yemek5)
                    
                    else:                        
                                                  
                        if kalanYemek5 < 0:
                                
                            acKalanMusteri5 = abs(kalanYemek5)
                            depo2 = depo2 - round(depo2*0.10)
                            depo3 = depo3 - round(depo3*0.10)
                            
                            print("Kalan Yemek ------------------------  0")
                            print("Depolanan Yemek --------------------  0")   
                            print("Aç Kalan Müşteri ------------------- ",acKalanMusteri5)
    
                        else:                            
    
                            depo2 = depo2 - round(depo2*0.10)
                            depo3 = depo3 - round(depo3*0.10)
                            depo5 = kalanYemek5
                                
                            print("Kalan Yemek ------------------------ ",kalanYemek5)
                            print("Depolanan Yemek -------------------- ",depo5)
                            
        print("                                          ")
        print("Salı Deposu ------------------------ ",depo2)
        print("Carsamba Deposu -------------------- ",depo3)
        print("Perşembe Deposu -------------------- ",depo4)
        print("Cuma Deposu ------------------------ ",depo5)
        print("//////////////////////////////////////// ")                    
                    

    if i == 6:
        
        musteri6 = musteri
        yemek6 = yemek
        acKalanMusteri6 = 0
        
        copeGiden2 = depo2
        depo2 = 0
        
        cikanYemek6 = round(depo3*0.10) + round(depo4*0.10) + round(depo5*0.10) + yemek6
        onceDepo3 = round(depo3*0.10) - musteri6
        onceDepo4 = round(depo3*0.10) + round(depo4*0.10) - musteri6
        onceDepo5 = round(depo3*0.10) + round(depo4*0.10) + round(depo5*0.10) - musteri6
        
        kalanYemek6 = cikanYemek6 - musteri6
        
        print("            6. Gün            ")
        print("Müşteri ---------------------------- ",musteri6)
        print("Çarşambadan Kalan Yemek ------------ ",depo3)
        print("Çarşambadan Aktarılan Yemek -------- ",round(depo3*0.10))
        print("Perşembeden Kalan Yemek ------------ ",depo4)
        print("Perşembeden Aktarılan Yemek--------- ",round(depo4*0.10))
        print("Dünden Kalan Yemek ----------------- ",depo5)
        print("Dünden Aktarılan Yemek ------------- ",round(depo5*0.10))
        print("Önceki Günlerden Aktarılan Yemek --- ",round(depo3*0.10)+round(depo4*0.10)+round(depo5*0,10))
        print("Günlük Çıkan Yemek ----------------- ",yemek6)
        print("Toplam Çıkan Yemek ----------------- ",cikanYemek6)        
        
        if depo3 == 0:
            
            if depo4 == 0:
                
                if depo5 == 0:
                    
                    if kalanYemek6 < 0:
                        
                        acKalanMusteri6 = abs(kalanYemek6)
                
                        print("Kalan Yemek ------------------------  0")
                        print("Depolanan Yemek --------------------  0")   
                        print("Aç Kalan Müşteri ------------------- ",acKalanMusteri6)
                    
                    else:
                        
                        depo6 = kalanYemek6
    
                        print("Kalan Yemek ------------------------ ",kalanYemek6)
                        print("Depolanan Yemek -------------------- ",depo6)
                        
                else:
                    
                    if onceDepo5 > 0:
                        
                        depo5 = depo5 + onceDepo5
                        yemek6 = depo6
                    
                        print("Dünden Kalan Yemekten Kalan -------- ",depo5)
                        print("Dünden Aktarılan Yemek ------------- ",round(depo5*0.10))
                        print("Kalan Yemek ------------------------ ",yemek6)
                        print("Toplam Kalan Yemek ----------------- ",depo5+yemek6)
                        print("Depolanan Yemek -------------------- ",yemek6+onceDepo5)
                        
                    else:
                        
                        if kalanYemek6 < 0:
                            
                            acKalanMusteri6 = abs(kalanYemek6)
                            depo5 = depo5 - round(depo5*0.10) 
                
                            print("Kalan Yemek ------------------------  0")
                            print("Depolanan Yemek --------------------  0")   
                            print("Aç Kalan Müşteri ------------------- ",acKalanMusteri6)
                        
                        else:
                            
                            depo5 = depo5 - round(depo5*0.10)
                            depo6 = kalanYemek6
                
                            print("Kalan Yemek ------------------------ ",kalanYemek6)
                            print("Depolanan Yemek -------------------- ",depo6)
                            
            else:
                
                if depo5 == 0:
                    
                    if onceDepo4 > 0:
                        
                        depo4 = depo4 + onceDepo4
                        yemek6 = depo6
                        
                        print("Perşembeden Kalan Yemekten Kalan --- ",depo4)
                        print("Perşembeden Aktarılan Yemek -------- ",round(depo4*0.10))
                        print("Kalan Yemek ------------------------ ",yemek6)
                        print("Toplam Kalan Yemek ----------------- ",depo4+yemek6)
                        print("Depolanan Yemek -------------------- ",onceDepo4+yemek6) 
                        
                    else:
                        
                        if kalanYemek6 < 0:
                            
                            acKalanMusteri6 = abs(kalanYemek6)
                            depo4 = depo4 - round(depo4*0.10)
                        
                            print("Kalan Yemek ------------------------  0")
                            print("Depolanan Yemek --------------------  0")   
                            print("Aç Kalan Müşteri ------------------- ",acKalanMusteri6)
                        
                        else:
                            
                            depo4 = depo4 - round(depo4*0.10)
                            depo6 = kalanYemek6
                            
                            print("Kalan Yemek ------------------------ ",kalanYemek6)
                            print("Depolanan Yemek -------------------- ",depo6)
                            
                else:
                    
                    if onceDepo4 > 0:
                        
                        depo4 = depo4 + onceDepo4
                        yemek6 = depo6
                        
                        print("Perşembeden Kalan Yemek ------------ ",depo4)
                        print("Perşembeden Aktarılan Yemek -------- ",round(depo4*0.10))
                        print("Dünden Kalan Yemekten Kalan -------- ",depo5)
                        print("Dünden Aktarılan Yemek ------------- ",round(depo5*0.10))
                        print("Kalan Yemek ------------------------ ",yemek6)
                        print("Toplam Kalan Yemek ----------------- ",onceDepo4+depo5+yemek6)
                        print("Depolanan Yemek -------------------- ",onceDepo4+depo5+yemek6)
                              
                    else:
                        
                        if onceDepo5 > 0:
    
                            depo5 = depo5 + onceDepo5
                            yemek6 = depo6
                            
                            print("Perşembeden Kalan Yemek ------------ ",depo4)
                            print("Perşembeden Aktarılan Yemek -------- ",round(depo4*0.10))                    
                            print("Dünden Kalan Yemekten Kalan -------- ",depo5)
                            print("Dünden Aktarılan Yemek ------------- ",round(depo5*0.10))
                            print("Kalan Yemek ------------------------ ",yemek6)
                            print("Toplam Kalan Yemek ----------------- ",depo5+yemek6)
                            print("Depolanan Yemek -------------------- ",onceDepo5+yemek6)
    
                        else:
                            
                            if kalanYemek6 < 0:
                                
                                acKalanMusteri6 = abs(kalanYemek6)
                                depo4 = depo4 - round(depo4*0.10)
                                depo5 = depo5 - round(depo5*0.10)
                            
                                print("Kalan Yemek ------------------------  0")
                                print("Depolanan Yemek --------------------  0")   
                                print("Aç Kalan Müşteri ------------------- ",acKalanMusteri6)
    
                            else:                            
    
                                depo4 = depo4 - round(depo4*0.10)
                                depo5 = depo5 - round(depo5*0.10)
                                depo6 = kalanYemek6
                                
                                print("Kalan Yemek ------------------------ ",kalanYemek6)
                                print("Depolanan Yemek -------------------- ",depo6)

        else:
            
            if depo4 == 0:
                
                if depo5 == 0:
                    
                    if onceDepo3 > 0:
                        
                        depo3 = depo3 + onceDepo3
                        yemek6 = depo6
                        
                        print("Çarşambadan Kalan Yemekten Kalan --- ",depo3)
                        print("Çarşambadan Aktarılan Yemek -------- ",round(depo3*0.10))
                        print("Kalan Yemek ------------------------ ",yemek6)
                        print("Toplam Kalan Yemek ----------------- ",depo3+yemek6)
                        print("Depolanan Yemek -------------------- ",onceDepo3+yemek6)
                        
                    else:
                        
                        if kalanYemek6 < 0:
                            
                            acKalanMusteri6 = abs(kalanYemek6)
                            depo3 = depo3 - round(depo3*0.10)
                        
                            print("Kalan Yemek ------------------------  0")
                            print("Depolanan Yemek --------------------  0")   
                            print("Aç Kalan Müşteri ------------------- ",acKalanMusteri6)
                        
                        else:
                            
                            depo3 = depo3 - round(depo3*0.10)
                            depo6 = kalanYemek6
                            
                            print("Kalan Yemek ------------------------ ",kalanYemek6)
                            print("Depolanan Yemek -------------------- ",depo6)
                            
                else:
                    
                    if onceDepo3 > 0:                    
                        
                        depo3 = depo3 + onceDepo3
                        yemek6 = depo6
                        
                        print("Çarşambadan Kalan Yemekten Kalan --- ",depo3)
                        print("Çarşambadan Aktarılan Yemek -------- ",round(depo3*0.10))
                        print("Kalan Yemek ------------------------ ",yemek6)
                        print("Toplam Kalan Yemek ----------------- ",depo3+yemek6)
                        print("Depolanan Yemek -------------------- ",onceDepo3+yemek6)
                    
                    else:
                        
                        if onceDepo5 > 0:
                            
                            depo5 = depo5 + onceDepo5
                            yemek6 = depo6
                            
                            print("Dünden Kalan Yemekten Kalan -------- ",depo5)
                            print("Dünden Aktarılan Yemek ------------- ",round(depo5*0.10))
                            print("Kalan Yemek ------------------------ ",yemek6)
                            print("Toplam Kalan Yemek ----------------- ",depo5+yemek6)
                            print("Depolanan Yemek -------------------- ",onceDepo5+yemek6)

                        else:
                            
                             if kalanYemek6 < 0:
                                
                                acKalanMusteri6 = abs(kalanYemek6)
                                depo3 = depo3 - round(depo3*0.10)
                                depo5 = depo5 - round(depo5*0.10)
                            
                                print("Kalan Yemek ------------------------  0")
                                print("Depolanan Yemek --------------------  0")   
                                print("Aç Kalan Müşteri ------------------- ",acKalanMusteri6)
    
                             else:                            
    
                                depo3 = depo3 - round(depo3*0.10)
                                depo5 = depo5 - round(depo5*0.10)
                                depo6 = kalanYemek6
                                
                                print("Kalan Yemek ------------------------ ",kalanYemek6)
                                print("Depolanan Yemek -------------------- ",depo6)
                                
            else:
                
                if depo5 == 0:
                    
                    if onceDepo3 > 0:
                        
                        depo3 = depo3 + onceDepo3
                        yemek6 = depo6
                        
                        print("Çarşambadan Kalan Yemekten Kalan --- ",depo3)
                        print("Çarşambadan Aktarılan Yemek -------- ",round(depo3*0.10))
                        print("Kalan Yemek ------------------------ ",yemek6)
                        print("Toplam Kalan Yemek ----------------- ",depo3+yemek6)
                        print("Depolanan Yemek -------------------- ",onceDepo3+yemek6)
                        
                    else:
                        
                        if kalanYemek6 < 0:
                            
                            acKalanMusteri6 = abs(kalanYemek6)
                            depo3 = depo3 - round(depo3*0.10)
                        
                            print("Kalan Yemek ------------------------  0")
                            print("Depolanan Yemek --------------------  0")   
                            print("Aç Kalan Müşteri ------------------- ",acKalanMusteri6)
                        
                        else:
                            
                            depo3 = depo3 - round(depo3*0.10)
                            depo6 = kalanYemek6
                            
                            print("Kalan Yemek ------------------------ ",kalanYemek6)
                            print("Depolanan Yemek -------------------- ",depo6)
                            
                else:
                    
                    if onceDepo3 > 0:                    
                        
                        depo3 = depo3 + onceDepo3
                        yemek6 = depo6
                        
                        print("Perşembeden Kalan Yemekten Kalan --- ",depo4)
                        print("Perşembeden Aktarılan Yemek -------- ",round(depo4*0.10))
                        print("Kalan Yemek ------------------------ ",yemek6)
                        print("Toplam Kalan Yemek ----------------- ",depo4+yemek6)
                        print("Depolanan Yemek -------------------- ",onceDepo4+yemek6)
                    
                    else:                        
                                                  
                        if kalanYemek6 < 0:
                                
                            acKalanMusteri6 = abs(kalanYemek6)
                            depo3 = depo3 - round(depo3*0.10)
                            depo4 = depo4 - round(depo4*0.10)
                            
                            print("Kalan Yemek ------------------------  0")
                            print("Depolanan Yemek --------------------  0")   
                            print("Aç Kalan Müşteri ------------------- ",acKalanMusteri6)
    
                        else:                            
    
                            depo3 = depo3 - round(depo3*0.10)
                            depo4 = depo4 - round(depo4*0.10)
                            depo6 = kalanYemek6
                                
                            print("Kalan Yemek ------------------------ ",kalanYemek6)
                            print("Depolanan Yemek -------------------- ",depo6)
                            
        print("                                          ")
        print("Carsamba Deposu -------------------- ",depo3)
        print("Perşembe Deposu -------------------- ",depo4)
        print("Cuma Deposu ------------------------ ",depo5)
        print("Cumartesi Deposu ------------------- ",depo6)
        print("//////////////////////////////////////// ")
        
        
    if i == 7:
        
        musteri7 = musteri
        yemek7 = yemek
        acKalanMusteri7 = 0
        
        copeGiden3 = depo3
        depo3 = 0
        
        cikanYemek7 = round(depo4*0.10) + round(depo5*0.10) + round(depo6*0.10) + yemek7
        onceDepo4 = round(depo4*0.10) - musteri7
        onceDepo5 = round(depo4*0.10) + round(depo5*0.10) - musteri7
        onceDepo6 = round(depo4*0.10) + round(depo5*0.10) + round(depo6*0.10) - musteri7
        
        kalanYemek7 = cikanYemek7 - musteri7
        
        print("            7. Gün            ")
        print("Müşteri ---------------------------- ",musteri7)
        print("Perşembaden Kalan Yemek ------------ ",depo4)
        print("Perşembaden Aktarılan Yemek -------- ",round(depo4*0.10))
        print("Cumadan Kalan Yemek ---------------- ",depo5)
        print("Cumadan Aktarılan Yemek------------- ",round(depo5*0.10))
        print("Dünden Kalan Yemek ----------------- ",depo6)
        print("Dünden Aktarılan Yemek ------------- ",round(depo6*0.10))
        print("Önceki Günlerden Aktarılan Yemek --- ",round(depo4*0.10)+round(depo5*0.10)+round(depo6*0,10))
        print("Günlük Çıkan Yemek ----------------- ",yemek7)
        print("Toplam Çıkan Yemek ----------------- ",cikanYemek7)        
        
        if depo4 == 0:
            
            if depo5 == 0:
                
                if depo6 == 0:
                    
                    if kalanYemek7 < 0:
                        
                        acKalanMusteri7 = abs(kalanYemek7)
                
                        print("Kalan Yemek ------------------------  0")
                        print("Depolanan Yemek --------------------  0")   
                        print("Aç Kalan Müşteri ------------------- ",acKalanMusteri7)
                    
                    else:
                        
                        depo7 = kalanYemek7
    
                        print("Kalan Yemek ------------------------ ",kalanYemek7)
                        print("Depolanan Yemek -------------------- ",depo7)
                        
                else:
                    
                    if onceDepo6 > 0:
                        
                        depo6 = depo6 + onceDepo6
                        yemek7 = depo7
                    
                        print("Dünden Kalan Yemekten Kalan -------- ",depo6)
                        print("Dünden Aktarılan Yemek ------------- ",round(depo6*0.10))
                        print("Kalan Yemek ------------------------ ",yemek7)
                        print("Toplam Kalan Yemek ----------------- ",depo6+yemek7)
                        print("Depolanan Yemek -------------------- ",yemek7+onceDepo6)
                        
                    else:
                        
                        if kalanYemek7 < 0:
                            
                            acKalanMusteri7 = abs(kalanYemek7)
                            depo6 = depo6 - round(depo6*0.10) 
                
                            print("Kalan Yemek ------------------------  0")
                            print("Depolanan Yemek --------------------  0")   
                            print("Aç Kalan Müşteri ------------------- ",acKalanMusteri7)
                        
                        else:
                            
                            depo6 = depo6 - round(depo6*0.10)
                            depo7 = kalanYemek7
                
                            print("Kalan Yemek ------------------------ ",kalanYemek7)
                            print("Depolanan Yemek -------------------- ",depo7)
                            
            else:
                
                if depo6 == 0:
                    
                    if onceDepo5 > 0:
                        
                        depo5 = depo5 + onceDepo5
                        yemek7 = depo7
                        
                        print("Cumadan Kalan Yemekten Kalan ------- ",depo5)
                        print("Cumadan Aktarılan Yemek ------------ ",round(depo5*0.10))
                        print("Kalan Yemek ------------------------ ",yemek7)
                        print("Toplam Kalan Yemek ----------------- ",depo5+yemek7)
                        print("Depolanan Yemek -------------------- ",onceDepo5+yemek7) 
                        
                    else:
                        
                        if kalanYemek7 < 0:
                            
                            acKalanMusteri7 = abs(kalanYemek7)
                            depo5 = depo5 - round(depo5*0.10)
                        
                            print("Kalan Yemek ------------------------  0")
                            print("Depolanan Yemek --------------------  0")   
                            print("Aç Kalan Müşteri ------------------- ",acKalanMusteri7)
                        
                        else:
                            
                            depo5 = depo5 - round(depo5*0.10)
                            depo7 = kalanYemek7
                            
                            print("Kalan Yemek ------------------------ ",kalanYemek7)
                            print("Depolanan Yemek -------------------- ",depo7)
                            
                else:
                    
                    if onceDepo5 > 0:
                        
                        depo5 = depo5 + onceDepo5
                        yemek7 = depo7
                        
                        print("Cumadan Kalan Yemek ---------------- ",depo5)
                        print("Cumadan Aktarılan Yemek ------------ ",round(depo5*0.10))
                        print("Dünden Kalan Yemekten Kalan -------- ",depo6)
                        print("Dünden Aktarılan Yemek ------------- ",round(depo6*0.10))
                        print("Kalan Yemek ------------------------ ",yemek7)
                        print("Toplam Kalan Yemek ----------------- ",onceDepo5+depo6+yemek7)
                        print("Depolanan Yemek -------------------- ",onceDepo5+depo6+yemek7)
                              
                    else:
                        
                        if onceDepo6 > 0:
    
                            depo6 = depo6 + onceDepo6
                            yemek7 = depo7
                            
                            print("Cumadan Kalan Yemek ---------------- ",depo5)
                            print("Cumadan Aktarılan Yemek ------------ ",round(depo5*0.10))                    
                            print("Dünden Kalan Yemekten Kalan -------- ",depo6)
                            print("Dünden Aktarılan Yemek ------------- ",round(depo6*0.10))
                            print("Kalan Yemek ------------------------ ",yemek7)
                            print("Toplam Kalan Yemek ----------------- ",depo6+yemek7)
                            print("Depolanan Yemek -------------------- ",onceDepo6+yemek7)
    
                        else:
                            
                            if kalanYemek7 < 0:
                                
                                acKalanMusteri7 = abs(kalanYemek7)
                                depo5 = depo5 - round(depo5*0.10)
                                depo6 = depo6 - round(depo6*0.10)
                            
                                print("Kalan Yemek ------------------------  0")
                                print("Depolanan Yemek --------------------  0")   
                                print("Aç Kalan Müşteri ------------------- ",acKalanMusteri7)
    
                            else:                            
    
                                depo5 = depo5 - round(depo5*0.10)
                                depo6 = depo6 - round(depo6*0.10)
                                depo7 = kalanYemek7
                                
                                print("Kalan Yemek ------------------------ ",kalanYemek7)
                                print("Depolanan Yemek -------------------- ",depo7)

        else:
            
            if depo5 == 0:
                
                if depo6 == 0:
                    
                    if onceDepo4 > 0:
                        
                        depo4 = depo4 + onceDepo4
                        yemek7 = depo7
                        
                        print("Perşembeden Kalan Yemekten Kalan --- ",depo4)
                        print("Perşembeden Aktarılan Yemek -------- ",round(depo4*0.10))
                        print("Kalan Yemek ------------------------ ",yemek7)
                        print("Toplam Kalan Yemek ----------------- ",depo4+yemek7)
                        print("Depolanan Yemek -------------------- ",onceDepo4+yemek7)
                        
                    else:
                        
                        if kalanYemek7 < 0:
                            
                            acKalanMusteri7 = abs(kalanYemek7)
                            depo4 = depo4 - round(depo4*0.10)
                        
                            print("Kalan Yemek ------------------------  0")
                            print("Depolanan Yemek --------------------  0")   
                            print("Aç Kalan Müşteri ------------------- ",acKalanMusteri7)
                        
                        else:
                            
                            depo4 = depo4 - round(depo4*0.10)
                            depo7 = kalanYemek7
                            
                            print("Kalan Yemek ------------------------ ",kalanYemek7)
                            print("Depolanan Yemek -------------------- ",depo7)
                            
                else:
                    
                    if onceDepo4 > 0:                    
                        
                        depo4 = depo4 + onceDepo4
                        yemek7 = depo7
                        
                        print("Perşembeden Kalan Yemekten Kalan --- ",depo4)
                        print("Perşembeden Aktarılan Yemek -------- ",round(depo4*0.10))
                        print("Kalan Yemek ------------------------ ",yemek7)
                        print("Toplam Kalan Yemek ----------------- ",depo4+yemek7)
                        print("Depolanan Yemek -------------------- ",onceDepo4+yemek7)
                    
                    else:
                        
                        if onceDepo6 > 0:
                            
                            depo6 = depo6 + onceDepo6
                            yemek7 = depo7
                            
                            print("Dünden Kalan Yemekten Kalan -------- ",depo6)
                            print("Dünden Aktarılan Yemek ------------- ",round(depo6*0.10))
                            print("Kalan Yemek ------------------------ ",yemek7)
                            print("Toplam Kalan Yemek ----------------- ",depo6+yemek7)
                            print("Depolanan Yemek -------------------- ",onceDepo6+yemek7)

                        else:
                            
                             if kalanYemek7 < 0:
                                
                                acKalanMusteri7 = abs(kalanYemek7)
                                depo4 = depo4 - round(depo4*0.10)
                                depo6 = depo6 - round(depo6*0.10)
                            
                                print("Kalan Yemek ------------------------  0")
                                print("Depolanan Yemek --------------------  0")   
                                print("Aç Kalan Müşteri ------------------- ",acKalanMusteri7)
    
                             else:                            
    
                                depo4 = depo4 - round(depo4*0.10)
                                depo6 = depo6 - round(depo6*0.10)
                                depo7 = kalanYemek7
                                
                                print("Kalan Yemek ------------------------ ",kalanYemek7)
                                print("Depolanan Yemek -------------------- ",depo7)
                                
            else:
                
                if depo6 == 0:
                    
                    if onceDepo4 > 0:
                        
                        depo4 = depo4 + onceDepo4
                        yemek7 = depo7
                        
                        print("Perşembeden Kalan Yemekten Kalan --- ",depo4)
                        print("Perşembeden Aktarılan Yemek -------- ",round(depo4*0.10))
                        print("Kalan Yemek ------------------------ ",yemek7)
                        print("Toplam Kalan Yemek ----------------- ",depo4+yemek7)
                        print("Depolanan Yemek -------------------- ",onceDepo4+yemek7)
                        
                    else:
                        
                        if kalanYemek7 < 0:
                            
                            acKalanMusteri7 = abs(kalanYemek7)
                            depo4 = depo4 - round(depo4*0.10)
                        
                            print("Kalan Yemek ------------------------  0")
                            print("Depolanan Yemek --------------------  0")   
                            print("Aç Kalan Müşteri ------------------- ",acKalanMusteri7)
                        
                        else:
                            
                            depo4 = depo4 - round(depo4*0.10)
                            depo7 = kalanYemek7
                            
                            print("Kalan Yemek ------------------------ ",kalanYemek7)
                            print("Depolanan Yemek -------------------- ",depo7)
                            
                else:
                    
                    if onceDepo4 > 0:                    
                        
                        depo4 = depo4 + onceDepo4
                        yemek7 = depo7
                        
                        print("Cumadan Kalan Yemekten Kalan ------- ",depo5)
                        print("Cumadan Aktarılan Yemek ------------ ",round(depo5*0.10))
                        print("Kalan Yemek ------------------------ ",yemek7)
                        print("Toplam Kalan Yemek ----------------- ",depo5+yemek7)
                        print("Depolanan Yemek -------------------- ",onceDepo5+yemek7)
                    
                    else:                        
                                                  
                        if kalanYemek7 < 0:
                                
                            acKalanMusteri7 = abs(kalanYemek7)
                            depo4 = depo4 - round(depo4*0.10)
                            depo5 = depo5 - round(depo5*0.10)
                            
                            print("Kalan Yemek ------------------------  0")
                            print("Depolanan Yemek --------------------  0")   
                            print("Aç Kalan Müşteri ------------------- ",acKalanMusteri7)
    
                        else:                            
    
                            depo4 = depo4 - round(depo4*0.10)
                            depo5 = depo5 - round(depo5*0.10)
                            depo7 = kalanYemek7
                                
                            print("Kalan Yemek ------------------------ ",kalanYemek7)
                            print("Depolanan Yemek -------------------- ",depo7)
                            
        print("                                          ")
        print("Perşembe Deposu -------------------- ",depo4)
        print("Cuma Deposu ------------------------ ",depo5)
        print("Cumartesi Deposu ------------------- ",depo6)
        print("Pazar Deposu ----------------------- ",depo7)
        print("//////////////////////////////////////// ")


    if i == 8:
        
        musteri8 = musteri
        yemek8 = yemek
        acKalanMusteri8 = 0
        
        copeGiden4 = depo4
        depo4 = 0
        
        cikanYemek8 = round(depo5*0.10) + round(depo6*0.10) + round(depo7*0.10) + yemek8
        onceDepo5 = round(depo5*0.10) - musteri8
        onceDepo6 = round(depo5*0.10) + round(depo6*0.10) - musteri8
        onceDepo7 = round(depo5*0.10) + round(depo6*0.10) + round(depo7*0.10) - musteri8
        
        kalanYemek8 = cikanYemek8 - musteri8
        
        print("            8. Gün            ")
        print("Müşteri ---------------------------- ",musteri8)
        print("Cumadan Kalan Yemek ---------------- ",depo5)
        print("Cumadan Aktarılan Yemek ------------ ",round(depo5*0.10))
        print("Cumartesiden Kalan Yemek ----------- ",depo6)
        print("Cumartesiden Aktarılan Yemek ------- ",round(depo6*0.10))
        print("Dünden Kalan Yemek ----------------- ",depo7)
        print("Dünden Aktarılan Yemek ------------- ",round(depo7*0.10))
        print("Önceki Günlerden Aktarılan Yemek --- ",round(depo5*0.10)+round(depo6*0.10)+round(depo7*0,10))
        print("Günlük Çıkan Yemek ----------------- ",yemek8)
        print("Toplam Çıkan Yemek ----------------- ",cikanYemek8)        
        
        if depo5 == 0:
            
            if depo6 == 0:
                
                if depo7 == 0:
                    
                    if kalanYemek8 < 0:
                        
                        acKalanMusteri8 = abs(kalanYemek8)
                
                        print("Kalan Yemek ------------------------  0")
                        print("Depolanan Yemek --------------------  0")   
                        print("Aç Kalan Müşteri ------------------- ",acKalanMusteri8)
                    
                    else:
                        
                        depo8 = kalanYemek8
    
                        print("Kalan Yemek ------------------------ ",kalanYemek8)
                        print("Depolanan Yemek -------------------- ",depo8)
                        
                else:
                    
                    if onceDepo7 > 0:
                        
                        depo7 = depo7 + onceDepo7
                        yemek8 = depo8
                    
                        print("Dünden Kalan Yemekten Kalan -------- ",depo7)
                        print("Dünden Aktarılan Yemek ------------- ",round(depo7*0.10))
                        print("Kalan Yemek ------------------------ ",yemek8)
                        print("Toplam Kalan Yemek ----------------- ",depo7+yemek8)
                        print("Depolanan Yemek -------------------- ",yemek8+onceDepo7)
                        
                    else:
                        
                        if kalanYemek8 < 0:
                            
                            acKalanMusteri8 = abs(kalanYemek8)
                            depo7 = depo7 - round(depo7*0.10) 
                
                            print("Kalan Yemek ------------------------  0")
                            print("Depolanan Yemek --------------------  0")   
                            print("Aç Kalan Müşteri ------------------- ",acKalanMusteri8)
                        
                        else:
                            
                            depo7 = depo7 - round(depo7*0.10)
                            depo8 = kalanYemek8
                
                            print("Kalan Yemek ------------------------ ",kalanYemek8)
                            print("Depolanan Yemek -------------------- ",depo8)
                            
            else:
                
                if depo7 == 0:
                    
                    if onceDepo6 > 0:
                        
                        depo6 = depo6 + onceDepo6
                        yemek8 = depo8
                        
                        print("Cumartesi Kalan Yemekten Kalan ----- ",depo6)
                        print("Cumartesi Aktarılan Yemek ---------- ",round(depo6*0.10))
                        print("Kalan Yemek ------------------------ ",yemek8)
                        print("Toplam Kalan Yemek ----------------- ",depo6+yemek8)
                        print("Depolanan Yemek -------------------- ",onceDepo6+yemek8) 
                        
                    else:
                        
                        if kalanYemek8 < 0:
                            
                            acKalanMusteri8 = abs(kalanYemek8)
                            depo6 = depo6 - round(depo6*0.10)
                        
                            print("Kalan Yemek ------------------------  0")
                            print("Depolanan Yemek --------------------  0")   
                            print("Aç Kalan Müşteri ------------------- ",acKalanMusteri8)
                        
                        else:
                            
                            depo6 = depo6 - round(depo6*0.10)
                            depo8 = kalanYemek8
                            
                            print("Kalan Yemek ------------------------ ",kalanYemek8)
                            print("Depolanan Yemek -------------------- ",depo8)
                            
                else:
                    
                    if onceDepo6 > 0:
                        
                        depo6 = depo6 + onceDepo6
                        yemek8 = depo8
                        
                        print("Cumartesiden Kalan Yemek ----------- ",depo6)
                        print("Cumartesiden Aktarılan Yemek ------- ",round(depo6*0.10))
                        print("Dünden Kalan Yemekten Kalan -------- ",depo7)
                        print("Dünden Aktarılan Yemek ------------- ",round(depo7*0.10))
                        print("Kalan Yemek ------------------------ ",yemek8)
                        print("Toplam Kalan Yemek ----------------- ",onceDepo6+depo7+yemek8)
                        print("Depolanan Yemek -------------------- ",onceDepo6+depo7+yemek8)
                              
                    else:
                        
                        if onceDepo7 > 0:
    
                            depo7 = depo7 + onceDepo7
                            yemek8 = depo8
                            
                            print("Cumartesiden Kalan Yemek ----------- ",depo6)
                            print("Cumartesiden Aktarılan Yemek ------- ",round(depo6*0.10))                    
                            print("Dünden Kalan Yemekten Kalan -------- ",depo7)
                            print("Dünden Aktarılan Yemek ------------- ",round(depo7*0.10))
                            print("Kalan Yemek ------------------------ ",yemek8)
                            print("Toplam Kalan Yemek ----------------- ",depo7+yemek8)
                            print("Depolanan Yemek -------------------- ",onceDepo7+yemek8)
    
                        else:
                            
                            if kalanYemek8 < 0:
                                
                                acKalanMusteri8 = abs(kalanYemek8)
                                depo6 = depo6 - round(depo6*0.10)
                                depo7 = depo7 - round(depo7*0.10)
                            
                                print("Kalan Yemek ------------------------  0")
                                print("Depolanan Yemek --------------------  0")   
                                print("Aç Kalan Müşteri ------------------- ",acKalanMusteri8)
    
                            else:                            
    
                                depo6 = depo6 - round(depo6*0.10)
                                depo7 = depo7 - round(depo7*0.10)
                                depo8 = kalanYemek8
                                
                                print("Kalan Yemek ------------------------ ",kalanYemek8)
                                print("Depolanan Yemek -------------------- ",depo8)

        else:
            
            if depo6 == 0:
                
                if depo7 == 0:
                    
                    if onceDepo5 > 0:
                        
                        depo5 = depo5 + onceDepo5
                        yemek8 = depo8
                        
                        print("Cumadan Kalan Yemekten Kalan ------- ",depo5) # Burayı kontrol et
                        print("Cumadan Aktarılan Yemek ------------ ",round(depo5*0.10))
                        print("Kalan Yemek ------------------------ ",yemek8)
                        print("Toplam Kalan Yemek ----------------- ",depo5+yemek8)
                        print("Depolanan Yemek -------------------- ",onceDepo5+yemek8)
                        
                    else:
                        
                        if kalanYemek8 < 0:
                            
                            acKalanMusteri8 = abs(kalanYemek8)
                            depo5 = depo5 - round(depo5*0.10)
                        
                            print("Kalan Yemek ------------------------  0")
                            print("Depolanan Yemek --------------------  0")   
                            print("Aç Kalan Müşteri ------------------- ",acKalanMusteri8)
                        
                        else:
                            
                            depo5 = depo5 - round(depo5*0.10)
                            depo8 = kalanYemek8
                            
                            print("Kalan Yemek ------------------------ ",kalanYemek8)
                            print("Depolanan Yemek -------------------- ",depo8)
                            
                else:
                    
                    if onceDepo5 > 0:                    
                        
                        depo5 = depo5 + onceDepo5
                        yemek8 = depo8
                        
                        print("Perşembeden Kalan Yemekten Kalan --- ",depo5)
                        print("Perşembeden Aktarılan Yemek -------- ",round(depo5*0.10))
                        print("Kalan Yemek ------------------------ ",yemek8)
                        print("Toplam Kalan Yemek ----------------- ",depo5+yemek8)
                        print("Depolanan Yemek -------------------- ",onceDepo5+yemek8)
                    
                    else:
                        
                        if onceDepo7 > 0:
                            
                            depo7 = depo7 + onceDepo7
                            yemek8 = depo8
                            
                            print("Dünden Kalan Yemekten Kalan -------- ",depo7)
                            print("Dünden Aktarılan Yemek ------------- ",round(depo7*0.10))
                            print("Kalan Yemek ------------------------ ",yemek8)
                            print("Toplam Kalan Yemek ----------------- ",depo7+yemek8)
                            print("Depolanan Yemek -------------------- ",onceDepo7+yemek8)

                        else:
                            
                             if kalanYemek8 < 0:
                                
                                acKalanMusteri8 = abs(kalanYemek8)
                                depo5 = depo5 - round(depo5*0.10)
                                depo7 = depo7 - round(depo7*0.10)
                            
                                print("Kalan Yemek ------------------------  0")
                                print("Depolanan Yemek --------------------  0")   
                                print("Aç Kalan Müşteri ------------------- ",acKalanMusteri8)
    
                             else:                            
    
                                depo5 = depo5 - round(depo5*0.10)
                                depo7 = depo7 - round(depo7*0.10)
                                depo8 = kalanYemek8
                                
                                print("Kalan Yemek ------------------------ ",kalanYemek8)
                                print("Depolanan Yemek -------------------- ",depo8)
                                
            else:
                
                if depo7 == 0:
                    
                    if onceDepo5 > 0:
                        
                        depo5 = depo5 + onceDepo5
                        yemek8 = depo8
                        
                        print("Cumadan Kalan Yemekten Kalan ------- ",depo5)
                        print("Cumadan Aktarılan Yemek ------------ ",round(depo5*0.10))
                        print("Kalan Yemek ------------------------ ",yemek8)
                        print("Toplam Kalan Yemek ----------------- ",depo5+yemek8)
                        print("Depolanan Yemek -------------------- ",onceDepo5+yemek8)
                        
                    else:
                        
                        if kalanYemek8 < 0:
                            
                            acKalanMusteri8 = abs(kalanYemek8)
                            depo5 = depo5 - round(depo5*0.10)
                        
                            print("Kalan Yemek ------------------------  0")
                            print("Depolanan Yemek --------------------  0")   
                            print("Aç Kalan Müşteri ------------------- ",acKalanMusteri8)
                        
                        else:
                            
                            depo5 = depo5 - round(depo5*0.10)
                            depo8 = kalanYemek8
                            
                            print("Kalan Yemek ------------------------ ",kalanYemek8)
                            print("Depolanan Yemek -------------------- ",depo8)
                            
                else:
                    
                    if onceDepo5 > 0:                    
                        
                        depo5 = depo5 + onceDepo5
                        yemek8 = depo8
                        
                        print("Cumartesiden Kalan Yemekten Kalan -- ",depo6)
                        print("Cumartesiden Aktarılan Yemek ------- ",round(depo6*0.10))
                        print("Kalan Yemek ------------------------ ",yemek8)
                        print("Toplam Kalan Yemek ----------------- ",depo6+yemek8)
                        print("Depolanan Yemek -------------------- ",onceDepo6+yemek8)
                    
                    else:                        
                                                  
                        if kalanYemek8 < 0:
                                
                            acKalanMusteri8 = abs(kalanYemek8)
                            depo5 = depo5 - round(depo5*0.10)
                            depo6 = depo6 - round(depo6*0.10)
                            
                            print("Kalan Yemek ------------------------  0")
                            print("Depolanan Yemek --------------------  0")   
                            print("Aç Kalan Müşteri ------------------- ",acKalanMusteri8)
    
                        else:                            
    
                            depo5 = depo5 - round(depo5*0.10)
                            depo6 = depo6 - round(depo6*0.10)
                            depo8 = kalanYemek8
                                
                            print("Kalan Yemek ------------------------ ",kalanYemek8)
                            print("Depolanan Yemek -------------------- ",depo8)
                            
        print("                                          ")
        print("Cuma Deposu ------------------------ ",depo5)
        print("Cumartesi Deposu ------------------- ",depo6)
        print("Pazar Deposu ----------------------- ",depo7)
        print("Pazartesi Deposu ------------------- ",depo8)
        print("//////////////////////////////////////// ")


    if i == 9:
        
        musteri9 = musteri
        yemek9 = yemek
        acKalanMusteri9 = 0
        
        copeGiden5 = depo5
        depo5 = 0
        
        cikanYemek9 = round(depo6*0.10) + round(depo7*0.10) + round(depo8*0.10) + yemek9
        onceDepo6 = round(depo6*0.10) - musteri9
        onceDepo7 = round(depo6*0.10) + round(depo7*0.10) - musteri9
        onceDepo8 = round(depo6*0.10) + round(depo7*0.10) + round(depo8*0.10) - musteri9
        
        kalanYemek9 = cikanYemek9 - musteri9
        
        print("            9. Gün            ")
        print("Müşteri ---------------------------- ",musteri9)
        print("Cumartesiden Kalan Yemek ----------- ",depo6)
        print("Cumartesidendan Aktarılan Yemek ---- ",round(depo6*0.10))
        print("Pazardan Kalan Yemek --------------- ",depo7)
        print("Pazardan Aktarılan Yemek ----------- ",round(depo7*0.10))
        print("Dünden Kalan Yemek ----------------- ",depo8)
        print("Dünden Aktarılan Yemek ------------- ",round(depo8*0.10))
        print("Önceki Günlerden Aktarılan Yemek --- ",round(depo6*0.10)+round(depo7*0.10)+round(depo8*0,10))
        print("Günlük Çıkan Yemek ----------------- ",yemek9)
        print("Toplam Çıkan Yemek ----------------- ",cikanYemek9)        
        
        if depo6 == 0:
            
            if depo7 == 0:
                
                if depo8 == 0:
                    
                    if kalanYemek9 < 0:
                        
                        acKalanMusteri9 = abs(kalanYemek9)
                
                        print("Kalan Yemek ------------------------  0")
                        print("Depolanan Yemek --------------------  0")   
                        print("Aç Kalan Müşteri ------------------- ",acKalanMusteri9)
                    
                    else:
                        
                        depo9 = kalanYemek9
    
                        print("Kalan Yemek ------------------------ ",kalanYemek9)
                        print("Depolanan Yemek -------------------- ",depo9)
                        
                else:
                    
                    if onceDepo8 > 0:
                        
                        depo8 = depo8 + onceDepo8
                        yemek9 = depo9
                    
                        print("Dünden Kalan Yemekten Kalan -------- ",depo8)
                        print("Dünden Aktarılan Yemek ------------- ",round(depo8*0.10))
                        print("Kalan Yemek ------------------------ ",yemek9)
                        print("Toplam Kalan Yemek ----------------- ",depo8+yemek9)
                        print("Depolanan Yemek -------------------- ",yemek9+onceDepo8)
                        
                    else:
                        
                        if kalanYemek9 < 0:
                            
                            acKalanMusteri9 = abs(kalanYemek9)
                            depo8 = depo8 - round(depo8*0.10) 
                
                            print("Kalan Yemek ------------------------  0")
                            print("Depolanan Yemek --------------------  0")   
                            print("Aç Kalan Müşteri ------------------- ",acKalanMusteri9)
                        
                        else:
                            
                            depo8 = depo8 - round(depo8*0.10)
                            depo9 = kalanYemek9
                
                            print("Kalan Yemek ------------------------ ",kalanYemek9)
                            print("Depolanan Yemek -------------------- ",depo9)
                            
            else:
                
                if depo8 == 0:
                    
                    if onceDepo7 > 0:
                        
                        depo7 = depo7 + onceDepo7
                        yemek9 = depo9
                        
                        print("Pazardan Kalan Yemekten Kalan ------ ",depo7)
                        print("Pazardan Aktarılan Yemek ----------- ",round(depo7*0.10))
                        print("Kalan Yemek ------------------------ ",yemek9)
                        print("Toplam Kalan Yemek ----------------- ",depo7+yemek9)
                        print("Depolanan Yemek -------------------- ",onceDepo7+yemek9) 
                        
                    else:
                        
                        if kalanYemek9 < 0:
                            
                            acKalanMusteri9 = abs(kalanYemek9)
                            depo7 = depo7 - round(depo7*0.10)
                        
                            print("Kalan Yemek ------------------------  0")
                            print("Depolanan Yemek --------------------  0")   
                            print("Aç Kalan Müşteri ------------------- ",acKalanMusteri9)
                        
                        else:
                            
                            depo7 = depo7 - round(depo7*0.10)
                            depo9 = kalanYemek9
                            
                            print("Kalan Yemek ------------------------ ",kalanYemek9)
                            print("Depolanan Yemek -------------------- ",depo9)
                            
                else:
                    
                    if onceDepo7 > 0:
                        
                        depo7 = depo7 + onceDepo7
                        yemek9 = depo9
                        
                        print("Pazardan Kalan Yemek --------------- ",depo7)
                        print("Pazardan Aktarılan Yemek ----------- ",round(depo7*0.10))
                        print("Dünden Kalan Yemekten Kalan -------- ",depo8)
                        print("Dünden Aktarılan Yemek ------------- ",round(depo8*0.10))
                        print("Kalan Yemek ------------------------ ",yemek9)
                        print("Toplam Kalan Yemek ----------------- ",onceDepo7+depo8+yemek9)
                        print("Depolanan Yemek -------------------- ",onceDepo7+depo8+yemek9)
                              
                    else:
                        
                        if onceDepo8 > 0:
    
                            depo8 = depo8 + onceDepo8
                            yemek9 = depo9
                            
                            print("Pazardan Kalan Yemek --------------- ",depo7)
                            print("Cumartesiden Aktarılan Yemek ------- ",round(depo7*0.10))                    
                            print("Dünden Kalan Yemekten Kalan -------- ",depo8)
                            print("Dünden Aktarılan Yemek ------------- ",round(depo8*0.10))
                            print("Kalan Yemek ------------------------ ",yemek9)
                            print("Toplam Kalan Yemek ----------------- ",depo8+yemek9)
                            print("Depolanan Yemek -------------------- ",onceDepo8+yemek9)
    
                        else:
                            
                            if kalanYemek9 < 0:
                                
                                acKalanMusteri9 = abs(kalanYemek9)
                                depo7 = depo7 - round(depo7*0.10)
                                depo8 = depo8 - round(depo8*0.10)
                            
                                print("Kalan Yemek ------------------------  0")
                                print("Depolanan Yemek --------------------  0")   
                                print("Aç Kalan Müşteri ------------------- ",acKalanMusteri9)
    
                            else:                            
    
                                depo7 = depo7 - round(depo7*0.10)
                                depo8 = depo8 - round(depo8*0.10)
                                depo9 = kalanYemek9
                                
                                print("Kalan Yemek ------------------------ ",kalanYemek9)
                                print("Depolanan Yemek -------------------- ",depo9)

        else:
            
            if depo7 == 0:
                
                if depo8 == 0:
                    
                    if onceDepo6 > 0:
                        
                        depo6 = depo6 + onceDepo6
                        yemek9 = depo9
                        
                        print("Cumartesiden Kalan Yemekten Kalan -- ",depo6)
                        print("Cumartesiden Aktarılan Yemek ------- ",round(depo6*0.10))
                        print("Kalan Yemek ------------------------ ",yemek9)
                        print("Toplam Kalan Yemek ----------------- ",depo6+yemek9)
                        print("Depolanan Yemek -------------------- ",onceDepo6+yemek9)
                        
                    else:
                        
                        if kalanYemek9 < 0:
                            
                            acKalanMusteri9 = abs(kalanYemek9)
                            depo6 = depo6 - round(depo6*0.10)
                        
                            print("Kalan Yemek ------------------------  0")
                            print("Depolanan Yemek --------------------  0")   
                            print("Aç Kalan Müşteri ------------------- ",acKalanMusteri9)
                        
                        else:
                            
                            depo6 = depo6 - round(depo6*0.10)
                            depo9 = kalanYemek9
                            
                            print("Kalan Yemek ------------------------ ",kalanYemek9)
                            print("Depolanan Yemek -------------------- ",depo9)
                            
                else:
                    
                    if onceDepo6 > 0:                    
                        
                        depo6 = depo6 + onceDepo6
                        yemek9 = depo9
                        
                        print("Cumadan Kalan Yemekten Kalan ------ ",depo6)
                        print("Cumadan Aktarılan Yemek ----------- ",round(depo6*0.10))
                        print("Kalan Yemek ------------------------ ",yemek9)
                        print("Toplam Kalan Yemek ----------------- ",depo6+yemek9)
                        print("Depolanan Yemek -------------------- ",onceDepo6+yemek9)
                    
                    else:
                        
                        if onceDepo8 > 0:
                            
                            depo8 = depo8 + onceDepo8
                            yemek9 = depo9
                            
                            print("Dünden Kalan Yemekten Kalan -------- ",depo8)
                            print("Dünden Aktarılan Yemek ------------- ",round(depo8*0.10))
                            print("Kalan Yemek ------------------------ ",yemek9)
                            print("Toplam Kalan Yemek ----------------- ",depo8+yemek9)
                            print("Depolanan Yemek -------------------- ",onceDepo8+yemek9)

                        else:
                            
                             if kalanYemek9 < 0:
                                
                                acKalanMusteri9 = abs(kalanYemek9)
                                depo6 = depo6 - round(depo6*0.10)
                                depo8 = depo8 - round(depo8*0.10)
                            
                                print("Kalan Yemek ------------------------  0")
                                print("Depolanan Yemek --------------------  0")   
                                print("Aç Kalan Müşteri ------------------- ",acKalanMusteri9)
    
                             else:                            
    
                                depo6 = depo6 - round(depo6*0.10)
                                depo8 = depo8 - round(depo8*0.10)
                                depo9 = kalanYemek9
                                
                                print("Kalan Yemek ------------------------ ",kalanYemek9)
                                print("Depolanan Yemek -------------------- ",depo9)
                                
            else:
                
                if depo8 == 0:
                    
                    if onceDepo6 > 0:
                        
                        depo6 = depo6 + onceDepo6
                        yemek9 = depo9
                        
                        print("Cumartesiden Kalan Yemekten Kalan -- ",depo6)
                        print("Cumartesiden Aktarılan Yemek ------- ",round(depo6*0.10))
                        print("Kalan Yemek ------------------------ ",yemek9)
                        print("Toplam Kalan Yemek ----------------- ",depo6+yemek9)
                        print("Depolanan Yemek -------------------- ",onceDepo6+yemek9)
                        
                    else:
                        
                        if kalanYemek9 < 0:
                            
                            acKalanMusteri9 = abs(kalanYemek9)
                            depo6 = depo6 - round(depo6*0.10)
                        
                            print("Kalan Yemek ------------------------  0")
                            print("Depolanan Yemek --------------------  0")   
                            print("Aç Kalan Müşteri ------------------- ",acKalanMusteri9)
                        
                        else:
                            
                            depo6 = depo6 - round(depo6*0.10)
                            depo9 = kalanYemek9
                            
                            print("Kalan Yemek ------------------------ ",kalanYemek9)
                            print("Depolanan Yemek -------------------- ",depo9)
                            
                else:
                    
                    if onceDepo6 > 0:                    
                        
                        depo6 = depo6 + onceDepo6
                        yemek9 = depo9
                        
                        print("Cumartesiden Kalan Yemekten Kalan -- ",depo7)
                        print("Cumartesiden Aktarılan Yemek ------- ",round(depo7*0.10))
                        print("Kalan Yemek ------------------------ ",yemek9)
                        print("Toplam Kalan Yemek ----------------- ",depo7+yemek9)
                        print("Depolanan Yemek -------------------- ",onceDepo7+yemek9)
                    
                    else:                        
                                                  
                        if kalanYemek9 < 0:
                                
                            acKalanMusteri9 = abs(kalanYemek9)
                            depo6 = depo6 - round(depo6*0.10)
                            depo7 = depo7 - round(depo7*0.10)
                            
                            print("Kalan Yemek ------------------------  0")
                            print("Depolanan Yemek --------------------  0")   
                            print("Aç Kalan Müşteri ------------------- ",acKalanMusteri9)
    
                        else:                            
    
                            depo6 = depo6 - round(depo6*0.10)
                            depo7 = depo7 - round(depo7*0.10)
                            depo9 = kalanYemek9
                                
                            print("Kalan Yemek ------------------------ ",kalanYemek9)
                            print("Depolanan Yemek -------------------- ",depo9)
                            
        print("                                          ")
        print("Cumartesi Deposu ------------------- ",depo6)
        print("Pazar Deposu ----------------------- ",depo7)
        print("Pazartesi Deposu ------------------- ",depo8)
        print("Salı Deposu ------------------------ ",depo9)
        print("//////////////////////////////////////// ")


    if i == 10:
        
        musteri10 = musteri
        yemek10 = yemek
        acKalanMusteri10 = 0
        
        copeGiden6 = depo6
        depo6 = 0
        
        cikanYemek10 = round(depo7*0.10) + round(depo8*0.10) + round(depo9*0.10) + yemek10
        onceDepo7 = round(depo7*0.10) - musteri10
        onceDepo8 = round(depo7*0.10) + round(depo8*0.10) - musteri10
        onceDepo9 = round(depo7*0.10) + round(depo8*0.10) + round(depo9*0.10) - musteri10
        
        kalanYemek10 = cikanYemek10 - musteri10
        
        print("            10. Gün            ")
        print("Müşteri ---------------------------- ",musteri10)
        print("Pazardan Kalan Yemek --------------- ",depo7)
        print("Pazardan Aktarılan Yemek ----------- ",round(depo7*0.10))
        print("Pazartesiden Kalan Yemek ----------- ",depo8)
        print("Pazartesiden Aktarılan Yemek ------- ",round(depo8*0.10))
        print("Dünden Kalan Yemek ----------------- ",depo9)
        print("Dünden Aktarılan Yemek ------------- ",round(depo9*0.10))
        print("Önceki Günlerden Aktarılan Yemek --- ",round(depo7*0.10)+round(depo8*0.10)+round(depo9*0,10))
        print("Günlük Çıkan Yemek ----------------- ",yemek10)
        print("Toplam Çıkan Yemek ----------------- ",cikanYemek10)
        
        if depo7 == 0:
            
            if depo8 == 0:
                
                if depo9 == 0:
                    
                    if kalanYemek10 < 0:
                        
                        acKalanMusteri10 = abs(kalanYemek10)
                
                        print("Kalan Yemek ------------------------  0")
                        print("Depolanan Yemek --------------------  0")   
                        print("Aç Kalan Müşteri ------------------- ",acKalanMusteri10)
                    
                    else:
                        
                        depo10 = kalanYemek10
    
                        print("Kalan Yemek ------------------------ ",kalanYemek10)
                        print("Depolanan Yemek -------------------- ",depo10)
                        
                else:
                    
                    if onceDepo9 > 0:
                        
                        depo9 = depo9 + onceDepo9
                        yemek10 = depo10
                    
                        print("Dünden Kalan Yemekten Kalan -------- ",depo9)
                        print("Dünden Aktarılan Yemek ------------- ",round(depo9*0.10))
                        print("Kalan Yemek ------------------------ ",yemek10)
                        print("Toplam Kalan Yemek ----------------- ",depo9+yemek10)
                        print("Depolanan Yemek -------------------- ",yemek10+onceDepo9)
                        
                    else:
                        
                        if kalanYemek10 < 0:
                            
                            acKalanMusteri10 = abs(kalanYemek10)
                            depo9 = depo9 - round(depo9*0.10) 
                
                            print("Kalan Yemek ------------------------  0")
                            print("Depolanan Yemek --------------------  0")   
                            print("Aç Kalan Müşteri ------------------- ",acKalanMusteri10)
                        
                        else:
                            
                            depo9 = depo9 - round(depo9*0.10)
                            depo10 = kalanYemek10
                
                            print("Kalan Yemek ------------------------ ",kalanYemek10)
                            print("Depolanan Yemek -------------------- ",depo10)
                            
            else:
                
                if depo9 == 0:
                    
                    if onceDepo8 > 0:
                        
                        depo8 = depo8 + onceDepo8
                        yemek10 = depo10
                        
                        print("Pazartesiden Kalan Yemekten Kalan -- ",depo8)
                        print("Pazartesiden Aktarılan Yemek ------- ",round(depo8*0.10))
                        print("Kalan Yemek ------------------------ ",yemek10)
                        print("Toplam Kalan Yemek ----------------- ",depo8+yemek10)
                        print("Depolanan Yemek -------------------- ",onceDepo8+yemek10) 
                        
                    else:
                        
                        if kalanYemek10 < 0:
                            
                            acKalanMusteri10 = abs(kalanYemek10)
                            depo8 = depo8 - round(depo8*0.10)
                        
                            print("Kalan Yemek ------------------------  0")
                            print("Depolanan Yemek --------------------  0")   
                            print("Aç Kalan Müşteri ------------------- ",acKalanMusteri10)
                        
                        else:
                            
                            depo8 = depo8 - round(depo8*0.10)
                            depo10 = kalanYemek10
                            
                            print("Kalan Yemek ------------------------ ",kalanYemek10)
                            print("Depolanan Yemek -------------------- ",depo10)
                            
                else:
                    
                    if onceDepo8 > 0:
                        
                        depo8 = depo8 + onceDepo8
                        yemek10 = depo10
                        
                        print("Pazartesiden Kalan Yemek ----------- ",depo8)
                        print("Pazartesiden Aktarılan Yemek ------- ",round(depo8*0.10))
                        print("Dünden Kalan Yemekten Kalan -------- ",depo9)
                        print("Dünden Aktarılan Yemek ------------- ",round(depo9*0.10))
                        print("Kalan Yemek ------------------------ ",yemek10)
                        print("Toplam Kalan Yemek ----------------- ",onceDepo8+depo9+yemek10)
                        print("Depolanan Yemek -------------------- ",onceDepo8+depo9+yemek10)
                              
                    else:
                        
                        if onceDepo9 > 0:
    
                            depo9 = depo9 + onceDepo9
                            yemek10 = depo10
                            
                            print("Pazartesiden Kalan Yemek ----------- ",depo8)
                            print("Pazardan Aktarılan Yemek ----------- ",round(depo8*0.10))                    
                            print("Dünden Kalan Yemekten Kalan -------- ",depo9)
                            print("Dünden Aktarılan Yemek ------------- ",round(depo9*0.10))
                            print("Kalan Yemek ------------------------ ",yemek10)
                            print("Toplam Kalan Yemek ----------------- ",depo9+yemek10)
                            print("Depolanan Yemek -------------------- ",onceDepo9+yemek10)
    
                        else:
                            
                            if kalanYemek10 < 0:
                                
                                acKalanMusteri10 = abs(kalanYemek10)
                                depo8 = depo8 - round(depo8*0.10)
                                depo9 = depo9 - round(depo9*0.10)
                            
                                print("Kalan Yemek ------------------------  0")
                                print("Depolanan Yemek --------------------  0")   
                                print("Aç Kalan Müşteri ------------------- ",acKalanMusteri10)
    
                            else:                            
    
                                depo8 = depo8 - round(depo8*0.10)
                                depo9 = depo9 - round(depo9*0.10)
                                depo10 = kalanYemek10
                                
                                print("Kalan Yemek ------------------------ ",kalanYemek10)
                                print("Depolanan Yemek -------------------- ",depo10)

        else:
            
            if depo8 == 0:
                
                if depo9 == 0:
                    
                    if onceDepo7 > 0:
                        
                        depo7 = depo7 + onceDepo7
                        yemek10 = depo10
                        
                        print("Pazardan Kalan Yemekten Kalan ------ ",depo7)
                        print("Pazardan Aktarılan Yemek ----------- ",round(depo7*0.10))
                        print("Kalan Yemek ------------------------ ",yemek10)
                        print("Toplam Kalan Yemek ----------------- ",depo7+yemek10)
                        print("Depolanan Yemek -------------------- ",onceDepo7+yemek10)
                        
                    else:
                        
                        if kalanYemek10 < 0:
                            
                            acKalanMusteri10 = abs(kalanYemek10)
                            depo7 = depo7 - round(depo7*0.10)
                        
                            print("Kalan Yemek ------------------------  0")
                            print("Depolanan Yemek --------------------  0")   
                            print("Aç Kalan Müşteri ------------------- ",acKalanMusteri10)
                        
                        else:
                            
                            depo7 = depo7 - round(depo7*0.10)
                            depo10 = kalanYemek10
                            
                            print("Kalan Yemek ------------------------ ",kalanYemek10)
                            print("Depolanan Yemek -------------------- ",depo10)
                            
                else:
                    
                    if onceDepo7 > 0:                    
                        
                        depo7 = depo7 + onceDepo7
                        yemek10 = depo10
                        
                        print("Cumartesiden Kalan Yemekten Kalan -- ",depo7)
                        print("Cumartesiden Aktarılan Yemek ------- ",round(depo7*0.10))
                        print("Kalan Yemek ------------------------ ",yemek10)
                        print("Toplam Kalan Yemek ----------------- ",depo7+yemek10)
                        print("Depolanan Yemek -------------------- ",onceDepo6+yemek10)
                    
                    else:
                        
                        if onceDepo9 > 0:
                            
                            depo9 = depo9 + onceDepo9
                            yemek10 = depo10
                            
                            print("Dünden Kalan Yemekten Kalan -------- ",depo9)
                            print("Dünden Aktarılan Yemek ------------- ",round(depo9*0.10))
                            print("Kalan Yemek ------------------------ ",yemek10)
                            print("Toplam Kalan Yemek ----------------- ",depo9+yemek10)
                            print("Depolanan Yemek -------------------- ",onceDepo9+yemek10)

                        else:
                            
                             if kalanYemek10 < 0:
                                
                                acKalanMusteri10 = abs(kalanYemek10)
                                depo7 = depo7 - round(depo7*0.10)
                                depo9 = depo9 - round(depo9*0.10)
                            
                                print("Kalan Yemek ------------------------  0")
                                print("Depolanan Yemek --------------------  0")   
                                print("Aç Kalan Müşteri ------------------- ",acKalanMusteri10)
    
                             else:                            
    
                                depo7 = depo7 - round(depo7*0.10)
                                depo9 = depo9 - round(depo9*0.10)
                                depo10 = kalanYemek10
                                
                                print("Kalan Yemek ------------------------ ",kalanYemek10)
                                print("Depolanan Yemek -------------------- ",depo10)
                                
            else:
                
                if depo9 == 0:
                    
                    if onceDepo7 > 0:
                        
                        depo7 = depo7 + onceDepo7
                        yemek10 = depo10
                        
                        print("Pazardan Kalan Yemekten Kalan ------ ",depo7)
                        print("Pazardan Aktarılan Yemek ----------- ",round(depo7*0.10))
                        print("Kalan Yemek ------------------------ ",yemek10)
                        print("Toplam Kalan Yemek ----------------- ",depo7+yemek10)
                        print("Depolanan Yemek -------------------- ",onceDepo7+yemek10)
                        
                    else:
                        
                        if kalanYemek10 < 0:
                            
                            acKalanMusteri10 = abs(kalanYemek10)
                            depo7 = depo7 - round(depo7*0.10)
                        
                            print("Kalan Yemek ------------------------  0")
                            print("Depolanan Yemek --------------------  0")   
                            print("Aç Kalan Müşteri ------------------- ",acKalanMusteri10)
                        
                        else:
                            
                            depo7 = depo7 - round(depo7*0.10)
                            depo10 = kalanYemek10
                            
                            print("Kalan Yemek ------------------------ ",kalanYemek10)
                            print("Depolanan Yemek -------------------- ",depo10)
                            
                else:
                    
                    if onceDepo7 > 0:                    
                        
                        depo7 = depo7 + onceDepo7
                        yemek10 = depo10
                        
                        print("Pazardan Kalan Yemekten Kalan ------ ",depo8)
                        print("Pazardan Aktarılan Yemek ----------- ",round(depo8*0.10))
                        print("Kalan Yemek ------------------------ ",yemek10)
                        print("Toplam Kalan Yemek ----------------- ",depo8+yemek10)
                        print("Depolanan Yemek -------------------- ",onceDepo8+yemek10)
                    
                    else:                        
                                                  
                        if kalanYemek10 < 0:
                                
                            acKalanMusteri10 = abs(kalanYemek10)
                            depo7 = depo7 - round(depo7*0.10)
                            depo8 = depo8 - round(depo8*0.10)
                            
                            print("Kalan Yemek ------------------------  0")
                            print("Depolanan Yemek --------------------  0")   
                            print("Aç Kalan Müşteri ------------------- ",acKalanMusteri10)
    
                        else:                            
    
                            depo7 = depo7 - round(depo7*0.10)
                            depo8 = depo8 - round(depo8*0.10)
                            depo10 = kalanYemek10
                                
                            print("Kalan Yemek ------------------------ ",kalanYemek10)
                            print("Depolanan Yemek -------------------- ",depo10)
                            
        print("                                          ")
        print("Pazar Deposu ----------------------- ",depo7)
        print("Pazartesi Deposu ------------------- ",depo8)
        print("Salı Deposu ------------------------ ",depo9)
        print("Çarşamba Deposu -------------------- ",depo6)
        print("//////////////////////////////////////// ")
        
        
        
        if kalanYemek1 < 0:
            
            kalanYemek1 = 0
            
        else:
            
            kalanYemek1 = kalanYemek1
            

        if kalanYemek2 < 0:
            
            kalanYemek2 = 0
            
        else:
            
            kalanYemek2 = kalanYemek2
            
            
            
        if kalanYemek3 < 0:
            
            kalanYemek3 = 0
            
        else:
            
            kalanYemek3 = kalanYemek3
            
            
            
        if kalanYemek4 < 0:
            
            kalanYemek4 = 0
            
        else:
            
            kalanYemek4 = kalanYemek4
            
            
            
        if kalanYemek5 < 0:
            
            kalanYemek5 = 0
            
        else:
            
            kalanYemek5 = kalanYemek5
            
            
            
        if kalanYemek6 < 0:
            
            kalanYemek6 = 0
            
        else:
            
            kalanYemek6 = kalanYemek6
            
            
            
        if kalanYemek7 < 0:
            
            kalanYemek7 = 0
            
        else:
            
            kalanYemek7 = kalanYemek7
            
            
            
        if kalanYemek8 < 0:
            
            kalanYemek8 = 0
            
        else:
            
            kalanYemek8 = kalanYemek8
            
            
            
        if kalanYemek9 < 0:
            
            kalanYemek9 = 0
            
        else:
            
            kalanYemek9 = kalanYemek9
            
            
            
        if kalanYemek10 < 0:
            
            kalanYemek10 = 0
            
        else:
            
            kalanYemek10 = kalanYemek10

        
        toplamMusteriSayisi = musteri1 + musteri2 + musteri3 + musteri4 + musteri5 + musteri6 + musteri7 + musteri8 + musteri9 + musteri10
        toplamCikanYemekSayisi = yemek1 + yemek2 + yemek3 + yemek4 + yemek5 + yemek6 + yemek7 + yemek8 + yemek9 + yemek10
        acKalanMusteriSayisi = acKalanMusteri1 + acKalanMusteri2 + acKalanMusteri3 + acKalanMusteri4 + acKalanMusteri5 + acKalanMusteri6 + acKalanMusteri7 + acKalanMusteri8 + acKalanMusteri9 + acKalanMusteri10
        toplamArtıkYemekSayisi = kalanYemek1 + kalanYemek2 + kalanYemek3 + kalanYemek4 + kalanYemek5 + kalanYemek6 + kalanYemek7 + kalanYemek8 + kalanYemek9 + kalanYemek10
        toplamCopeGiden = copeGiden3 + copeGiden4 + copeGiden5 +copeGiden6
        toplamKullanilanArtikYemekSayisi = toplamArtıkYemekSayisi - toplamCopeGiden
        
        print("Toplam Müşteri Sayısı = ",toplamMusteriSayisi)
        print("Toplam Günlük Çıkan Yemek Sayısı = ",toplamCikanYemekSayisi)
        print("Toplam Aç Kalan Müşteri Sayısı = ",acKalanMusteriSayisi)
        print("Toplam Artık Yemek = ",toplamArtıkYemekSayisi)
        print("Toplam Yeniden Kullanılan Yemek = ",toplamKullanilanArtikYemekSayisi)
        print("Toplam Çöpe Giden Yemek = ",toplamCopeGiden)
