# Matriks Bukti Ilmiah & Integrasi Literatur Penugasan ETS
**Mata Kuliah:** Visualisasi Data Medis — Departemen Teknologi Kedokteran FKK ITS  
**Topik:** Molecular Docking Enzim $\alpha$-Glukosidase pada Diabetes Melitus Tipe 2 (DMT2)  
**Target Komparasi:** Ligan Native Miglitol (PDB ID: `3L4W`) vs. Kandidat Quercetin, Luteolin, dan Mangiferin

---

## 1. Analisis & Verifikasi Dokumen Jurnal

Ketiga artikel ilmiah yang Anda lampirkan memiliki validitas ilmiah yang kuat untuk dijadikan dasar penulisan laporan ETS:

1. **Artikel 1 (Quercetin & Analognya):**
   * *Judul:* Quercetin analogs as $\alpha$-glucosidase inhibitors with antidiabetic activity
   * *Jurnal:* *Food Bioscience* 58 (2024), 103713 (Elsevier, Q1)
   * *Penulis:* Honghui Liu, Yan Wang, Jing Tong, Jing Li, Hong Ding
   * *Relevansi Proyek:* Menyajikan data kuantitatif inhibisi $\alpha$-glukosidase oleh quercetin alami murni ($IC_{50} = 7.97 \pm 0.89\ \mu\text{M}$) sebagai pembanding terhadap acarbose ($IC_{50} = 124.22 \pm 4.48\ \mu\text{M}$), kinetika enzim, serta simulasi komputasi docking dan dinamika molekuler (MD).

2. **Artikel 2 (Luteolin):**
   * *Judul:* $\alpha$-Glucosidase inhibition by luteolin: Kinetics, interaction and molecular docking
   * *Jurnal:* *International Journal of Biological Macromolecules* 64 (2014), 213–223 (Elsevier, Q1)
   * *Penulis:* Jiakai Yan, Guowen Zhang, Junhui Pan, Yajie Wang
   * *Relevansi Proyek:* Membuktikan secara spektroskopis (fluoresensi, CD, FT-IR) dan komputasi bahwa luteolin menghambat $\alpha$-glukosidase secara reversibel dan non-kompetitif ($IC_{50} = 172 \pm 5\ \mu\text{M}$, $K_i = 140 \pm 2\ \mu\text{M}$), menginduksi perubahan konformasi sekunder protein, serta mengonfirmasi peran dominan interaksi hidrofobik dan ikatan hidrogen.

3. **Artikel 3 (Mangiferin):**
   * *Judul:* $\alpha$-Glucosidase inhibitory activity of mangiferin-loaded F127/PEG micellar system
   * *Jurnal:* *Materials Letters* 255 (2019), 126522 (Elsevier, Q2)
   * *Penulis:* Francisco W.A. Bezerra, Lillian M.U.D. Fechine, Karen P.S. Lopes, et al.
   * *Relevansi Proyek:* Membuktikan daya inhibisi $\alpha$-glukosidase oleh senyawa aktif mangiferin murni (*free-form*) sebesar $90.42\%$ dengan $IC_{50} = 0.283\ \text{mg/mL}$ ($670\ \mu\text{M}$), serta menyoroti keterbatasan kelarutan airnya yang menjadi landasan pembahasan uji ADMET/Lipinski Rule of 5.

---

## 2. Tabel Matriks Komparatif Bukti Eksperimental & Komputasi

| Parameter Evaluasi | Quercetin (Liu et al., 2024) | Luteolin (Yan et al., 2014) | Mangiferin (Bezerra et al., 2019) |
| :--- | :--- | :--- | :--- |
| **Kelas Kimiawi** | Flavonoid (Flavonol, aglikon) | Flavonoid (Flavon, aglikon) | Xanton C-glikosida (*glucosylxanthone*) |
| **Formula & Bobot** | $\text{C}_{15}\text{H}_{10}\text{O}_7$ (302.24 g/mol) | $\text{C}_{15}\text{H}_{10}\text{O}_6$ (286.24 g/mol) | $\text{C}_{19}\text{H}_{18}\text{O}_{11}$ (422.34 g/mol) |
| **PubChem CID** | 5280343 | 5280445 | 5281647 |
| **Nilai $IC_{50}$ Eksperimental** | $7.97 \pm 0.89\ \mu\text{M}$ (vs. Acarbose $124.22\ \mu\text{M}$) | $172 \pm 5\ \mu\text{M}$ (vs. Acarbose $108\ \mu\text{M}$) | $0.283\ \text{mg/mL}$ ($\sim 670\ \mu\text{M}$; daya inhibisi 90.42%) |
| **Tipe Inhibisi Enzim** | Campuran / Non-kompetitif (Kinetika Lineweaver-Burk) | Non-kompetitif murni ($K_i = 140\ \mu\text{M}$, reaksi reversibel) | Inhibisi hidrolisis enzimatik substrat pNPG |
| **Termodinamika / Gaya Dominan** | Ikatan hidrogen elektrostatik & interaksi halogen/aromatik | Entropi-driven ($\Delta H^\circ > 0, \Delta S^\circ > 0$), dominasi hidrofobik & H-bond | Interaksi polihidroksi & cincin xanton lipofilik |
| **Dampak Konformasi Enzim** | Kompleks stabil pada simulasi MD 100 ns (RMSD $1.89\ \text{Å}$) | Mengurangi $\alpha$-helix (37.9% $\rightarrow$ 30.2%), memicu *cleft closure* | Memblokir hidrolisis ikatan $\alpha$-(1,4)-glikosidik |
| **Perilaku ADMET / Kelarutan** | Memenuhi Lipinski Ro5, absorpsi moderat | Memenuhi Lipinski Ro5, permeabilitas membran baik | Pelanggaran Lipinski (HBD $> 5$), kelarutan air rendah ($S_0 = 18.1\ \text{mg/dL}$) |

