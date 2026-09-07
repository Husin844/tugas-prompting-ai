[Peran]
Kamu adalah product manager senior untuk produk Mobile berfitur AI.

[Tugas]
Susun DRAF PRD ringkas untuk "Wastify - Aplikasi Pendeteksi Jenis Sampah" berdasarkan kasus berikut.

[Konteks]
Problem statement: Pertumbuhan jumlah sampah di Indonesia terus meningkat sejalan dengan pertambahan penduduk, mencapai 35 juta timbulan pada tahun 2022. Pengelolaan sampah menjadi tidak efisien karena rendahnya kesadaran dan kurangnya edukasi masyarakat mengenai jenis-jenis sampah yang dapat didaur ulang. Hal ini memicu perilaku membuang sampah sembarangan dan membakar sampah yang mencemari lingkungan.
Target user: Masyarakat umum, pengguna smartphone Android tingkat rumah tangga, dan mahasiswa [ASUMSI-01].
Stakeholder lain: Petugas bank sampah lokal dan Dinas Lingkungan Hidup [ASUMSI-02].
Persona ringkas: Budi, 25 tahun, pekerja kantoran yang ingin mulai memilah sampah di rumah namun sering bingung membedakan mana plastik PET, organik, atau limbah B3 [ASUMSI-03].
Bukti riset: 
- Menurut data BPS, hanya sekitar 1,2% rumah tangga yang aktif melakukan daur ulang sampah, sedangkan 66,8% cenderung memilih untuk membakar sampah karena kurangnya pengetahuan tentang jenis sampah[cite: 3].
- Dari total 350.000 ton botol PET yang dikonsumsi, hanya 216.047 ton yang berhasil dikumpulkan untuk didaur ulang[cite: 3].
- Penelitian sebelumnya menunjukkan bahwa teknologi machine learning dengan tingkat akurasi 90% sangat efektif dalam membantu mendeteksi sampah[cite: 3].
Platform & stack: Mobile (Android / Kotlin), arsitektur MVVM, Firebase (Auth, Storage, Realtime Database), dan model AI berbasis TensorFlow Lite (TFLite) untuk klasifikasi offline/cache lokal[cite: 3].
Fitur AI inti: Klasifikasi gambar (Computer Vision) berbasis kamera smartphone untuk mengidentifikasi kategori dan jenis sampah, serta status apakah sampah tersebut dapat didaur ulang (recyclable) atau tidak[cite: 3].
Konstrain: Prototype 1 semester; data & biaya AI terbatas.

[Format output]
1) Ringkasan eksekutif;
2) Problem statement & bukti (pisahkan fakta vs asumsi);
3) Target user & stakeholder (tabel peran-kebutuhan-pengaruh);
4) Value proposition: pain yang dikurangi, gain yang diciptakan, mengapa fitur AI bukan gimmick;
5) Tujuan produk & KPI terukur (+ cara mengukurnya);
6) Scope fitur 3 bulan: tabel MoSCoW (fitur AI bertanda 🤖);
7) Non-goals eksplisit; 
8) Asumsi & risiko utama + mitigasi.

[Aturan]
Hanya gunakan data pada [Konteks]; bila kurang, tulis [ASUMSI-XX] lalu lanjutkan.
Jangan menulis solusi teknis/arsitektur (itu urusan SRS/HLD/LLD).
Gunakan Bahasa Indonesia baku dan format Markdown.