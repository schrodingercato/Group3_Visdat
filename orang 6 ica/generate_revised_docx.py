# -*- coding: utf-8 -*-
"""
Master Builder for Revised Kelompok 3 ETS Medical Data Visualization Report.
Generates the complete, professional, publication-grade Word document:
- Resolves all 12 reviewer critique points.
- Keeps Bab 1-5 tightly focused and cohesive (meeting the 2-5 page equivalent core report limit).
- Moves extensive ADMET screening tables to Lampiran 5.
- Embeds all high-res visual assets and captions.
- Harmonizes all numbers, tables, and references.
"""

import os
import sys
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"c:\Users\Aisyah R. Nadjib\Downloads\Semester 5\Visdat\ets"
ORANG6_DIR = os.path.join(BASE_DIR, "orang 6 ica")
EXTRACTED_IMG_DIR = os.path.join(ORANG6_DIR, "extracted_docx_images")
OUTPUT_DOCX_MAIN = os.path.join(BASE_DIR, "ETS Visualisasi Data Medis_Kelompok 3.docx")
OUTPUT_DOCX_ORANG6 = os.path.join(ORANG6_DIR, "ETS Visualisasi Data Medis_Kelompok 3_REVISI_FINAL.docx")

doc = docx.Document()

# Page Setup: A4, 1 inch margins
section = doc.sections[0]
section.page_width = Inches(8.27)
section.page_height = Inches(11.69)
section.top_margin = Inches(1.0)
section.bottom_margin = Inches(1.0)
section.left_margin = Inches(1.0)
section.right_margin = Inches(1.0)

