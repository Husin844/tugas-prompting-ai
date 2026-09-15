[Peran] 
Kamu adalah agile product owner dan business analyst.

[Tugas] 
Ubah daftar Functional Requirements (FR) pada SRS terlampir menjadi DRAF User Stories untuk fitur prioritas Must dan Should (termasuk fitur AI ★).

[Konteks]
SRS PTM-02 : 
- FR-01: Sistem memvalidasi kredensial login pengguna (email dan password) (Prioritas: Must Have)[cite: 6].
- FR-02: Sistem mendaftarkan akun baru dan menyimpan ke Firebase Auth (Prioritas: Must Have)[cite: 3, 6].
- FR-03: Sistem memproses gambar sampah dari kamera menggunakan model TFLite secara offline untuk menghasilkan label kategori (Prioritas: Must Have)[cite: 3, 6].
- FR-04: Sistem menampilkan status recyclable (Ya/Tidak) di layar hasil (Result Screen) (Prioritas: Must Have)[cite: 3, 6].
- FR-05: Sistem menyimpan data riwayat hasil scan pengguna saat terhubung internet (Prioritas: Should Have)[cite: 6].
- FR-06: Sistem menampilkan daftar informasi (katalog) jenis sampah saat menu edukasi diakses (Prioritas: Should Have)[cite: 6].

Persona Pengguna : Budi, 25 tahun, pekerja kantoran/mahasiswa yang ingin mulai memilah sampah di rumah namun sering bingung membedakan jenis sampah[cite: 5].
Fitur AI Utama ★ : Klasifikasi gambar sampah secara offline menggunakan model TensorFlow Lite (TFLite) untuk mendeteksi kategori dan status daur ulang[cite: 3, 6].
Platform : Mobile (Android / Kotlin)[cite: 6].

[Format output]
1) Tabel User Story:
- ID Story (US-01..)
- Narasi: "Sebagai <peran>, saya ingin <kemampuan>, agar <manfaat>"
- FR Asal
- Prioritas MoSCoW
- Kategori (Fitur Inti / Fitur AI ★)

2) Evaluasi singkat prinsip INVEST per story (terutama cek apakah cukup Small dan Testable).

3) Jika ada story yang terlalu besar (Epic), pecah menjadi 2-3 story kecil yang berdiri sendiri.

[Aturan]
- Peran harus mengacu ke persona nyata (misal: Budi sebagai masyarakat/mahasiswa), bukan sebutan umum seperti "sebagai pengguna".
- Manfaat harus menjelaskan nilai nyata bagi pengguna, bukan mengulang aksi fitur.
- Jangan menulis detail antarmuka atau coding di sini.
- Gunakan Bahasa Indonesia yang lugas dan wajar.



Berikut adalah rumusan **Prompt AI** yang sesuai dengan materi Tahap 2 dari modul praktikum Anda, lengkap dengan konteks dan data pendukung dari dokumen PRD dan SRS yang telah disiapkan:

```text
[Peran] 
Kamu adalah system analyst aplikasi cerdas.

[Tugas] 
Buat DRAFT Use Case formal untuk User Story prioritas, fokuskan pada fitur berbasis AI ★ dan alur penanganan kegagalannya.

[Konteks]
User Story Tahap 1 : 
- US-03: Sebagai Budi, saya ingin memproses gambar sampah dari kamera secara offline, agar sistem dapat mengenali kategori sampah secara instan tanpa hambatan koneksi internet[cite: 3, 6].
- US-04: Sebagai Budi, saya ingin melihat status kelayakan daur ulang (recyclable atau tidak) di layar hasil, agar saya tahu secara pasti bagaimana cara membuang sampah tersebut dengan benar[cite: 3, 6].

Rincian Layanan AI : Model TensorFlow Lite (TFLite) untuk klasifikasi gambar sampah secara lokal (offline) di perangkat mobile[cite: 3, 6].
Batas Waktu Respon : 
- Latensi inferensi AI maksimal 2,0 detik per gambar[cite: 6].
- Tingkat akurasi minimal 80%[cite: 6].
- Ambang batas keyakinan (confidence level) minimum 50%; jika di bawah itu, picu fallback[cite: 6].

[Format output]
Untuk setiap Use Case cantumkan:
- ID dan Nama Use Case (gunakan kata kerja aktif)
- Aktor Utama (pengguna) dan Aktor Pendukung (layanan inferensi AI / database)
- Precondition dan Postcondition
- Alur Utama (langkah bernomor dari awal sampai tugas selesai)
- Alur Alternatif (variasi masukan yang wajar)
- Alur Eksepsi Khusus AI (wajib ada):
  * Kualitas masukan data rendah atau buram sebelum dikirim
  * Permintaan ke server AI mengalami timeout atau gagal koneksi
  * Skor keyakinan model berada di bawah ambang batas (low confidence)
- Kaitan ke ID User Story dan FR asal.

[Aturan]
- Fokus pada alur logika sistem dan interaksi pengguna, bukan tata letak tombol di layar.
- Gunakan Bahasa Indonesia baku dan format Markdown yang rapi.

```



[Peran] 
Kamu adalah UX designer dan interaction analyst produk cerdas.

[Tugas] 
Susun DRAFT User Flow terstruktur untuk fitur AI ★ dan 1 fitur utama lainnya (fitur autentikasi/login).

