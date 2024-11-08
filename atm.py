import tkinter as tk
from tkinter import messagebox

bakiye = 97560

def bakiye_sorgula():
    ekran.set(f"Mevcut Bakiyeniz : {bakiye} TL")
def para_yatir():
    global bakiye
    try:
        yatirilan=int(tutar_girişi.get())
        if yatirilan <= 0:
            messagebox.showerror("Hata", "Lütfen Geçerli Bir Tutar Giriniz ! ")
        else:
            bakiye=bakiye+yatirilan
            ekran.set(f"{yatirilan} TL Yatırıldı. Yeni Bakiye : {bakiye} TL")
            tutar_girişi.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Hata", "Lütfen Geçerli Bir Sayı Giriniz ! ")

def para_cek():
    global bakiye
    try:
        çekilen=int(tutar_girişi.get())
        if çekilen <= 0:
            messagebox.showerror("Hata", "Lütfen Geçerli Bir Tutar Giriniz.")
        elif çekilen > bakiye:
            ekran.set("Yetersiz Bakiye.")
        else:
            bakiye=bakiye-çekilen
            ekran.set(f"{çekilen} TL Çekildi. Yeni Bakiye : {bakiye} TL")
            tutar_girişi.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Hata", "Lütfen Geçerli Bir Sayı Giriniz ! ")

window=tk.Tk()
window.title("ATM")
window.geometry("500x250")

ekran=tk.StringVar()
ekran.set("Mevcut Bakiyeniz : ----")
ekran2=tk.Label(window, textvariable=ekran, relief="sunken", font=("Arial", 12), width=45, height=3)
ekran2.pack(pady=10)

tutar_girişi=tk.Entry(window)
tutar_girişi.pack(pady=5)
tutar_girişi.insert(0, "Tutar Giriniz")

button_frame=tk.Frame(window)
button_frame.pack(pady=10)

btn_bakiye_sorgula = tk.Button(button_frame, text="Bakiye Sorgulama", command=bakiye_sorgula, width=15)
btn_bakiye_sorgula.grid(row=0, column=0, padx=5, pady=5)
btn_para_yatir=tk.Button(button_frame, text="Para Yatırma", command=para_yatir, width=15)
btn_para_yatir.grid(row=0, column=1, padx=5, pady=5)
btn_para_cek=tk.Button(button_frame, text="Para Çekme", command=para_cek, width=15)
btn_para_cek.grid(row=1, column=0, padx=5, pady=5)
btn_cikis=tk.Button(button_frame, text="Çıkış", command=window.quit, width=15)
btn_cikis.grid(row=1, column=1, padx=5, pady=5)

window.mainloop()