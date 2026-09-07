Berikut adalah Draf *Software Requirements Specification* (SRS) untuk aplikasi Wastify berdasarkan dokumen PRD yang telah disepakati:

---

# Draf Software Requirements Specification (SRS)

**Nama Produk:** Wastify - Aplikasi Pendeteksi Jenis Sampah
**Versi:** 1.0 (Fase Prototype)

## 1. Tujuan, Scope, dan Definisi Istilah

**Tujuan:**
Dokumen ini bertujuan untuk mendefinisikan spesifikasi kebutuhan teknis perangkat lunak untuk purwarupa aplikasi Wastify guna memandu tim pengembang selama siklus pengembangan 1 semester.

**Scope:**
Pengembangan mencakup aplikasi *mobile* Android (Kotlin) yang memiliki fungsionalitas registrasi pengguna, pemindaian jenis sampah berbasis kamera (klasifikasi visual *offline*), penyimpanan riwayat pemindaian, dan penyediaan ensiklopedia jenis sampah. Lingkup ini tidak mencakup integrasi logistik penjemputan ke bank sampah maupun fitur jual-beli/marketplace.

**Definisi Istilah:**

* **Recyclable:** Status yang menunjukkan bahwa suatu jenis sampah dapat diproses daur ulang.
* **TFLite (TensorFlow Lite):** Format model *machine learning* yang dioptimalkan untuk perangkat *mobile* (berjalan secara *offline*).
* **Firebase:** Layanan *backend-as-a-service* untuk autentikasi dan basis data cloud.

## 2. User & Stakeholder, Lingkungan Operasi, Asumsi & Dependensi

* **User & Stakeholder:** Masyarakat umum/mahasiswa (End User), Petugas Bank Sampah (Penerima Manfaat), Dinas Lingkungan Hidup (Regulator).
* **Lingkungan Operasi:** Aplikasi berjalan di atas Sistem Operasi Android (minimal versi 8.0/Oreo). Perangkat harus memiliki memori kerja (RAM) minimal 2 GB dan resolusi kamera utama minimal 5 Megapiksel.
* **Asumsi & Dependensi:**
* [ASUMSI-07] Model AI dapat dikompresi ke dalam format TFLite tanpa kehilangan akurasi lebih dari 5% dari pengujian riset.
* Aplikasi bergantung pada ketersediaan koneksi internet hanya untuk *login* dan sinkronisasi riwayat (Firebase), namun fitur pemindaian utama (*inferensi AI*) bersifat mandiri (*offline*).



## 3. Functional Requirements (FR)

| ID | Deskripsi Kebutuhan fungsional | Prioritas MoSCoW | Metode Verifikasi |
| --- | --- | --- | --- |
| **FR-01** | Sistem harus dapat **memvalidasi kredensial login** pengguna saat **email dan password diinputkan** -> **masuk ke halaman utama**. | Must Have | Uji fungsional (Test Case: Valid & Invalid login) |
| **FR-02** | Sistem harus dapat **mendaftarkan akun baru** saat **form registrasi diisi lengkap** -> **data tersimpan di Firebase Auth**. | Must Have | Uji fungsional |
| **FR-03** | Sistem harus dapat **memproses gambar sampah** dari kamera saat **tombol pindai/shutter ditekan** -> **menghasilkan label kategori**. | Must Have | Uji fungsional (Kamera & Pemrosesan) |
| **FR-04** | Sistem harus dapat **menampilkan status recyclable (Ya/Tidak)** dari objek saat **label prediksi AI ditemukan** -> **tampil di layar hasil (Result Screen)**. | Must Have | Uji fungsional |
| **FR-05** | Sistem harus dapat **menyimpan data riwayat hasil scan** pengguna saat **terhubung internet** -> **daftar riwayat tampil di menu profil**. | Should Have | Uji fungsional (Database integration) |
| **FR-06** | Sistem harus dapat **menampilkan daftar informasi (katalog)** jenis sampah saat **menu edukasi diakses** -> **katalog teks dan gambar terbuka**. | Should Have | Uji fungsional |

## 4. Non-Functional Requirements (NFR)

