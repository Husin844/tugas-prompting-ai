## 3.3 Alur Penelitian

Alur penelitian ini dirancang menggunakan pendekatan rekayasa perangkat lunak **Metode Prototype** yang diintegrasikan dengan tahapan pengembangan model *Deep Learning* (*Computer Vision Workflow*). Prosedur dan urutan langkah penelitian secara sistematis divisualisasikan pada Gambar 3.1 berikut:

```mermaid
flowchart TD
    Start([MULAI]) --> Step1[1. Studi Literatur & Analisis Kebutuhan]
    Step1 --> Step2[2. Pengumpulan & Preprocessing Dataset]
    Step2 --> Step3[3. Pemodelan & Pelatihan Deep Learning]
    Step3 --> Step4[4. Perancangan & Pembangunan Sistem Prototype]
    Step4 --> Step5[5. Pengujian & Evaluasi Sistem]
    
    Step5 --> Check{Sesuai Kebutuhan?}
    
    Check -- Tidak --> Fix[Perbaikan / Penyesuaian Prototype] --> Step4
    Check -- Ya --> Step6[6. Implementasi & Penyerahan Akhir]
    
    Step6 --> End([SELESAI])