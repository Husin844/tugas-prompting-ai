[Peran]   Kamu adalah backend engineer senior ahli FastAPI / Next.js API Routes.

[Tugas]   Generate scaffold struktur folder modular (Router -> Service -> Repository) berdasarkan spesifikasi OpenAPI Wastify berikut.

[Konteks]
  - OpenAPI : openapi: 3.0.3
info:
  title: Wastify API Service
  version: 1.0.0
  description: >
    Spesifikasi REST API untuk aplikasi Wastify (Mobile Android & Backend Pendukung).
    Menangani manajemen pengguna, sinkronisasi riwayat pemindaian sampah, serta katalog edukasi.
    [ASUMSI-01]: Inferensi model AI utama berjalan secara on-device (offline) menggunakan TFLite,
    sementara endpoint /predictions digunakan untuk sinkronisasi hasil scan dan pencatatan riwayat.
servers:
  - url: http://localhost:8000/api/v1
    description: Development Server (Local FastAPI)
  - url: https://api.wastify.app/v1
    description: Production Server (Placeholder)

paths:
  /users/register:
    post:
      summary: Pendaftaran Akun Pengguna Baru
      description: Mendaftarkan akun baru ke sistem backend dan menyimpan kredensial dengan enkripsi hash.
      tags:
        - Users
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UserRegisterRequest'
      responses:
        '201':
          description: Akun berhasil dibuat
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UserResponse'
        '400':
          description: Data input tidak valid atau email sudah terdaftar
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '422':
          description: Kesalahan validasi format skema data (Unprocessable Entity)
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: Kesalahan internal server (Internal Server Error)
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'

  /users/login:
    post:
      summary: Autentikasi Pengguna (Login)
      description: Memvalidasi email dan password pengguna, serta mengembalikan token akses sesi.
      tags:
        - Users
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UserLoginRequest'
      responses:
        '200':
          description: Login berhasil dan token akses diterbitkan
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AuthTokenResponse'
        '401':
          description: Autentikasi gagal (kredensial salah atau tidak terdaftar)
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '422':
          description: Format data masukan tidak sesuai
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: Kesalahan server internal
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'

  /histories:
    post:
      summary: Menyimpan Riwayat Pemindaian Sampah
      description: Menyinkronkan dan menyimpan data hasil klasifikasi pemindaian sampah dari perangkat ke database server.
      tags:
        - AI
        - Histories
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ScanHistoryRequest'
      responses:
        '201':
          description: Riwayat pemindaian berhasil disimpan
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ScanHistoryResponse'
        '400':
          description: Format payload tidak lengkap atau salah
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '401':
          description: Token akses tidak valid atau kedaluwarsa (Unauthorized)
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: Kesalahan database server
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
    get:
      summary: Mendapatkan Daftar Riwayat Pemindaian Pengguna
      description: Mengambil seluruh riwayat pemindaian sampah yang pernah dilakukan oleh pengguna tertentu.
      tags:
        - Histories
      parameters:
        - name: user_id
          in: query
          required: true
          schema:
            type: string
          description: ID unik pengguna
      responses:
        '200':
          description: Daftar riwayat berhasil diambil
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/ScanHistoryResponse'
        '401':
          description: Sesi tidak terautentikasi
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '404':
          description: Data riwayat pengguna tidak ditemukan
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: Kesalahan internal server
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'

  /catalogs:
    get:
      summary: Mengambil Katalog Informasi Jenis Sampah
      description: Menyediakan daftar panduan edukasi jenis sampah dan cara pengelolaan mandirinya.
      tags:
        - Catalogs
      responses:
        '200':
          description: Berhasil mengambil daftar katalog edukasi
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/CatalogItemResponse'
        '404':
          description: Data katalog tidak tersedia
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: Kesalahan internal server
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'

