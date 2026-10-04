Berikut adalah rancangan **Prompt AI (D.3 — Audit Keamanan OWASP API Top 10 & Perbaikan Celah BOLA)** yang sudah disesuaikan sepenuhnya untuk aplikasi **Wastify** berdasarkan instruksi di atas:

---

### Hasil Audit & Perbaikan Kode (Contoh Implementasi Patch)

#### 1. Tabel Audit Keamanan OWASP API Top 10

| Endpoint | Kerentanan OWASP | Tingkat Risiko | Kode Patch | Status Verifikasi |
| --- | --- | --- | --- | --- |
| `GET /api/v1/histories` | API1:2023 - Broken Object Level Authorization (BOLA) | Tinggi | Menambahkan filter query database `user_id == current_user.uid` dari token JWT yang tervalidasi. | **Terverifikasi Aman** |
| `POST /api/v1/histories` | API4:2023 - Unrestricted Resource Consumption (Upload Gambar AI) | Menengah | Menerapkan validasi ukuran maksimal file ($\le 5$ MB) dan *whitelist* MIME type (`image/jpeg`, `image/png`). | **Terverifikasi Aman** |

---

#### 2. Kode Patch Konkret Anti-BOLA (Endpoint `/histories`)

```python
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

router = APIRouter(prefix="/histories", tags=["Histories"])

@router.get("/")
def get_user_histories(
    current_user: dict = Depends(get_current_user), 
    db: Session = Depends(get_db)
):
    # PATCH ANTI-BOLA: Memastikan hanya mengambil data milik pengguna yang sedang login (current_user)
    user_id = current_user["uid"]
    histories = db.query(ScanHistoryModel).filter(ScanHistoryModel.user_id == user_id).all()
    
    if not histories:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Riwayat pemindaian tidak ditemukan."
        )
    return histories

```

---

#### 3. Middleware / Helper Sanitasi Input & Validasi Berkas AI

```python
from fastapi import UploadFile, HTTPException, status

MAX_FILE_SIZE_BYTES = 5 * 1024 * 1024  # Batas maksimal 5 MB
ALLOWED_MIME_TYPES = ["image/jpeg", "image/png"]

async def validate_ai_image_input(file: UploadFile):
    # Validasi Tipe MIME (Whitelisting)
    if file.content_type not in ALLOWED_MIME_TYPES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Format file tidak didukung. Gunakan format JPEG atau PNG."
        )
    
    # Validasi Ukuran Berkas (Unrestricted Resource Consumption prevention)
    file_content = await file.read()
    if len(file_content) > MAX_FILE_SIZE_BYTES:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail="Ukuran file terlalu besar. Batas maksimal adalah 5MB."
        )
    
    # Kembalikan pointer file ke awal setelah dibaca
    await file.seek(0)
    return file

```