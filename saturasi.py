import tkinter as tk
from tkinter import ttk, messagebox
from ttkbootstrap import Style

class AplikasiSaturasiOksigen:
    def __init__(self, master):
        self.master = master
        self.style = Style(theme='superhero')  # You can choose a different theme

        master.title("Pengukuran Saturasi Oksigen")

        self.label__instruksi = ttk.Label(master, text="Masukkan data diri dan nilai saturasi oksigen dalam darah:")
        self.label__instruksi.pack(pady=10)

        self.label__nama = ttk.Label(master, text="Nama:")
        self.label__nama.pack(pady=5)
        self.entry__nama = ttk.Entry(master)
        self.entry__nama.pack(pady=5)

        self.label__umur = ttk.Label(master, text="Umur:")
        self.label__umur.pack(pady=5)
        self.entry__umur = ttk.Entry(master)
        self.entry__umur.pack(pady=5)

        self.label__saturasi = ttk.Label(master, text="Nilai Saturasi Oksigen:")
        self.label__saturasi.pack(pady=5)
        self.entry__saturasi = ttk.Entry(master)
        self.entry__saturasi.pack(pady=5)

        self.tombol__hitung = ttk.Button(master, text="Hitung", command=self.hitung__saturasi)
        self.tombol__hitung.pack(pady=10)

    def hitung__saturasi(self):
        try:
            nama = self.entry__nama.get()
            umur = int(self.entry__umur.get())
            saturasi = float(self.entry__saturasi.get())

            if 0 <= saturasi <= 100:
                if saturasi >= 95:
                    hasil = f"Hi {nama}, {umur} tahun, tingkat saturasi oksigen normal."
                elif 90 <= saturasi < 95:
                    hasil = f"Hi {nama}, {umur} tahun, tingkat saturasi oksigen rendah istirahat lah yang cukup ."    
                else:
                    hasil = f"Hi {nama}, {umur} tahun, tingkat saturasi oksigen sangat rendah. Segera konsultasikan dengan dokter."
            else:
                hasil = "Masukkan nilai saturasi yang valid (0-100)."
        except ValueError:
            hasil = "Masukkan nilai umur dan saturasi yang valid."

        messagebox.showinfo("Hasil Pengukuran", hasil)

if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiSaturasiOksigen(root)
    root.config(background="black")
    root.mainloop()