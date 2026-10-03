Berikut adalah rancangan lengkap **ERD (Mermaid)** dan **Skema Pydantic v2 (Python)** untuk aplikasi **Wastify**, disusun sinkron dengan spesifikasi OpenAPI dan LLD yang telah kita buat:

---

## 1. ERD (Entity-Relationship Diagram) - Format Mermaid

```mermaid
erDiagram
    USER ||--o{ SCAN_HISTORY : "memiliki riwayat"
    
    USER {
        string uid PK "UUID / String (Unique)"
        string name "NOT NULL"
        string email "NOT NULL, UNIQUE"
        string password_hash "NOT NULL"
        datetime created_at "NOT NULL"
    }

    SCAN_HISTORY {
        string history_id PK "UUID / String (Unique)"
        string user_id FK "NOT NULL (References USER.uid)"
        string category_name "NOT NULL"
        boolean is_recyclable "NOT NULL"
        float confidence_score "NOT NULL (Range 0.0 - 1.0)"
        bigint timestamp "NOT NULL"
    }

    CATALOG {
        string catalog_id PK "UUID / String (Unique)"
        string title "NOT NULL"
        string description "NOT NULL"
        string category_type "NOT NULL"
    }

```

*[ASUMSI-02]: Entitas `CATALOG` berdiri sendiri sebagai referensi edukasi statis yang dapat diakses oleh semua pengguna tanpa relasi langsung *foreign key* ke tabel riwayat di database.*

---