# Configure default styles
normal_style = doc.styles['Normal']
normal_style.font.name = 'Times New Roman'
normal_style.font.size = Pt(11)
normal_style.font.color.rgb = RGBColor(0x1F, 0x29, 0x37)
normal_style.paragraph_format.line_spacing = 1.15
normal_style.paragraph_format.space_after = Pt(4)

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def add_title(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(14)
    run.font.bold = True
    run.font.color.rgb = RGBColor(0x11, 0x18, 0x27)
    return p

def add_subtitle(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(12)
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(11)
    run.font.bold = True
    run.font.color.rgb = RGBColor(0x37, 0x41, 0x51)
    return p

def add_h1(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12.5)
    run.font.bold = True
    run.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A) # Deep Navy
    return p

def add_h2(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(11)
    run.font.bold = True
    run.font.color.rgb = RGBColor(0x1F, 0x29, 0x37)
    return p

def add_h3(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(10.5)
    run.font.bold = True
    run.font.italic = True
    run.font.color.rgb = RGBColor(0x37, 0x41, 0x51)
    return p

def add_body(text, bold_prefix="", italic_suffix=""):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        r_b = p.add_run(bold_prefix)
        r_b.font.name = 'Times New Roman'
        r_b.font.bold = True
    r_t = p.add_run(text)
    r_t.font.name = 'Times New Roman'
    if italic_suffix:
        r_i = p.add_run(italic_suffix)
        r_i.font.name = 'Times New Roman'
        r_i.font.italic = True
    return p

def add_bullet(text, bold_prefix=""):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        r_b = p.add_run(bold_prefix)
        r_b.font.name = 'Times New Roman'
        r_b.font.bold = True
    r_t = p.add_run(text)
    r_t.font.name = 'Times New Roman'
    return p

def add_table_title(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(9.5)
    r.font.bold = True
    return p

def add_image_with_caption(img_path, caption_text, width_inches=6.0):
    if os.path.exists(img_path):
        p_img = doc.add_paragraph()
        p_img.paragraph_format.space_before = Pt(8)
        p_img.paragraph_format.space_after = Pt(2)
        p_img.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.keep_with_next = True
        run_img = p_img.add_run()
        run_img.add_picture(img_path, width=Inches(width_inches))
        
        p_cap = doc.add_paragraph()
        p_cap.paragraph_format.space_before = Pt(2)
        p_cap.paragraph_format.space_after = Pt(6)
        p_cap.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_cap = p_cap.add_run(caption_text)
        r_cap.font.name = 'Times New Roman'
        r_cap.font.size = Pt(8.5)
        r_cap.font.italic = True
    else:
        print(f"Warning: Image not found at {img_path}")

def format_custom_table(headers, rows_data, col_widths, highlight_row_idx=None, highlight_hex="F0FDF4"):
    table = doc.add_table(rows=1, cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    
    # Header
    hdr_cells = table.rows[0].cells
    for i, h in enumerate(headers):
        hdr_cells[i].text = h
        set_cell_background(hdr_cells[i], "1E3A8A") # Navy
        set_cell_margins(hdr_cells[i], top=100, bottom=100, left=120, right=120)
        p = hdr_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.font.name = 'Times New Roman'
            r.font.size = Pt(8.5)
            r.font.bold = True
            r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    
    # Rows
    for r_idx, r_data in enumerate(rows_data):
        row_cells = table.add_row().cells
        is_highlight = (r_idx == highlight_row_idx)
        bg = highlight_hex if is_highlight else ("F9FAFB" if r_idx % 2 == 1 else "FFFFFF")
        for c_idx, val in enumerate(r_data):
            row_cells[c_idx].text = str(val)
            set_cell_background(row_cells[c_idx], bg)
            set_cell_margins(row_cells[c_idx], top=70, bottom=70, left=100, right=100)
            p = row_cells[c_idx].paragraphs[0]
            if c_idx == 0:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            else:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER if len(str(val)) < 15 else WD_ALIGN_PARAGRAPH.LEFT
            for r in p.runs:
                r.font.name = 'Times New Roman'
                r.font.size = Pt(8)
                if is_highlight:
                    r.font.bold = True
    
    # Apply widths
    for row in table.rows:
        for i, w in enumerate(col_widths):
            row.cells[i].width = Inches(w)
    
    p_spacer = doc.add_paragraph()
    p_spacer.paragraph_format.space_after = Pt(2)
    return table

# =========================================================================
# 1. COVER PAGE
# =========================================================================
add_title("LAPORAN EVALUASI TENGAH SEMESTER")
add_subtitle("Simulasi Molecular Docking dan Analisis In Silico Senyawa Bahan Alam terhadap Enzim α-Glukosidase Usus Manusia (PDB ID: 3L4W) sebagai Kandidat Ligan pada Diabetes Melitus Tipe 2")

p_crs = doc.add_paragraph()
p_crs.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
r_crs = p_crs.add_run("Mata Kuliah: VISUALISASI DATA MEDIS")
r_crs.font.name = 'Times New Roman'
r_crs.font.size = Pt(11)
r_crs.font.bold = True

logo_path = os.path.join(EXTRACTED_IMG_DIR, "img_0.png")
if os.path.exists(logo_path):
    p_logo = doc.add_paragraph()
    p_logo.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_logo.paragraph_format.space_before = Pt(12)
    p_logo.paragraph_format.space_after = Pt(12)
    run_logo = p_logo.add_run()
    run_logo.add_picture(logo_path, width=Inches(3.2))

p_by = doc.add_paragraph()
p_by.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_by.paragraph_format.space_before = Pt(8)
r_by = p_by.add_run("Disusun Oleh Kelompok 3:")
r_by.font.name = 'Times New Roman'
r_by.font.size = Pt(10.5)
r_by.font.bold = True

team_members = [
    "Desta Kezia Priyono (NRP: 5049241005)",
    "Fidellynne Khaleesha Abidi (NRP: 5049241014)",
    "Najma Khoirun Nisa (NRP: 5049241016)",
    "Ni Wayan Melva Vemitra (NRP: 5049241021)",
    "Aisyah Rahmi Nadjib (NRP: 5049241030)",
    "Ziyadatur Rif'ah (NRP: 5049241032)"
]
for m in team_members:
    p_m = doc.add_paragraph()
    p_m.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_m.paragraph_format.space_after = Pt(1)
    r_m = p_m.add_run(m)
    r_m.font.name = 'Times New Roman'
    r_m.font.size = Pt(10)

p_inst = doc.add_paragraph()
p_inst.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_inst.paragraph_format.space_before = Pt(16)
r_inst = p_inst.add_run(
    "PROGRAM STUDI TEKNOLOGI KEDOKTERAN\n"
    "FAKULTAS KEDOKTERAN DAN KESEHATAN\n"
    "INSTITUT TEKNOLOGI SEPULUH NOPEMBER\n"
    "SURABAYA\n"
    "2026"
)
r_inst.font.name = 'Times New Roman'
r_inst.font.size = Pt(10.5)
r_inst.font.bold = True

doc.add_page_break()

# =========================================================================
# KATA PENGANTAR & DAFTAR ISI
# =========================================================================
add_h1("KATA PENGANTAR")
add_body("Puji syukur kami panjatkan ke hadirat Tuhan Yang Maha Esa atas rahmat dan karunia-Nya sehingga Laporan Evaluasi Tengah Semester (ETS) mata kuliah Visualisasi Data Medis ini dapat diselesaikan dengan baik. Laporan ini menyajikan hasil simulasi penambatan molekuler (molecular docking) senyawa bahan alam (Quercetin, Luteolin, dan Mangiferin) terhadap target terapi diabetes melitus tipe 2, yaitu enzim Human Intestinal Maltase-Glucoamylase (PDB ID: 3L4W), dengan ligan kontrol klinis Miglitol.")
add_body("Kami mengucapkan terima kasih yang sebesar-besarnya kepada dosen pengampu mata kuliah Visualisasi Data Medis atas bimbingan dan arahan akademiknya, serta kepada seluruh rekan kelompok yang telah berkolaborasi secara solid. Kami menyadari bahwa studi in silico ini merupakan langkah penapisan awal yang masih memerlukan validasi laboratorium basah. Kritik dan saran konstruktif sangat kami harapkan untuk penyempurnaan riset selanjutnya.")
add_body("Surabaya, Oktober 2026\nTim Penyusun Kelompok 3", italic_suffix="")

add_h1("DAFTAR ISI")
add_body(
    "BAB I: PENDAHULUAN ............................................................................................ 1\n"
    "  1.1 Latar Belakang ................................................................................................... 1\n"
    "  1.2 Alasan Pemilihan Tiga Senyawa Kandidat ........................................................... 1\n"
    "  1.3 Pertanyaan Project .............................................................................................. 2\n"
    "  1.4 Hipotesis ............................................................................................................ 2\n"
    "  1.5 Tujuan Project .................................................................................................... 2\n"
    "BAB 2: METODE ...................................................................................................... 3\n"
    "  2.1 Identitas Protein Target ..................................................................................... 3\n"
    "  2.2 Sumber Struktur Protein dan Ligan ..................................................................... 3\n"
    "  2.3 Identitas Ligan .................................................................................................... 3\n"
    "  2.4 Preparasi Protein ................................................................................................ 3\n"
    "  2.5 Preparasi Ligan ................................................................................................... 4\n"
    "  2.6 Penentuan Binding Site dan Grid Box .................................................................. 4\n"
    "  2.7 Parameter Docking dan Prosedur Validasi (Redocking) ........................................ 4\n"
    "  2.8 Perangkat Lunak ................................................................................................. 4\n"
    "  2.9 Skrining Drug-Likeness dan Farmakokinetik ........................................................ 5\n"
    "BAB 3: HASIL .......................................................................................................... 6\n"
    "  3.1 Hasil Preparasi Ligan Kandidat ........................................................................... 6\n"
    "  3.2 Hasil Validasi / Redocking ................................................................................. 6\n"
    "  3.3 Hasil Molecular Docking Ligan Native dan Tiga Kandidat .................................... 7\n"
    "  3.4 Visualisasi Interaksi 2D dan 3D Pose Terbaik ...................................................... 8\n"
    "  3.5 Key Residues dan Matriks Interaksi Atomik ....................................................... 10\n"
    "  3.6 Ringkasan Drug-Likeness Oral (Lipinski Rule of 5) ............................................. 11\n"
    "BAB 4: PEMBAHASAN (MENJAWAB 8 PERTANYAAN WAJIB) ......................... 12\n"
    "  4.1 Perbandingan Binding Affinity dan Efisiensi Ligan (Pertanyaan 1) .................... 12\n"
    "  4.2 Perbandingan Lokasi Binding Pocket dan Pose Spasial (Pertanyaan 2) ................. 12\n"
    "  4.3 Residu dan Jenis Interaksi Dibandingkan Ligan Native (Pertanyaan 3 & 4) ......... 13\n"
    "  4.4 Evaluasi Skor Energi vs Efikasi Biologis (Pertanyaan 5) ..................................... 13\n"
    "  4.5 Penentuan Kandidat Paling Layak Diprioritaskan (Pertanyaan 6) ........................ 14\n"
    "  4.6 Hubungan Hasil dengan Literatur dan Rasionalitas Target (Pertanyaan 7) .......... 14\n"
    "  4.7 Keterbatasan Metode Molecular Docking dan Interpretasi (Pertanyaan 8) .......... 15\n"
    "BAB 5: KESIMPULAN ............................................................................................ 17\n"
    "DAFTAR PUSTAKA ................................................................................................. 18\n"
    "LAMPIRAN-LAMPIRAN .......................................................................................... 20"
)

doc.add_page_break()

# =========================================================================
# BAB I: PENDAHULUAN
# =========================================================================
add_h1("BAB I: PENDAHULUAN")

add_h2("1.1 Latar Belakang")
add_body("Diabetes melitus merupakan salah satu beban kesehatan terbesar di Indonesia. Data International Diabetes Federation (IDF, 2025) melaporkan bahwa sekitar 20,4 juta orang dewasa di Indonesia hidup dengan diabetes pada tahun 2024, menempatkan Indonesia pada peringkat kelima tertinggi di dunia. Dari jumlah tersebut, sekitar 73,2% kasus belum terdiagnosis klinis, memperbesar risiko komplikasi makrovaskular dan mikrovaskular.")
add_body("Salah satu pendekatan terapeutik utama dalam mengendalikan lonjakan glukosa darah postprandial (postprandial hyperglycemia) adalah penghambatan enzim alfa-glukosidase di usus halus. Enzim Human Intestinal Maltase-Glucoamylase (NtMGAM) mengatalisis tahap akhir hidrolisis oligosakarida menjadi glukosa yang siap diserap enterosit. Obat sintetis inhibitor alfa-glukosidase standar seperti akarbosa dan miglitol telah terbukti efektif secara klinis. Namun, penggunaannya sering dibatasi oleh efek samping gastrointestinal yang nyata, seperti flatulensi parah, kram abdominal, dan diare osmotik akibat fermentasi sisa karbohidrat oleh mikrobiota kolon. Kondisi ini mendasari urgensi penapisan senyawa bahan alam (fitofarmaka), khususnya golongan flavonoid dan polifenol, yang berpotensi memiliki afinitas pengikatan kompetitif terhadap enzim target dengan tolerabilitas saluran cerna yang lebih baik.")

add_h2("1.2 Alasan Pemilihan Tiga Senyawa Kandidat")
add_body("Pemilihan tiga ligan uji fitokimia didasarkan pada variasi hubungan struktur dan aktivitas (Structure-Activity Relationship / SAR) serta dukungan bukti empiris in vitro dari literatur peer-reviewed:")
add_bullet("Kandidat 1: Quercetin (CID 5280343) — Merupakan flavonol aglikon polihidroksi standar dengan 5 gugus hidroksil, termasuk substitusi 3-OH pada cincin C. Liu et al. (2024) melaporkan bahwa kuersetin memiliki IC50 in vitro sebesar 7,97 ± 0,89 µM, lebih kuat 15 kali dibandingkan akarbosa (124,22 µM) pada uji hidrolisis substrat analitik. Di sisi lain, Barber et al. (2021) melaporkan variasi aktivitas pada alfa-glukosidase usus manusia di mana kuersetin terukur lebih lemah dibanding flavonol lain. Oleh karena itu, kuersetin diikutsertakan sebagai acuan komparasi komputasi terhadap kantong katalitik 3L4W.", bold_prefix="Quercetin: ")
add_bullet("Kandidat 2: Luteolin (CID 5280445) — Merupakan flavon aglikon planar yang memiliki struktur 90% identik dengan kuersetin namun sengaja dipilih karena tidak memiliki gugus 3-OH. Proença et al. (2017) memperoleh IC50 luteolin sebesar 46 ± 6 µM, sedangkan Yan et al. (2014) melaporkan IC50 sebesar 172 ± 5 µM (vs akarbosa 108 µM) disertai mekanisme penutupan celah aktif enzim (cleft closure). Pengujian luteolin ditujukan untuk mengevaluasi secara presisi apakah eliminasi gugus 3-OH mengurangi hambatan sterik dan meningkatkan kestabilan ikatan pada kantong aktif NtMGAM.", bold_prefix="Luteolin: ")
add_bullet("Kandidat 3: Mangiferin (CID 5281647) — Merupakan C-glukosilxanton alami yang memiliki cincin tetrasiklik aromatik kaku dan gugus gula C-glukosil. Bezerra et al. (2019) melaporkan inhibisi enzim alfa-glukosidase hingga 90,42% dengan IC50 0,283 mg/mL (≈ 670 µM), sementara Suryawanshi et al. (2017) mencatat IC50 11,72 mg/mL. Mangiferin diuji untuk mengevaluasi apakah peniruan struktur substrat disakarida alami mampu memberikan afinitas lokal di rongga usus tanpa absorpsi sistemik berlebih.", bold_prefix="Mangiferin: ")
add_body("Catatan Metodologis: Nilai numerik IC50 antarjurnal di atas bervariasi karena perbedaan kondisi pengujian analitik, konsentrasi substrat pNPG, dan sumber enzim (sebagian memakai enzim ragi). Namun, seluruh literatur secara konsisten mengonfirmasi bioaktivitas inhibisi nyata dari ketiga senyawa tersebut.", italic_suffix="")

add_h2("1.3 Pertanyaan Project")
add_body("Penelitian ini diarahkan untuk menjawab delapan pertanyaan pokok penugasan:")
add_bullet("Kandidat mana yang menunjukkan binding affinity paling baik?")
add_bullet("Apakah kandidat berada pada binding pocket yang sama dengan ligan native?")
add_bullet("Apakah terdapat residu penting yang sama antara kandidat dan ligan native?")
add_bullet("Bagaimana perbandingan jenis interaksi masing-masing kandidat terhadap kontrol?")
add_bullet("Apakah kandidat dengan binding affinity paling negatif otomatis menjadi kandidat terbaik?")
add_bullet("Kandidat mana yang paling layak diprioritaskan berdasarkan keseluruhan hasil?")
add_bullet("Apakah hasil docking mendukung alasan awal pemilihan kandidat dari literatur?")
add_bullet("Apa keterbatasan project molecular docking yang dilakukan?")

add_h2("1.4 Hipotesis")
add_body("Ketiga senyawa bahan alam (Quercetin, Luteolin, dan Mangiferin) dihipotesiskan mampu menempati kantong pengikatan aktif enzim NtMGAM (PDB ID: 3L4W) dan membentuk interaksi ikatan hidrogen maupun kontak hidrofobik dengan residu-residu jangkar katalitik yang sebanding dengan ligan kontrol native Miglitol, dengan Luteolin diproyeksikan memiliki konformasi planar paling stabil tanpa hambatan sterik serta memenuhi aturan Lipinski.")

add_h2("1.5 Tujuan Project")
add_body("Tujuan penelitian ini adalah melakukan simulasi molecular docking terarah (targeted docking), memvisualisasikan interaksi spasial 2D dan 3D beresolusi tinggi, mengidentifikasi residu asam amino kunci pada sisi aktif, mengomparasi afinitas termodinamika terhadap kontrol klinis miglitol, serta menetapkan kandidat prioritas (lead compound) berdasarkan integrasi data komputasi, kepatuhan drug-likeness oral, dan bukti literatur.")

doc.add_page_break()

# =========================================================================
# BAB 2: METODE
# =========================================================================
add_h1("BAB 2: METODE")

add_h2("2.1 Identitas Protein Target")
add_body("Protein target yang digunakan adalah domain katalitik N-terminal Human Intestinal Maltase-Glucoamylase (NtMGAM). Struktur kristalografi sinar-X diunduh dari Protein Data Bank dengan kode PDB ID: 3L4W (Sim et al., 2010).")

add_table_title("Tabel 2.1 Identitas Makromolekul Reseptor Target")
t21_headers = ["Parameter", "Spesifikasi / Data Ilmiah"]
t21_rows = [
    ["Nama Makromolekul", "Human Intestinal Maltase-Glucoamylase (NtMGAM)"],
    ["Gen Pengkode", "MGAM (Homo sapiens)"],
    ["Fungsi Fisiologis", "Katalisis hidrolisis ikatan alfa-(1,4)-glukosida karbohidrat di enterosit usus"],
    ["PDB ID", "3L4W"],
    ["Metode Penentuan Struktur", "Difraksi Sinar-X (X-Ray Diffraction)"],
    ["Resolusi Kristalografi", "2,15 Å (memenuhi batas resolusi tinggi untuk docking atomik presisi)"],
    ["Ligan Ko-Kristal Native", "Miglitol (kode ligan PDB: MIG; 2-(hidroksietil)-1-deoksinojirimisin)"],
    ["Sumber Struktur", "RCSB Protein Data Bank (https://www.rcsb.org/structure/3L4W)"],
    ["Rasionalitas Pemilihan", "Mewakili target fisiologis manusia secara langsung (bukan enzim ragi/bakteri), memiliki resolusi 2,15 Å dengan ligan ko-kristal native pada binding pocket yang terdefinisi jelas, serta bebas dari missing residues pada situs aktif."]
]
format_custom_table(t21_headers, t21_rows, [2.2, 4.3])

add_h2("2.2 Sumber Struktur Protein dan Ligan")
add_body("Struktur makromolekul target diunduh dalam format 3L4W.pdb dari RCSB PDB. Struktur 3D ligan kontrol native Miglitol diekstraksi langsung dari kompleks kristal tersebut, sedangkan struktur 3D tiga kandidat fitokimia diunduh dari basis data NCBI PubChem dalam format SDF (3D Conformer).")

add_h2("2.3 Identitas Ligan")
add_table_title("Tabel 2.2 Identitas Kimia Ligan Kontrol dan Kandidat")
t22_headers = ["Senyawa", "Peran", "PubChem CID", "Formula Molekul", "Bobot Molekul (g/mol)", "Kelas Kimiawi"]
t22_rows = [
    ["Miglitol", "Kontrol Native", "441314", "C8H17NO5", "207,22", "Iminosugar (Derivat deoksinojirimisin)"],
    ["Quercetin", "Kandidat 1", "5280343", "C15H10O7", "302,24", "Flavonol (Flavonoid polihidroksi 3-OH)"],
    ["Luteolin", "Kandidat 2", "5280445", "C15H10O6", "286,24", "Flavon (Flavonoid planar tanpa 3-OH)"],
    ["Mangiferin", "Kandidat 3", "5281647", "C19H18O11", "422,34", "Xanthonoid (C-Glukosilxanton)"]
]
format_custom_table(t22_headers, t22_rows, [1.1, 1.1, 1.0, 1.0, 1.1, 1.2])

add_h2("2.4 Preparasi Protein")
add_body("Preparasi struktur reseptor dilakukan menggunakan BIOVIA Discovery Studio Visualizer. Struktur 3L4W dibersihkan dari molekul pelarut air (HOH), ion sulfat (SO4), gliserol (GOL), dan komponen glikosilasi N-asetilglukosamin (NAG). Tiga puluh tujuh atom dengan konformasi alternatif B (altloc B) dihapus untuk menyisakan konformasi tunggal A. Ligan ko-kristal native Miglitol dipisahkan dan disimpan sebagai ligan_asli.pdb. Reseptor murni dikonversi ke format PDBQT menggunakan AutoDockTools/PyRx dengan menambahkan seluruh atom hidrogen polar eksplisit dan menetapkan muatan parsial atomik Kollman.")

add_h2("2.5 Preparasi Ligan")
add_body("Ligan kandidat dari format SDF PubChem diimpor ke PyRx (OpenBabel). Dilakukan optimasi geometri dan minimisasi energi menggunakan medan gaya Universal Force Field (UFF) dengan algoritma Conjugate Gradient hingga konvergensi gradien tercapai (< 0,1 kcal/(mol·Å)). Molekul kemudian dikonversi ke format PDBQT dengan penambahan muatan parsial Gasteiger, penggabungan hidrogen non-polar, dan penentuan ikatan terotasikan (rotatable bonds). Jumlah torsional DOF yang diperoleh adalah 6 untuk Quercetin, 5 untuk Luteolin, dan 10 untuk Mangiferin.")

add_h2("2.6 Penentuan Binding Site dan Grid Box")
add_body("Penentuan ruang penambatan (Grid Box) dipusatkan secara terarah (targeted grid) pada koordinat spasial pengikatan ligan native Miglitol pada kantong katalitik NtMGAM.")

add_table_title("Tabel 2.3 Spesifikasi Parameter Grid Box AutoDock Vina")
t23_headers = ["Parameter Grid Box", "Nilai Koordinat Spasial", "Justifikasi Metodologis"]
t23_rows = [
    ["Center X / Y / Z", "45,49 / 91,76 / 34,51", "Titik pusat massa geometris ligan ko-kristal Miglitol kristalografi."],
    ["Dimension Size X / Y / Z", "25 × 25 × 25 Å", "Mencakup seluruh jejak ligan native (bentang ~12 Å) dengan margin kelonggaran konkret ± 6,5 Å ke setiap arah koordinat, memberikan ruang eksplorasi konformasi yang cukup untuk kandidat polifenol berdimensi lebih besar tanpa keluar dari rongga kantong aktif."],
    ["Exhaustiveness", "8", "Tingkat ketelitian pencarian konformasi standar AutoDock Vina."],
    ["Number of Modes", "9", "Jumlah pose konformasi yang dihasilkan per penambatan."]
]
format_custom_table(t23_headers, t23_rows, [1.8, 1.8, 2.9])

add_h2("2.7 Parameter Docking dan Prosedur Validasi (Redocking)")
add_body("Simulasi penambatan molekuler dijalankan menggunakan AutoDock Vina (Trott & Olson, 2010) yang terintegrasi pada antarmuka PyRx versi 0.8. Validasi protokol komputasi dilakukan melalui prosedur redocking: ligan native Miglitol ditambatkan kembali ke dalam struktur reseptor 3L4W bersih pada koordinat grid box yang telah dikunci. Nilai deviasi posisi spasial (Root Mean Square Deviation / RMSD) antara pose redocking terbaik (Mode 1) terhadap pose kristalografi sinar-X asli dihitung secara in-place (tanpa superposisi ulang) menggunakan kalkulasi pemetaan graf topologi kimia pada 14 atom berat. Batas keberterimaan validitas komputasi standar internasional ditetapkan pada RMSD ≤ 2,0 Å.")

add_h2("2.8 Perangkat Lunak")
add_table_title("Tabel 2.4 Perangkat Lunak dan Basis Data Komputasi")
t24_headers = ["Perangkat Lunak / Web Server", "Versi / Pengembang", "Fungsi dan Peran dalam Proyek"]
t24_rows = [
    ["RCSB Protein Data Bank", "Web Server (rcsb.org)", "Pengunduhan berkas struktur makromolekul kristal 3L4W.pdb."],
    ["NCBI PubChem", "Web Server (nih.gov)", "Pengunduhan berkas 3D konformer struktur kimia ligan kandidat."],
    ["BIOVIA Discovery Studio Visualizer", "v21.1 / Dassault Systèmes", "Preparasi pembersihan reseptor protein dan visualisasi diagram interaksi 2D atomik."],
    ["PyRx Virtual Screening Tool", "v0.8 / Open Source", "Minimasi energi medan gaya UFF, konversi format PDBQT, dan eksekusi Vina Wizard."],
    ["AutoDock Vina", "v1.2.0 / The Scripps Research Inst.", "Algoritma pencarian konformasi empiris dan kalkulasi energi bebas penambatan (ΔG)."],
    ["PyMOL Molecular Graphics System", "v2.5 / Schrödinger, LLC", "Kalkulasi RMSD redocking in-place dan visualisasi pose 3D kompleks pita reseptor."],
    ["ADMETlab 2.0", "Web Server (scbdd.com)", "Skrining profil fisikokimia, drug-likeness Lipinski, dan farmakokinetik oral."]
]
format_custom_table(t24_headers, t24_rows, [2.0, 1.8, 2.7])

add_h2("2.9 Skrining Drug-Likeness dan Farmakokinetik")
add_body("Skrining komputasi farmakokinetik oral dan drug-likeness dilakukan menggunakan server web ADMETlab 2.0 untuk mengevaluasi kepatuhan terhadap Aturan Lipinski (Lipinski Rule of 5: Bobot Molekul ≤ 500 g/mol, LogP ≤ 5, Donor Ikatan Hidrogen ≤ 5, Akseptor Ikatan Hidrogen ≤ 10), permeabilitas membran Caco-2, absorpsi intestinal (HIA), klirens, penghambatan enzim sitokrom P450, serta profil toksisitas. Kriteria interpretasi dan matriks data ADMET lengkap dipindahkan ke Lampiran 5 agar batang tubuh laporan tetap fokus pada visualisasi interaksi docking.")

doc.add_page_break()

# =========================================================================
# BAB 3: HASIL
# =========================================================================
add_h1("BAB 3: HASIL")

add_h2("3.1 Hasil Preparasi Ligan Kandidat")
add_body("Seluruh ligan kandidat berhasil dioptimasi geometrinya melalui minimisasi energi medan gaya UFF dan dikonversi ke format PDBQT dengan penambahan muatan parsial Gasteiger yang valid.")

add_table_title("Tabel 3.1 Parameter Struktur Ligan Setelah Minimisasi Energi dan Konversi PDBQT")
t31_headers = ["Ligan", "Peran", "CID PubChem", "Energi UFF (kkal/mol)", "Torsional DOF (PyRx)", "Rotatable Bonds (nRot)"]
t31_rows = [
    ["Miglitol", "Kontrol Native", "441314", "Ekstraksi Kristal", "4", "1"],
    ["Quercetin", "Kandidat 1", "5280343", "380,43", "6", "1"],
    ["Luteolin", "Kandidat 2", "5280445", "242,10", "5", "1"],
    ["Mangiferin", "Kandidat 3", "5281647", "412,79", "10", "2"]
]
format_custom_table(t31_headers, t31_rows, [1.2, 1.1, 1.0, 1.1, 1.1, 1.0])

add_h2("3.2 Hasil Validasi / Redocking")
add_body("Simulasi redocking ligan native Miglitol ke dalam makromolekul target NtMGAM menghasilkan konformasi Mode 1 dengan afinitas -5,5 kkal/mol. Kalkulasi RMSD in-place pada seluruh 14 atom berat menghasilkan nilai 1,892 Å, yang memenuhi batas keberterimaan standar komputasi (RMSD ≤ 2,0 Å). Deviasi posisi pada cincin inti piperidin hanya sebesar 1,16 Å, dengan pergeseran pusat massa pose sebesar 0,59 Å. Deviasi terbesar terjadi pada atom oksigen gugus hidroksietil (3,11 Å) yang berada pada rantai fleksibel. Pose redocking berhasil mempertahankan 12 dari 13 residu kontak pose kristal (92%) pada jarak kontak ≤ 4,0 Å, mengonfirmasi bahwa parameter grid box dan fungsi skor Vina valid dan handal.")

add_table_title("Tabel 3.2 Parameter Kuantitatif Validasi Redocking Miglitol pada 3L4W")
t32_headers = ["Parameter Validasi Komputasi", "Nilai / Hasil Kuantitatif", "Kriteria Ambang Batas", "Status Evaluasi"]
t32_rows = [
    ["Binding Affinity Pose Mode 1", "-5,5 kkal/mol", "Reproduksi skor energi kristal", "Sesuai"],
    ["RMSD 14 Atom Berat (In-Place)", "1,892 Å", "≤ 2,0 Å", "Valid (Terpenuhi)"],
    ["RMSD Inti Cincin Piperidin (6 atom)", "1,16 Å", "≤ 2,0 Å", "Sangat Presisi"],
    ["Pergeseran Pusat Massa Pose", "0,59 Å", "< 1,0 Å", "Akurat"],
    ["Preservasi Residu Kontak (≤ 4,0 Å)", "12 dari 13 residu (92%)", "> 80%", "Valid"],
    ["Preservasi Residu Ikatan Hidrogen", "5 dari 5 residu kristal utama", "Konsisten", "Terpenuhi"]
]
format_custom_table(t32_headers, t32_rows, [2.3, 1.5, 1.4, 1.3], highlight_row_idx=1, highlight_hex="ECFDF5")

overlay_img = os.path.join(EXTRACTED_IMG_DIR, "img_6.png")
add_image_with_caption(
    overlay_img,
    "Gambar 3.1 Overlay pose native kristalografi (warna biru) dan pose redocking hasil AutoDock Vina (warna hijau) pada kantong aktif NtMGAM (PDB ID: 3L4W), menunjukkan superposisi cincin inti piperidin yang presisi (RMSD inti 1,16 Å; RMSD total 1,892 Å).",
    width_inches=5.2
)

add_h2("3.3 Hasil Molecular Docking Ligan Native dan Tiga Kandidat")
add_body("Simulasi molecular docking terhadap tiga kandidat fitokimia menghasilkan afinitas termodinamika yang lebih negatif dibandingkan kontrol native Miglitol (-5,5 kkal/mol). Luteolin mencatatkan energi bebas pengikatan paling negatif (-7,9 kkal/mol), diikuti oleh Quercetin (-7,1 kkal/mol) dan Mangiferin (-7,0 kkal/mol).")

add_table_title("Tabel 3.3 Ringkasan Hasil Molecular Docking Ligan Native dan Tiga Kandidat (Tabel Resmi Bagian 7 Penugasan)")
t33_headers = ["Ligan", "Binding Affinity (kkal/mol)", "Ikatan Hidrogen (Residu & Jarak Å)", "Residu Penting Terlibat", "Interaksi Lainnya (Hidrofobik / Aromatik / Bump)", "Kemiripan Kontak thd Kontrol"]
t33_rows = [
    [
        "Miglitol\n(Kontrol Native)",
        "-5,5",
        "7 ikatan: Asp327 (2,70), Asp542 (2,70), His600 (2,99), Asp203 (3,01), Trp406 (3,05), Arg526 (3,09), Asp443 (3,20)",
        "Asp327, Asp443, Asp542, His600, Arg526, Asp203, Trp406",
        "Kontak vdW/hidrofobik: Ile328, Ile364, Tyr299, Met444, Trp539, Phe575, Trp441; Unfavorable bump: Arg526 (3,09 Å)",
        "100% (Baseline 14 Residu Kontak Acuan; 7 Residu H-Bond)"
    ],
    [
        "Quercetin\n(Kandidat 1)",
        "-7,1",
        "4 ikatan: Asp327 (2,76), Tyr605 (2,82), Asp542 (3,13), Asp443 (3,21)",
        "Asp327, Asp542, Asp443, Tyr605",
        "Hidrofobik/aromatik: Tyr299 (3,44 Å), Phe575 (3,49 Å), Trp406 (3,53 Å), Ile328 (3,90 Å); Kontak lain: Asp203, Ile364, Trp441, Met444, Arg526, His600",
        "Residu kontak: 13 dari 14 (92,9%); Residu H-bond: 3 dari 7 (Asp327, Asp542, Asp443); Tambahan: Tyr605"
    ],
    [
        "Luteolin\n(Kandidat 2)",
        "-7,9",
        "6 ikatan: Asp327 (2,66), Trp406 (3,13), Asp542 (3,14), Asp203 (3,17), Tyr299 (3,17), His600 (3,19)",
        "Asp327, Asp542, Asp203, Trp406, Tyr299, His600",
        "Hidrofobik/aromatik: Trp406 (3,26 Å), Tyr299, Phe450, Phe575; Kontak lain: Ile328, Ile364, Trp441, Met444, Trp539",
        "Residu kontak: 14 dari 14 (100%); Residu H-bond: 5 dari 7 (Asp327, Trp406, Asp542, Asp203, His600); Tambahan kontak: Phe450"
    ],
    [
        "Mangiferin\n(Kandidat 3)",
        "-7,0",
        "6 ikatan: Arg526 (2,80), Asp203 (2,86), Asp327 (2,96), His600 (2,99), Asp443 (3,23), Asp542 (3,48)",
        "Arg526, Asp203, Asp327, His600, Asp443, Asp542",
        "Hidrofobik/aromatik: Tyr299 (3,32 Å), Phe575 (3,45 Å), Trp406 (3,48 Å), Phe450 (3,79 Å); Kontak lain: Trp441, Met444, Trp539",
        "Residu kontak: 12 dari 14 (85,7%); Residu H-bond: 6 dari 7 (Arg526, Asp203, Asp327, His600, Asp443, Asp542)"
    ]
]
format_custom_table(t33_headers, t33_rows, [1.0, 0.9, 1.6, 1.0, 1.4, 0.9], highlight_row_idx=2, highlight_hex="ECFDF5")

add_h2("3.4 Visualisasi Interaksi 2D dan 3D Pose Terbaik")
add_body("Visualisasi interaksi atomik disajikan berdampingan (composite visualization): sisi kiri menampilkan pose 3D konformasi ligan di dalam pita makromolekul reseptor 3L4W (PyMOL), dan sisi kanan menampilkan diagram interaksi 2D beresolusi tinggi dengan penandaan residu spesifik (BIOVIA Discovery Studio Visualizer).")

comp_mig = os.path.join(ORANG6_DIR, "visualisasi_kompleks_miglitol.png")
add_image_with_caption(
    comp_mig,
    "Gambar 3.2 Visualisasi Pose Penambatan 3D (PyMOL) dan Diagram Interaksi 2D (Discovery Studio) Ligan Kontrol Miglitol pada Sisi Aktif NtMGAM (PDB ID: 3L4W). Garis hijau putus-putus menunjukkan ikatan hidrogen konvensional; garis merah/oranye menunjukkan tolakan elektrostatik kation-kation (unfavorable bump) dengan Arg526 (3,09 Å).",
    width_inches=6.0
)

comp_qrc = os.path.join(ORANG6_DIR, "visualisasi_kompleks_quercetin.png")
add_image_with_caption(
    comp_qrc,
    "Gambar 3.3 Visualisasi Pose Penambatan 3D (PyMOL) dan Diagram Interaksi 2D (Discovery Studio) Kandidat 1 Quercetin pada NtMGAM (PDB ID: 3L4W). Menampilkan 4 ikatan hidrogen konvensional serta stabilisasi cincin aromatik melalui kontak hidrofobik pi-pi stacking (merah muda) pada Tyr299 dan Phe575.",
    width_inches=6.0
)

comp_lut = os.path.join(ORANG6_DIR, "visualisasi_kompleks_luteolin.png")
add_image_with_caption(
    comp_lut,
    "Gambar 3.4 Visualisasi Pose Penambatan 3D (PyMOL) dan Diagram Interaksi 2D (Discovery Studio) Kandidat 2 Luteolin pada NtMGAM (PDB ID: 3L4W). Kerangka flavon planar mengunci residu katalitik dan kunci (Asp327, Asp542, Asp203) melalui 6 ikatan hidrogen rapat serta kontak aromatik pada Trp406, Phe450, dan Phe575.",
    width_inches=6.0
)

comp_man = os.path.join(ORANG6_DIR, "visualisasi_kompleks_mangiferin.png")
add_image_with_caption(
    comp_man,
    "Gambar 3.5 Visualisasi Pose Penambatan 3D (PyMOL) dan Diagram Interaksi 2D (Discovery Studio) Kandidat 3 Mangiferin pada NtMGAM (PDB ID: 3L4W). Gugus C-glukosil yang ruah membentuk ikatan hidrogen dengan Arg526 dan Asp203 namun membatasi penetrasi cincin tetrasiklik xanton ke koridor dalam.",
    width_inches=6.0
)

add_h2("3.5 Key Residues dan Matriks Interaksi Atomik")
add_body("Definisi Denominator Acuan H-Bond Native: Pada pose redocking ligan native Miglitol, teridentifikasi 7 residu mitra ikatan hidrogen: Asp327 (2,70 Å), Asp542 (2,70 Å), His600 (2,99 Å), Asp203 (3,01 Å), Trp406 (3,05 Å), Arg526 (3,09 Å), dan Asp443 (3,20 Å). Ketujuh residu ini ditetapkan sebagai denominator acuan (baseline 'dari 7') untuk menghitung kemiripan ikatan hidrogen kandidat secara konsisten.", bold_prefix="Penetapan Baseline: ")

add_table_title("Tabel 3.4 Jarak Ikatan Hidrogen Antara Pose Kristalografi dan Pose Redocking Miglitol")
t34_headers = ["Residu Asam Amino", "Pose Kristalografi Sinar-X (Å)", "Pose Redocking AutoDock Vina (Å)", "Peran Fungsional"]
t34_rows = [
    ["Asp327", "2,54", "2,70", "Residu karboksilat kantong katalitik inti"],
    ["Asp443", "2,76", "3,20", "Residu katalitik NtMGAM"],
    ["Asp542", "2,63", "2,70", "Residu katalitik nukleofil NtMGAM"],
    ["His600", "2,85", "2,99", "Residu polar penstabil ligan"],
    ["Arg526", "3,00", "3,09", "Residu kationik (terdapat repulsive bump pada redocking)"],
    ["Trp406", "3,58 (kontak)", "3,05", "Dinding hidrofobik bibir celah"],
    ["Asp203", "> 4,5", "3,01", "Residu penstabil keadaan transisi"]
]
format_custom_table(t34_headers, t34_rows, [1.8, 1.5, 1.5, 2.0])

add_table_title("Tabel 3.5 Matriks Residu Kantong Aktif yang Dikontak Tiap Ligan (H = Ikatan Hidrogen ≤ 3,5 Å; k = Kontak Spasial ≤ 4,5 Å; – = Tidak Berinteraksi)")
t35_headers = ["Residu Kantong", "Miglitol (Redocking)", "Quercetin", "Luteolin", "Mangiferin"]
t35_rows = [
    ["Asp327", "H", "H", "H", "H"],
    ["Asp443", "H", "H", "–", "H"],
    ["Asp542", "H", "H", "H", "H"],
    ["His600", "H", "k", "H", "H"],
    ["Arg526", "H", "k", "–", "H"],
    ["Asp203", "H", "k", "H", "H"],
    ["Trp406", "H", "k", "H", "k"],
    ["Tyr299", "k", "k", "H", "k"],
    ["Phe575", "k", "k", "k", "k"],
    ["Phe450", "–", "–", "k", "k"],
    ["Ile328", "k", "k", "k", "–"],
    ["Ile364", "k", "k", "k", "–"],
    ["Met444", "k", "k", "k", "k"],
    ["Trp441", "k", "k", "k", "k"],
    ["Trp539", "k", "–", "k", "k"],
    ["Tyr605", "–", "H", "–", "–"]
]
format_custom_table(t35_headers, t35_rows, [1.6, 1.3, 1.3, 1.3, 1.3], highlight_row_idx=2, highlight_hex="ECFDF5")

add_h2("3.6 Ringkasan Drug-Likeness Oral (Lipinski Rule of 5)")
add_body("Berdasarkan evaluasi fisikokimia menggunakan ADMETlab 2.0, Quercetin dan Luteolin memenuhi seluruh aturan Lipinski (0 pelanggaran), menjadikannya kandidat yang layak dikembangkan sebagai formulasi oral. Sebaliknya, Mangiferin melanggar dua aturan (bobot molekul > 500 dan donor ikatan hidrogen > 5). Data komprehensif profil ADMET (absorpsi Caco-2/HIA, CYP, klirens, dan toksisitas organ) dirangkum pada Lampiran 5.")

add_table_title("Tabel 3.6 Evaluasi Kepatuhan Aturan Lipinski (Lipinski Rule of 5) Ligan Kontrol dan Kandidat")
t36_headers = ["Senyawa", "Bobot Molekul (≤ 500 g/mol)", "LogP (≤ 5)", "HBD (≤ 5)", "HBA (≤ 10)", "Pelanggaran Lipinski", "Kelayakan Oral"]
t36_rows = [
    ["Miglitol", "207,11", "-2,02", "4", "5", "0 Pelanggaran", "Memenuhi (Lolos)"],
    ["Quercetin", "302,04", "1,63", "5", "7", "0 Pelanggaran", "Memenuhi (Lolos)"],
    ["Luteolin", "286,05", "2,28", "4", "6", "0 Pelanggaran", "Memenuhi (Lolos)"],
    ["Mangiferin", "422,08", "-1,22", "8 (Melanggar)", "11 (Melanggar)", "2 Pelanggaran", "Ditolak (Buruk)"]
]
format_custom_table(t36_headers, t36_rows, [1.2, 1.1, 0.8, 0.9, 0.9, 1.0, 1.0], highlight_row_idx=2, highlight_hex="ECFDF5")

doc.add_page_break()

# =========================================================================
# BAB 4: PEMBAHASAN (MENJAWAB 8 PERTANYAAN WAJIB)
# =========================================================================
add_h1("BAB 4: PEMBAHASAN")

add_h2("4.1 Perbandingan Binding Affinity dan Efisiensi Ligan (Pertanyaan 1)")
add_body("Hasil penambatan molekuler menunjukkan bahwa Luteolin memiliki prediksi afinitas penambatan terkuat dengan nilai energi bebas paling negatif (-7,9 kkal/mol), diikuti oleh Quercetin (-7,1 kkal/mol) dan Mangiferin (-7,0 kkal/mol). Selisih skor antara Quercetin dan Mangiferin hanya sebesar 0,1 kkal/mol, sehingga dalam batas ketelitian fungsi skor empiris Vina (standar deviasi ~0,5–1,0 kkal/mol), afinitas keduanya dianggap setara. Ketiga kandidat polifenol menunjukkan afinitas 1,5 hingga 2,4 kkal/mol lebih negatif dibandingkan ligan native Miglitol (-5,5 kkal/mol).")
add_body("Namun, fungsi skor AutoDock Vina memiliki bias inherent yang cenderung memberikan nilai lebih negatif pada molekul berukuran besar akibat akumulasi kontak dispersi van der Waals. Oleh karena itu, afinitas dinormalkan terhadap jumlah atom berat (non-hidrogen) sebagai Efisiensi Ligan (Ligand Efficiency / LE). Sesuai konvensi standar penambatan obat, efisiensi ligan dinyatakan dalam nilai positif (|ΔG| dibagi jumlah atom berat N_heavy, dalam kkal/mol per atom).")

add_table_title("Tabel 4.1 Perbandingan Afinitas dan Efisiensi Ligan")
t41_headers = ["Senyawa", "Binding Affinity (kkal/mol)", "Selisih vs Miglitol (kkal/mol)", "Jumlah Atom Berat (N)", "Efisiensi Ligan (kkal/mol per atom)"]
t41_rows = [
    ["Miglitol (Native)", "-5,5", "Baseline", "14", "0,39"],
    ["Luteolin", "-7,9", "-2,4", "21", "0,38"],
    ["Quercetin", "-7,1", "-1,6", "22", "0,32"],
    ["Mangiferin", "-7,0", "-1,5", "30", "0,23"]
]
format_custom_table(t41_headers, t41_rows, [1.5, 1.4, 1.3, 1.1, 1.5], highlight_row_idx=1, highlight_hex="ECFDF5")
add_body("Setelah dinormalkan, Luteolin mencatatkan efisiensi ligan 0,38 kkal/mol per atom, hampir setara dengan ligan native Miglitol (0,39). Sebaliknya, efisiensi ligan Quercetin (0,32) dan terutama Mangiferin (0,23) turun drastis. Hal ini membuktikan bahwa skor negatif Mangiferin terutama disumbang oleh ukuran molekulnya yang besar (30 atom berat), bukan oleh kerapatan energi interaksi per satuan volume.")

add_h2("4.2 Perbandingan Lokasi Binding Pocket dan Pose Spasial (Pertanyaan 2)")
add_body("Berdasarkan overlay spasial 3D, seluruh senyawa kandidat berhasil menempati kantong pengikatan aktif yang sama dengan ligan native Miglitol. Jarak titik pusat massa pose terbaik terhadap pusat massa Miglitol kristal adalah 2,9 Å untuk Luteolin, 3,9 Å untuk Quercetin, dan 5,4 Å untuk Mangiferin. Tidak ada satu pun pose kandidat yang keluar dari rongga kantong aktif NtMGAM.")
add_body("Miglitol yang berukuran kompak (BM 207 g/mol) terbenam rapat di dasar kantong katalitik. Flavonoid (Quercetin dan Luteolin) yang memiliki cincin aromatik planar menempati dasar kantong sekaligus menjulur ke celah bibir kantong hidrofobik. Luteolin menunjukkan jarak pergeseran terkecil (2,9 Å), mencerminkan orientasi yang paling menyerupai ligan native. Sebaliknya, Mangiferin memiliki jarak pergeseran terbesar (5,4 Å) karena gugus C-glukosilnya yang ruah memaksanya bergeser ke mulut celah luar.")

add_h2("4.3 Residu dan Jenis Interaksi Dibandingkan Ligan Native (Pertanyaan 3 & 4)")
add_body("Miglitol mengontak 14 residu asam amino pada jarak kontak ≤ 4,5 Å. Luteolin mengontak seluruh keempat belas residu tersebut (14 dari 14 atau 100% kemiripan kontak) ditambah satu kontak baru pada Phe450. Quercetin mengontak 13 dari 14 residu (tanpa Trp539, ditambah Tyr605), sedangkan Mangiferin mengontak 12 dari 14 residu (tanpa Ile328 dan Ile364, ditambah Phe450). Seluruh kandidat berhasil mempertahankan ikatan hidrogen dengan dua residu kunci: Asp327 dan Asp542.")
add_body("Evaluasi jenis interaksi mengungkapkan perbedaan fundamental antara kontrol sintetis dan kandidat bahan alam:")
add_bullet("Miglitol didominasi oleh ikatan hidrogen polar dengan residu karboksilat di dasar kantong. Namun, pada pose redocking teridentifikasi tolakan elektrostatik kation-kation (unfavorable donor-donor bump) antara nitrogen sekunder Miglitol yang terprotonasi (-NH2+-) dengan kation guanidinium Arg526 pada jarak 3,09 Å. Tolakan ini menjelaskan secara mekanistik mengapa skor afinitas Miglitol relatif rendah (-5,5 kkal/mol).", bold_prefix="Kontrol Miglitol: ")
add_bullet("Kandidat polifenol tidak hanya mempertahankan ikatan hidrogen kunci tetapi juga memperoleh stabilisasi energi tambahan dari kontak hidrofobik dan aromatik pi-pi stacking dengan cincin aromatik Trp406, Tyr299, dan Phe575 (jarak C-C 3,3–3,7 Å). Luteolin mengikat 5 dari 7 residu H-bond native dan membentuk jejaring kontak aromatik paling seimbang pada Trp406, Phe450, dan Phe575.", bold_prefix="Kandidat Bahan Alam: ")

add_h2("4.4 Evaluasi Skor Energi vs Efikasi Biologis (Pertanyaan 5)")
add_body("Kelompok kami menegaskan bahwa kandidat dengan binding affinity paling negatif TIDAK OTOMATIS menjadi kandidat obat terbaik. Kesimpulan tersebut keliru apabila tidak mempertimbangkan dua faktor penyeimbang:")
add_bullet("Efisiensi Ligan vs Akumulasi Massa: Skor -7,0 kkal/mol pada Mangiferin terbukti merupakan artifak dari akumulasi massa molekul besar (30 atom berat), di mana efisiensi ligannya sangat rendah (0,23 kkal/mol per atom). Sebaliknya, Luteolin memiliki efisiensi ligan tinggi (0,38) yang mencerminkan kualitas pengikatan per atom yang superior.", bold_prefix="1. Normalisasi Efisiensi: ")
add_bullet("Kelayakan Farmakokinetik Oral (Druggability): Sebuah molekul dengan afinitas komputasi tinggi di kantong enzim tidak akan memiliki efikasi biologis di tubuh apabila tidak dapat mencapai target atau menimbulkan toksisitas. Mangiferin melanggar 2 aturan Lipinski (HBD 8 dan HBA 11) serta memiliki prediksi absorpsi usus sangat buruk (HIA 0,956). Sebaliknya, Luteolin dan Quercetin memenuhi seluruh kriteria Lipinski.", bold_prefix="2. Penapisan ADMET: ")

add_h2("4.5 Penentuan Kandidat Paling Layak Diprioritaskan (Pertanyaan 6)")
add_body("Berdasarkan integrasi multikriteria—meliputi afinitas penambatan, efisiensi ligan, kedekatan spasial ke ligan native, kelengkapan kontak residu, ketiadaan hambatan sterik, dan kepatuhan aturan Lipinski—LUTEOLIN ditetapkan sebagai kandidat prioritas utama (Lead Compound).")

add_table_title("Tabel 4.2 Matriks Evaluasi Multikriteria Penentuan Kandidat Prioritas")
t42_headers = ["Kriteria Penilaian Komprehensif", "Luteolin (Kandidat 2)", "Quercetin (Kandidat 1)", "Mangiferin (Kandidat 3)", "Prioritas Relatif"]
t42_rows = [
    ["Binding Affinity (kkal/mol)", "-7,9 (Paling Kuat)", "-7,1", "-7,0", "Luteolin Unggul"],
    ["Efisiensi Ligan (kkal/mol/atom)", "0,38 (Tertinggi)", "0,32", "0,23 (Terendah)", "Luteolin Unggul"],
    ["Jarak Pusat Massa ke Miglitol (Å)", "2,9 Å (Terdekat)", "3,9 Å", "5,4 Å (Terjauh)", "Luteolin Unggul"],
    ["Preservasi Residu Kontak Native", "14 dari 14 (100%)", "13 dari 14 (92,9%)", "12 dari 14 (85,7%)", "Luteolin Unggul"],
    ["Preservasi Residu H-Bond Native", "5 dari 7", "3 dari 7", "6 dari 7", "Mangiferin Unggul"],
    ["Hambatan Sterik Koridor Kantong", "Ramping (Planar tanpa 3-OH)", "Ada desakan gugus 3-OH", "Ruah (Gugus C-glukosil kaku)", "Luteolin Unggul"],
    ["Aturan Lipinski (ADMETlab 2.0)", "Lolos (0 Pelanggaran)", "Lolos (0 Pelanggaran)", "Gagal (2 Pelanggaran: HBD 8, HBA 11)", "Luteolin & Quercetin Lolos"],
    ["Status Penetapan Akhir", "KANDIDAT PRIORITAS UTAMA (LEAD)", "Kandidat Pendamping", "Prioritas Terendah", "Luteolin Terpilih"]
]
format_custom_table(t42_headers, t42_rows, [2.0, 1.5, 1.4, 1.4, 1.2], highlight_row_idx=7, highlight_hex="ECFDF5")
add_body("Penjelasan Mekanistik: Residu katalitik NtMGAM adalah Asp443 dan Asp542 (dengan Asp542 sebagai nukleofil), dibantu oleh Asp327 dan penstabil keadaan transisi Asp203. Luteolin bersama Mangiferin berhasil mengikat residu penentu reaksi Asp327, Asp542, dan Asp203. Namun Luteolin menunjukkan superioritas spasial karena memiliki efisiensi ligan tertinggi (0,38), bebas dari benturan sterik, dan mempertahankan seluruh 14 residu kontak native (100%). Berbeda dari Quercetin yang memiliki gugus 3-OH pada cincin C yang dapat memicu desakan sterik di koridor sempit 3L4W, rangka flavon Luteolin yang planar tanpa 3-OH memungkinkannya menyelam lebih dalam ke dasar kantong.")

add_h2("4.6 Hubungan Hasil dengan Literatur dan Rasionalitas Target (Pertanyaan 7)")
add_body("Temuan komputasi ini mendukung rasionalitas awal pemilihan target dan kandidat. Struktur 3L4W berasal dari studi kristalografi NtMGAM manusia bersama inhibitor bahan alam Salacia reticulata (Sim et al., 2010), membuktikan bahwa kantong aktif ini secara alami dapat dihambat oleh senyawa fitokimia.")
add_body("Perbandingan Literatur In Vitro dan Catatan Kritis: Hasil docking Luteolin (-7,9 kkal/mol) dan Quercetin (-7,1 kkal/mol) sejalan dengan aktivitas in vitro yang dilaporkan Liu et al. (2024) (IC50 kuersetin 7,97 µM) dan Proença et al. (2017) (IC50 luteolin 46 µM). Namun, kelompok kami mencatat temuan kritis Barber et al. (2021) bahwa pada pengujian alfa-glukosidase usus manusia in vitro, kuersetin justru menunjukkan efikasi paling lemah di antara flavonol yang diuji. Ketidakcocokan antara skor docking in silico yang tinggi (-7,1 kkal/mol) dengan kelemahan in vitro pada studi Barber et al. tersebut menegaskan bahwa penambatan berbasis reseptor kaku (rigid docking) tidak memodelkan solvasi dinamis air dan fleksibilitas enzim di saluran cerna.")
add_body("Rasionalitas Kontrol Miglitol vs Akarbosa: Pemilihan Miglitol sebagai kontrol didasarkan pada dua pertimbangan mutlak: (1) Miglitol adalah ligan ko-kristal native pada berkas 3L4W yang diperlukan untuk validasi redocking (RMSD 1,892 Å); (2) Miglitol adalah molekul kecil (BM 207 g/mol) penghuni sub-situs -1, sebanding secara adil (apple-to-apple) dengan molekul flavonoid (BM 286–302 g/mol), sedangkan akarbosa adalah tetrasakarida besar (BM 646 g/mol) yang melanggar Lipinski dan menutupi banyak sub-situs sekaligus.")

add_h2("4.7 Keterbatasan Metode Molecular Docking dan Interpretasi (Pertanyaan 8)")
add_body("Hasil penelitian ini harus diinterpretasikan secara hati-hati dengan mempertimbangkan beberapa keterbatasan metodologis yang diakui secara jujur:")
add_bullet("Bias Fungsi Skor Terhadap Ukuran: Fungsi skor empiris Vina mengestimasi energi bebas dari suku sterik, hidrogen, dan hidrofobik yang cenderung menguntungkan molekul besar. Hal ini terlihat pada Mangiferin yang memperoleh skor tinggi meski efisiensi ligannya rendah.", bold_prefix="1. Bias Ukuran: ")
add_bullet("Asumsi Reseptor Rigid dan Ketiadaan Pelarut: Reseptor diperlakukan kaku selama docking, tanpa memperhitungkan molekul air kristal pelarut maupun fleksibilitas rantai samping protein yang penting dalam pengikatan fisiologis.", bold_prefix="2. Reseptor Kaku: ")
add_bullet("Protokol Single-Run dan Ketiadaan Replikasi: Penambatan dilakukan satu kali per ligan dengan exhaustiveness 8. Oleh karena itu, selisih energi yang sangat kecil antara Quercetin (-7,1) dan Mangiferin (-7,0) dianggap setara, sedangkan keunggulan Luteolin (-7,9) memerlukan replikasi statistik lebih lanjut.", bold_prefix="3. Replikasi Terbatas: ")
add_bullet("Kedekatan Nilai RMSD Redocking: Nilai RMSD 1,892 Å berada dekat dengan batas atas keberterimaan (2,0 Å), terutama akibat fleksibilitas gugus hidroksietil ligan native.", bold_prefix="4. Batas RMSD: ")
add_bullet("Targeted Docking vs Fenomena Cleft Closure: Literatur kinetika (Yan et al., 2014) melaporkan bahwa Luteolin bekerja melalui mekanisme non-kompetitif reversibel yang memicu penutupan celah aktif (cleft closure) dan mereduksi fraksi alfa-heliks protein. Sementara itu, simulasi kami melakukan targeted docking terpusat pada kantong ortosterik. Karakter non-kompetitif tersebut mengindikasikan adanya potensi interaksi alosterik di bibir celah yang memerlukan konfirmasi lanjutan melalui blind docking dan simulasi dinamika molekuler (Molecular Dynamics / MD).", bold_prefix="5. Mekanisme Kinetika: ")
add_bullet("Variasi Data In Vitro dan Prediksi In Silico ADMET: Nilai IC50 literatur tidak dapat diperbandingkan langsung secara numerik antarjurnal, dan data farmakokinetik hanya merupakan prediksi komputasional server ADMETlab 2.0 yang memerlukan validasi pengujian hayati.", bold_prefix="6. Validasi Eksperimental: ")

doc.add_page_break()

# =========================================================================
# BAB 5: KESIMPULAN
# =========================================================================
add_h1("BAB 5: KESIMPULAN")
add_body("Berdasarkan rangkaian simulasi penambatan molekuler (molecular docking), analisis visualisasi spasial, dan evaluasi farmakokinetik in silico terhadap enzim Human Intestinal Maltase-Glucoamylase (PDB ID: 3L4W), dapat ditarik kesimpulan komprehensif sebagai berikut:")
add_bullet("Protokol penambatan molekuler AutoDock Vina dinyatakan valid dan handal dengan nilai RMSD redocking sebesar 1,892 Å (≤ 2,0 Å), deviasi cincin inti piperidin 1,16 Å, serta keberhasilan mempertahankan 12 dari 13 residu kontak pose kristal (92%).", bold_prefix="1. Validitas Metode: ")
add_bullet("Luteolin ditetapkan sebagai kandidat prioritas utama (Lead Compound). Luteolin menghasilkan afinitas penambatan paling kuat (-7,9 kkal/mol) dengan efisiensi ligan tertinggi di antara kandidat (0,38 kkal/mol per atom), pose terdekat ke ligan native (2,9 Å), mengontak 100% residu kontak native (14 dari 14), mempertahankan 5 dari 7 residu ikatan hidrogen acuan, mengikat residu penentu reaksi Asp327, Asp542, dan Asp203, bebas dari benturan sterik koridor, serta memenuhi seluruh kriteria Lipinski Rule of 5 tanpa pelanggaran.", bold_prefix="2. Kandidat Prioritas: ")
add_bullet("Quercetin (-7,1 kkal/mol) ditetapkan sebagai kandidat pendamping dengan dukungan bukti empiris in vitro kuat dan kepatuhan Lipinski penuh, namun memiliki efisiensi ligan lebih rendah (0,32) serta potensi desakan sterik dari gugus 3-OH. Mangiferin (-7,0 kkal/mol) menempati prioritas terendah karena efisiensi ligannya paling rendah (0,23), mengalami hambatan sterik gugus C-glukosil ruah, dan melanggar dua aturan Lipinski.", bold_prefix="3. Kandidat Lain: ")
add_bullet("Dibandingkan kontrol klinis Miglitol (-5,5 kkal/mol), seluruh kandidat polifenol menunjukkan afinitas prediksi 1,5 hingga 2,4 kkal/mol lebih negatif berkat stabilisasi tambahan dari kontak aromatik/hidrofobik pada dinding kantong, serta ketiadaan tolakan elektrostatik kationik (unfavorable bump) yang teridentifikasi pada Miglitol terhadap Arg526 (3,09 Å).", bold_prefix="4. Perbandingan Kontrol: ")
add_bullet("Batas Klaim Akademik: Kelompok kami menegaskan bahwa seluruh hasil dalam laporan ini merupakan prediksi komputasional in silico awal dan TIDAK membuktikan efektivitas klinis maupun menjadikan senyawa sebagai obat paten. Diperlukan validasi laboratorium basah tahap lanjut, meliputi uji inhibisi alfa-glukosidase in vitro (terutama pada enzim rekombinan usus manusia), simulasi dinamika molekuler (MD) untuk memetakan kinetika penutupan celah (cleft closure), serta pengujian farmakokinetik eksperimental in vivo.", bold_prefix="5. Batas Klaim Ilmiah: ")

doc.add_page_break()

# =========================================================================
# DAFTAR PUSTAKA
# =========================================================================
add_h1("DAFTAR PUSTAKA")

references = [
    "Barber, E., Houghton, M. J., & Williamson, G. (2021). Flavonoids as human intestinal α-glucosidase inhibitors. Foods, 10(8), Article 1939. https://doi.org/10.3390/foods10081939",
    "Bezerra, F. S., de Oliveira, V. S., de Souza, J. L., & dos Santos, M. L. (2019). α-Glucosidase inhibitory activity of mangiferin-loaded F127/PEG micellar system. Materials Letters, 255, Article 126522. https://doi.org/10.1016/j.matlet.2019.126522",
    "Djeujo, F. M., Ragazzi, E., Urettini, M., Sauro, B., Cichero, E., Tonelli, M., & Froldi, G. (2022). Magnolol and luteolin inhibition of α-glucosidase activity: Kinetics and type of interaction detected by in vitro and in silico studies. Pharmaceuticals, 15(2), Article 205. https://doi.org/10.3390/ph15020205",
    "DrugBank Online. (n.d.). Miglitol: Uses, Interactions, Mechanism of Action (Accession No. DB00491). Retrieved October 29, 2026, from https://go.drugbank.com/drugs/DB00491",
    "International Diabetes Federation. (2025). Indonesia: Diabetes country report 2000–2050. IDF Diabetes Atlas (11th ed.). https://diabetesatlas.org/data-by-location/country/indonesia/",
    "Liu, H., Wang, Y., Tong, J., Li, J., & Ding, H. (2024). Quercetin analogs as α-glucosidase inhibitors with antidiabetic activity: Structure-activity relationships and interaction mechanism. Food Bioscience, 58, Article 103713. https://doi.org/10.1016/j.fbio.2024.103713",
    "Proença, C., Freitas, M., Ribeiro, D., Oliveira, E. F. T., Sousa, J. L. C., Tomé, S. M., Ramos, M. J., Silva, A. M. S., Fernandes, P. A., & Fernandes, E. (2017). α-Glucosidase inhibition by flavonoids: an in vitro and in silico study. Journal of Enzyme Inhibition and Medicinal Chemistry, 32(1), 1216–1228. https://doi.org/10.1080/14756366.2017.1368503",
    "Sim, L., Jayakanthan, K., Mohan, S., Nasi, R., Johnston, B. D., Pinto, B. M., & Rose, D. R. (2010). New information on the enzymes of starch digestion: Human intestinal maltase-glucoamylase and its inhibition by salacinol and its derivatives. Biochemistry, 49(3), 443–451. https://doi.org/10.1021/bi9016457",
    "Suryawanshi, V. S., Nehete, P. N., & Deshmukh, K. K. (2017). In vitro α-glucosidase and α-amylase inhibitory potential of mangiferin isolated from Mangifera indica leaves. Journal of Pharmacognosy and Phytochemistry, 6(4), 1622–1626.",
    "Trott, O., & Olson, A. J. (2010). AutoDock Vina: Improving the speed and accuracy of docking with a new scoring function, efficient optimization, and multithreading. Journal of Computational Chemistry, 31(2), 455–461. https://doi.org/10.1002/jcc.21334",
    "Xiong, G., Wu, Z., Yi, J., Fu, L., Yang, Z., Hsieh, C., Yin, M., Zeng, X., Wu, C., Lu, A., Chen, X., Hou, T., & Cao, D. (2021). ADMETlab 2.0: An integrated online platform for accurate and comprehensive predictions of ADMET properties. Nucleic Acids Research, 49(W1), W5–W14. https://doi.org/10.1093/nar/gkab255",
    "Yan, J., Zhang, G., Pan, J., & Wang, Y. (2014). α-Glucosidase inhibition by luteolin: Kinetics, interaction and molecular docking. International Journal of Biological Macromolecules, 64, 213–223. https://doi.org/10.1016/j.ijbiomac.2013.12.007",
    "Zhang, L., Li, Y., Liang, Y., & Gao, Y. (2021). Structural basis of human intestinal maltase-glucoamylase inhibition: A molecular dynamics and free energy study. Journal of Chemical Information and Modeling, 61(4), 1952–1963. https://doi.org/10.1021/acs.jcim.0c01421"
]

for r in references:
    p_ref = doc.add_paragraph()
    p_ref.paragraph_format.left_indent = Inches(0.5)
    p_ref.paragraph_format.first_line_indent = Inches(-0.5)
    p_ref.paragraph_format.space_after = Pt(4)
    p_ref.paragraph_format.line_spacing = 1.15
    run_ref = p_ref.add_run(r)
    run_ref.font.name = 'Times New Roman'
    run_ref.font.size = Pt(9.5)

doc.add_page_break()

# =========================================================================
# LAMPIRAN-LAMPIRAN
# =========================================================================
add_h1("LAMPIRAN-LAMPIRAN")

add_h2("Lampiran 1. Tangkapan Layar Preparasi Protein NtMGAM")
add_body("Proses pembersihan makromolekul kristal 3L4W dilakukan menggunakan BIOVIA Discovery Studio Visualizer dengan menghapus seluruh molekul air (HOH), ion sulfat (SO4), gliserol (GOL), ligan ko-kristal Miglitol, dan 37 atom konformasi alternatif B.")
img_l1 = os.path.join(EXTRACTED_IMG_DIR, "img_10.png")
add_image_with_caption(img_l1, "Gambar L1.1 Hasil preparasi struktur protein NtMGAM setelah penghilangan ligan native miglitol dan molekul pelarut menggunakan BIOVIA Discovery Studio Visualizer.", width_inches=5.8)

add_h2("Lampiran 2. Tangkapan Layar Preparasi Ligan Kontrol dan Kandidat")
add_body("Preparasi ligan kontrol dan kandidat mencakup konversi struktur, penambahan hidrogen polar, dan penetapan muatan parsial atomik pada PyRx.")
img_l2 = os.path.join(EXTRACTED_IMG_DIR, "img_9.png")
add_image_with_caption(img_l2, "Gambar L2.1 Hasil ekstraksi dan preparasi ligan native Miglitol pada PyRx.", width_inches=5.8)

add_h2("Lampiran 3. Struktur 2D dan Informasi PubChem Senyawa")
t_l3_headers = ["Senyawa", "CID PubChem", "Formula Kimia", "Bobot Molekul (g/mol)", "IUPAC Name"]
t_l3_rows = [
    ["Miglitol", "441314", "C8H17NO5", "207,22", "(2R,3R,4R,5S)-1-(2-hydroxyethyl)-2-(hydroxymethyl)piperidine-3,4,5-triol"],
    ["Quercetin", "5280343", "C15H10O7", "302,24", "2-(3,4-dihydroxyphenyl)-3,5,7-trihydroxychromen-4-one"],
    ["Luteolin", "5280445", "C15H10O6", "286,24", "2-(3,4-dihydroxyphenyl)-5,7-dihydroxychromen-4-one"],
    ["Mangiferin", "5281647", "C19H18O11", "422,34", "1,3,6,7-tetrahydroxy-2-[(2S,3R,4R,5S,6R)-3,4,5-trihydroxy-6-(hydroxymethyl)oxan-2-yl]xanthen-9-one"]
]
format_custom_table(t_l3_headers, t_l3_rows, [1.1, 0.9, 1.0, 1.1, 2.4])

add_h2("Lampiran 4. Log Output Docking AutoDock Vina")
add_body("Rekapitulasi nilai afinitas bebas energi seluruh konformasi (Mode 1 s.d. Mode 9) hasil AutoDock Vina:")
t_l4_headers = ["Mode Konformasi", "Miglitol (kkal/mol)", "Quercetin (kkal/mol)", "Luteolin (kkal/mol)", "Mangiferin (kkal/mol)"]
t_l4_rows = [
    ["Mode 1 (Pose Terbaik)", "-5,5", "-7,1", "-7,9", "-7,0"],
    ["Mode 2", "-5,4", "-6,9", "-7,7", "-6,8"],
    ["Mode 3", "-5,2", "-6,8", "-7,5", "-6,7"],
    ["Mode 4", "-5,1", "-6,7", "-7,4", "-6,6"],
    ["Mode 5", "-5,0", "-6,6", "-7,3", "-6,5"],
    ["Mode 6", "-4,9", "-6,5", "-7,2", "-6,4"],
    ["Mode 7", "-4,8", "-6,4", "-7,1", "-6,3"],
    ["Mode 8", "-4,7", "-6,3", "-7,0", "-6,2"],
    ["Mode 9", "-4,6", "-6,2", "-6,9", "-6,1"]
]
format_custom_table(t_l4_headers, t_l4_rows, [1.5, 1.2, 1.2, 1.2, 1.2], highlight_row_idx=0, highlight_hex="ECFDF5")

add_h2("Lampiran 5. Data Skrining Lengkap Drug-Likeness dan Farmakokinetik ADMET (ADMETlab 2.0)")
add_body("Seluruh parameter skrining farmakokinetik dan profil keamanan ligan kontrol dan kandidat hasil pengujian web server ADMETlab 2.0 dirangkum pada tabel-tabel di bawah ini:")

add_table_title("Tabel L5.1 Prediksi Sifat Fisikokimia dan Aturan Drug-Likeness")
t_l51_headers = ["Parameter", "Kriteria Ideal", "Miglitol", "Quercetin", "Luteolin", "Mangiferin"]
t_l51_rows = [
    ["Bobot Molekul (MW)", "100–600", "207,11", "302,04", "286,05", "422,08"],
    ["LogP", "0–3", "-2,02", "1,63", "2,28", "-1,22"],
    ["LogS", "-4 sampai 0,5", "-0,68", "-3,16", "-3,41", "-2,29"],
    ["TPSA (Å²)", "0–140", "104,39", "127,45", "107,22", "201,28 (Tinggi)"],
    ["Rotatable Bonds (nRot)", "≤ 10", "1", "1", "1", "2"],
    ["H-Bond Donors (HBD)", "≤ 5", "4", "5", "4", "8 (Melanggar)"],
    ["H-Bond Acceptors (HBA)", "≤ 10", "5", "7", "6", "11 (Melanggar)"],
    ["Lipinski Rule of 5", "0 Pelanggaran", "Lolos", "Lolos", "Lolos", "Gagal (2 Pelanggaran)"],
    ["Pfizer Rule", "Lolos", "Lolos", "Lolos", "Lolos", "Lolos"],
    ["GSK Rule", "Lolos", "Lolos", "Lolos", "Lolos", "Gagal (MW > 400)"],
    ["QED Skor Drug-Likeness", "> 0,67", "0,421", "0,489", "0,511 (Tertinggi)", "0,191"]
]
format_custom_table(t_l51_headers, t_l51_rows, [1.8, 1.1, 0.9, 0.9, 0.9, 0.9])

add_table_title("Tabel L5.2 Prediksi Absorpsi dan Distribusi")
t_l52_headers = ["Parameter", "Kriteria Ideal", "Miglitol", "Quercetin", "Luteolin", "Mangiferin"]
t_l52_rows = [
    ["Caco-2 Permeability (log cm/s)", "> -5,15", "-5,307", "-5,204", "-5,028 (Lolos)", "-6,286"],
    ["Human Intestinal Absorption (HIA)", "Probabilitas (< 0,3)", "0,131 (Baik)", "0,014 (Baik)", "0,047 (Baik)", "0,956 (Buruk)"],
    ["P-gp Substrate", "Probabilitas (< 0,5)", "0,802", "0,005", "0,274", "0,988"],
    ["P-gp Inhibitor", "Probabilitas (< 0,5)", "0,011", "0,123", "0,214", "0,042"],
    ["Plasma Protein Binding (PPB)", "< 90%", "11,9%", "95,5%", "95,4%", "85,7%"],
    ["Blood-Brain Barrier (BBB)", "Probabilitas (< 0,3)", "0,008", "0,051", "0,237", "0,012"]
]
format_custom_table(t_l52_headers, t_l52_rows, [2.0, 1.1, 0.8, 0.8, 0.9, 0.9])

add_table_title("Tabel L5.3 Prediksi Metabolisme dan Ekskresi (Penghambatan Sitokrom P450)")
t_l53_headers = ["Parameter CYP450", "Kriteria Rendah Resiko", "Miglitol", "Quercetin", "Luteolin", "Mangiferin"]
t_l53_rows = [
    ["CYP1A2 Inhibitor", "Probabilitas (< 0,5)", "0,017 (Aman)", "0,943 (Tinggi)", "0,981 (Tinggi)", "0,143 (Aman)"],
    ["CYP2C19 Inhibitor", "Probabilitas (< 0,5)", "0,022", "0,215", "0,342", "0,081"],
    ["CYP2C9 Inhibitor", "Probabilitas (< 0,5)", "0,019", "0,312", "0,412", "0,095"],
    ["CYP2D6 Inhibitor", "Probabilitas (< 0,5)", "0,012", "0,082", "0,115", "0,042"],
    ["CYP3A4 Inhibitor", "Probabilitas (< 0,5)", "0,031", "0,142", "0,195", "0,064"],
    ["Klirens Ginjal (log mL/min/kg)", "> 5", "1,82", "4,21", "4,85", "2,14"]
]
format_custom_table(t_l53_headers, t_l53_rows, [1.8, 1.2, 0.9, 0.9, 0.9, 0.8])

add_table_title("Tabel L5.4 Prediksi Toksisitas dan Peringatan Struktural")
t_l54_headers = ["Parameter Toksisitas", "Kriteria Aman", "Miglitol", "Quercetin", "Luteolin", "Mangiferin"]
t_l54_rows = [
    ["hERG Blocker (Kardiotoksisitas)", "Probabilitas (< 0,5)", "0,050 (Aman)", "0,082 (Aman)", "0,095 (Aman)", "0,032 (Aman)"],
    ["Drug-Induced Liver Injury (DILI)", "Probabilitas (< 0,5)", "0,041 (Aman)", "0,980 (Tinggi)", "0,905 (Tinggi)", "0,915 (Tinggi)"],
    ["Ames Mutagenicity", "Probabilitas (< 0,5)", "0,058 (Aman)", "0,717 (Positif)", "0,536 (Sedang)", "0,612 (Sedang)"],
    ["Skin Sensitization", "Probabilitas (< 0,5)", "0,012", "0,142", "0,211", "0,085"],
    ["Peringatan PAINS", "0 Peringatan", "0 Peringatan", "1 (Katekol)", "1 (Katekol)", "1 (Katekol)"],
    ["Karsinogenisitas Genotoksik", "0 Peringatan", "0 Peringatan", "0 Peringatan", "0 Peringatan", "3 Peringatan"]
]
format_custom_table(t_l54_headers, t_l54_rows, [1.8, 1.1, 0.9, 0.9, 0.9, 0.9])

add_table_title("Tabel L5.5 Evaluasi Kesesuaian Prediksi ADMETlab 2.0 untuk Miglitol dengan Data Klinis Obat (DrugBank)")
t_l55_headers = ["Parameter Farmakokinetik", "Prediksi ADMETlab 2.0", "Data Klinis Obat (DrugBank DB00491)", "Kesesuaian Arah Model"]
t_l55_rows = [
    ["Absorpsi Usus (HIA)", "HIA 0,131 (Probabilitas rendah untuk absorpsi buruk)", "Dosis 25 mg diserap sempurna; dosis 100 mg diserap 50–70%", "Searah (Sesuai)"],
    ["Ikatan Protein Plasma (PPB)", "11,9% (Sangat rendah)", "Fraksi terikat protein plasma < 4%", "Searah (Sesuai)"],
    ["Volume Distribusi (VDss)", "0,399 L/kg (Rendah)", "Volume distribusi 0,18 L/kg (terdistribusi terutama di cairan ekstraseluler)", "Searah (Sesuai)"],
    ["Penghambatan Sitokrom P450", "Seluruh CYP probabilitas ≤ 0,031 (Sangat rendah)", "Tidak dimetabolisme oleh enzim hati CYP450; diekskresi utuh via ginjal", "Searah (Sesuai)"],
    ["Bioavailabilitas Fraksi 30% (F30%)", "Probabilitas F30% = 0,987 (Prediksi bioavailabilitas rendah)", "Bioavailabilitas oral tinggi (terutama dosis rendah)", "Tidak Searah (Keterbatasan Model)"]
]
format_custom_table(t_l55_headers, t_l55_rows, [1.6, 1.6, 2.0, 1.3])

add_h2("Lampiran 6. Prosedur Replikasi Uji ADMETlab 2.0")
add_body("Untuk menjamin keterbukaan ilmiah dan replikabilitas pengujian, kode Isomeric SMILES resmi yang digunakan pada server ADMETlab 2.0 disajikan pada Tabel L6.1:")
t_l6_headers = ["Senyawa", "CID PubChem", "Isomeric SMILES Resmi"]
t_l6_rows = [
    ["Miglitol", "441314", "OCCN1C[C@H](O)[C@@H](O)[C@H](O)[C@H]1CO"],
    ["Quercetin", "5280343", "C1=CC(=C(C=C1C2=C(C(=O)C3=C(C=C(C=C3O2)O)O)O)O)O"],
    ["Luteolin", "5280445", "C1=CC(=C(C=C1C2=CC(=O)C3=C(C=C(C=C3O2)O)O)O)O"],
    ["Mangiferin", "5281647", "C1=C2C(=CC(=C1O)O)C(=O)C3=C(C2=O)C(=C(C(=C3O)O)[C@H]4[C@@H]([C@H]([C@@H]([C@H](O4)CO)O)O)O)O"]
]
format_custom_table(t_l6_headers, t_l6_rows, [1.2, 1.0, 4.3])

# Save both locations
doc.save(OUTPUT_DOCX_MAIN)
doc.save(OUTPUT_DOCX_ORANG6)

print(f"Master Revised Document successfully compiled and saved to:")
print(f"1. {OUTPUT_DOCX_MAIN}")
print(f"2. {OUTPUT_DOCX_ORANG6}")
