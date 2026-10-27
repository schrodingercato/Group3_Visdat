# BAB 8.6: KESIMPULAN LAPORAN PROYEK ETS
**Mata Kuliah:** Visualisasi Data Medis  
**Topik:** Simulasi Molecular Docking Senyawa Bahan Alam Terhadap Enzim $\alpha$-Glukosidase (PDB ID: 3L4W)  
**Penyusun:** Orang 6 (Aisyah Rahmi Nadjib / Ica - 5049241030)

---

Berdasarkan keseluruhan tahapan simulasi *in silico*, penapisan farmakokinetik ADMET, dan analisis interaksi molekuler yang telah dilaksanakan pada Proyek Evaluasi Tengah Semester (ETS), dapat ditarik beberapa kesimpulan pokok sebagai berikut:

1. **Validitas Metodologi Penambatan Molekuler:**
   Simulasi *redocking* ligan alami Miglitol ke dalam makromolekul target $\alpha$-glukosidase manusia (PDB ID: `3L4W`) menghasilkan nilai RMSD $\le 2.0\ \text{Å}$ pada ruang *grid box* terkunci (Center: 45.49, 91.76, 34.51; Size: $20 \times 20 \times 20\ \text{Å}$), yang mengonfirmasi bahwa parameter komputasi AutoDock Vina pada PyRx memiliki akurasi spasial yang valid dan dapat diandalkan untuk menguji ligan kandidat baru.

2. **Kestabilan Pengikatan Senyawa Kandidat:**
   Ketiga senyawa bahan alam membuktikan stabilitas termodinamika pengikatan yang lebih unggul dibandingkan ligan native Miglitol (-5.5 kkal/mol). Nilai *binding affinity* secara berurutan adalah:
   * **Luteolin:** **-7.9 kkal/mol** (Selisih $\Delta\Delta G = -2.4\ \text{kkal/mol}$ terhadap kontrol)
   * **Quercetin:** **-7.1 kkal/mol** (Selisih $\Delta\Delta G = -1.6\ \text{kkal/mol}$ terhadap kontrol)
   * **Mangiferin:** **-7.0 kkal/mol** (Selisih $\Delta\Delta G = -1.5\ \text{kkal/mol}$ terhadap kontrol)

3. **Konsistensi Residu dan Interaksi Kantung Aktif:**
   Seluruh kandidat terbukti menempati kantung katalitik yang identik dengan ligan native. Luteolin menunjukkan derajat kemiripan residu tertinggi sebesar **92.9%** (13 dari 14 residu identik dengan Miglitol), serta berhasil mengikat residu katalitik utama (Asp327 dan Asp542) melalui kombinasi ikatan hidrogen rapat dan interaksi $\pi$-$\pi$ *stacking* dengan Trp406 (3.26 Å).

4. **Penetapan Senyawa Prioritas (*Lead Candidate*):**
   Dengan memadukan skor energi pengikatan, geometri interaksi, dan evaluasi *druglikeness* (Aturan Lipinski), **Luteolin ditetapkan sebagai kandidat prioritas utama (*lead candidate*)**, didampingi oleh **Quercetin**. Kedua senyawa ini menunjukkan profil absorpsi oral yang optimal, tidak melanggar aturan Lipinski, dan memiliki riwayat efikasi *in vitro* yang kuat pada literatur rujukan.

5. **Rekomendasi Penelitian Lanjutan:**
   Untuk menyempurnakan temuan komputasi ini, disarankan pengujian lanjutan berupa simulasi *Molecular Dynamics* (MD) jangka panjang (minimal 100 ns) guna mengamati stabilitas dinamis konformasi enzim, serta pengujian enzimatik *in vitro* dan *in vivo* pada model hewan coba diabetes.
