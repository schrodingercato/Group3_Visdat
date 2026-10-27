# BAB 8.5: PEMBAHASAN KRITIS HASIL SIMULASI MOLECULAR DOCKING
**Mata Kuliah:** Visualisasi Data Medis — Departemen Teknologi Kedokteran FKK ITS  
**Penyusun Analisis & Interpretasi:** Orang 6 (Aisyah Rahmi Nadjib / Ica - 5049241030)

---

### 1. Pertanyaan 1: Senyawa Kandidat dengan Afinitas Pengikatan (*Binding Affinity*) Terbaik
Berdasarkan hasil simulasi *molecular docking* menggunakan AutoDock Vina pada PyRx, senyawa **Luteolin (Kandidat 2)** menunjukkan nilai energi bebas pengikatan (*binding affinity*) paling negatif, yaitu sebesar **-7.9 kkal/mol**. Urutan afinitas pengikatan dari yang paling stabil adalah:
$$\text{Luteolin } (-7.9\ \text{kkal/mol}) > \text{Quercetin } (-7.1\ \text{kkal/mol}) > \text{Mangiferin } (-7.0\ \text{kkal/mol}) > \text{Miglitol (Ligan Kontrol: } -5.5\ \text{kkal/mol})$$
Ketiga senyawa bahan alam membuktikan afinitas termodinamika yang jauh lebih stabil (selisih $\Delta\Delta G$ antara $-1.5$ hingga $-2.4\ \text{kkal/mol}$) dibandingkan ligan ko-kristal native Miglitol. Hal ini mengindikasikan bahwa secara teoritis, pembentukan kompleks antara reseptor $\alpha$-glukosidase (3L4W) dengan senyawa polifenol bahan alam bersifat lebih spontan dan stabil.

---

### 2. Pertanyaan 2: Kesesuaian Kantung Pengikatan (*Binding Pocket*)
Berdasarkan visualisasi spasial 3D (Gambar tumpukan pose ligan pada berkas `all ligand with protein.jpeg`), seluruh pose terbaik (Mode 0) dari Quercetin, Luteolin, dan Mangiferin terbukti menempati rongga katalitik yang **konsisten dan identik** dengan posisi kristalografi ligan native Miglitol.
Hal ini dipastikan karena parameter *grid box* (Center X: 45.49, Y: 91.76, Z: 34.51 dengan dimensi $20 \times 20 \times 20\ \text{Å}$) dikunci secara ketat berdasarkan koordinat ligan native hasil preparasi Orang 4 (Najma) dengan validasi RMSD $\le 2.0\ \text{Å}$. Tidak ditemukan kandidat yang melenceng ke kantung alosterik luar, membuktikan bahwa perbedaan skor afinitas murni dipengaruhi oleh efektivitas kecocokan konformasi (*induced fit*) di dalam kantung aktif katalitik NtMGAM.

---

### 3. Pertanyaan 3: Identifikasi Residu Asam Amino Penting yang Diikat Bersama
Analisis interaksi interatomik membuktikan adanya keterlibatan residu asam amino katalitik kunci yang diikat secara bersamaan (*conserved catalytic residues*) antara ligan kontrol Miglitol dan ketiga senyawa kandidat:
* **Asp327 dan Asp542:** Kedua residu aspartat ini merupakan residu katalitik utama enzim $\alpha$-glukosidase (nukleofil dan donor proton asam-basa). Seluruh kandidat (Quercetin, Luteolin, Mangiferin) dan kontrol Miglitol secara konsisten membentuk ikatan hidrogen kuat dengan jarak $2.66\ \text{Å} - 3.48\ \text{Å}$ pada Asp327 dan Asp542.
* **Asp203 & Arg526:** Berperan menstabilkan orientasi gugus hidroksil ligan; terbukti membentuk ikatan hidrogen pada Luteolin (3.17 Å) dan Mangiferin (2.80 Å).
* **His600:** Residu pengapit kantung aktif yang turut membentuk ikatan hidrogen pada Luteolin (3.19 Å) dan Mangiferin (2.99 Å).
Tingkat kesamaan residu (*residue similarity*) terhadap kantung kontak Miglitol mencapai **92.9% pada Luteolin** (13 dari 14 residu identik) serta **85.7% pada Quercetin dan Mangiferin** (12 dari 14 residu identik).

