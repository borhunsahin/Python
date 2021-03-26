import tkinter as tk

pencere = tk.Tk()

sayi1 = tk.IntVar(pencere)
sayi2 = tk.IntVar(pencere)

def toplama():
    toplam = sayi1.get()+sayi2.get()
    print (toplam)
    return toplam

et1 = tk.Label(text = "Birinci Sayi= ").pack()
e1 = tk.Entry(pencere, textvariable = sayi1, width=20,fg="blue").pack()


et2 = tk.Label(text = "İkinci Sayi= ").pack()
e2 = tk.Entry(pencere, textvariable=sayi2,width=20,fg="green").pack()

buton = tk.Button(pencere, text='Hesapla', fg='White', bg= 'blue', height = 5, width = 5, command = toplama ).pack()


pencere.mainloop()
