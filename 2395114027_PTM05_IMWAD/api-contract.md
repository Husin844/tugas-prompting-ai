## 3. Constraint Bisnis Penting

* **Unik & Kunci Utama (PK):** Setiap entitas (`User`, `ScanHistory`, `Catalog`) menggunakan pengidentifikasi unik (`uid`, `history_id`, `catalog_id`) sebagai *Primary Key*. Kolom `email` pada entitas `USER` diberikan konstrain `UNIQUE` untuk mencegah duplikasi pendaftaran akun.
* **Validasi Rentang Nilai (Range Constraint):** Field `confidence_score` pada `ScanHistoryRequest` wajib divalidasi ketat menggunakan validator Pydantic (`ge=0.0`, `le=1.0`) untuk memastikan skor keyakinan model TFLite selalu berada dalam batas persentase yang valid.
* **Non-Nullability:** Seluruh atribut utama seperti nama, email, *password_hash*, kategori sampah, dan status *recyclable* diatur wajib terisi (`NOT NULL`).

---

## 4. Tabel Mapping: Entitas vs Endpoint API

| Nama Entitas (Database/Pydantic) | Endpoint Terkait | Method | Keterangan Penggunaan |
| --- | --- | --- | --- |
| **User** | `/users/register` | `POST` | Menyimpan data pendaftaran pengguna baru ke basis data. |
| **User** | `/users/login` | `POST` | Memvalidasi kredensial email & password terhadap data entitas pengguna. |
| **ScanHistory** | `/histories` | `POST` | Menyimpan data hasil inferensi AI yang dikirim dari aplikasi *mobile*. |
| **ScanHistory** | `/histories` | `GET` | Mengambil sekumpulan data riwayat berdasarkan filter `user_id`. |
| **Catalog** | `/catalogs` | `GET` | Menyediakan data acuan informasi dan panduan pengelolaan sampah. |