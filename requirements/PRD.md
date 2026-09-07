Berikut adalah Draf Product Requirements Document (PRD) untuk aplikasi Wastify berdasarkan instruksi dan konteks yang telah Anda berikan:

---

# Draf Product Requirements Document (PRD)

**Nama Produk:** Wastify - Aplikasi Pendeteksi Jenis Sampah
**Fase:** Pengembangan Prototype (1 Semester)

## 1. Ringkasan Eksekutif

Wastify adalah aplikasi *mobile* berbasis edukasi dan utilitas yang bertujuan untuk menyelesaikan masalah inefisiensi pengelolaan sampah di tingkat rumah tangga. Menggunakan teknologi *Artificial Intelligence* (AI) berupa *Computer Vision*, aplikasi ini membantu masyarakat umum dengan cepat mengidentifikasi jenis sampah, kategori, dan kelayakan daur ulangnya hanya melalui jepretan kamera *smartphone*. Diharapkan solusi ini mampu menurunkan angka pembakaran sampah sembarangan dengan meningkatkan kesadaran serta pengetahuan praktis pengguna tentang pemilahan sampah.

## 2. Problem Statement & Bukti

**Problem Statement:**
Pertumbuhan jumlah sampah di Indonesia mencapai 35 juta timbulan pada tahun 2022. Namun, pengelolaan sampah menjadi sangat tidak efisien akibat rendahnya kesadaran dan edukasi masyarakat mengenai pemilahan jenis sampah. Ketidaktahuan ini secara langsung memicu perilaku membuang sampah sembarangan dan kebiasaan membakar sampah yang merusak lingkungan.

**Fakta (Berdasarkan Riset):**

* Jumlah timbulan sampah di Indonesia mencapai 35 juta pada tahun 2022.
* Hanya 1,2% rumah tangga di Indonesia yang aktif melakukan daur ulang sampah.
* Sebanyak 66,8% rumah tangga cenderung memilih membakar sampah akibat kurangnya pengetahuan tentang jenis sampah.
* Dari total 350.000 ton konsumsi botol PET, hanya 216.047 ton yang berhasil dikumpulkan untuk daur ulang.
* Teknologi *machine learning* (Computer Vision) telah terbukti mampu mencapai tingkat akurasi 90% dalam mendeteksi jenis sampah.

**Asumsi Tambahan (Validasi Dibutuhkan):**

* `[ASUMSI-04]` Masyarakat enggan memilah sampah karena merasa proses mempelajari jenis-jenis sampah terlalu rumit dan memakan waktu.

## 3. Target User & Stakeholder

| Peran | Kebutuhan Utama | Pengaruh terhadap Produk |
| --- | --- | --- |
| **Masyarakat Umum / Mahasiswa** (End User) `[ASUMSI-01]` | Cara yang cepat, praktis, dan akurat untuk mengetahui jenis sampah yang ada di rumah mereka tanpa harus menebak-nebak (seperti membedakan PET, organik, B3). | Tinggi - Menentukan adopsi dan retensi aplikasi. (Contoh Persona: Budi, 25 thn) |
| **Petugas Bank Sampah Lokal** (Stakeholder) `[ASUMSI-02]` | Memperoleh pasokan sampah dari warga yang sudah terpilah dengan benar sehingga mengurangi beban kerja penyortiran. | Menengah - Penerima manfaat tidak langsung. |
| **Dinas Lingkungan Hidup** (Stakeholder) `[ASUMSI-02]` | Penurunan volume sampah yang dibakar oleh rumah tangga dan peningkatan persentase daur ulang di tingkat masyarakat. | Menengah - Pengambil kebijakan/regulator. |

## 4. Value Proposition

* **Pain yang dikurangi:** Mengeliminasi kebingungan dan beban kognitif pengguna (seperti Budi) saat harus menghafal dan membedakan jenis-jenis plastik (misal: PET) atau limbah B3.
* **Gain yang diciptakan:** Memberikan kepastian instan (*instant feedback*) mengenai apakah suatu barang bekas masih memiliki nilai daur ulang (*recyclable*) atau tidak, sehingga menumbuhkan rasa percaya diri untuk memilah sampah.
* **Mengapa AI bukan gimmick:** Fitur *Computer Vision* adalah solusi inti (bukan sekadar pelengkap visual) karena masalah utamanya adalah "kesenjangan pengetahuan visual". Menggunakan *rule-based* konvensional (misal: fitur pencarian teks "botol bening") sangat tidak efisien dan rentan salah. AI secara langsung menerjemahkan visual yang dilihat pengguna menjadi informasi yang dapat ditindaklanjuti dengan akurasi teruji (90%).