---

### 4. Pertanyaan 4: Perbandingan Karakteristik Jenis Interaksi Intermolekuler
Terdapat perbedaan fundamental dalam arsitektur ikatan antara ligan iminosugar sintetis (Miglitol) dan polifenol bahan alam:
* **Miglitol (Kontrol):** Didominasi oleh **ikatan hidrogen polar murni** (7 ikatan hidrogen) yang dibentuk oleh cincin piperidin polihidroksi dan rantai hidroksietilnya. Miglitol memiliki ukuran kecil (MW 207.22 g/mol) sehingga hanya mengisi subkantung -1 tanpa interaksi aromatik yang signifikan.
* **Quercetin & Luteolin (Flavonoid):** Memiliki interaksi ganda: **ikatan hidrogen elektrostatik** pada gugus fenolik serta **interaksi $\pi$-$\pi$ stacking / hidrofobik** yang sangat kuat antara cincin aromatik kromon ligan dengan residu aromatik reseptor (Trp406 pada jarak 3.26–3.53 Å, Phe575 pada jarak 3.49–3.71 Å, dan Tyr299 pada jarak 3.44–3.67 Å). Ketiadaan gugus 3-OH pada Luteolin menjadikannya lebih planar sehingga penataan cincin terhadap celah hidrofobik Trp406/Phe450 menjadi paling optimal.
* **Mangiferin (Glukosilxanton):** Memiliki gugus C-glukosil yang berperan meniru rantai gula substrat melalui 6 ikatan hidrogen, dikombinasikan dengan inti xanton planar yang membentuk kontak $\pi$ terhadap Tyr299 dan Phe575.

---

