# IMPLEMENTASI METRIK EVALUASI

Skrip ini menghitung metrik evaluasi kualitas citra sebelum dan sesudah enhancement menggunakan histogram equalization.

## Persyaratan

- Python 3
- Paket Python:
  - `opencv-python`
  - `numpy`

## Install Paket

Buka terminal di folder proyek, lalu jalankan:

```bash
cd "/home/neki/PENGOLAHAN CITRA DIGITAL"
python3 -m pip install --upgrade pip
python3 -m pip install opencv-python numpy
```

## Cara Menggunakan

1. Pastikan file gambar `low_contrast.jpg` ada di folder yang sama dengan skrip.
2. Jalankan skrip dengan perintah:

```bash
python3 IMPLEMENTASI-METRIK-EVALUASI.py
```

3. Setelah dijalankan, skrip akan:
   - menampilkan metrik perbandingan `Original` vs `Enhanced`
   - menyimpan hasil enhancement ke file `enhanced.jpg`

## Catatan

- Jika file gambar berada di nama atau lokasi lain, ubah baris berikut di `IMPLEMENTASI-METRIK-EVALUASI.py`:

```python
img = cv2.imread('low_contrast.jpg', cv2.IMREAD_GRAYSCALE)
```

- Pastikan skrip dijalankan dari folder yang sama dengan file gambar atau gunakan path lengkap.