---

## 3. Strategi Integrasi Sitasi ke dalam Struktur Laporan ETS

### Bab 8.2 Pendahuluan (Latar Belakang & Rasionalitas Pemilihan Kandidat)
* **Target Enzim:** Jelaskan bahwa $\alpha$-glukosidase merupakan hidrolase epitel usus yang memecah oligosakarida menjadi glukosa terabsorpsi. Inhibisi enzim ini efektif menekan lonjakan glukosa darah pascapranjak (*postprandial hyperglycemia*), namun obat klinis sintetis seperti miglitol dan acarbose kerap menimbulkan efek samping gastrointestinal (Liu et al., 2024; Yan et al., 2014).
* **Rasionalitas Quercetin:** Quercetin dipilih sebagai senyawa model flavonol polihidroksi karena dilaporkan memiliki nilai $IC_{50}$ sebesar $7.97\ \mu\text{M}$, lebih dari 15 kali lebih poten daripada acarbose pada uji in vitro (Liu et al., 2024).
* **Rasionalitas Luteolin:** Luteolin merepresentasikan kerangka flavon planar tanpa gugus 3-OH. Luteolin terbukti menghambat $\alpha$-glukosidase secara reversibel dan non-kompetitif, memicu *fluorescence quenching* statis, serta menginduksi perubahan konformasi sekunder enzim (Yan et al., 2014).
* **Rasionalitas Mangiferin:** Mangiferin dipilih untuk mengevaluasi pengaruh penambahan gugus glukosil alami pada cincin xanton. Senyawa ini terbukti mampu menghambat $\alpha$-glukosidase dengan efektivitas mencapai 90.42% (Bezerra et al., 2019), menjadikannya pembanding alami terhadap ligan iminosugar Miglitol.

### Bab 8.3 Metode (Parameter Komputasi)
* Cantumkan rujukan Liu et al. (2024) dan Yan et al. (2014) untuk mendukung validitas penggunaan AutoDock Vina, preparasi penambahan hidrogen polar, serta visualisasi interaksi menggunakan Discovery Studio Visualizer.

### Bab 8.5 Pembahasan (Sintesis Kritis & 8 Pertanyaan Wajib)
1. **Analisis SAR (Structure-Activity Relationship):**
   * Bandingkan struktur quercetin ($\text{C}_{15}\text{H}_{10}\text{O}_7$) dan luteolin ($\text{C}_{15}\text{H}_{10}\text{O}_6$). Hilangnya gugus 3-OH pada luteolin membuat cincin kromon lebih planar dan cenderung menstabilkan interaksi hidrofobik/$\pi$-$\pi$ stacking di dekat binding pocket, sesuai temuan termodinamika Yan et al. (2014).
   * Sebaliknya, kehadiran gugus glukosil pada mangiferin ($\text{C}_{19}\text{H}_{18}\text{O}_{11}$) meningkatkan jumlah donor/akseptor ikatan hidrogen, meniru gugus gula alami dan menghasilkan skor energi docking yang sangat negatif.
2. **Evaluasi Skor Afinitas vs. Profil ADMET (Pertanyaan Wajib No. 5 & 6):**
   * Jelaskan bahwa skor binding affinity paling negatif **tidak otomatis** menjadikan senyawa sebagai kandidat klinis terbaik.
   * Mangiferin dapat menunjukkan afinitas tinggi di PyRx karena banyaknya interaksi non-kovalen. Namun, sebagaimana dibuktikan oleh Bezerra et al. (2019), mangiferin memiliki keterbatasan kelarutan air ($S_0 = 18.1\ \text{mg/dL}$) dan melanggar aturan Lipinski (donor ikatan hidrogen $> 5$), sehingga memerlukan sistem penghantaran khusus (*drug delivery system*).
   * Sebaliknya, quercetin dan luteolin lebih seimbang antara afinitas ikatan dan kelayakan farmakokinetik oral.
3. **Korelasi Terhadap Ligan Kontrol (Miglitol):**
   * Miglitol (MW 207.22 g/mol) berikatan secara pas pada sub-situs katalitik -1. Ketiga kandidat polifenol berukuran lebih besar (MW 286–422 g/mol), sehingga selain menempati kantung aktif utama, mereka juga berinteraksi dengan residu pintu masuk kantung melalui gaya van der Waals dan kontak hidrofobik, selaras dengan model docking Liu et al. (2024) dan Yan et al. (2014).

---

## 4. Daftar Pustaka Format APA 7th Edition (Bab 8.7)

```text
Bezerra, F. W. A., Fechine, L. M. U. D., Lopes, K. P. S., de Sousa, A. F., do Nascimento, G. O., 
    Amaral, H. H. d. S., Leal, L. K. A. M., Trevisan, M. T. S., Ribeiro, M. E. N. P., & Ricardo, 
    N. M. P. S. (2019). α-Glucosidase inhibitory activity of mangiferin-loaded F127/PEG micellar 
    system. Materials Letters, 255, Article 126522. https://doi.org/10.1016/j.matlet.2019.126522

Liu, H., Wang, Y., Tong, J., Li, J., & Ding, H. (2024). Quercetin analogs as α-glucosidase 
    inhibitors with antidiabetic activity. Food Bioscience, 58, Article 103713. 
    https://doi.org/10.1016/j.fbio.2024.103713

Yan, J., Zhang, G., Pan, J., & Wang, Y. (2014). α-Glucosidase inhibition by luteolin: Kinetics, 
    interaction and molecular docking. International Journal of Biological Macromolecules, 64, 
    213–223. https://doi.org/10.1016/j.ijbiomac.2013.12.007
```