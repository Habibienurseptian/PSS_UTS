UTS PEMROGRAMAN SISI SERVER

SISTEM BACKEND MANAJEMEN INVENTORY

Anggota Kelompok :
1. Habibie Nur Septian - A11.2022.14829
2. Rafli Nur Rahmadianto - A11.2022.14827

Cara Menjalankan Proyek :
1. Clone repository.
2. Pastikan file docker-compose.yml sudah terkonfigurasi sesuai kebutuhan.
3. Jalankan aplikasi menggunakan docker-compose up -d.
4. Masuk ke Attach Shell jalankan 'python manage.py runserver 0.0.0.0:8000'.
5. /stock Menampilkan ringkasan stok barang termasuk stok total, total nilai stok, dan rata-rata harga barang.
6. /stock_bawah Menampilkan daftar barang yang stoknya di bawah ambang batas 5.
7. /kategori/34-39 Menampilkan laporan barang berdasarkan kategori tertentu.
8. /statkategori Menampilkan ringkasan per kategori, termasuk jumlah barang per kategori, total nilai stok tiap kategori, dan rata-rata harga barang dalam kategori tersebut.
9. /supplier Menampilkan ringkasan barang yang disuplai oleh masing-masing pemasok, termasuk jumlah barang per pemasok dan total nilai barang yang disuplai.
10. /allproduct Menampilkan ringkasan dari keseluruhan sistem, termasuk total jumlah barang, nilai stok keseluruhan, jumlah kategori, dan jumlah pemasok