| ID | Kategori (ISO/IEC 25010) | Metrik Target & Kondisi Ukur | Metode Verifikasi |
| --- | --- | --- | --- |
| **NFR-01** | *Performance Efficiency* (Time Behaviour) | Latensi/waktu inferensi AI maksimal **2,0 detik** per gambar saat diproses *offline* pada ponsel kelas menengah (Spesifikasi referensi: RAM 3GB, prosesor setara Snapdragon 600 series). | *Performance / Load Testing* (Pengukuran *timestamp*) |
| **NFR-02** | *Reliability* (Maturity/Accuracy) | Akurasi klasifikasi model AI minimal **80%** (F1-Score) saat diuji menggunakan dataset pengujian eksternal di bawah kondisi pencahayaan normal (minimal 300 lux). | *Accuracy Evaluation / Data Science Metrics* |
| **NFR-03** | *Performance Efficiency* (Resource Utilization) | Ukuran file model AI terenkapsulasi (TFLite) tidak melebihi batas maksimal **25 MB** dan alokasi memori RAM saat aplikasi memindai maksimal **150 MB**. | *Resource Profiling* (Android Studio Profiler) |
| **NFR-04** | *Usability* (Operability) | Pengguna dapat mencapai hasil pemindaian sampah dari halaman utama (*Home*) maksimal dalam **3 kali ketukan layar (clicks)**. | *Usability Testing* |
| **NFR-05** | *Security & Privacy* (Confidentiality) | Seluruh sandi pengguna (password) **wajib di-*hash*** (minimal bcrypt/PBKDF2 bawaan Firebase) sebelum disimpan ke basis data *cloud*. | *Code Review / Security Audit* |

## 5. Kebutuhan Data Minimum Fitur AI

* **Input Data:** File gambar statis dari tangkapan kamera perangkat (*array* matriks RGB). Gambar akan secara otomatis diubah ukurannya (*resize/crop*) oleh sistem (misalnya menjadi 224x224 piksel) dan dinormalisasi nilainya sebelum masuk ke lapisan model TFLite.
* **Output Model:**
* Sebuah *array* skor probabilitas (rentang 0.0 hingga 1.0) untuk 5-7 kelas sampah utama (misal: Organik, Kertas, Plastik PET, Logam, B3).
* *String* teks nama kategori klasifikasi dengan skor probabilitas tertinggi (contoh: "Plastik PET").
* *Boolean/Flag* untuk menentukan status (Contoh: `isRecyclable = True`).



## 6. Aturan Bisnis Hasil Riset

1. **Klasifikasi Utama:** Sistem wajib mampu membedakan jenis material yang sering dibakar/tidak didaur ulang oleh rumah tangga (merujuk pada riset BPS 66,8% dan studi botol PET). Batasan prototipe: Organik, Plastik PET, Kertas/Kardus, Logam, dan Limbah Berbahaya (B3).
2. **Keputusan Prediksi:** Jika skor probabilitas atau *confidence level* dari model *Computer Vision* berada di bawah angka 50%, sistem dilarang menebak secara acak, melainkan harus mengeluarkan respons (*fallback*): "Objek tidak dikenali, arahkan kamera dengan lebih jelas".
3. **Sinkronisasi:** Pemindaian harus selalu bisa dilakukan *offline*. Penyimpanan riwayat ke server (Firebase Realtime Database) dilakukan secara *asynchronous* ketika pengguna terhubung ke internet.

## 7. Matriks Traceability

| Fitur di PRD (Scope MoSCoW) | ID Functional Requirements (FR) | ID Non-Functional Requirements (NFR) |
| --- | --- | --- |
| Registrasi dan Login Pengguna | FR-01, FR-02 | NFR-05 |
| Deteksi Jenis Sampah (AI Vision) | FR-03 | NFR-01, NFR-02, NFR-03, NFR-04 |
| Tampilan Hasil Identifikasi & *Recyclable* | FR-04 | NFR-01, NFR-04 |
| Riwayat Pemindaian (*Scan History*) | FR-05 | NFR-05 |
| Daftar Ensiklopedia Singkat (*Catalog*) | FR-06 | NFR-04 |