# Custom Tkinter UI Components

Repo ini berisi kumpulan komponen UI untuk Python menggunakan `tkinter` dan `customtkinter`.  
Memudahkan pembuatan aplikasi desktop dengan tampilan modern dan fungsi tambahan seperti input dengan ikon, tombol toggle password, progress bar, dan lainnya.

---

## Fitur

- **Config window** — Fungsi `config` untuk membuat window utama dengan judul dan ukuran fleksibel.
- **TextView** — Label teks dengan custom warna dan font.
- **ButtonView** — Tombol dengan warna dan radius yang bisa dikustomisasi.
- **InputView** — Input field dengan placeholder, ikon di kiri, dan tombol toggle mata untuk password.
- **ProgressView** — Progress bar standar menggunakan `ttk`.
- **ImageViewPilLow** — Menampilkan gambar dengan PIL dan `tkinter`.
- **AppDesktop** — Kerangka aplikasi sederhana untuk mengatur layout dan posisi widget.

---

## Instalasi

Pastikan kamu sudah install Python 3.x dan pip.  
Install dependencies berikut:

```bash
pip install customtkinter pillow
python -m build
