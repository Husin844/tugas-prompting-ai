[Peran]   Kamu adalah backend architect senior, ahli REST API dan OpenAPI 3.0.

[Tugas]   Buat DRAF spesifikasi OpenAPI 3.0 (YAML) untuk semua endpoint berdasarkan LLD dan user stories aplikasi Wastify berikut.

[Konteks]
  - LLD awal (entitas & endpoint kasar) : Endpoint otentikasi (Firebase Auth / kustom backend) dan pengelolaan riwayat pemindaian sampah (ScanHistory) serta katalog edukasi.
  - User stories & acceptance criteria  : US-01 (Login), US-02 (Registrasi), US-03 (Pemrosesan TFLite offline), dan US-04 (Layar Hasil Recyclable).
  - Stack backend                     : FastAPI (Python)
  - Database                          : SQLite

[Format output]
  Hasilkan YAML OpenAPI 3.0:
-   info: title, version, description
-   servers: localhost (dev) + placeholder production
-   paths: tiap endpoint dengan method, summary, parameters, requestBody, responses (200/201, 400, 401, 404, 422, 500)
-   components/schemas: model data reusable
  Tandai endpoint fitur AI dengan tag AI.

[Aturan]
-   Resource naming noun jamak (/users, /predictions, /histories).
-   Minimal 3 kode respons per endpoint (sukses + 4xx + 5xx).
-   Gap dari LLD: komentar [ASUMSI-XX] di YAML.
-   DILARANG tambah endpoint di luar LLD/user stories.



[Peran]   Kamu adalah database architect dan backend engineer senior.

[Tugas]   Buat ERD (Mermaid) dan skema Pydantic (Python) sesuai stack tim Wastify, dari OpenAPI + LLD yang direvisi.

[Konteks]
  - OpenAPI hasil revisi : Komponen schemas dari file openapi.yaml Wastify (UserRegisterRequest, UserLoginRequest, UserResponse, ScanHistoryRequest, ScanHistoryResponse, CatalogItemResponse, ErrorResponse).
  - LLD awal (entitas)   : Entitas User (Pengguna), ScanHistory (Riwayat Pemindaian AI TFLite), dan Catalog (Katalog Edukasi Sampah).
  - Stack                : FastAPI + Pydantic v2 (Python)
  - Database             : SQLite

[Format output]
  1) ERD Mermaid: entitas, atribut (nama, tipe, constraint), relasi, PK, FK.
  2) Skema Pydantic (Python): field types, validator (misal: rentang confidence_score 0.0-1.0, format email), relasi, enum.
  3) Constraint bisnis penting (unique email, not null, enum/range value).
  4) Tabel mapping: entitas vs endpoint yang memakainya.

[Aturan]
- Field Pydantic WAJIB sinkron dengan components/schemas OpenAPI.
- Tipe tepat: string/UUID PK, datetime/timestamp, float, boolean.
- Gap: tandai [ASUMSI-XX].
- Gunakan Bahasa Indonesia untuk penjelasan dan komentar kode Python.