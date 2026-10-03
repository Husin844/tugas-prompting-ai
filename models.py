## 2. Skema Pydantic v2 (Python)

Berikut adalah implementasi skema validasi menggunakan **Pydantic v2** yang sepenuhnya sinkron dengan komponen skema OpenAPI:

```python
from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Optional
from datetime import datetime

# --- Skema Autentikasi & Pengguna ---

class UserRegisterRequest(BaseModel):
    name: str = Field(..., min_length=2, max_length=100, description="Nama lengkap pengguna")
    email: EmailStr = Field(..., description="Alamat email aktif (Unique)")
    password: str = Field(..., min_length=8, description="Kata sandi minimal 8 karakter")

class UserLoginRequest(BaseModel):
    email: EmailStr = Field(..., description="Alamat email terdaftar")
    password: str = Field(..., description="Kata sandi akun")

class UserResponse(BaseModel):
    uid: str = Field(..., description="ID unik pengguna (PK)")
    name: str
    email: EmailStr
    created_at: datetime = Field(..., description="Waktu pembuatan akun")

    class Config:
        from_attributes = True

class AuthTokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserResponse


# --- Skema Riwayat Pemindaian AI (Scan History) ---

class ScanHistoryRequest(BaseModel):
    user_id: str = Field(..., description="ID pengguna pemilik riwayat (FK)")
    category_name: str = Field(..., description="Hasil label kategori sampah dari TFLite")
    is_recyclable: bool = Field(..., description="Status kelayakan daur ulang (True/False)")
    confidence_score: float = Field(..., ge=0.0, le=1.0, description="Tingkat keyakinan model AI antara 0.0 sampai 1.0")

    @field_validator('confidence_score')
    @classmethod
    def validate_confidence(cls, v: float) -> float:
        if not (0.0 <= v <= 1.0):
            raise ValueError('Confidence score harus berada di antara rentang 0.0 dan 1.0')
        return v

class ScanHistoryResponse(BaseModel):
    history_id: str = Field(..., description="ID unik riwayat (PK)")
    user_id: str
    category_name: str
    is_recyclable: bool
    confidence_score: float
    timestamp: int = Field(..., description="Epoch timestamp milidetik")

    class Config:
        from_attributes = True


# --- Skema Katalog Edukasi Sampah ---

class CatalogItemResponse(BaseModel):
    catalog_id: str = Field(..., description="ID unik katalog edukasi (PK)")
    title: str
    description: str
    category_type: str

    class Config:
        from_attributes = True


# --- Skema Penanganan Error Global ---

class ErrorResponse(BaseModel):
    error_code: str
    message: str
    status: int

```

---