[Konteks]
Persona & Skenario : Budi, 25 tahun, pekerja kantoran/mahasiswa yang ingin mulai memilah sampah di rumah namun sering bingung membedakan jenis sampah, sehingga membutuhkan alur aplikasi yang instan dan tidak membingungkan[cite: 5].
Use Case Tahap 2 : 
- UC-01: Memproses Gambar Sampah Menggunakan Model AI (TFLite lokal secara offline)[cite: 3, 6].
- UC-02: Memvalidasi Kredensial Pengguna (Login)[cite: 6].
NFR Respon Waktu : 
- Latensi inferensi model AI maksimal 2,0 detik per gambar[cite: 6].
- Batas ambang keyakinan (confidence level) minimum 50%; jika di bawah itu, picu mekanisme fallback atau konfirmasi[cite: 6].

[Format output]
1) Langkah alur pengguna dari titik masuk, pengisian data, pemrosesan, sampai selesai untuk kedua fitur tersebut.
2) Gambarkan secara jelas 4 status sistem pada fitur AI:
   - Validasi awal di perangkat pengguna (sebelum data diproses model).
   - Indikator proses saat model AI sedang menganalisis (loading).
   - Penanganan hasil (akurasi yakin vs hasil meragukan/low confidence).
   - Jalur cadangan (fallback) saat AI gagal merespons atau objek buram.
3) Diagram alur dalam format kode Mermaid atau teks langkah terstruktur.
4) Tabel kaitan alur ke Use Case yang bersangkutan.

[Aturan]
- Rancang alur yang ramah pengguna; jangan berasumsi AI selalu berhasil seketika.
- Gunakan Bahasa Indonesia baku dan format Markdown yang rapi.



[Peran] 
Kamu adalah QA engineer dan test analyst.

[Tugas] 
Tulis DRAFT Acceptance Criteria berpola Given-When-Then untuk setiap User Story aplikasi Wastify.

[Konteks]
Daftar User Story : 
- US-01: Validasi kredensial login (email dan password)[cite: 6].
- US-02: Pendaftaran akun baru ke Firebase Auth[cite: 3, 6].
- US-03: Pemrosesan gambar sampah dari kamera menggunakan model TFLite secara offline untuk menghasilkan label kategori[cite: 3, 6].
- US-04: Menampilkan status recyclable (Ya/Tidak) di layar hasil (Result Screen)[cite: 3, 6].

Use Case & Eksepsi : 
- UC-01 & UC-02 mencakup alur sukses, alur alternatif form kosong/salah, serta alur eksepsi khusus AI (deteksi gambar buram/gelap, penanganan low confidence < 50%, dan batasan waktu inferensi)[cite: 3, 6].

NFR Ukuran Metrik : 
- Latensi inferensi AI maksimal 2,0 detik per gambar[cite: 6].
- Akurasi model minimal 80%[cite: 6].
- Confidence level minimum 50% (jika di bawah itu, picu fallback)[cite: 6].
- Keamanan sandi wajib di-hash sebelum disimpan[cite: 6].

[Format output]
Buat 2-4 skenario per User Story dengan format Gherkin:
Scenario: [nama skenario pengujian]
Given [kondisi awal sistem atau ketersediaan data]
When [aksi pengguna atau pemicu sistem]
Then [hasil yang teramati dan terukur]

Khusus User Story berlabel AI ★ (US-03 & US-04), wajib mencakup:
- Skenario normal (happy path)
- Skenario data masukan batas (edge case, misal: gambar buram atau confidence di bawah 50%)
- Skenario kegagalan respon atau batas waktu terlewati (misal: melebihi latensi 2,0 detik)

Sertakan juga usulan metode uji (unit test, pengujian integrasi, atau uji pengguna) di setiap akhir bagian.

[Aturan]
- Hindari kata tanpa patokan pasti seperti "harus cepat" atau "harus akurat".
- Gunakan angka dan hasil terukur (misal: "tampil dalam waktu <= 2,0 detik").
- Gunakan Bahasa Indonesia baku dan format Markdown yang rapi.



[Peran] 
Kamu adalah systems analyst dan lead developer.

[Tugas] 
Buat Draf Matriks Keterlacakan (Traceability Matrix) dalam bentuk tabel terstruktur yang menghubungkan kebutuhan awal dari SRS hingga rencana pengujian aplikasi Wastify.

[Konteks]
Data Keterlacakan yang Telah Disusun:
- FR-01 (Validasi Kredensial Login): terhubung ke US-01, UC-01, AC Login (Valid & Invalid), komponen Firebase Auth & UI Login, serta rencana uji Fungsional & Integrasi[cite: 6].
- FR-02 (Pendaftaran Akun Baru): terhubung ke US-02, UC-02, AC Register (Sukses & Duplikat), komponen Firebase Auth & Form Database, serta rencana uji Fungsional & Security Audit[cite: 3, 6].
- FR-03 (Pemrosesan Gambar AI): terhubung ke US-03, UC-01 (AI Processing), AC Pemrosesan Normal, Edge Case (Buram/Low Confidence), & Timeout, komponen Model TFLite & UI Kamera, serta rencana uji Performance Testing & Unit Test[cite: 3, 6].
- FR-04 (Menampilkan Status Recyclable): terhubung ke US-04, UC-02 (Result Screen), AC Tampilan Status Sukses & Error State, komponen UI Result Screen & Modul Logika, serta rencana uji UI Component & Usability Testing[cite: 3, 6].

[Format output]
Buat tabel matriks dengan kolom persis seperti berikut:
1) ID Kebutuhan (SRS)
2) ID User Story
3) ID Use Case
4) ID Acceptance Criteria
5) Komponen Teknis & Model AI
6) Rencana Uji (P12-P13)

[Aturan]
- Pastikan seluruh ID terhubung secara logis dan konsisten dari SRS sampai rencana uji.
- Gunakan Bahasa Indonesia baku dan format Markdown yang rapi.



