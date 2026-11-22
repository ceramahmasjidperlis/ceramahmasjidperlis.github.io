# Panduan Admin & Editor — Masjid Events Perlis

Panduan terperinci dalam Bahasa Melayu untuk mengurus **masjid, penceramah, kategori, dan acara (ceramah, kuliyyah, tazkirah, program)** serta menerbitkannya ke laman web rasmi [https://ceramahmasjidperlis.github.io/](https://ceramahmasjidperlis.github.io/).

> **Nota penting:** Panel admin (`admin/`) hanya berjalan secara **lokal di komputer anda** (`127.0.0.1`). Ia tidak dideploy ke laman web awam. Sebarang perubahan hanya akan muncul di laman web sebenar selepas anda melakukan `git push` ke GitHub.

---

## 1. Memulakan Panel Admin

Buka terminal di dalam folder projek (`masjidperlis/`) dan jalankan:

```bash
python3 tools/serve.py
```

Kemudian buka pelayar web (browser) dan pergi ke:

```text
http://localhost:8000/admin/
```

- Setiap perubahan disemak secara automatik sebelum disimpan; jika data tidak sah, perubahan akan dibatalkan (rollback).
- Pilihan tambahan jika perlu: `python3 tools/serve.py --port 8080`.

---

## 2. Susunan Data Sebelum Menambah Acara

Sebelum menambah acara atau ceramah baharu, pastikan data rujukan sudah wujud mengikut susunan ini:

1. **Mukim** — senarai mukim di Perlis (data contoh sudah menyediakan 15 mukim).
2. **Masjid** — maklumat masjid (merujuk kepada mukim).
3. **Penceramah** — profil ustaz / penceramah.
4. **Kategori** — jenis program (contoh sedia ada: `Kuliyyah`, `Ceramah`, `Tafsir`, `Hadith`, `Fiqh`, `Akidah`, `Sirah`, `Tazkirah`, `Khutbah`, `Program`, `Seminar`, `Youth`, `Children`, `Women`, `Ramadan`, `Community`, `Other`).
5. **Acara** — jadual ceramah / kuliyyah yang merujuk kepada **Masjid**, **Penceramah**, dan **Kategori**.

---

## 3. Cara Tambah Masjid, Penceramah & Kategori

### 3.1 Tambah Masjid (`Masjid`)
1. Di menu atas panel admin, klik **Masjid**.
2. Isi butiran masjid:
   - **Nama** (contoh: `Masjid Alwi`)
   - **Mukim** (pilih daripada senarai)
   - **Alamat**, **Latitud / Longitud** (pilihan, untuk pautan peta)
   - **Kenalan / Laman web** (pilihan)
3. Simpan perubahan.

### 3.2 Tambah Penceramah (`Penceramah`)
1. Klik **Penceramah** di menu atas.
2. Masukkan nama ustaz/penceramah (contoh: `Ustaz Ahmad Firdaus`) dan penerangan ringkas (pilihan).
3. Simpan.

### 3.3 Tambah Kategori (`Kategori`)
1. Klik **Kategori** di menu atas.
2. Jika kategori yang dikehendaki belum ada (selain senarai asas seperti `Kuliyyah`, `Ceramah`, `Tazkirah`, dll.), tambah kategori baharu dan simpan.

---

## 4. Cara Tambah Acara / Ceramah / Kuliyyah

1. Di panel admin, klik **Acara** → tekan butang **"+ Cipta acara"** (atau buka terus `admin/event-editor.html`).
2. Isi maklumat acara:
   - **Tajuk** *(wajib)* — contoh: `Kuliyyah Maghrib: Tafsir Surah Al-Kahfi`
   - **Masjid** *(wajib)* — pilih masjid daripada senarai
   - **Tarikh** *(wajib)* — format `YYYY-MM-DD` (contoh: `2026-11-25`)
   - **Mula** *(wajib)* — format 24 jam `HH:MM` (contoh: `20:00`)
   - **Tamat** *(pilihan)* — format `HH:MM` (contoh: `21:00`)
   - **Penceramah** — pilih ustaz / penceramah
   - **Kategori** — pilih kategori (contoh: `Ceramah`, `Kuliyyah`, `Tazkirah`)
   - **Lokasi** *(pilihan)* — contoh: `Dewan Solat Utama`
   - **Keterangan** *(pilihan)* — catatan tambahan atau topik ceramah
   - **Status** — pilih `published` supaya dipaparkan di laman awam (atau `draft` jika belum sedia)
3. Klik **Simpan**.

> **Borang Pantas:** Jika anda ingin menambah sebuah masjid baharu berserta jadual kuliah berulangnya sekali gus dalam satu borang, anda juga boleh menggunakan halaman `admin/add-masjid.html`.

---

## 5. Cara Tetapkan Kuliah / Ceramah Berulang Mingguan

Untuk kuliah mingguan yang tetap (contoh: setiap Isnin dan Jumaat):

1. Dalam editor acara (**Acara → + Cipta acara** atau sunting acara sedia ada), aktifkan bahagian **Berulang mingguan**.
2. Pilih hari dalam minggu (contoh: `monday`, `friday`).
3. Tetapkan tarikh **Mula ulangan** dan **Tamat ulangan** (pilihan).
4. **Pengecualian (`pengecualian`):**
   - Jika satu tarikh tertentu dibatalkan (contoh: cuti umum atau masjid ada majlis khas), masukkan tarikh tersebut dalam format `YYYY-MM-DD` pada ruangan **Pengecualian**.
   - Tarikh itu akan digugurkan daripada kalendar awam, halaman statik, dan fail `.ics` tanpa memadam keseluruhan siri kuliah.

---

## 6. Mengubah Status Acara (Batal, Tangguh, Arkib)

Di halaman **Acara**, anda boleh menukar status mana-mana acara menggunakan butang tindakan:

| Status      | Kesan di Laman Awam                                      |
| ----------- | -------------------------------------------------------- |
| `draft`     | Draf — **tidak dipaparkan** di laman awam                |
| `published` | Diterbitkan — **dipaparkan** di laman awam               |
| `cancelled` | Dipaparkan dengan notis **dibatalkan**                   |
| `postponed` | Dipaparkan dengan notis **ditangguhkan**                 |
| `completed` | Diarkibkan — **disembunyikan** daripada senarai aktif    |

> **Nota pemadaman:** Masjid, penceramah, atau kategori yang masih dirujuk oleh mana-mana acara tidak boleh dipadam. Tukar atau padam acara yang merujuknya terlebih dahulu.

---

## 7. Cara Alternatif: Kemas Kini Pukal Guna Excel / CSV (`data-entry/`)

Jika anda mahu menambah banyak ceramah sekaligus tanpa mengisi borang satu per satu:

1. Buka folder `data-entry/` dan sunting fail CSV (atau simpan sebagai `.xlsx` dan kemas kini nama fail dalam `data-entry/config.json`):
   - `1-kategori.csv`
   - `2-penceramah.csv`
   - `3-masjids.csv`
   - `4-acara.csv`
2. Isi data baharu di bawah baris tajuk (tinggalkan lajur `id` kosong untuk rekod baharu; ia dijana automatik).
3. Jalankan skrip pengimport dari terminal:

```bash
./data-entry/update.sh
```

Pengimport ini menambah/mengemas kini mengikut `id` (tidak memadam data sedia ada) dan menyemak keseluruhan data sebelum menulis ke `data/*.json`.

Untuk import daripada **Google Sheets** (tanpa API key), rujuk `DATA_ENTRY_GUIDE.md` dan `SHEET_IMPORT.md`.

---

## 8. Semak Data, Pratonton Tempatan & Terbitkan ke Laman Web

### Langkah 1: Semak & Pratonton di Komputer Anda
Di halaman **Ringkasan** (`http://localhost:8000/admin/`):

1. Klik **Semak data** — menjalankan pengesah (`tools/validate_data.py`) ke atas folder `data/` tanpa mengubah fail.
2. Klik **Terbitkan (salin ke public/data)** — menyalin data sah ke `public/data/` untuk pratonton tempatan.

Untuk melihat laman awam penuh (termasuk halaman setiap masjid dan acara) di komputer anda:

```bash
python3 tools/build_site.py
python3 -m http.server 8000 --directory public
```

Buka `http://localhost:8000` untuk menyemak paparan.

### Langkah 2: Terbitkan ke Laman Sebenar (`ceramahmasjidperlis.github.io`)
Selepas berpuas hati dengan perubahan dalam `data/`, tolak (push) perubahan ke GitHub:

```bash
git add data/
git commit -m "kemaskini jadual ceramah"
git push ceramahmasjidperlis master
```

GitHub Actions (`.github/workflows/deploy.yml`) akan secara automatik:
1. Mengesahkan semua fail dalam `data/`.
2. Menjana halaman statik SEO, `sitemap.xml`, dan ikon PWA.
3. Memuat naik dan menerbitkan laman terkini ke [https://ceramahmasjidperlis.github.io/](https://ceramahmasjidperlis.github.io/).

---

## 9. Penyelesaian Masalah Lazim

| Masalah | Punca & Penyelesaian |
| ------- | -------------------- |
| Acara tidak muncul di laman awam | Pastikan `Status` acara ialah `published` (bukan `draft` atau `completed`), dan anda sudah menjalankan `git push` ke GitHub. |
| Ralat semasa **Semak data** / **Terbitkan** | Semak format tarikh (`YYYY-MM-DD`), masa (`HH:MM`), dan pastikan `id` hanya menggunakan huruf kecil, nombor, dan tanda sengkang (`-`). |
| Perubahan di panel admin belum keluar di `ceramahmasjidperlis.github.io` | Butang **Terbitkan** hanya menyalin ke `public/data/` di komputer anda. Jalankan `git add data/ && git commit -m "..." && git push ceramahmasjidperlis master` untuk menerbitkan ke laman web sebenar. |
| Laman web masih tunjuk data lama selepas deploy | Muat semula (refresh) pelayar web; service worker menggunakan strategi *network-first* untuk data supaya pembatalan dan acara baharu sentiasa dikemas kini. |
