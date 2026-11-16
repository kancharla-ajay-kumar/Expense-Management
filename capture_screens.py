import subprocess
import time
import os

py311 = r"C:\Users\ajayk\AppData\Local\Programs\Python\Python311\python.exe"
chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
out_dir = r"d:\Expense-Management\report_assets"
os.makedirs(out_dir, exist_ok=True)

# 1. Start static server for frontend/dist
http_proc = subprocess.Popen([
    py311, "-m", "http.server", "4173", "--directory", r"d:\Expense-Management\frontend\dist"
])
print("Started static server PID:", http_proc.pid)
time.sleep(2)

screens = [
    ("login.png", "http://localhost:4173/"),
    ("dashboard_dark.png", "http://localhost:4173/"),
    ("register.png", "http://localhost:4173/register"),
]

for name, url in screens:
    out_file = os.path.join(out_dir, name)
    cmd = [
        chrome,
        "--headless",
        "--disable-gpu",
        "--hide-scrollbars",
        "--window-size=1280,850",
        f"--screenshot={out_file}",
        url
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
    print(f"Captured {name}: exists={os.path.exists(out_file)}, size={os.path.getsize(out_file) if os.path.exists(out_file) else 0}")

http_proc.terminate()
print("Terminated server")
