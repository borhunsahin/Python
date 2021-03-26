class denklem():
    def katsayilar():
        try:
            a = int(input("a = "))
        except ValueError:
            print("Bir sayı Giriniz!!!")
            return katsayilar()
        try:
            b = int(input("b = "))
        except ValueError:
            print("Bir sayı Giriniz!!!")
            return katsayilar()
        try:
            c = int(input("c = "))
        except ValueError:
            print("Bir sayı Giriniz!!!")
            return katsayilar()


        def islem():
            d = b*b-4*a*c
            print("Delta =", d)

            if d > 0:
                x1 = (-b+(d**2))/2*a
                x2 = (-b-(d**2))/2*a
                print("X1 =", x1, "X2 =", x2)
            elif d == 0:
                x= -b/2*a
                print("Çakışık kök vardır.X =", x)
            else:
                print("Reel Kök Yoktur.")
        islem()
        return "basadon"
    while katsayilar() == "basadon":
        katsayilar()
    denklem()
