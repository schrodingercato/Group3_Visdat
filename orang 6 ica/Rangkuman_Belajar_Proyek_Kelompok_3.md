# 📘 RANGKUMAN CEPAT BELAJAR PROYEK KELOMPOK 3
## "Biar Paham Luar-Dalam Proyek Kita Ngapain, Siapa Ngerjain Apa, dan Kenapa!"

**Mata Kuliah**: Visualisasi Data Medis (ETS)  
**Kelompok**: Kelompok 3 (Teknologi Kedokteran FKK ITS)  
**Target Penelitian**: Enzim *Human Intestinal α-Glucosidase* (Kode PDB: `3L4W`)  
**Tujuan Proyek**: Mencari kandidat obat herbal alami (Flavonoid/Polifenol) untuk terapi **Diabetes Melitus Tipe 2** melalui simulasi komputer (*Molecular Docking*).

---

## 💡 1. Konsep Dasar & Logika Medis Proyek Ini (The Big Picture)

### Masalah Klinis:
Orang diabetes punya kadar gula darah yang melonjak drastis setelah makan (*postprandial hyperglycemia*). Kenapa bisa melonjak? Karena di dinding usus halus ada enzim bernama **α-Glukosidase**. Enzim ini tugasnya memotong karbohidrat kompleks (nasi, tepung, gula) menjadi glukosa murni yang diserap ke darah.

### Solusi Klinis:
Kalau enzim **α-Glukosidase ini kita sumbat (kita inhibisi)** dengan suatu molekul obat, enzimnya tidak bisa memotong gula. Akibatnya, penyerapan glukosa melambat dan gula darah tidak melonjak!
* Obat sintetis standar yang sudah ada di pasaran namanya **Miglitol** dan **Akarbosa**. Tapi obat ini sering bikin perut kembung parah, flatulensi (buang gas terus), dan diare.
* **Misi Kelompok Kita**: Menguji apakah 3 senyawa bahan alam (**Quercetin**, **Luteolin**, dan **Mangiferin**) bisa menempel lebih kuat, lebih stabil, dan lebih aman di enzim tersebut dibanding obat kontrol Miglitol!

---

## 🏃‍♀️ 2. Alur Estafet Kerja: Siapa Ngerjain Apa (Orang 1 – 6)

Pengerjaan proyek ini adalah rantai estafet ilmiah. Setiap orang melanjutkan output dari orang sebelumnya:

```
[Orang 1: Konsep & Jurnal] ➔ [Orang 2: Bersihin Protein] ➔ [Orang 3: Siapin Ligan & ADMET]
                                                                        │
                                                                        ▼
[Orang 6: Visualisasi & Kesimpulan] ◄── [Orang 5: Docking Kandidat] ◄── [Orang 4: Validasi Redocking]
```

---

### 👤 ORANG 1: Ziyadatur Rif'ah (Ziya) — Perumusan Target & Literatur
* **Tugas**: Mencari jurnal acuan ilmiah dan menentukan fondasi riset.
* **Apa yang dikerjakan**:
  1. Menentukan target reseptor penyakit: Enzim pencernaan karbohidrat usus manusia, yaitu **Human Intestinal α-Glucosidase** dengan kode kristal PDB: **`3L4W`**.
  2. Memilih 3 senyawa bahan alam yang punya bukti empiris antidiabetes: **Quercetin** (apel/bawang), **Luteolin** (seledri/teh chamomile), dan **Mangiferin** (daun mangga).
  3. Menulis latar belakang ilmiah pada laporan (Bab 1 – Bab 3).

---

### 👤 ORANG 2: Ni Wayan Melva Vemitra (Melva) — Protein Cleaning (Preparasi Reseptor)
* **Tugas**: Menyiapkan struktur 3D protein agar bersih dan siap dimasuki ligan.
* **Apa yang dikerjakan**:
  1. Mengunduh file 3D enzim `3L4W.pdb` dari situs resmi RSCB Protein Data Bank.
  2. Membuka protein di software **BIOVIA Discovery Studio Visualizer**.
  3. Membuang molekul air ($H_2O$), ion pengotor, gliserol, dan mencabut ligan native aslinya (Miglitol) yang menempel saat kristalografi.
  4. Menyimpan file reseptor murni: `Reseptor 3L4W Bersih_fixed.pdb` (agar kantung aktif enzim plong tanpa halangan).

