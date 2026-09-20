[Peran] 
Kamu adalah software architect senior untuk aplikasi Mobile berfitur AI.

[Tugas] 
Buat DRAF High-Level Design (HLD) dari dokumen PRD, SRS, dan User Story/AC Wastify berikut.

[Konteks]
- PRD hasil revisi : Draf PRD Wastify (Fokus prototype 1 semester, target persona Budi, pemindaian sampah untuk edukasi dan status recyclable).
- SRS hasil revisi : Draf SRS Wastify (FR-01 s.d. FR-06, NFR latensi AI maksimal 2,0 detik, akurasi minimal 80%, model TFLite offline, dan Firebase Auth).
- User stories/AC P3 : Kumpulan User Story (US-01 s.d. US-04), Use Case (UC-01 & UC-02), User Flow, dan Acceptance Criteria berpola Given-When-Then yang sudah disusun sebelumnya.
- Platform & stack : Mobile Android / Kotlin / TensorFlow Lite (TFLite) / Firebase.
- Konstrain : Prototype 1 semester; satu fitur AI inti (klasifikasi sampah offline); biaya minimal.

[Format output]
1) Diagram arsitektur (Mermaid): client (Android App) → local AI engine (TFLite) & local storage → cloud backend (Firebase Auth / Database);
2) Deskripsi komponen: peran, tanggung jawab, teknologi usulan. Untuk keputusan penting (khususnya pemilihan AI on-device TFLite vs cloud API), sajikan tabel trade-off: akurasi, latensi, biaya, privasi, effort, lalu beri rekomendasi;
3) Aliran data end-to-end fitur AI: input kamera → preprocessing/validasi awal → inference TFLite → postprocessing → output layar hasil & penyimpanan riwayat, termasuk titik fallback saat model gagal atau low confidence (<50%);
4) Kontrak antarkomponen tingkat tinggi: API utama (Firebase Auth/Database), format data gambar (matrix RGB / resize 224x224), pemicu event;
5) Penempatan security & privacy by design: auth token, enkripsi hash password, data sensitif, logging;
6) Lingkungan deployment ringkas (development/staging/production untuk aplikasi mobile Android).

[Aturan]
- Desain hanya dari FR/NFR yang ada; jangan menambah fitur baru. Gap apa pun nyatakan sebagai [ASUMSI-XX].
- Jangan masuk ke detail class, method, atau query SQL (itu ranah LLD).
- Setiap keputusan besar diberi alasan 1–2 kalimat + alternatif.



[Peran] 
Kamu adalah software engineer senior (Android/Kotlin & Firebase).

[Tugas] 
Buat DRAF LLD untuk fitur prioritas Must pada SRS berdasarkan HLD hasil revisi aplikasi Wastify.

[Konteks]
- SRS hasil revisi : Draf SRS Wastify (FR-01 s.d. FR-04 untuk fitur Must Have: Validasi Login, Registrasi Firebase Auth, Pemrosesan TFLite offline, dan Layar Hasil Recyclable).
- HLD hasil revisi : High-Level Design Wastify (Arsitektur klien Android dengan modul kamera, TFLite local engine, SharedPreferences, dan Firebase Cloud Backend).
- Stack & pola : Android, Kotlin, MVVM Architecture, TensorFlow Lite, Firebase Authentication & Realtime Database.

[Format output]
1) Desain modul/class 2-3 fitur Must terpenting (termasuk fitur AI dan Auth): tanggung jawab, atribut kunci, method utama — cukup detail agar siap dikode;
2) Skema data: entitas, relasi, constraint (skema teks ERD/NoSQL untuk Firebase Realtime Database: User dan ScanHistory);
3) Spesifikasi API detail endpoint inti / layanan cloud (Firebase Auth & Database): method, path/reference, request/response (contoh JSON), daftar kode error;
4) Sequence/alur detail fitur AI: validasi input (cek buram/gelap) → preprocessing (resize 224x224) → pemanggilan model TFLite (inferensi lokal) → fallback (low confidence <50% / timeout) → respons; sertakan skenario timeout & kegagalan model;
5) Rancangan error handling & fallback (retry, pesan ramah, mode offline TFLite);
6) Tabel traceability: elemen desain ↔ ID FR/NFR (FR-01 s.d. FR-04, NFR-01 s.d. NFR-05).

[Aturan]
- Turunkan dari SRS/HLD; DILARANG mengubah requirement.
- Pilihan yang belum diputuskan (library tambahan, dsb.): sarankan 2 opsi + kriteria pilih, lalu tulis [KEPUTUSAN TIM: ...] yang wajib diisi tim.
- Nama class/field menggunakan bahasa Inggris; penjelasan menggunakan Bahasa Indonesia.