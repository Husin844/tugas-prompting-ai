flowchart TD
    Start([Akses Website Laravel]) --> ChooseRole{Pilih Menu / Aktor}

    %% --- AKTOR 1: ADMIN ---
    ChooseRole -- Admin --> AdminLogin[Input Username & Password] --> ValAdmin{Valid?}
    ValAdmin -- Tidak --> ErrAdmin[Tampilkan Pesan Error Login] --> AdminLogin
    ValAdmin -- Ya --> AdminDashboard([Dashboard Admin])
    AdminDashboard --> ManageData[Kelola Data Master / Kategori Sampah & Tong]
    AdminDashboard --> ViewLogs[Pantau Riwayat / Log Pemindaian Sistem]
    ManageData --> AdminEnd([Selesai / Logout])
    ViewLogs --> AdminEnd

    %% --- AKTOR 2: USER (MASYARAKAT) ---
    ChooseRole -- User --> HomeUser([Halaman Utama / Pemindai Real-Time])
    HomeUser --> ActiveCam[Aktifkan Kamera Peramban / Web Browser]
    ActiveCam --> CaptureFrame[Tangkap Citra / Frame Video Sampah]
    
    CaptureFrame --> Preprocess[Preprocessing Citra & Normalisasi]
    Preprocess --> TFLiteInference[Eksekusi Model TensorFlow Lite .tflite]
    
    TFLiteInference --> CheckConf{Confidence Score >= Threshold?}
    CheckConf -- Rendah (<50%) --> LowConf[Minta Pengguna Merapikan Posisi / Pencahayaan Kamera] --> ActiveCam
    
    CheckConf -- Tinggi (>=50%) --> DisplayResult[Tampilkan Hasil Deteksi:]
    
    %% --- DETAIL LUARAN / OUTPUT & PANDUAN TONG SAMPAH ---
    DisplayResult --> ShowDetail[ - Nama Kelas Spesifik & % Akurasi\n - Kategori Utama: Organik / Anorganik\n - Sub-Kategori Limbah]
    
    ShowDetail --> GuideBin{Pencocokan Panduan Warna Tong Sampah}
    
    GuideBin --> BinGreen[Organik ➔ Tong Sampah Warna Hijau]
    GuideBin --> BinYellow[Anorganik / Daur Ulang ➔ Tong Sampah Warna Kuning]
    GuideBin --> BinRed[Limbah B3 ➔ Tong Sampah Warna Merah]
    
    BinGreen --> SaveHistory[Simpan Log / Riwayat ke Database MySQL]
    BinYellow --> SaveHistory
    BinRed --> SaveHistory
    
    SaveHistory --> UserEnd([Selesai])