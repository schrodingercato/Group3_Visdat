# -*- coding: utf-8 -*-
"""
Script to generate a 2-page comprehensive cheatsheet PDF for Kelompok 3 (Visdat ETS).
Designed for Ica (Aisyah Rahmi Nadjib) with clear visual hierarchy, color coding,
and professional typography.
"""
import os
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether, PageBreak, HRFlowable
)
import fitz  # PyMuPDF

sys.stdout.reconfigure(encoding='utf-8')

OUTPUT_PDF = r"c:\Users\Aisyah R. Nadjib\Downloads\Semester 5\Visdat\ets\orang 6 ica\Cheatsheet_Proyek_Kelompok_3_Lengkap.pdf"

# Page setup: A4 = 210 x 297 mm. Margins: 10 mm left/right, 10 mm top/bottom
PAGE_W, PAGE_H = A4
MARGIN = 10 * mm
USABLE_W = PAGE_W - 2 * MARGIN

doc = SimpleDocTemplate(
    OUTPUT_PDF,
    pagesize=A4,
    leftMargin=MARGIN,
    rightMargin=MARGIN,
    topMargin=8 * mm,
    bottomMargin=8 * mm
)

# Color Palette: Burgundy/Wine & Navy/Teal accents
C_PRIMARY = colors.HexColor("#5E1214")     # Deep Wine Red
C_SECONDARY = colors.HexColor("#1A365D")   # Deep Navy
C_ACCENT = colors.HexColor("#C59B27")      # Antique Gold
C_DARK = colors.HexColor("#1F2937")        # Dark slate
C_LIGHT_BG = colors.HexColor("#F8FAFC")    # Cool light grey
C_WINE_BG = colors.HexColor("#FDF2F2")     # Soft wine tint
C_NAVY_BG = colors.HexColor("#F0F4F8")     # Soft navy tint
C_GREEN_BG = colors.HexColor("#ECFDF5")    # Soft green tint
C_BORDER = colors.HexColor("#E2E8F0")

# Styles
styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    'DocTitle',
    fontName='Helvetica-Bold',
    fontSize=13,
    leading=15,
    textColor=C_PRIMARY,
    alignment=1
)
subtitle_style = ParagraphStyle(
    'DocSub',
    fontName='Helvetica',
    fontSize=8.5,
    leading=11,
    textColor=C_DARK,
    alignment=1
)
section_h1 = ParagraphStyle(
    'SecH1',
    fontName='Helvetica-Bold',
    fontSize=9.5,
    leading=12,
    textColor=colors.white
)
p_bold = ParagraphStyle(
    'PBold',
    fontName='Helvetica-Bold',
    fontSize=8,
    leading=10.5,
    textColor=C_DARK
)
p_body = ParagraphStyle(
    'PBody',
    fontName='Helvetica',
    fontSize=7.5,
    leading=9.8,
    textColor=C_DARK
)
p_body_small = ParagraphStyle(
    'PBodySmall',
    fontName='Helvetica',
    fontSize=7,
    leading=9,
    textColor=C_DARK
)
p_code = ParagraphStyle(
    'PCode',
    fontName='Helvetica-Bold',
    fontSize=7.5,
    leading=9.5,
    textColor=C_SECONDARY
)

def make_section_banner(title_text, bg_color=C_PRIMARY):
    p = Paragraph(f"<b>{title_text.upper()}</b>", section_h1)
    t = Table([[p]], colWidths=[USABLE_W])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), bg_color),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
    ]))
    return t

story = []

# =========================================================================
# PAGE 1: HEADER + THE BIG PICTURE + ALUR KERJA ESTAFET (ORANG 1 - 6)
# =========================================================================

# Main Header
story.append(Paragraph("CHEATSHEET LENGKAP PROYEK KELOMPOK 3 — VISDAT ETS", title_style))
story.append(Paragraph(
    "<b>In Silico Molecular Docking Senyawa Bahan Alam vs Human Intestinal &alpha;-Glucosidase (PDB: 3L4W)</b><br/>"
    "<i>Departemen Teknologi Kedokteran FKK ITS &bull; Bahan Hafalan Menyeluruh untuk Aisyah Rahmi Nadjib (Orang 6)</i>",
    subtitle_style
))
story.append(Spacer(1, 1.5 * mm))

# SECTION 1: THE BIG PICTURE & LOGIKA MEDIS
story.append(make_section_banner("1. Konsep Dasar Medis & Rasionalisasi Desain Riset", C_PRIMARY))
story.append(Spacer(1, 1 * mm))

