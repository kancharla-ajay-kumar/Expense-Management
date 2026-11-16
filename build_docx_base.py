import os
import sys

# Script to generate both DOCX and HTML/PDF for the Industrial Training Report
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

base_dir = r"d:\Expense-Management"
assets_dir = os.path.join(base_dir, "report_assets")

doc = Document()

# Set standard 1-inch margins
for section in doc.sections:
    section.top_margin = Inches(1.0)
    section.bottom_margin = Inches(1.0)
    section.left_margin = Inches(1.0)
    section.right_margin = Inches(1.0)
    section.different_first_page_header_footer = True
    
    # Configure Header & Footer
    header = section.header
    hp = header.paragraphs[0]
    hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    hrun = hp.add_run("SpendWise — MERN Expense Tracker | MANIT Bhopal")
    hrun.font.name = "Times New Roman"
    hrun.font.size = Pt(8.5)
    hrun.font.color.rgb = RGBColor(100, 100, 100)
    
    footer = section.footer
    fp = footer.paragraphs[0]
    fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    frun = fp.add_run("Department of Computer Science and Engineering, MANIT Bhopal")
    frun.font.name = "Times New Roman"
    frun.font.size = Pt(8.5)
    frun.font.color.rgb = RGBColor(100, 100, 100)

def set_para_font(p, name="Times New Roman", size=11, bold=False, italic=False, color=(0,0,0), align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=6, space_before=0, line_spacing=1.15):
    p.alignment = align
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.line_spacing = line_spacing
    for r in p.runs:
        r.font.name = name
        r.font.size = Pt(size)
        r.bold = bold
        r.italic = italic
        r.font.color.rgb = RGBColor(*color)

def add_styled_heading(doc, text, level=1):
    h = doc.add_heading(level=level)
    if level == 1:
        run = h.add_run(text)
        set_para_font(h, name="Times New Roman", size=15, bold=True, align=WD_ALIGN_PARAGRAPH.LEFT, space_before=14, space_after=8)
    elif level == 2:
        run = h.add_run(text)
        set_para_font(h, name="Times New Roman", size=13, bold=True, align=WD_ALIGN_PARAGRAPH.LEFT, space_before=10, space_after=6)
    elif level == 3:
        run = h.add_run(text)
        set_para_font(h, name="Times New Roman", size=11.5, bold=True, italic=True, align=WD_ALIGN_PARAGRAPH.LEFT, space_before=6, space_after=4)
    return h

def add_body_p(doc, text):
    p = doc.add_paragraph()
    r = p.add_run(text)
    set_para_font(p, name="Times New Roman", size=11, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=6, line_spacing=1.15)
    return p

def add_bullet_p(doc, bold_prefix, text):
    p = doc.add_paragraph(style='List Bullet')
    r1 = p.add_run(bold_prefix)
    r1.bold = True
    r1.font.name = "Times New Roman"
    r1.font.size = Pt(11)
    r2 = p.add_run(text)
    r2.font.name = "Times New Roman"
    r2.font.size = Pt(11)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.15
    return p

def add_figure(doc, img_path, caption, width=Inches(5.5)):
    if os.path.exists(img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(8)
        p_img.paragraph_format.space_after = Pt(4)
        run = p_img.add_run()
        run.add_picture(img_path, width=width)
        
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p_cap.add_run(caption)
        r.italic = True
        r.font.name = "Times New Roman"
        r.font.size = Pt(10)
        p_cap.paragraph_format.space_after = Pt(10)

def add_styled_table(doc, headers, data, col_widths=None):
    tbl = doc.add_table(rows=len(data) + 1, cols=len(headers))
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    
    # Header row
    hdr_cells = tbl.rows[0].cells
    for i, h in enumerate(headers):
        hdr_cells[i].text = h
        shading = parse_xml(r'<w:shd {} w:fill="2A2F35"/>'.format(nsdecls('w')))
        hdr_cells[i]._tc.get_or_add_tcPr().append(shading)
        p = hdr_cells[i].paragraphs[0]
        set_para_font(p, name="Times New Roman", size=10, bold=True, color=(255, 255, 255), align=WD_ALIGN_PARAGRAPH.LEFT, space_after=3)
        
    for r_idx, row in enumerate(data):
        row_cells = tbl.rows[r_idx + 1].cells
        bg_col = "F7F9FA" if r_idx % 2 == 1 else "FFFFFF"
        for c_idx, val in enumerate(row):
            row_cells[c_idx].text = str(val)
            shading = parse_xml(r'<w:shd {} w:fill="{}"/>'.format(nsdecls('w'), bg_col))
            row_cells[c_idx]._tc.get_or_add_tcPr().append(shading)
            p = row_cells[c_idx].paragraphs[0]
            set_para_font(p, name="Times New Roman", size=9.5, align=WD_ALIGN_PARAGRAPH.LEFT, space_after=2)
            
    if col_widths:
        for row in tbl.rows:
            for i, w in enumerate(col_widths):
                row.cells[i].width = Inches(w)
                
    doc.add_paragraph().paragraph_format.space_after = Pt(6)

print("Helper functions defined successfully")
