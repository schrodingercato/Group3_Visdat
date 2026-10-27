# BAB 7: TABEL UTAMA HASIL SIMULASI KOMPUTASI & MOLECULAR DOCKING
**Mata Kuliah:** Visualisasi Data Medis  
**Target Makromolekul:** Enzim Human Intestinal $\alpha$-Glukosidase / NtMGAM (PDB ID: `3L4W`)  
**Penanggung Jawab Analisis Data:** Orang 6 (Aisyah Rahmi Nadjib / Ica - 5049241030)

---

## 7.1 Tabel Matriks Komparatif Interaksi Molekuler

| Parameter Evaluasi | Miglitol (Ligan Kontrol) | Quercetin (Kandidat 1) | Luteolin (Kandidat 2) | Mangiferin (Kandidat 3) |
| :--- | :--- | :--- | :--- | :--- |
| **Formula & Bobot Molekul** | $\text{C}_{8}\text{H}_{17}\text{NO}_{5}$ (207.22 g/mol) | $\text{C}_{15}\text{H}_{10}\text{O}_{7}$ (302.24 g/mol) | $\text{C}_{15}\text{H}_{10}\text{O}_{6}$ (286.24 g/mol) | $\text{C}_{19}\text{H}_{18}\text{O}_{11}$ (422.34 g/mol) |
| **PubChem CID** | 441314 | 5280343 | 5280445 | 5281647 |
| **Binding Affinity (AutoDock Vina)** | **-5.5 kkal/mol** | **-7.1 kkal/mol** | **-7.9 kkal/mol** *(Skor Tertinggi)* | **-7.0 kkal/mol** |
| **Selisih Kestabilan ($\Delta\Delta G$ vs Native)** | Baseline (0.0 kkal/mol) | **-1.6 kkal/mol** | **-2.4 kkal/mol** | **-1.5 kkal/mol** |
| **Ikatan Hidrogen Konvensional (< 3.5 Å)** | • **ASP327** (2.70 Å)<br>• **ASP542** (2.70 Å)<br>• **HIS600** (2.99 Å)<br>• **ASP203** (3.01 Å)<br>• **TRP406** (3.05 Å)<br>• **ARG526** (3.09 Å)<br>• **ASP443** (3.20 Å) | • **ASP327** (2.76 Å)<br>• **TYR605** (2.82 Å)<br>• **ASP542** (3.13 Å)<br>• **ASP443** (3.21 Å) | • **ASP327** (2.66 Å)<br>• **TRP406** (3.13 Å)<br>• **ASP542** (3.14 Å)<br>• **ASP203** (3.17 Å)<br>• **TYR299** (3.17 Å)<br>• **HIS600** (3.19 Å) | • **ARG526** (2.80 Å)<br>• **ASP203** (2.86 Å)<br>• **ASP327** (2.96 Å)<br>• **HIS600** (2.99 Å)<br>• **ASP443** (3.23 Å)<br>• **ASP542** (3.48 Å) |
| **Interaksi Hidrofobik & $\pi$-Stacking (< 4.5 Å)** | • TRP406 (3.66 Å)<br>• PHE575 (3.95 Å)<br>• TYR299 (4.12 Å)<br>• ILE328 (4.17 Å)<br>• MET444 (4.22 Å)<br>• TRP539 (4.28 Å) | • TYR299 (3.44 Å)<br>• PHE575 (3.49 Å)<br>• TRP406 (3.53 Å)<br>• ILE328 (3.90 Å)<br>• ILE364 (4.41 Å) | • TRP406 (3.26 Å)<br>• PHE450 (3.67 Å)<br>• TYR299 (3.67 Å)<br>• PHE575 (3.71 Å)<br>• MET444 (4.21 Å)<br>• TRP441 (4.24 Å) | • TYR299 (3.32 Å)<br>• PHE575 (3.45 Å)<br>• TRP406 (3.48 Å)<br>• PHE450 (3.79 Å)<br>• TRP539 (4.46 Å) |
| **Kontak Van der Waals Tambahan (< 4.0 Å)** | ILE328, ILE364, MET444, TRP441 | ASP203, ARG526, HIS600, TRP441 | ASP443, ARG526, ILE328, ILE364, TRP539 | TRP441, MET444 |
| **Total Residu Kontak di Kantung Katalitik** | 14 Residu | 13 Residu | 14 Residu | 13 Residu |
| **Tingkat Kesamaan Residu dgn Kontrol (%)** | **100.0%** *(14/14 residu acuan)* | **85.7%** *(12/14 residu identik)* | **92.9%** *(13/14 residu identik)* | **85.7%** *(12/14 residu identik)* |
| **Residu Katalitik Kunci yang Diikat Bersama** | Asp203, Asp327, Asp542, Arg526, His600 | Asp327, Asp443, Asp542, Trp406, Tyr299 | Asp203, Asp327, Asp542, His600, Trp406 | Asp203, Asp327, Asp542, Arg526, His600 |

---

## 7.2 Rangkuman Profil Farmakokinetik & ADMET (ADMETlab 2.0)

| Kode Senyawa | Kepatuhan Lipinski Ro5 | LogP | H-Bond Donor / Akseptor | TPSA ($\text{Å}^2$) | Absorpsi Usus (HIA) | Permeabilitas Caco-2 | Toksisitas Oral (LD50) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Miglitol (Kontrol)** | Diterima (0 pelanggaran) | -2.40 | 5 / 5 | 92.0 | 0.98 (Tinggi) | Tinggi | Rendah / Aman |
| **Quercetin (Kandidat 1)** | **Diterima (0 pelanggaran)** | 2.15 | 5 / 7 | 131.36 | 0.93 (Baik) | Sedang | Rendah (Aman) |
| **Luteolin (Kandidat 2)** | **Diterima (0 pelanggaran)** | 2.90 | 4 / 6 | 111.13 | 0.99 (Sangat Baik) | Optimal | Rendah (Aman) |
| **Mangiferin (Kandidat 3)** | Ditolak (2 pelanggaran: HBD>5, TPSA>140) | 0.14 | 8 / 11 | 201.28 | 0.83 (Rendah) | Rendah (Aksi Lokal) | Non-toksik |