big_picture_data = [
    [
        Paragraph("<b>Masalah Klinis (Diabetes Melitus Tipe 2):</b><br/>"
                  "Lonjakan gula darah pasca makan (<i>postprandial hyperglycemia</i>) dipicu oleh enzim pencernaan "
                  "<b>&alpha;-glukosidase</b> di brush border usus halus yang memecah karbohidrat kompleks menjadi glukosa siap serap.", p_body),
        Paragraph("<b>Solusi & Target Reseptor (PDB: 3L4W):</b><br/>"
                  "Inhibisi enzim mematikan hidrolisis gula. Digunakan struktur kristal resolusi tinggi <b>2.15 &Aring;</b> "
                  "<i>Human Maltase-Glucoamylase</i> (Nt-MGAM). Mengapa 3L4W? Karena mewakili enzim manusia langsung, bukan ragi/bakteri.", p_body)
    ],
    [
        Paragraph("<b>Kenapa Kontrolnya Miglitol, Bukan Acarbose?</b><br/>"
                  "<b>1. Faktor Kristalografi:</b> PDB 3L4W dikristalkan bersama <b>Miglitol</b> (kode: <code>MIG</code>). Miglitol adalah ligan native asli yang wajib digunakan untuk uji validasi redocking (kontrol positif).<br/>"
                  "<b>2. Kesetaraan Kimiawi:</b> Miglitol (BM 207) adalah <i>small molecule</i> kompak penghuni subsite inti (-1), sangat adil (<i>apple-to-apple</i>) dibanding flavonoid kita (BM 286-302). Acarbose adalah tetrasakarida besar (BM 646) yang melanggar Lipinski.", p_body),
        Paragraph("<b>Misi & Hipotesis Kelompok 3:</b><br/>"
                  "Menguji apakah senyawa polifenol alami (<b>Quercetin, Luteolin, Mangiferin</b>) dapat berikatan lebih kuat (&Delta;G lebih negatif), "
                  "lebih stabil mengunci triad katalitik, dan memiliki profil farmakokinetik oral yang lebih ramah dibanding obat standar.", p_body)
    ]
]
t_bp = Table(big_picture_data, colWidths=[USABLE_W * 0.5, USABLE_W * 0.5])
t_bp.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), C_WINE_BG),
    ('BOX', (0,0), (-1,-1), 0.5, C_PRIMARY),
    ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#F3C5C7")),
    ('TOPPADDING', (0,0), (-1,-1), 3),
    ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ('LEFTPADDING', (0,0), (-1,-1), 5),
    ('RIGHTPADDING', (0,0), (-1,-1), 5),
]))
story.append(t_bp)
story.append(Spacer(1, 2 * mm))

# SECTION 2: ALUR KERJA ESTAFET (ORANG 1 - 6)
story.append(make_section_banner("2. Alur Estafet Kerja Kelompok: Siapa Mengerjakan Apa & Output Kuncinya", C_SECONDARY))
story.append(Spacer(1, 1 * mm))

# Table of 6 People
flow_headers = [
    Paragraph("<b>Anggota & Peran</b>", p_bold),
    Paragraph("<b>Fokus Tugas & Software yang Digunakan</b>", p_bold),
    Paragraph("<b>Hasil / Deliverable Utama yang Diserahkan ke Tahap Berikutnya</b>", p_bold),
]

