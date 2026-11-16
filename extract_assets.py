import fitz
import os

pdf_path = r"C:\Users\ajayk\.gemini\antigravity\brain\3eb81874-b3fc-4ca8-8190-9dd70fa69ded\.user_uploaded\media_1794846370925_1b9ce376.pdf"
doc = fitz.open(pdf_path)
print("Page count:", len(doc))

out_dir = r"d:\Expense-Management\report_assets"
os.makedirs(out_dir, exist_ok=True)

# Page 1 (index 0) has the MANIT Bhopal logo
page0 = doc[0]
for i, img in enumerate(page0.get_images(full=True)):
    xref = img[0]
    base_image = doc.extract_image(xref)
    ext = base_image["ext"]
    logo_path = os.path.join(out_dir, f"manit_logo.{ext}")
    with open(logo_path, "wb") as f:
        f.write(base_image["image"])
    print(f"Extracted MANIT logo: {logo_path} ({len(base_image['image'])} bytes)")

# Check Unstop logo on page 2 or page 9
for page_idx in [1, 8]:
    p = doc[page_idx]
    for j, img in enumerate(p.get_images(full=True)):
        xref = img[0]
        base_image = doc.extract_image(xref)
        ext = base_image["ext"]
        p_path = os.path.join(out_dir, f"page_{page_idx+1}_img_{j}.{ext}")
        with open(p_path, "wb") as f:
            f.write(base_image["image"])
        print(f"Saved page {page_idx+1} image {j}: {p_path} ({len(base_image['image'])} bytes)")