components:
  schemas:
    UserRegisterRequest:
      type: object
      required:
        - name
        - email
        - password
      properties:
        name:
          type: string
          example: Budi Pratama
        email:
          type: string
          format: email
          example: budi.user@email.com
        password:
          type: string
          format: password
          minLength: 8
          example: SecurePassword123

    UserLoginRequest:
      type: object
      required:
        - email
        - password
      properties:
        email:
          type: string
          format: email
          example: budi.user@email.com
        password:
          type: string
          format: password
          example: SecurePassword123

    UserResponse:
      type: object
      properties:
        uid:
          type: string
          example: usr_9f83a7bc1234
        name:
          type: string
          example: Budi Pratama
        email:
          type: string
          format: email
          example: budi.user@email.com
        created_at:
          type: string
          format: date-time
          example: '2026-10-03T12:00:00Z'

    AuthTokenResponse:
      type: object
      properties:
        access_token:
          type: string
          example: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
        token_type:
          type: string
          example: bearer
        user:
          $ref: '#/components/schemas/UserResponse'

    ScanHistoryRequest:
      type: object
      required:
        - user_id
        - category_name
        - is_recyclable
        - confidence_score
      properties:
        user_id:
          type: string
          example: usr_9f83a7bc1234
        category_name:
          type: string
          example: Plastik PET
        is_recyclable:
          type: boolean
          example: true
        confidence_score:
          type: number
          format: float
          example: 0.89

    ScanHistoryResponse:
      type: object
      properties:
        history_id:
          type: string
          example: hst_1122334455
        user_id:
          type: string
          example: usr_9f83a7bc1234
        category_name:
          type: string
          example: Plastik PET
        is_recyclable:
          type: boolean
          example: true
        confidence_score:
          type: number
          format: float
          example: 0.89
        timestamp:
          type: integer
          example: 1727978400000

    CatalogItemResponse:
      type: object
      properties:
        catalog_id:
          type: string
          example: cat_01
        title:
          type: string
          example: Panduan Pengelolaan Botol Plastik PET
        description:
          type: string
          example: Pastikan botol dicuci bersih dan dilepas labelnya sebelum dimasukkan ke tempat daur ulang.
        category_type:
          type: string
          example: Anorganik / Daur Ulang

    ErrorResponse:
      type: object
      properties:
        error_code:
          type: string
          example: INVALID_CREDENTIALS
        message:
          type: string
          example: Email atau password yang Anda masukkan salah.
        status:
          type: integer
          example: 401
  - Stack   : FastAPI
  - DB      : SQLite+SQLAlchemy

[Format output]
  1) Struktur folder lengkap (tree teks modular: routers/, services/, repositories/, models/, core/).
  2) Boilerplate kode tiap lapisan untuk 1 resource contoh (/users).
  3) Konfigurasi koneksi DB (SQLAlchemy session generator).
  4) Template .env.example: DATABASE_URL, SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES, MODEL_PATH, SCALER_PATH, MAX_FILE_SIZE_MB.

[Aturan]
- Pisahkan lapisan secara ketat; tidak ada logika bisnis langsung di router.
- Repository hanya mengurus query DB; Service menangani validasi bisnis & inferensi.
- Semua konfigurasi sensitif wajib lewat env, DILARANG KERAS di-hardcode.



[Peran]   Kamu adalah backend security engineer ahli OAuth2 Password Flow dan JWT.

[Tugas]   Implementasikan autentikasi JWT lengkap pada stack FastAPI berdasarkan endpoint auth pada spesifikasi OpenAPI Wastify.

[Konteks]
  - Endpoint auth : POST /auth/signup, POST /auth/login, POST /auth/refresh, GET /auth/me
  - Stack         : FastAPI + python-jose + passlib[bcrypt]

[Format output]
  1) Utility hash password bcrypt (hash_password dan verify_password).
  2) Generator token pair: Access Token (exp: 30 menit) + Refresh Token (exp: 7 hari).
  3) Dependency / middleware protected route (ekstraksi & validasi Bearer JWT token).
  4) Handler signup: validasi schema, cek duplikasi email, hashing password, simpan ke repository.
  5) Handler login: verifikasi identitas pengguna, cek password hash, kembalikan token pair JSON.
  6) Handler refresh: validasi refresh token dari body/header, terbitkan access token baru.
  7) Protected endpoint GET /auth/me: kembalikan payload profil pengguna yang sedang login.