## 5. Tujuan Produk & KPI Terukur

**Tujuan:** Mengedukasi dan memfasilitasi pengguna untuk memilah sampah secara mandiri melalui identifikasi visual yang cepat dan akurat.

**KPI & Cara Mengukurnya:**

1. **Usage/Adopsi:** Rata-rata jumlah gambar sampah yang dipindai per pengguna aktif bulanan (MAU).
* *Cara ukur:* Melacak *event trigger* penggunaan kamera/deteksi di analitik *mobile*.


2. **Keberhasilan Model AI (Real-world Accuracy):** Persentase deteksi AI yang dianggap "Benar/Membantu" oleh pengguna mencapai minimal 80%.
* *Cara ukur:* Menerapkan tombol *feedback* sederhana (Jempol ke Atas / Bawah) pada layar hasil deteksi `[ASUMSI-05]`.


3. **Retensi Pengguna:** 30% dari pengguna baru kembali menggunakan fitur *scan* pada minggu kedua (W2 Retention).
* *Cara ukur:* Melacak sesi pengguna aktif (*session tracking*).



## 6. Scope Fitur 3 Bulan (MoSCoW)

| Kategori | Fitur |
| --- | --- |
| **Must Have** | - 🤖 **Deteksi Jenis Sampah:** Pemindai visual via kamera untuk mendeteksi kategori (Organik, Anorganik, dll) dan status *Recyclable* (Ya/Tidak).<br>

<br>- Tampilan Hasil Identifikasi (*Result Screen*).<br>

<br>- Registrasi dan Login Pengguna. |
| **Should Have** | - Riwayat Pemindaian (*Scan History*) yang disimpan di akun pengguna.<br>

<br>- Daftar ensiklopedia singkat (*Waste Types Catalog*) untuk referensi manual. |
| **Could Have** | - Rekomendasi/Edukasi singkat cara membuang jenis sampah yang baru saja di-scan `[ASUMSI-06]`. |
| **Won't Have** | - Integrasi penjemputan sampah otomatis ke bank sampah (di luar batasan 1 semester).<br>

<br>- Sistem Poin/Gamifikasi kompleks. |

## 7. Non-Goals Eksplisit

* Aplikasi ini **tidak** bertujuan untuk menjadi *marketplace* tempat pengguna dapat melakukan jual beli sampah daur ulang secara finansial.
* Aplikasi ini **tidak** menyediakan layanan logistik (penjemputan atau pengiriman sampah) ke Tempat Pembuangan Akhir (TPA) atau Bank Sampah.

## 8. Asumsi & Risiko Utama + Mitigasi

| Risiko | Asumsi yang Mendasari | Rencana Mitigasi |
| --- | --- | --- |
| **Akurasi AI Menurun di Lingkungan Nyata** | Asumsi: Model yang akurat 90% di riset akan sama akuratnya dengan kondisi pencahayaan dan resolusi kamera pengguna yang beragam `[ASUMSI-07]`. | Membatasi ruang lingkup pendeteksian pada 5-7 kategori sampah domestik yang paling umum terlebih dahulu selama masa *prototype*. Menambahkan panduan pencahayaan saat kamera aktif. |
| **Keterbatasan Kapasitas / Konstrain Perangkat** | Asumsi: Mengingat ada limitasi waktu (1 semester) dan biaya, model klasifikasi berbasis *offline* akan berjalan lancar tanpa membuat aplikasi membesar. | Mengoptimalkan ukuran model menggunakan format khusus *mobile* yang ringan, agar tidak memakan memori ponsel secara berlebihan dan proses inferensi tetap cepat. |
| **Pengabaian Hasil Deteksi** | Asumsi: Pengguna yang sudah tahu status sampah akan otomatis membuangnya ke tempat yang benar `[ASUMSI-08]`. | Memberikan informasi aksi yang jelas pada halaman hasil (*Call to Action*), misalnya: teks merah untuk "Bahaya" jika itu limbah B3. |