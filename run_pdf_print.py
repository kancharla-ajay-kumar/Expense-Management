import subprocess
import os
import pymupdf

chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
html = os.path.abspath(r"d:\Expense-Management\Industrial_Training_Report_Ajay_Kumar.html")
pdf = os.path.abspath(r"d:\Expense-Management\Industrial_Training_Report_Ajay_Kumar.pdf")

file_url = "file:///" + html.replace("\\", "/")

cmd = [
    chrome,
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf}",
    file_url
]
print("Running command...")
res = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
print("Return code:", res.returncode)
print("Stderr:", res.stderr)
print("PDF exists:", os.path.exists(pdf))

if os.path.exists(pdf):
    doc = pymupdf.open(pdf)
    print("Total PDF Page Count:", len(doc))
    print("File size:", os.path.getsize(pdf), "bytes")
