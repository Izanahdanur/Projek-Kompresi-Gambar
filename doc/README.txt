## Kelompok 5 ##
- Intan Trinanda (L0124018)
- Izanahda Nurkhasna (L0124019)
- Waldani Nabila Tamamah (L0124122)

## Image Compression Web App (Resize Blur Method)
Aplikasi ini adalah web berbasis Python Flask untuk melakukan kompresi gambar. Teknik yang digunakan adalah resize down lalu resize up (gambar diperkecil ukurannya untuk menghilangkan detail, lalu diperbesar Kembali agar terlihat blur, lalu disimpan sebagaiJPEG untuk mengecilkan ukuran file.

## Fitur Utama
- Upload gambar dari koimputer via browser
- Tentukan tingkat kompresi (misalnya 50)
- Menampilkan:
	- Gambar asli dan hasil kompresi
	- Runtime proses (dalam detik)
	- Ukuran file asli dan hasil (dalam KB)
	- Perubahan pixel berdasarkan skala resize
- Download hasil gambar terkompresi langsung dari web

## Teknologi
- Python 3
- Flask (Backend web)
- Pillow / PIL (Pengolahan gambar)

## Struktur Folder
image_compression_project/
	- src/
		-- app.py
		-- image_utils.py
		-- templates/
			--- index.html
	- test/
		-- uploads
		-- compressed
	- doc/
		-- Laporan
		-- Readme.txt

## Cara Menjalankan Program
- Buka terminal di folder src
- Install dependencies
  pip install flask pillow
- Jalankan server
  python app.py
- Akses di browser
  http://127.0.0.1:5000

## Cara Menggunakan Aplikasi
- Upload gambar
  Pilih tombol "Choose File" dan pilih gambar dari komputer
- Tentukan tingkat kompresi
  Masukkan angka presentase pada kolom "Tingkat Kompresi" (contoh : 50)
- Klik tombol kompres
  Sistem akan memproses gambar, memperkecil resolusi internalnya, lalu memperbesar kembali agar blur
- Lihat hasil kompresi
  Halaman akan menampilkan :
  - Gambar asli dan hasil kompresi
  - Runtime proses (dalam detik)
  - Ukuran file asli dan hasil (dalam KB)
  - Perubahan pixel berdasarkan skala resize
- Unduh hasilnya
  Klik tombol "Download" di Bawah gambar kompresi untuk menyimpan gambar hasil kompresi ke perangkat.

## Link Google Drive
Semua file (kode, laporan, screenshot, dsb) dapat diakses di: https://drive.google.com/drive/folders/1cnLqf6rlY_aDRTG0cBYUiwtOW266fhvn

## Link Repository
GitHub : https://github.com/Izanahdanur/Projek-Kompresi-Gambar

## Referensi
- https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html
- https://github.com/liliansteven/image-compression-and-decompression-using-PCA-implemented-from-scratch
- https://ieeexplore.ieee.org/document/9047014