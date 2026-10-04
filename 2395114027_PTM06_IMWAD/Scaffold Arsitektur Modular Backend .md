Berikut adalah hasil *scaffold* arsitektur modular backend berdasarkan spesifikasi OpenAPI Wastify yang Anda berikan:

---

### 1. Struktur Folder Modular (Tree Teks)

```text
wastify-backend/
├── core/
│   ├── __init__.py
│   ├── config.py          # Pengelolaan environment variables dari .env
│   └── database.py        # Konfigurasi koneksi SQLAlchemy & Session generator
├── models/
│   ├── __init__.py
│   └── user_model.py      # SQLAlchemy ORM Model untuk entitas User
├── repositories/
│   ├── __init__.py
│   └── user_repository.py # Lapisan khusus eksekusi query database untuk User
├── services/
│   ├── __init__.py
│   └── user_service.py    # Lapisan logika bisnis & validasi (pendaftaran & hashing)
├── routers/
│   ├── __init__.py
│   └── user_router.py     # Lapisan endpoint FastAPI (Router / Controller)
├── .env.example           # Template konfigurasi variabel lingkungan
└── main.py                # Titik masuk utama aplikasi FastAPI

```

---

### 2. Boilerplate Kode Tiap Lapisan (Contoh Resource: `/users`)

#### A. Konfigurasi Database (`core/database.py`)

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./wastify.db")

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

```

#### B. Model Database (`models/user_model.py`)

```python
from sqlalchemy import Column, String, DateTime
from datetime import datetime
from core.database import Base

class UserModel(Base):
    __tablename__ = "users"

    uid = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

```

#### C. Repository (`repositories/user_repository.py`)

```python
from sqlalchemy.orm import Session
from models.user_model import UserModel

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_email(self, email: str) -> UserModel | None:
        return self.db.query(UserModel).filter(UserModel.email == email).first()

    def create(self, user_data: dict) -> UserModel:
        db_user = UserModel(**user_data)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

```

#### D. Service (`services/user_service.py`)

```python
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from repositories.user_repository import UserRepository
import uuid
import bcrypt

class UserService:
    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def register_user(self, name: str, email: str, password: str):
        existing_user = self.repository.get_by_email(email)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email sudah terdaftar dalam sistem."
            )
        
        # Enkripsi password menggunakan bcrypt
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        
        user_data = {
            "uid": f"usr_{uuid.uuid4().hex[:12]}",
            "name": name,
            "email": email,
            "password_hash": hashed_password
        }
        
        return self.repository.create(user_data)

```

#### E. Router (`routers/user_router.py`)

```python
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from core.database import get_db
from services.user_service import UserService
from pydantic import BaseModel, EmailStr

router = APIRouter(prefix="/users", tags=["Users"])

class UserRegisterRequest(BaseModel):
    name: str
    email: EmailStr
    password: str

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(payload: UserRegisterRequest, db: Session = Depends(get_db)):
    service = UserService(db)
    new_user = service.register_user(payload.name, payload.email, payload.password)
    return {
        "uid": new_user.uid,
        "name": new_user.name,
        "email": new_user.email,
        "created_at": new_user.created_at
    }

```

---

### 3. Konfigurasi Koneksi DB & Lifecycle (`core/database.py`)

Koneksi basis data SQLite diatur melalui SQLAlchemy dengan pengelolaan sesi (*session lifecycle*) menggunakan fungsi generator `get_db()` yang menjamin sesi ditutup secara otomatis (`db.close()`) guna mencegah kebocoran koneksi (*connection leak*).

---

### 4. Template `.env.example`

```env
# Konfigurasi Database
DATABASE_URL=sqlite:///./wastify.db

# Keamanan & Autentikasi JWT
SECRET_KEY=super_secret_key_change_in_production_998877
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60

# Konfigurasi Model AI & Preprocessing
MODEL_PATH=ml/models/wastify_mobilenet.tflite
SCALER_PATH=ml/models/scaler.pkl
MAX_FILE_SIZE_MB=5

```