flow_rows = [
    [
        Paragraph("<b>Orang 1: Ziya</b><br/><i>Perumusan &amp; Literatur</i>", p_body),
        Paragraph("Studi pustaka patofisiologi diabetes; seleksi makromolekul reseptor dan ligan bahan alam.<br/>"
                  "<b>Tools:</b> PubMed, ScienceDirect, RSCB PDB.", p_body),
        Paragraph("&bull; Target terpilih: <b>Human &alpha;-Glucosidase (3L4W)</b>.<br/>"
                  "&bull; 3 Kandidat: Quercetin, Luteolin, Mangiferin.<br/>"
                  "&bull; Naskah Bab 1 - Bab 3 Laporan.", p_body)
    ],
    [
        Paragraph("<b>Orang 2: Melva</b><br/><i>Preparasi Reseptor</i>", p_body),
        Paragraph("Pembersihan struktur 3D protein agar kantung aktif bersih dan bebas interferensi.<br/>"
                  "<b>Tools:</b> BIOVIA Discovery Studio Visualizer.", p_body),
        Paragraph("&bull; Membuang molekul air (H<sub>2</sub>O), ion pengotor, dan ligan alami Miglitol.<br/>"
                  "&bull; File output: <code>Reseptor 3L4W Bersih_fixed.pdb</code> siap pakai.", p_body)
    ],
    [
        Paragraph("<b>Orang 3: Kezia</b><br/><i>Preparasi Ligan &amp; ADMET</i>", p_body),
        Paragraph("Unduh struktur 3D ligan, minimasi energi geometri, dan evaluasi kelayakan obat oral.<br/>"
                  "<b>Tools:</b> NCBI PubChem, PyRx (OpenBabel, UFF), ADMETlab 2.0.", p_body),
        Paragraph("&bull; File ligan format <code>.pdbqt</code> teroptimasi energi.<br/>"
                  "&bull; Skrining Lipinski: Luteolin &amp; Quercetin <b>0 violation (lolos)</b>; Mangiferin 2 violation (BM 422, 8 HBD).", p_body)
    ],
    [
        Paragraph("<b>Orang 4: Najma</b><br/><i>Validasi Metode (Redocking)</i>", p_body),
        Paragraph("Membuktikan akurasi parameter penambatan dengan me-redock ligan native Miglitol ke kantung aktif.<br/>"
                  "<b>Tools:</b> AutoDock Vina (PyRx), PyMOL (RMSD calculation).", p_body),
        Paragraph("&bull; <b>Grid Box:</b> Center (45.49, 91.76, 34.51), Size 20 &times; 20 &times; 20 &Aring;.<br/>"
                  "&bull; <b>RMSD = 1.05 &Aring; (&le; 2.0 &Aring; = VALID &amp; Reliable)</b>.<br/>"
                  "&bull; Parameter grid box siap dipakai untuk docking kandidat.", p_body)
    ],
    [
        Paragraph("<b>Orang 5: Fidel</b><br/><i>Docking Senyawa Kandidat</i>", p_body),
        Paragraph("Menjalankan simulasi docking 3 ligan herbal menggunakan koordinat grid box valid milik Najma.<br/>"
                  "<b>Tools:</b> AutoDock Vina (PyRx), PyMOL.", p_body),
        Paragraph("&bull; Skor &Delta;G (kcal/mol): <b>Luteolin -7.9</b>, Quercetin -7.1, Mangiferin -7.0, Miglitol -5.5.<br/>"
                  "&bull; File pose 3D terbaik (Pose 0 <code>.pdbqt</code>) untuk dianalisis oleh Ica.", p_body)
    ],
    [
        Paragraph("<b>Orang 6: Ica (Kamu!)</b><br/><i>Visualisasi, Analisis, &amp; Simpulan</i>", p_body),
        Paragraph("Visualisasi interaksi atomik 2D/3D resolusi tinggi, identifikasi gaya antarmolekul, evaluasi biokimia triad katalitik, penyusunan pembahasan kritis &amp; kesimpulan.<br/>"
                  "<b>Tools:</b> Discovery Studio, PyMOL ray-trace, Word/PPT/Python.", p_body),
        Paragraph("&bull; 4 Gambar Komposit High-Res (&gt;5000 px).<br/>"
                  "&bull; Analisis Triad Katalitik (Asp542, Asp327, Asp203) &amp; repulsive bump.<br/>"
                  "&bull; Bab 8.5 (8 Pertanyaan), Bab 8.6, Slide 8-10, &amp; Cheatsheet Sidang.", p_body)
    ]
]

t_flow = Table([flow_headers] + flow_rows, colWidths=[USABLE_W * 0.22, USABLE_W * 0.38, USABLE_W * 0.40])
t_flow.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), C_NAVY_BG),
    ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
    ('TOPPADDING', (0,0), (-1,-1), 2.5),
    ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ('LEFTPADDING', (0,0), (-1,-1), 4),
    ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('BACKGROUND', (0,6), (-1,6), colors.HexColor("#FEF3C7")), # highlight Ica
    ('BOX', (0,6), (-1,6), 1, C_ACCENT),
]))
story.append(t_flow)

# Footer hint Page 1
story.append(Spacer(1, 2 * mm))
story.append(Paragraph("<i>*Bersambung ke Halaman 2: Matriks Hasil Lengkap, Bedah Kimia Analisis, dan Panduan Menjawab Pertanyaan Dosen &bull; Kelompok 3 ETS Visdat</i>", ParagraphStyle('F1', fontName='Helvetica-Oblique', fontSize=6.5, textColor=colors.gray, alignment=1)))