---

### 👤 ORANG 3: Desta Kezia Priyono (Kezia) — Preparasi Ligan & Skrining ADMET
* **Tugas**: Menyiapkan struktur kimia 3 ligan kandidat dan menguji kelayakannya sebagai obat oral.
* **Apa yang dikerjakan**:
  1. Mengunduh struktur kimia 3D Quercetin, Luteolin, dan Mangiferin dari database **NCBI PubChem**.
  2. Melakukan *Energy Minimization* menggunakan forcefield UFF di software PyRx/OpenBabel (supaya bentuk molekulnya rileks dan stabil secara fisika), lalu mengubahnya ke format `.pdbqt`.
  3. Memasukkan senyawa ke web **ADMETlab 2.0** untuk skrining farmakokinetik:
     * **Lipinski Rule of 5**: Luteolin & Quercetin lolos 100% tanpa pelanggaran (berat molekul < 500, LogP < 5).
     * Mangiferin melanggar 2 aturan karena molekulnya terlalu besar dan donor hidrogennya terlalu banyak (8 HBD).

---

### 👤 ORANG 4: Najma Khoirun Nisa (Najma) — Validasi Metode (Redocking Kontrol)
* **Tugas**: Membuktikan bahwa software dan parameter komputer kelompok kita akurat dan valid.
* **Apa yang dikerjakan**:
  1. Mengatur kotak pencarian (**Grid Box**) di kantung aktif enzim pada koordinat spesifik tempat obat menempel.
  2. Menambatkan ulang (*redocking*) ligan asli **Miglitol** ke protein bersih menggunakan software **AutoDock Vina (PyRx)**.
  3. Menghitung nilai **RMSD** (*Root Mean Square Deviation*) di PyMOL untuk membandingkan pose docking komputer vs pose kristalografi nyata.
  4. **Hasilnya**: Nilai **RMSD = 1.05 Å**. Karena nilai RMSD $\le 2.0$ Å, maka metode docking kelompok kita dinyatakan **100% VALID dan terpercaya secara ilmiah!**

---

### 👤 ORANG 5: Fidellynne Khaleesha Abidi (Fidel) — Molecular Docking Senyawa Kandidat
* **Tugas**: Menjalankan simulasi penambatan 3 kandidat bahan alam.
* **Apa yang dikerjakan**:
  1. Melakukan docking untuk Quercetin, Luteolin, dan Mangiferin menggunakan koordinat *Grid Box* yang sama persis dengan yang dibuat Najma.
  2. Mengekstraksi nilai energi bebas pengikatan (*Binding Affinity* $\Delta G$ dalam satuan **kcal/mol**):
     * Semakin minus nilainya = semakin kuat dan stabil ikatannya!
     * Luteolin: **-7.9 kcal/mol**
     * Quercetin: **-7.1 kcal/mol**
     * Mangiferin: **-7.0 kcal/mol**
     * Miglitol (Kontrol): **-5.5 kcal/mol**
  3. Menyimpan file pose 3D terbaik (Pose 0) untuk diserahkan ke Ica.

---

### 👤 ORANG 6: Aisyah Rahmi Nadjib (Ica — Kamu!) — Visualisasi, Analisis, & Kesimpulan
* **Tugas**: Menerjemahkan angka-angka docking menjadi gambar beresolusi tinggi, menjelaskan biokimianya, dan menentukan kesimpulan akhir.
* **Apa yang dikerjakan**:
  1. **Visualisasi Komposit 3D & 2D**: Membuka pose terbaik di Discovery Studio & PyMOL. Membuat diagram 2D interaksi resolusi tinggi (>5000 px) berdampingan dengan 3D pita protein.
  2. **Identifikasi Interaksi Residu**: Menemukan residu asam amino pembentuk ikatan hidrogen, kontak aromatik $\pi$-$\pi$ *stacking*, dan gaya *van der Waals*.
  3. **Pembahasan Kritis (Bab 8.5)**: Menjawab 8 pertanyaan wajib dosen, termasuk menjelaskan kenapa Luteolin mengunci **Triad Katalitik (Asp542, Asp327, Asp203)** dan kenapa Miglitol punya *unfavorable bump* dengan Arg526.
  4. **Kesimpulan & Batasan Ilmiah (Bab 8.6)**: Menetapkan Luteolin sebagai *lead compound* terbaik (92.9% kemiripan situs aktif) dengan batasan ilmiah (*disclaimer*) bahwa docking adalah prediksi statis yang wajib diuji basah di lab (*in vitro*).
  5. **Materi Presentasi**: Menyusun Slide 8, 9, dan 10 pada tayangan PPT.

