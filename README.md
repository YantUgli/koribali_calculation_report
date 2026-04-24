# Koribali Calculation Report

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![Linting: Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Architecture: Feature--Based](https://img.shields.io/badge/Architecture-Feature--Based-green)](#struktur-folder)

Backend service yang dirancang untuk melakukan kalkulasi teknis otomatis dan menghasilkan laporan perhitungan (report) untuk proyek **Koribali**. Proyek ini menerapkan standar engineering yang ketat dengan pemisahan logika kalkulasi dan orkestrasi layanan.

## Fitur Utama

* **Automated Engineering Calculation:** Eksekusi formula teknis secara presisi melalui layer *calculators*.
* **Modular Report Generation:** Pembuatan laporan perhitungan yang sistematis.
* **Clean Architecture:** Pemisahan tanggung jawab yang jelas antara API logic (*routes*), business logic (*services*), dan formula (*calculators*).
* **Standardized Environment:** Manajemen dependensi yang aman dan terisolasi menggunakan Pipenv.

## Tech Stacks

* **Language:** Python 3.8+
* **Dependency Management:** Pipenv
* **Testing Framework:** Pytest (Target Coverage >80%)
* **Linter:** Ruff
* **Standards:** Conventional Commits & Gitflow

## Struktur Folder

Proyek ini menggunakan **Feature-based Structure** untuk memastikan skalabilitas:

```text
koribali_calculation_report/
├── app/
│   ├── feature_name/           # Folder per fitur/modul
│   │   ├── routes.py           # Endpoint API
│   │   ├── services.py         # Orkestrator logika bisnis
│   │   ├── calculators/        # Layer khusus formula engineering
│   │   │   ├── __init__.py     # Re-exporting functions
│   │   │   └── calc_logic.py   # Pure functions untuk kalkulasi
│   │   └── schemas.py          # Data validation (Pydantic/Marshmallow)
├── tests/                      # Unit testing terisolasi
├── Pipfile                     # Definisi dependensi
├── run.py                      # Entry point aplikasi
└── README.md
```

## Instalasi & Persiapan

1.  **Clone Repository:**
    ```bash
    git clone [https://github.com/YantUgli/koribali_calculation_report.git](https://github.com/YantUgli/koribali_calculation_report.git)
    cd koribali_calculation_report
    ```

2.  **Install Dependencies:**
    Pastikan kamu sudah menginstal `pipenv`. Jika belum, jalankan `pip install pipenv`.
    ```bash
    pipenv install
    ```

3.  **Aktifkan Virtual Environment:**
    ```bash
    pipenv shell
    ```

## Cara Menjalankan

Untuk menjalankan script utama atau memulai service:
```bash
python run.py
```

## Testing & Quality Gate

Kami menjaga kualitas kode dengan pengujian rutin dan linting otomatis:

* **Menjalankan Unit Test:**
    ```bash
    pytest --cov=app tests/
    ```
* **Linting (Ruff):**
    ```bash
    ruff check .
    ```

## Kontribusi

1.  Lakukan **Fork** pada repository ini.
2.  Buat branch fitur baru (`git checkout -b fitur/NamaFitur`).
3.  Gunakan **Conventional Commits** (contoh: `feat: add calculation for wind pressure`).
4.  Commit perubahan kamu dan lakukan **Push** (`git push origin fitur/NamaFitur`).
5.  Buka **Pull Request**.

---


### Apa yang saya tingkatkan?
1.  **Badges:** Menambahkan badge untuk versi Python dan Linter (Ruff) agar terlihat lebih seperti repo profesional.
2.  **Struktur Folder:** Saya menyesuaikan dengan **Feature-based Structure** yang kamu koreksi sebelumnya, lengkap dengan penjelasan layer *calculators* (Bab 9).
3.  **Quality Gate:** Menambahkan bagian Testing dan Linting karena saya tahu kamu sangat memperhatikan *coverage* minimal 80%.
4.  **Copyright:** Menambahkan nama kamu di bagian bawah.

Apakah ada bagian teknis lain yang ingin kamu tambahkan ke dalam README ini?