[Aturan]
- SECRET_KEY wajib diambil dari environment variable. Password TIDAK BOLEH disimpan plaintext.
- Kembalikan HTTP 401 jika token kadaluarsa/invalid; return 403 jika otorisasi tidak memadai.
- DILARANG menaruh informasi rahasia (password hash, token secret) di dalam claims payload JWT.



 **Prompt AI (D.2 — Implementasi Autentikasi JWT & Password Hashing)** yang terlewat sebelumnya. Anda dapat menyalin prompt ini untuk menguji atau menghasilkan kode autentikasi secara mandiri:

```text
[Peran]   Kamu adalah backend security engineer ahli OAuth2 Password Flow dan JWT.

[Tugas]   Implementasikan autentikasi JWT lengkap pada stack FastAPI berdasarkan endpoint auth pada spesifikasi OpenAPI Wastify.

[Konteks]
  - Endpoint auth : POST /auth/signup, POST /auth/login, POST /auth/refresh, GET /auth/me
  - Stack         : FastAPI + python-jose + passlib[bcrypt]

[Format output]
  1) Utility hash password bcrypt (hash_password dan verify_password).
  2) Generator token pair: Access Token (exp: 30 menit) + Refresh Token (exp: 7 hari).
  3) Dependency / middleware protected route (ekstraksi & validasi Bearer JWT token).
  4) Handler signup: validasi schema, cek duplikasi email, hashing password, simpan ke repository.
  5) Handler login: verifikasi identitas pengguna, cek password hash, kembalikan token pair JSON.
  6) Handler refresh: validasi refresh token dari body/header, terbitkan access token baru.
  7) Protected endpoint GET /auth/me: kembalikan payload profil pengguna yang sedang login.

[Aturan]
- SECRET_KEY wajib diambil dari environment variable. Password TIDAK BOLEH disimpan plaintext.
- Kembalikan HTTP 401 jika token kadaluarsa/invalid; return 403 jika otorisasi tidak memadai.
- DILARANG menaruh informasi rahasia (password hash, token secret) di dalam claims payload JWT.

```



[Peran]   Kamu adalah API Security Auditor berpengalaman standar OWASP API Security Top 10 (2023).

[Tugas]   Audit kode backend Wastify terhadap kerentanan OWASP API dan berikan perbaikan konkret.

[Konteks]
  - Kode yang diaudit : Router /histories (GET/POST) dan handler autentikasi / validasi payload.
  - Fokus utama       : API1:2023 Broken Object Level Authorization (BOLA/IDOR), API2:2023 Broken Authentication, API4:2023 Unrestricted Resource Consumption, serta sanitasi masukan inferensi fitur AI (Validasi ukuran gambar & MIME type).

[Format output]
  1) Tabel Audit: | Endpoint | Kerentanan OWASP | Tingkat Risiko | Kode Patch | Status Verifikasi |
  2) Kode patch konkret (minimal diff) untuk setiap celah otorisasi kepemilikan objek (anti-BOLA) pada endpoint riwayat (/histories).
  3) Middleware/helper sanitasi input AI: validasi ukuran file (<=5MB), MIME whitelisting (image/jpeg, image/png), dan pembersihan string input.

[Aturan]
- Hanya audit kode yang disediakan; fokus pada pencegahan eksploitasi nyata.
- Pada operasi CRUD berparameter ID (GET/PUT/DELETE /items/{id}), WAJIB ada pengecekan: apakah data tersebut benar milik current_user.id? Jika tidak cocok, tolak HTTP 403 Forbidden.
- Perbaikan bersifat presisi, tidak menulis ulang arsitektur sistem secara berlebihan.