---

## 📊 3. Matriks Hasil Akhir (Hafalan Wajib)

| Senyawa | Energi Bebas ($\Delta G$) | Jumlah Ikatan H | Residu Katalitik yang Terkunci | % Kemiripan Situs | Lipinski Rule | Status |
| :--- | :---: | :---: | :--- | :---: | :---: | :--- |
| **Miglitol** *(Kontrol)* | **-5.5 kcal/mol** | 7 | Asp327, Asp542, Asp203 | 100% | 0 Violations | Pembanding Standar (Ada *unfavorable bump* Arg526) |
| **Quercetin** *(Kandidat 1)* | **-7.1 kcal/mol** | 4 | Asp327, Asp542 | 85.7% | 0 Violations | Cukup Kuat ($\pi$-$\pi$ Tyr299, Phe575) |
| **Luteolin** *(Kandidat 2)* | **-7.9 kcal/mol** | **6** | **Asp327, Asp542, Asp203 (Lengkap!)** | **92.9% (Tertinggi)** | **0 Violations** | 🏆 **KANDIDAT TERBAIK (LEAD COMPOUND)** |
| **Mangiferin** *(Kandidat 3)* | **-7.0 kcal/mol** | 6 | Asp327, Asp542, Asp203 | 85.7% | 2 Violations | Terhambat sterik molekul besar |

---

## 🎯 4. Cheat Sheet Menjawab Pertanyaan Dosen Saat Sidang/Tanya-Jawab

Kalau dosen bertanya acak ke kamu atau anggota lain, gunakan panduan jawaban ini:

1. **"Kenapa pakai PDB 3L4W?"**  
   *👉 "Karena 3L4W adalah struktur kristal resolusi tinggi (2.15 Å) dari enzim Human Intestinal Maltase-Glucoamylase (α-glucosidase) yang merupakan target terapi diabetes tipe 2 pada manusia."*

2. **"Kenapa metode docking kalian bisa dibilang valid?"**  
   *👉 "Karena pada tahap validasi redocking oleh Orang 4 (Najma), nilai RMSD ligan native Miglitol diperoleh sebesar 1.05 Å, jauh di bawah batas standar internasional yaitu ≤ 2.0 Å."*

3. **"Kenapa kontrol Miglitol skor energinya lebih jelek (-5.5) dibanding bahan alam?"**  
   *👉 "Karena Miglitol terdeteksi memiliki tolakan elektrostatik kationik ('unfavorable donor-donor bump') dengan Arg526 (3.09 Å). Selain itu, flavonoid alami memiliki cincin planar yang mendapat kestabilan ekstra dari interaksi π-π stacking dan efek entropi desolvasi."*

4. **"Kenapa Luteolin menang dibanding Quercetin?"**  
   *👉 "Luteolin tidak memiliki gugus 3-OH pada cincin C. Ketiadaan 3-OH ini menghindarkannya dari hambatan sterik di celah sempit kantung aktif dan membuat Luteolin lebih tahan terhadap reaksi metabolisme tubuh (glukuronidasi cepat)."*

5. **"Apa kesimpulan akhir dari penelitian kalian?"**  
   *👉 "Luteolin terpilih secara meyakinkan sebagai lead compound terbaik dengan afinitas -7.9 kcal/mol, kemiripan situs aktif 92.9%, mengunci seluruh triad katalitik, dan lolos aturan Lipinski. Namun temuan ini adalah prediksi in silico awal yang wajib divalidasi uji in vitro dan in vivo lanjutan."*
