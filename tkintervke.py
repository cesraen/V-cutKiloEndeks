import tkinter

pencere = tkinter.Tk()
pencere.title("Boy Kilo Endeksi Hesaplama")
pencere.minsize(width=300, height=200)

def simdilik():
    #kullanici_yazi = giris_alani_1.get()
    #print(kullanici_yazi)
    try:
        boy_deger = int(giris_alani_1.get())
        kilo_deger = int(giris_alani_2.get())
    except ValueError:
        metin_alani_3.config(text="Lütfen boyunuzu ve kilonuzu doğru girin!")
        return
    endeks_deger = kilo_deger / ((boy_deger/100) ** 2)
    endeks_deger_yuvarlama = (round(endeks_deger, 1))
    metin_alani_3.config(text=endeks_deger_yuvarlama)
    if endeks_deger <= 18.5:
        metin_alani_4.config(text="Düşük külolu bir bireysiniz.")
    elif endeks_deger > 18.5 and endeks_deger < 25:
        metin_alani_4.config(text="Normal kiloda bir bireysiniz.")
    elif endeks_deger >= 25 and endeks_deger < 30:
        metin_alani_4.config(text="Fazla kilolu bir bireysiniz")
    elif endeks_deger >= 30 and endeks_deger < 40:
        metin_alani_4.config(text="Obezite belirtisi!")
    elif endeks_deger >= 40:
        metin_alani_4.config(text="Aşırı obezite!")
    else:
        print("Hatalı oldu")
#metin alanı 1
metin_alani_1 = tkinter.Label(text="Boyunuzu girin:")
metin_alani_1.config(font=('Arial', 12, 'normal'))
metin_alani_1.pack()

#giriş alanı 1 (metin girilecek alan)
giris_alani_1 = tkinter.Entry()
giris_alani_1.pack()

#metin alanı 2
metin_alani_2 = tkinter.Label(text="Kilonuzu girin:")
metin_alani_2.config(font=('Arial', 12, 'normal'))
metin_alani_2.pack()

#giriş alanı 2 (metin girilecek alan)
giris_alani_2 = tkinter.Entry()
giris_alani_2.pack()

#boşluk için şimdilik koydum
bosluk = tkinter.Label()
bosluk.pack()
#buton alanı

buton_alani_1 = tkinter.Button(text="Hesapla", command=simdilik)
buton_alani_1.config(width=10)
buton_alani_1.pack()

#sonuç değeri metin alanı

metin_alani_3 = tkinter.Label(text="")
metin_alani_3.pack()

metin_alani_3.pack()
# sonuç gösterge metin alanı
metin_alani_4 = tkinter.Label(text="")
metin_alani_4.pack()

pencere.mainloop()