# FORCE EXACT PAGE BREAK
story.append(PageBreak())

# =========================================================================
# PAGE 2: MATRIKS KOMPARASI + BEDAH KIMIA ANALISIS + Q&A PAMUNGKAS
# =========================================================================

# Header Page 2
story.append(Paragraph("CHEATSHEET LENGKAP PROYEK KELOMPOK 3 — HALAMAN 2", title_style))
story.append(Spacer(1, 1.5 * mm))

# SECTION 3: TABEL HASIL KOMPUTASI LENGKAP (BAB 7)
story.append(make_section_banner("3. Matriks Komparasi Parameter Komputasi & Farmakokinetik (Bab 7)", C_PRIMARY))
story.append(Spacer(1, 1 * mm))

tabel_bab7_headers = [
    Paragraph("<b>Senyawa</b>", p_bold),
    Paragraph("<b>&Delta;G (kcal/mol)</b>", p_bold),
    Paragraph("<b>H-Bonds</b>", p_bold),
    Paragraph("<b>Residu Triad Katalitik</b>", p_bold),
    Paragraph("<b>Interaksi Kunci Lainnya</b>", p_bold),
    Paragraph("<b>% Sim.</b>", p_bold),
    Paragraph("<b>Lipinski</b>", p_bold),
    Paragraph("<b>Status Evaluasi</b>", p_bold),
]

tabel_bab7_data = [
    [
        Paragraph("<b>Miglitol</b><br/><i>(Kontrol Native)</i>", p_body),
        Paragraph("<b>-5.5</b>", p_bold),
        Paragraph("7", p_body),
        Paragraph("Asp327, Asp542, Asp203", p_body),
        Paragraph("Unfavorable bump dg Arg526 (3.09 &Aring;)", p_body),
        Paragraph("100%", p_body),
        Paragraph("0 viol.", p_body),
        Paragraph("Kontrol validasi (skor terlemah)", p_body),
    ],
    [
        Paragraph("<b>Quercetin</b><br/><i>(Kandidat 1)</i>", p_body),
        Paragraph("<b>-7.1</b>", p_body),
        Paragraph("4", p_body),
        Paragraph("Asp327, Asp542", p_body),
        Paragraph("&pi;-&pi; Stacking (Tyr299, Phe575)", p_body),
        Paragraph("85.7%", p_body),
        Paragraph("0 viol.", p_body),
        Paragraph("Kuat, tapi ada 3-OH labil", p_body),
    ],
    [
        Paragraph("<b>Luteolin</b><br/><i>(Kandidat 2)</i>", p_bold),
        Paragraph("<b>-7.9</b>", ParagraphStyle('GLead', fontName='Helvetica-Bold', fontSize=8, textColor=colors.HexColor("#047857"))),
        Paragraph("<b>6</b>", p_bold),
        Paragraph("<b>Asp327, Asp542, Asp203 (Lengkap!)</b>", p_body),
        Paragraph("<b>3&times; &pi;-&pi; Stacking (Trp406, Phe450, Phe575)</b>", p_body),
        Paragraph("<b>92.9%</b>", p_bold),
        Paragraph("0 viol.", p_body),
        Paragraph("<b>LEAD COMPOUND TERBAIK</b>", ParagraphStyle('LStat', fontName='Helvetica-Bold', fontSize=7, textColor=colors.HexColor("#B45309"))),
    ],
    [
        Paragraph("<b>Mangiferin</b><br/><i>(Kandidat 3)</i>", p_body),
        Paragraph("<b>-7.0</b>", p_body),
        Paragraph("6", p_body),
        Paragraph("Asp327, Asp542, Asp203", p_body),
        Paragraph("Ikatan H ruah, sterik sempit", p_body),
        Paragraph("85.7%", p_body),
        Paragraph("2 viol.", p_body),
        Paragraph("Gagal oral (BM 422, 8 HBD)", p_body),
    ]
]

t_bab7 = Table([tabel_bab7_headers] + tabel_bab7_data, colWidths=[
    USABLE_W * 0.15, USABLE_W * 0.11, USABLE_W * 0.08, USABLE_W * 0.19, USABLE_W * 0.20, USABLE_W * 0.07, USABLE_W * 0.07, USABLE_W * 0.13
])
t_bab7.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), C_WINE_BG),
    ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
    ('TOPPADDING', (0,0), (-1,-1), 2.2),
    ('BOTTOMPADDING', (0,0), (-1,-1), 2.2),
    ('LEFTPADDING', (0,0), (-1,-1), 3),
    ('RIGHTPADDING', (0,0), (-1,-1), 3),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('BACKGROUND', (0,3), (-1,3), C_GREEN_BG), # highlight Luteolin
    ('BOX', (0,3), (-1,3), 1, colors.HexColor("#059669")),
]))
story.append(t_bab7)
story.append(Spacer(1, 2 * mm))

