import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = tk.Tk()

def hitung_estimasi():
    berat = float(entry_berat.get())
    tarif_per_kg = float(entry_tarif.get())
    kota_tujuan = combo_kota_tujuan.get()

    tarif_kota = {
        'Jakarta': 1.9,
        'Bogor': 2.7,
        'Tangerang': 4.2,
        'Bekasi': 3.8,
       
    }
    if kota_tujuan in tarif_kota:
        tarif_per_kg *= tarif_kota[kota_tujuan]
        estimasi_harga = berat * tarif_per_kg
        label_hasil.config(text=f'Estimasi Harga ke {kota_tujuan}: Rp.{estimasi_harga:.2f}')
    else:
        label_hasil.config(text='Kota tujuan tidak valid.')

root.title("Estimasi Harga Ekspedisi")

label_berat = tk.Label(root, text="Berat Paket (kg):")
label_berat.pack()

entry_berat = tk.Entry(root)
entry_berat.pack()

label_tarif = tk.Label(root, text="Tarif per Kg (Rp.):")
label_tarif.pack()

entry_tarif = tk.Entry(root)
entry_tarif.pack()

label_kota_tujuan = tk.Label(root, text="Kota Tujuan:")
label_kota_tujuan.pack()

kota_tujuan_options = ['Jakarta', 'Bogor', 'Tangerang', 'Bekasi']
combo_kota_tujuan = tk.StringVar()
combo_kota_tujuan.set(kota_tujuan_options[0])
dropdown_kota_tujuan = ttk.OptionMenu(root, combo_kota_tujuan, *kota_tujuan_options, bootstyle="light")
dropdown_kota_tujuan.pack()

button_hitung = ttk.Button(root, text="Hitung Estimasi", command=hitung_estimasi, bootstyle="success")
button_hitung.pack()

label_hasil = tk.Label(root, text="Estimasi Harga:")
label_hasil.pack()

root.mainloop()