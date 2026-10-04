Berikut adalah hasil implementasi **D.2 Implementasi Autentikasi JWT & Password Hashing** yang telah disesuaikan sepenuhnya dengan proyek aplikasi **Wastify** menggunakan stack FastAPI, Python-Jose, dan Passlib:

---

### 1. Utility Hash Password (Bcrypt)

```python
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

```

---

### 2. Generator Token Pair (Access & Refresh Token)

```python
from datetime import datetime, timedelta
from jose import jwt
import os

SECRET_KEY = os.getenv("SECRET_KEY", "super_secret_key_change_in_production")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_DAYS = 7

def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire, "type": "access"})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def create_refresh_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp": expire, "type": "refresh"})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

```

---

### 3. Dependency / Middleware Protected Route

```python
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError

security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> dict:
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token akses tidak valid atau sudah kedaluwarsa",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None or payload.get("type") != "access":
            raise credentials_exception
        return {"uid": user_id}
    except JWTError:
        raise credentials_exception

```

---

### 4. Handler Signup (Registrasi)

```python
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
import uuid

def handle_signup(name: str, email: str, password: str, db: Session, user_repo) -> dict:
    existing_user = user_repo.get_by_email(db, email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email sudah terdaftar dalam sistem."
        )
    
    hashed_pwd = hash_password(password)
    user_data = {
        "uid": f"usr_{uuid.uuid4().hex[:12]}",
        "name": name,
        "email": email,
        "password_hash": hashed_pwd
    }
    
    new_user = user_repo.create(db, user_data)
    return {
        "uid": new_user.uid,
        "name": new_user.name,
        "email": new_user.email,
        "created_at": new_user.created_at
    }

```

---

### 5. Handler Login

```python
from fastapi import HTTPException, status

def handle_login(email: str, password: str, db: Session, user_repo) -> dict:
    user = user_repo.get_by_email(db, email)
    if not user or not verify_password(password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email atau kata sandi salah."
        )
    
    access_token = create_access_token(data={"sub": user.uid})
    refresh_token = create_refresh_token(data={"sub": user.uid})
    
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
        "user": {
            "uid": user.uid,
            "name": user.name,
            "email": user.email,
            "created_at": user.created_at
        }
    }

```

---

### 6. Handler Refresh Token

```python
def handle_refresh(refresh_token: str) -> dict:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Refresh token tidak valid atau kedaluwarsa"
    )
    try:
        payload = jwt.decode(refresh_token, SECRET_KEY, algorithms=[ALGORITHM])
        if payload.get("type") != "refresh":
            raise credentials_exception
        user_id = payload.get("sub")
        
        new_access_token = create_access_token(data={"sub": user_id})
        return {
            "access_token": new_access_token,
            "token_type": "bearer"
        }
    except JWTError:
        raise credentials_exception

```

---

### 7. Protected Endpoint `GET /auth/me`

```python
from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.get("/me")
def get_my_profile(current_user: dict = Depends(get_current_user), db: Session = Depends(get_db), user_repo = None):
    # Mengambil profil pengguna aktif berdasarkan UID dari token JWT
    user = user_repo.get_by_id(db, current_user["uid"])
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Pengguna tidak ditemukan."
        )
    return {
        "uid": user.uid,
        "name": user.name,
        "email": user.email,
        "created_at": user.created_at
    }

```