# SECTION 4: BEDAH KONSEP KIMIA ANALISIS UNTUK ICA
story.append(make_section_banner("4. Poin Kunci Kimia Analisis (SAR, Termodinamika & Mekanisme)", C_SECONDARY))
story.append(Spacer(1, 1 * mm))

chem_cards = [
    [
        Paragraph("<b>A. Triad Katalitik Aspartat (Pusat Reaksi):</b><br/>"
                  "Enzim 3L4W memotong ikatan glikosida via 3 residu karboksilat (-COO<sup>-</sup>):<br/>"
                  "&bull; <b>Asp542:</b> Nukleofil penyerang C1 anomerik gula.<br/>"
                  "&bull; <b>Asp327:</b> Asam Bronsted penyumbang proton ke oksigen glikosida.<br/>"
                  "&bull; <b>Asp203:</b> Penstabil keadaan transisi ionik.<br/>"
                  "&bull; <i>Luteolin mengunci ketiganya secara simultan (jarak 2.66 - 3.17 &Aring;), mematikan fungsi hidrolisis secara total!</i>", p_body),
        Paragraph("<b>B. Mengapa Skor Miglitol Lebih Rendah (-5.5)?</b><br/>"
                  "&bull; <b>Coulombic Repulsion:</b> Miglitol memiliki atom nitrogen sekunder terprotonasi (-NH<sub>2</sub><sup>+</sup>-). Terjadi tolakan elektrostatik kation-kation dengan kation guanidinium <b>Arg526</b> pada jarak 3.09 &Aring; (<i>unfavorable bump</i>).<br/>"
                  "&bull; <b>Ketiadaan Aromatik:</b> Miglitol tidak punya cincin benzena, sehingga kehilangan gaya stabilisasi &pi;-&pi; stacking.", p_body)
    ],
    [
        Paragraph("<b>C. Termodinamika & Desolvation Entropy:</b><br/>"
                  "Persamaan: <b>&Delta;G = &Delta;H - T&Delta;S</b>.<br/>"
                  "Saat cincin planar flavonoid (Luteolin) menempel di dinding kantung nonpolar (Phe450, Trp406, Phe575), molekul air hidrasi terlepas ke fasa ruah.<br/>"
                  "Pelepasan molekul air ini meningkatkan ketidakteraturan sistem (&Delta;S &gt; 0), memberikan sumbangan entalpi-entropi yang membuat &Delta;G jauh lebih negatif (-7.9 kcal/mol).", p_body),
        Paragraph("<b>D. Mengapa Luteolin Mengungguli Quercetin?</b><br/>"
                  "&bull; <b>Struktur SAR:</b> Quercetin punya gugus 3-OH pada cincin C, sedangkan Luteolin tidak punya (posisi 3 hidrogen murni).<br/>"
                  "&bull; <b>Steric Hindrance:</b> Ketiadaan 3-OH membuat Luteolin lebih ramping masuk ke koridor sempit 3L4W.<br/>"
                  "&bull; <b>Stabilitas Metabolik:</b> Gugus 3-OH pada Quercetin sangat rentan terhadap metabolisme lintas pertama (glukuronidasi cepat di usus/hati).", p_body)
    ]
]
t_chem = Table(chem_cards, colWidths=[USABLE_W * 0.5, USABLE_W * 0.5])
t_chem.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), C_LIGHT_BG),
    ('BOX', (0,0), (-1,-1), 0.5, C_SECONDARY),
    ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
    ('TOPPADDING', (0,0), (-1,-1), 2.5),
    ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ('LEFTPADDING', (0,0), (-1,-1), 4),
    ('RIGHTPADDING', (0,0), (-1,-1), 4),
]))
story.append(t_chem)
story.append(Spacer(1, 2 * mm))

# SECTION 5: SENJATA PAMUNGKAS TANYA-JAWAB SIDANG (Q&A CHEAT)
story.append(make_section_banner("5. Senjata Pamungkas Menjawab Pertanyaan Dosen Saat Ujian / Tanya-Jawab", C_PRIMARY))
story.append(Spacer(1, 1 * mm))

