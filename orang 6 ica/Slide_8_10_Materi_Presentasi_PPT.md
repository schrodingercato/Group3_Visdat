# MATERI SLIDE PRESENTASI PPT (SLIDE 8, 9, DAN 10)
**Bagian Presentasi Orang 6:** Visualisasi Data, Interpretasi Hasil, dan Kesimpulan  
**Penyusun:** Aisyah Rahmi Nadjib (Ica - 5049241030)

---

## 📽️ SLIDE 8: VISUALISASI INTERAKSI 2D & KOMPARASI BINDING SITE

### Judul Slide:
**Visualisasi Interaksi 2D Molekuler pada Kantung Aktif $\alpha$-Glukosidase (3L4W)**

### Elemen Visual:
* Tampilkan 4 Gambar Diagram 2D Interaksi dari folder `orang 6 ica/`:
  1. `2D_interaction_miglitol.png` (Kontrol: -5.5 kkal/mol)
  2. `2D_interaction_quercetin.png` (Kandidat 1: -7.1 kkal/mol)
  3. `2D_interaction_luteolin.png` (Kandidat 2: -7.9 kkal/mol — *Skor Terbaik*)
  4. `2D_interaction_mangiferin.png` (Kandidat 3: -7.0 kkal/mol)

### Poin Utama Pembicara (*Speaker Notes*):
* **Kantung Pengikatan Terbukti Konsisten:** Ketiga kandidat menempati koordinat rongga katalitik yang identik dengan ligan native Miglitol, dengan tingkat kesamaan residu mencapai **92.9% pada Luteolin** dan **85.7% pada Quercetin & Mangiferin**.
* **Residu Katalitik Kunci Terikat:** Seluruh kandidat berhasil berikatan hidrogen dengan asam amino esensial katalitik **Asp327** dan **Asp542** (jarak ikatan sangat dekat, $2.66 - 3.48\ \text{Å}$).
* **Pergeseran Tipe Interaksi:** Miglitol hanya mengandalkan ikatan hidrogen polar murni, sedangkan Quercetin dan Luteolin diperkuat oleh ikatan hidrogen elektrostatik **ditambah interaksi aromatik $\pi$-$\pi$ stacking** dengan residu Trp406, Phe575, dan Tyr299, menghasilkan energi ikatan yang jauh lebih stabil.

---

## 📽️ SLIDE 9: ANALISIS SAR, SKOR AFINITAS, DAN EVALUASI ADMET

### Judul Slide:
**Evaluasi Kritis: Hubungan Struktur-Aktivitas (SAR) vs. Profil Farmakokinetik ADMET**

### Elemen Visual:
* Tabel Ringkas Skor Binding Affinity vs Status Lipinski Ro5:
  * Luteolin: -7.9 kkal/mol | Lolos Lipinski (0 Pelanggaran) | Permeabilitas Optimal
  * Quercetin: -7.1 kkal/mol | Lolos Lipinski (0 Pelanggaran) | Permeabilitas Baik
  * Mangiferin: -7.0 kkal/mol | 2 Pelanggaran Lipinski (HBD>5, TPSA>140) | Aksi Lokal
  * Miglitol: -5.5 kkal/mol | Lolos Lipinski | Efek Samping Saluran Cerna Berat

### Poin Utama Pembicara (*Speaker Notes*):
* **Mengapa Luteolin Paling Unggul?** Ketiadaan gugus 3-OH pada Luteolin memberikan planaritas cincin flavon yang sempurna, memungkinkan penataan cincin kromon masuk lebih dalam ke celah hidrofobik Trp406 (jarak 3.26 Å).
* **Mengapa Skor Negatif Mangiferin Tidak Menjadikannya Obat Terbaik?** Mangiferin memiliki bobot besar dan gugus glukosil yang menambah skor kontak non-spesifik, namun memiliki TPSA tinggi ($201.28\ \text{Å}^2$) yang menghambat absorpsi sistemik. Kendati demikian, sifat ini berpotensi dijadikan inhibitor lokal di lumen usus tanpa membebani organ hati.
* **Keseimbangan Druglikeness:** Luteolin dan Quercetin memenuhi seluruh kriteria Lipinski, Pfizer, dan GSK dengan bioavailabilitas oral tinggi.

---

## 📽️ SLIDE 10: KESIMPULAN AKHIR & REKOMENDASI PENELITIAN

### Judul Slide:
**Kesimpulan Proyek & Rekomendasi Terapi Diabetes Melitus**

### Poin Ringkasan Slide:
1. **Validasi Berhasil:** Simulasi redocking ligan native Miglitol terbukti valid dengan nilai $\text{RMSD} \le 2.0\ \text{Å}$.
2. **Kandidat Prioritas Utama (*Lead Candidate*):** **LUTEOLIN** terpilih sebagai kandidat terbaik dengan *binding affinity* tertinggi (**-7.9 kkal/mol**, selisih $-2.4\ \text{kkal/mol}$ vs kontrol), kesamaan residu kantung aktif **92.9%**, dan kepatuhan ADMET sempurna.
3. **Kandidat Pendamping Poten:** **QUERCETIN** (-7.1 kkal/mol) menjadi kandidat kedua dengan rekor $IC_{50}$ in vitro literatur yang 15× lebih kuat dari obat standar Acarbose.
4. **Keunggulan vs Obat Sintetis:** Senyawa flavonoid alami menawarkan alternatif terapi yang minim efek samping gastrointestinal kronis (seperti kram dan flatulensi parah pada Miglitol).
5. **Rekomendasi Lanjutan:** Diperlukan simulasi *Molecular Dynamics* (MD 100 ns) dan pengujian *in vitro / in vivo* lanjutan untuk memvalidasi efikasi biologis kandidat.