### 5. Pertanyaan 5: Evaluasi Kritis Skor Energi vs. Profil ADMET (Mengapa Skor Paling Negatif Tidak Otomatis Terbaik?)
Dalam penemuan obat (*drug discovery*), skor *binding affinity* komputasi yang sangat negatif **tidak dapat dijadikan satu-satunya tolok ukur penentu kelayakan klinis**.
* **Fenomena Molekul Besar pada Skor Vina:** Fungsi skoring AutoDock Vina memberikan penalti dan penghargaan berbasis gaya van der Waals serta kontak luas permukaan. Molekul dengan bobot besar dan banyak cincin (seperti Mangiferin, MW 422.34 g/mol) secara matematis mudah memperoleh skor energi negatif akibat akumulasi kontak non-spesifik.
* **Dilema Farmakokinetik Mangiferin:** Hasil penapisan ADMETlab 2.0 menunjukkan Mangiferin melanggar Aturan Lipinski (*Lipinski's Rule of Five*), yaitu memiliki jumlah donor ikatan hidrogen berlebih ($\text{HBD} = 8 > 5$), akseptor berlebih ($\text{HBA} = 11 > 10$), dan luas permukaan polar tinggi ($\text{TPSA} = 201.28\ \text{Å}^2 > 140\ \text{Å}^2$). Hal ini menyebabkan Mangiferin memiliki permeabilitas membran rendah dan absorpsi usus minimal. Walaupun demikian, karena target enzim $\alpha$-glukosidase bekerja lokal di saluran pencernaan (*brush border* usus), sifat tidak terserapnya Mangiferin justru dapat menguntungkan untuk meminimalkan beban hepar/ginjal, meski memerlukan formulasi pembawa khusus (seperti misel PEG/F127 pada jurnal Bezerra et al., 2019).
* **Keseimbangan Luteolin & Quercetin:** Luteolin dan Quercetin 100% mematuhi aturan Lipinski, Pfizer, dan GSK, memiliki LogP optimal (2.15–2.90), serta bioavailabilitas oral tinggi tanpa kendala polaritas ekstrem.

---

### 6. Pertanyaan 6: Penetapan Kandidat Prioritas Utama (*Lead Candidate*)
Berdasarkan integrasi holistik antara **energi penambatan (*binding affinity*)**, **kesamaan residu kantung aktif (92.9%)**, **kepatuhan profil ADMET (100% Lolos Lipinski)**, dan **keamanan toksisitas**, maka:
> **LUTEOLIN ditetapkan sebagai KANDIDAT PRIORITAS UTAMA (Lead Candidate).**
Luteolin unggul karena:
1. Menghasilkan skor afinitas tertinggi (-7.9 kkal/mol).
2. Membentuk ikatan hidrogen langsung dengan 2 residu katalitik kunci (Asp327 dan Asp542).
3. Memiliki konformasi flavon planar sempurna yang memicu interaksi $\pi$-$\pi$ *stacking* terstabil dengan Trp406 (3.26 Å).
4. Profil farmakokinetik oral prima (LogP 2.90, TPSA 111.13 $\text{Å}^2$, 0 pelanggaran Lipinski).

Sebagai alternatif sekunder, **Quercetin** diposisikan sebagai kandidat pendamping berkat rekor $IC_{50}$ in vitro yang luar biasa poten ($7.97\ \mu\text{M}$ pada Liu et al., 2024).

---

### 7. Pertanyaan 7: Kesesuaian Hasil Komputasi dengan Hipotesis & Data Literatur *In Vitro*
Hasil pemodelan *in silico* kelompok kami terbukti **sangat sejalan dan memperkuat temuan eksperimental pada ketiga jurnal acuan**:
* **Kesesuaian Luteolin (Yan et al., 2014):** Jurnal membuktikan secara spektroskopi fluoresensi bahwa Luteolin membentuk kompleks spontan ($\Delta G^\circ < 0$) yang didorong oleh interaksi hidrofobik dan ikatan hidrogen. Temuan simulasi docking kami mengonfirmasi bahwa afinitas tertinggi (-7.9 kkal/mol) didorong oleh kontak hidrofobik Trp406/Phe575 dan 6 ikatan hidrogen pada kantung aktif.
* **Kesesuaian Quercetin (Liu et al., 2024):** Jurnal mencatat Quercetin memiliki $IC_{50} = 7.97\ \mu\text{M}$ (>15x lebih poten dari Acarbose). Hasil docking kami membuktikan Quercetin berikatan kuat (-7.1 kkal/mol vs Miglitol -5.5 kkal/mol) dengan jarak ikatan hidrogen sangat pendek pada Asp327 (2.76 Å).
* **Kesesuaian Mangiferin (Bezerra et al., 2019):** Jurnal melaporkan inhibisi hidrolisis pNPG hingga 90.42%. Simulasi kami membuktikan gugus C-glukosilnya berhasil meniru posisi substrat dengan ikatan hidrogen Arg526 (2.80 Å).

---

### 8. Pertanyaan 8: Keterbatasan Metode Komputasi & Batasan Integritas Akademik
Dalam menginterpretasikan hasil simulasi ini, beberapa keterbatasan metodologis harus diakui secara transparan:
1. **Asumsi Reseptor Kaku (*Rigid Receptor Backbone*):** AutoDock Vina mengasumsikan kerangka protein bersifat kaku selama proses docking, sehingga tidak mencerminkan fleksibilitas dinamis (*induced-fit*) penuh yang terjadi di dalam sel hidup.
2. **Peniadaan Molekul Air Kristal (*Solvation Effects*):** Seluruh molekul air kristal dihilangkan saat preparasi reseptor, padahal beberapa molekul air struktural dapat berperan sebagai jembatan ikatan hidrogen (*water-mediated H-bonds*).
3. **Fungsi Skoring Empiris:** Nilai binding affinity merupakan estimasi termodinamika teoritis yang memerlukan validasi lanjutan melalui simulasi Dinamika Molekuler (*Molecular Dynamics Simulation*, minimal 100 ns) serta uji hambatan enzimatik *in vitro*.

**Batasan Klaim Ilmiah (*Academic Integrity*):**
> Kelompok kami menegaskan bahwa hasil simulasi ini **tidak menyatakan** bahwa Luteolin atau Quercetin secara langsung telah menjadi obat paten penyembuh Diabetes Melitus. Pernyataan yang valid secara ilmiah adalah: *"Senyawa Luteolin dan Quercetin terbukti memiliki afinitas dan kestabilan penambatan teoritis yang sangat kompetitif terhadap sisi aktif enzim $\alpha$-glukosidase (3L4W), serta memenuhi kriteria druglikeness oral, sehingga sangat layak diprioritaskan sebagai kandidat ligan untuk pengujian hayati tahap lanjut."*