qa_rows = [
    [
        Paragraph("<b>Q1: Mengapa memakai PDB 3L4W?</b><br/>"
                  "<b>&bull; Jawaban:</b> <i>\"Karena 3L4W adalah struktur kristal sinar-X resolusi tinggi (2.15 &Aring;) dari Human Intestinal Maltase-Glucoamylase, target terapi primer diabetes melitus tipe 2 pada usus manusia (bukan enzim ragi/bakteri).\"</i>", p_body),
        Paragraph("<b>Q4: Mengapa Luteolin nomor 1 dan Mangiferin gugur?</b><br/>"
                  "<b>&bull; Jawaban:</b> <i>\"Luteolin mengunci 3 triad katalitik lengkap, 3&times; &pi;-&pi; stacking, kemiripan tertinggi (92.9%), dan 0 Lipinski violation. Mangiferin memiliki gugus C-glukosil ruah yang memicu benturan sterik serta melanggar 2 aturan Lipinski.\"</i>", p_body)
    ],
    [
        Paragraph("<b>Q2: Mengapa kontrolnya Miglitol, bukan Acarbose?</b><br/>"
                  "<b>&bull; Jawaban:</b> <i>\"Pertama, Miglitol adalah ligan alami ko-kristal asli di dalam file PDB 3L4W yang diperlukan untuk validasi redocking (RMSD 1.05 &Aring;). Kedua, Miglitol adalah small molecule (BM 207) penghuni subsite -1, sebanding secara adil (apple-to-apple) dengan flavonoid bahan alam kita.\"</i>", p_body),
        Paragraph("<b>Q5: Apakah hasil ini membuktikan Luteolin sudah jadi obat paten?</b><br/>"
                  "<b>&bull; Jawaban:</b> <i>\"Tidak, Bu/Pak. Simulasi in silico adalah pemodelan komputasi berbasis struktur rigid (prediksi awal). Luteolin ditetapkan sebagai lead candidate yang sangat prospektif, namun wajib divalidasi melalui uji laboratorium basah in vitro (IC50) dan in vivo.\"</i>", p_body)
    ],
    [
        Paragraph("<b>Q3: Mengapa metode docking kelompok Anda dinyatakan valid?</b><br/>"
                  "<b>&bull; Jawaban:</b> <i>\"Validasi dilakukan dengan me-redock Miglitol ke reseptor bersih pada grid box spesifik. Nilai RMSD yang diperoleh adalah 1.05 &Aring;, jauh di bawah ambang batas standar internasional (&le; 2.0 &Aring;), membuktikan algoritma PyRx mampu mereplikasi pose kristalografi alami.\"</i>", p_body),
        Paragraph("<b>Q6: Apa peran Anda (Orang 6) secara spesifik?</b><br/>"
                  "<b>&bull; Jawaban:</b> <i>\"Saya bertanggung jawab pada tahap hilir: memvalidasi pose spasial 3D/2D resolusi tinggi (&gt;5000 px), menganalisis gaya antarmolekul kimiawi, mengevaluasi interaksi triad katalitik, menyusun Bab 8.5 dan Bab 8.6, serta menyiapkan slide 8-10.\"</i>", p_body)
    ]
]

t_qa = Table(qa_rows, colWidths=[USABLE_W * 0.5, USABLE_W * 0.5])
t_qa.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), C_WINE_BG),
    ('BOX', (0,0), (-1,-1), 0.5, C_PRIMARY),
    ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#F3C5C7")),
    ('TOPPADDING', (0,0), (-1,-1), 2.5),
    ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ('LEFTPADDING', (0,0), (-1,-1), 4),
    ('RIGHTPADDING', (0,0), (-1,-1), 4),
]))
story.append(t_qa)

# Build PDF
doc.build(story)
print(f"Generated PDF: {OUTPUT_PDF}")

# Verify exact page count using fitz
doc_check = fitz.open(OUTPUT_PDF)
page_count = len(doc_check)
print(f"Total Page Count: {page_count}")
for i in range(page_count):
    page = doc_check[i]
    pix = page.get_pixmap(dpi=150)
    img_path = f"c:\\Users\\Aisyah R. Nadjib\\Downloads\\Semester 5\\Visdat\\ets\\orang 6 ica\\preview_cheatsheet_page_{i+1}.png"
    pix.save(img_path)
    print(f"Page {i+1} saved to {img_path}")
