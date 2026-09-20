Berikut adalah Draf **Low-Level Design (LLD)** untuk fitur prioritas *Must Have* pada aplikasi **Wastify**, disusun berdasarkan spesifikasi SRS dan arsitektur HLD yang telah disepakati:

---

## 1. Desain Modul / Class (Fitur Must-Have)

Berikut adalah rancangan class utama menggunakan pola arsitektur **MVVM (Model-View-ViewModel)** untuk modul Autentikasi dan Pemrosesan AI:

### A. Modul Autentikasi (`auth`)

* **Class:** `AuthViewModel`
* **Tanggung jawab:** Mengelola logika bisnis proses login dan registrasi pengguna, serta menghubungkan *UI Layer* dengan *Firebase Auth Repository*.
* **Atribut Kunci:**
* `private val authRepository: AuthRepository`
* `private val _authState = MutableLiveData<Resource<FirebaseUser>>()`
* `val authState: LiveData<Resource<FirebaseUser>> get() = _authState`


* **Method Utama:**
* `fun loginUser(email: String, pass: String)`: Memvalidasi format input dan memanggil fungsi login ke *Firebase*.
* `fun registerUser(name: String, email: String, pass: String)`: Mendaftarkan akun baru dan memicu enkripsi *hash* sandi di *backend*.





### B. Modul AI Klasifikasi Sampah (`ai`)

* **Class:** `WasteClassifierViewModel`
* **Tanggung jawab:** Menangani alur penangkapan gambar, validasi kualitas lokal, pemanggilan modul TFLite secara *offline*, dan pengontrolan status *fallback*.
* **Atribut Kunci:**
* `private val tfliteHelper: TFLiteInterpreterHelper`
* `private val _scanResult = MutableLiveData<ScanResultState>()`
* `val scanResult: LiveData<ScanResultState> get() = _scanResult`


* **Method Utama:**
* `fun validateAndProcessImage(bitmap: Bitmap)`: Mengecek kelayakan gambar (tidak buram/gelap).
* `fun runInference(bitmap: Bitmap)`: Melakukan *resize* ($224 \times 224$), eksekusi model TFLite, dan evaluasi ambang batas *confidence* ($\ge 50\%$).





---

## 2. Skema Data (NoSQL / Firebase Realtime Database)

Struktur data berbasis entitas hierarkis untuk Firebase Realtime Database:

```json
{
  "users": {
    "$userId": {
      "uid": "string (PK)",
      "name": "string",
      "email": "string",
      "createdAt": "timestamp"
    }
  },
  "scan_histories": {
    "$historyId": {
      "historyId": "string (PK)",
      "userId": "string (FK to users)",
      "categoryName": "string (e.g., Plastic PET, Organic)",
      "isRecyclable": "boolean",
      "confidenceScore": "float",
      "timestamp": "timestamp"
    }
  }
}

```

* **Constraint:**
* `userId` wajib terikat dengan autentikasi unik dari Firebase Auth.
* `confidenceScore` bernilai desimal antara `0.0` sampai `1.0`.



---

## 3. Spesifikasi Layanan Cloud & Endpoint Inti (Firebase SDK)

Karena menggunakan Firebase, interaksi dilakukan via SDK dengan spesifikasi data abstrak berikut:

### A. Layanan Autentikasi (`Firebase Auth`)

* **Method:** `POST (SDK Internal)` via `FirebaseAuth.getInstance().signInWithEmailAndPassword()`
* **Request JSON Payload:**
```json
{
  "email": "budi.user@email.com",
  "password": "SecurePassword123"
}

```


* **Response JSON (Success):**
```json
{
  "uid": "Abc123Xyz999",
  "email": "budi.user@email.com",
  "idToken": "eyJhbGciOiJSUzI1NiIs..."
}

```


* **Daftar Kode Error:** `ERROR_INVALID_EMAIL`, `ERROR_WRONG_PASSWORD`, `ERROR_USER_NOT_FOUND`, `ERROR_EMAIL_ALREADY_IN_USE`.

### B. Layanan Basis Data (`Firebase Realtime Database`)

* **Method:** `PUT / PUSH` via `DatabaseReference.child("scan_histories").push()`
* **Request JSON Payload:**
```json
{
  "userId": "Abc123Xyz999",
  "categoryName": "Plastik PET",
  "isRecyclable": true,
  "confidenceScore": 0.89,
  "timestamp": 1726820400000
}

```


* **Daftar Kode Error:** `PERMISSION_DENIED`, `NETWORK_ERROR`, `DISCONNECTED`.

---

## 4. Sequence / Alur Detail Fitur AI ★

1. **Validasi Input:** Pengguna menekan tombol tangkap kamera $\rightarrow$ `CameraModule` mengambil *frame* bitmap $\rightarrow$ Sistem mengevaluasi tingkat ketajaman (*sharpness*) secara lokal.
* *Jika buram/gelap:* Sistem menghentikan proses dan memunculkan pesan error.


2. **Preprocessing:** Jika layak, gambar diteruskan ke `TFLiteInterpreterHelper` untuk diubah ukurannya (*resize*) menjadi matriks tensor piksel $224 \times 224 \times 3$ RGB.
3. **Pemanggilan Model (Inference):** Modul TFLite mengeksekusi inferensi lokal secara *offline* di perangkat dengan batasan waktu respons maksimal 2,0 detik.
4. **Evaluasi & Fallback (Low Confidence / Timeout):**
* Sistem membaca skor probabilitas tertinggi.
* Jika skor $< 50\%$ (*low confidence*) atau waktu eksekusi melewati batas $2,0$ detik (*timeout*), sistem memicu jalur *fallback* tanpa melakukan tebakan acak.


5. **Respons:** Jika skor $\ge 50\%$, sistem mengemas label kategori dan status *recyclable* untuk ditampilkan ke *Result Screen*.

---

## 5. Rancangan Error Handling & Fallback

* **Retry Mechanism:** Untuk sinkronisasi data riwayat ke Firebase saat jaringan terputus, sistem menggunakan penyimpanan lokal (*local caching / Room Database*) untuk mencoba ulang pengiriman (*retry*) secara otomatis saat koneksi internet kembali stabil.
* **Pesan Ramah Pengguna:** Mengganti kode galat teknis dengan teks interaktif yang mudah dipahami, contoh: *"Kamera kurang stabil atau objek terlalu gelap, silakan ambil ulang foto"* [KEPUTUSAN TIM: Menggunakan *Toast* atau *Custom Dialog* interaktif untuk notifikasi pesan error].
* **Mode Offline TFLite:** Fitur utama pemindai sampah tetap dapat berfungsi 100% tanpa koneksi internet karena model dienkapsulasi secara lokal di dalam aplikasi (*on-device*).

---

## 6. Tabel Traceability (Elemen Desain ↔ ID FR/NFR)

| Elemen Desain LLD | ID Kebutuhan Terkait | Keterangan Pemetaan |
| --- | --- | --- |
| `AuthViewModel`, `Firebase Auth SDK` | FR-01, FR-02, NFR-05 | Menangani validasi login, registrasi akun, dan keamanan *hashing* sandi. |
| `WasteClassifierViewModel`, `TFLiteInterpreterHelper` | FR-03, NFR-01, NFR-02, NFR-03 | Menangani pemrosesan gambar *offline*, batasan latensi $\le 2,0$ detik, dan akurasi model $\ge 80\%$. |
| `Result Screen UI`, logika *flag* `isRecyclable` | FR-04, NFR-04 | Menyajikan informasi status daur ulang maksimal dalam 3 kali ketukan layar. |