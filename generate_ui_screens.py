import os
from PIL import Image, ImageDraw, ImageFont

out_dir = r"d:\Expense-Management\report_assets"
os.makedirs(out_dir, exist_ok=True)

try:
    f_title = ImageFont.truetype("arialbd.ttf", 22)
    f_card_val = ImageFont.truetype("arialbd.ttf", 20)
    f_card_lbl = ImageFont.truetype("arial.ttf", 13)
    f_bold = ImageFont.truetype("arialbd.ttf", 14)
    f_norm = ImageFont.truetype("arial.ttf", 13)
    f_small = ImageFont.truetype("arial.ttf", 11)
except:
    f_title = f_card_val = f_card_lbl = f_bold = f_norm = f_small = ImageFont.load_default()

# 1. Render High-Fidelity SpendWise Dashboard Screenshot (Figure 14.1)
def generate_dashboard_screenshot():
    w, h = 1200, 750
    img = Image.new("RGB", (w, h), "#F7F5F0")  # SpendWise paper background
    draw = ImageDraw.Draw(img)
    
    # Left Sidebar (w: 220)
    draw.rectangle([0, 0, 220, h], fill="#FFFFFF", outline="#E4E0D6", width=1)
    # Brand
    draw.rounded_rectangle([25, 25, 60, 60], radius=8, fill="#2F6F4E")
    draw.text([70, 32], "SpendWise", fill="#1B1F23", font=f_title)
    
    # Nav items
    navs = [
        ("Dashboard", True),
        ("Transactions", False),
        ("Budgets", False),
        ("Profile", False)
    ]
    y_nav = 90
    for nav, active in navs:
        if active:
            draw.rounded_rectangle([15, y_nav, 205, y_nav+38], radius=6, fill="#E0ECE5")
            draw.text([35, y_nav+10], nav, fill="#2F6F4E", font=f_bold)
        else:
            draw.text([35, y_nav+10], nav, fill="#6E6759", font=f_norm)
        y_nav += 46
        
    # Top Navbar
    draw.rectangle([220, 0, w, 70], fill="#FFFFFF", outline="#E4E0D6", width=1)
    draw.text([250, 24], "Dashboard", fill="#1B1F23", font=f_title)
    # User Profile badge
    draw.ellipse([w-160, 18, w-125, 53], fill="#2F6F4E")
    draw.text([w-150, 26], "KA", fill="#FFFFFF", font=f_bold)
    draw.text([w-115, 27], "Kancharla Ajay", fill="#1B1F23", font=f_norm)
    
    # 4 Summary Cards
    cards = [
        ("Total balance", "₹ 1,42,850", "all time", "#2F6F4E", "#E0ECE5"),
        ("Income this month", "₹ 85,000", "current month", "#298A5B", "#E8F5E9"),
        ("Expenses this month", "₹ 34,620", "current month", "#C2542C", "#FBE9E7"),
        ("Net this month", "+ ₹ 50,380", "you're in the green", "#298A5B", "#E8F5E9")
    ]
    cx = 250
    cw = 215
    for lbl, val, sub, col, bg in cards:
        draw.rounded_rectangle([cx, 90, cx+cw, 180], radius=10, fill="#FFFFFF", outline="#E4E0D6", width=1)
        draw.rounded_rectangle([cx+12, 102, cx+40, 130], radius=6, fill=bg)
        draw.text([cx+14, 140], lbl, fill="#6E6759", font=f_card_lbl)
        draw.text([cx+14, 155], val, fill=col, font=f_card_val)
        cx += cw + 25
        
    # Chart 1: Monthly Bar Chart (Income vs Expense)
    draw.rounded_rectangle([250, 205, 780, 440], radius=10, fill="#FFFFFF", outline="#E4E0D6", width=1)
    draw.text([270, 220], "Monthly Overview (Last 6 Months)", fill="#1B1F23", font=f_bold)
    months = ["Jun", "Jul", "Aug", "Sep", "Oct", "Nov"]
    bx = 290
    for m in months:
        # Green bar (income)
        draw.rectangle([bx, 380-110, bx+26, 380], fill="#298A5B")
        # Rust bar (expense)
        draw.rectangle([bx+30, 380-65, bx+56, 380], fill="#C2542C")
        draw.text([bx+14, 395], m, fill="#6E6759", font=f_small)
        bx += 78
    # Legend
    draw.rectangle([620, 225, 635, 235], fill="#298A5B")
    draw.text([642, 222], "Income", fill="#6E6759", font=f_small)
    draw.rectangle([700, 225, 715, 235], fill="#C2542C")
    draw.text([722, 222], "Expense", fill="#6E6759", font=f_small)
    
    # Chart 2: Category Breakdown Pie Chart
    draw.rounded_rectangle([805, 205, w-30, 440], radius=10, fill="#FFFFFF", outline="#E4E0D6", width=1)
    draw.text([825, 220], "Expense Breakdown", fill="#1B1F23", font=f_bold)
    # Draw pie segments representation
    draw.pieslice([860, 255, 1020, 415], start=0, end=130, fill="#2F6F4E")
    draw.pieslice([860, 255, 1020, 415], start=130, end=210, fill="#C2542C")
    draw.pieslice([860, 255, 1020, 415], start=210, end=290, fill="#B8862E")
    draw.pieslice([860, 255, 1020, 415], start=290, end=360, fill="#3E7CB1")
    # Legend
    cats = [("Groceries", "#2F6F4E"), ("Rent", "#C2542C"), ("Utilities", "#B8862E"), ("Others", "#3E7CB1")]
    ly = 265
    for cname, ccol in cats:
        draw.rectangle([1050, ly+2, 1062, ly+14], fill=ccol)
        draw.text([1070, ly], cname, fill="#333333", font=f_small)
        ly += 30

    # Recent Transactions Table Card
    draw.rounded_rectangle([250, 460, w-30, 720], radius=10, fill="#FFFFFF", outline="#E4E0D6", width=1)
    draw.text([270, 475], "Recent Transactions", fill="#1B1F23", font=f_bold)
    
    # Headers
    draw.text([270, 510], "TITLE / DESCRIPTION", fill="#6E6759", font=f_small)
    draw.text([540, 510], "CATEGORY", fill="#6E6759", font=f_small)
    draw.text([710, 510], "DATE", fill="#6E6759", font=f_small)
    draw.text([870, 510], "METHOD", fill="#6E6759", font=f_small)
    draw.text([1030, 510], "AMOUNT", fill="#6E6759", font=f_small)
    draw.line([270, 530, w-50, 530], fill="#E4E0D6", width=1)
    
    txs = [
        ("Monthly Software Internship Stipend", "Salary", "15 Nov 2026", "Bank Transfer", "+ ₹ 45,000", "#298A5B"),
        ("Organic Groceries & Supplies", "Groceries", "14 Nov 2026", "Credit Card", "- ₹ 3,450", "#C2542C"),
        ("High-Speed Fiber Internet Bill", "Utilities", "12 Nov 2026", "Debit Card", "- ₹ 1,199", "#C2542C"),
        ("Apartment Monthly Rent", "Rent/Mortgage", "01 Nov 2026", "Bank Transfer", "- ₹ 16,000", "#C2542C"),
        ("Freelance Web App Development", "Freelance", "28 Oct 2026", "Mobile Wallet", "+ ₹ 22,500", "#298A5B")
    ]
    ty = 545
    for title, cat, dt, meth, amt, col in txs:
        draw.text([270, ty], title, fill="#1B1F23", font=f_norm)
        draw.text([540, ty], cat, fill="#6E6759", font=f_norm)
        draw.text([710, ty], dt, fill="#6E6759", font=f_norm)
        draw.text([870, ty], meth, fill="#6E6759", font=f_norm)
        draw.text([1030, ty], amt, fill=col, font=f_bold)
        draw.line([270, ty+24, w-50, ty+24], fill="#F0EDE6", width=1)
        ty += 34
        
    out_path = os.path.join(out_dir, "dashboard_view.png")
    img.save(out_path, dpi=(300, 300))
    print("Saved dashboard_view.png")

# 2. Render High-Fidelity Budgets View Screenshot (Figure 14.2)
def generate_budgets_screenshot():
    w, h = 1200, 700
    img = Image.new("RGB", (w, h), "#F7F5F0")
    draw = ImageDraw.Draw(img)
    
    # Left Sidebar
    draw.rectangle([0, 0, 220, h], fill="#FFFFFF", outline="#E4E0D6", width=1)
    draw.rounded_rectangle([25, 25, 60, 60], radius=8, fill="#2F6F4E")
    draw.text([70, 32], "SpendWise", fill="#1B1F23", font=f_title)
    
    y_nav = 90
    for nav, active in [("Dashboard", False), ("Transactions", False), ("Budgets", True), ("Profile", False)]:
        if active:
            draw.rounded_rectangle([15, y_nav, 205, y_nav+38], radius=6, fill="#E0ECE5")
            draw.text([35, y_nav+10], nav, fill="#2F6F4E", font=f_bold)
        else:
            draw.text([35, y_nav+10], nav, fill="#6E6759", font=f_norm)
        y_nav += 46
        
    # Top Navbar
    draw.rectangle([220, 0, w, 70], fill="#FFFFFF", outline="#E4E0D6", width=1)
    draw.text([250, 24], "Monthly Budgets & Alerts", fill="#1B1F23", font=f_title)
    
    # Set Budget Form Card
    draw.rounded_rectangle([250, 90, w-30, 210], radius=10, fill="#FFFFFF", outline="#E4E0D6", width=1)
    draw.text([270, 105], "Set Category Budget", fill="#1B1F23", font=f_bold)
    draw.rectangle([270, 140, 520, 180], fill="#F7F5F0", outline="#E4E0D6")
    draw.text([280, 152], "Category: Dining Out", fill="#333333", font=f_norm)
    draw.rectangle([540, 140, 780, 180], fill="#F7F5F0", outline="#E4E0D6")
    draw.text([550, 152], "Monthly Limit: ₹ 8,000", fill="#333333", font=f_norm)
    draw.rectangle([800, 140, 980, 180], fill="#F7F5F0", outline="#E4E0D6")
    draw.text([810, 152], "Threshold: 80%", fill="#333333", font=f_norm)
    draw.rounded_rectangle([1000, 140, 1140, 180], radius=6, fill="#2F6F4E")
    draw.text([1025, 152], "Save Budget", fill="#FFFFFF", font=f_bold)
    
    # Budgets Cards
    budgets = [
        ("Groceries", "₹ 7,450", "₹ 10,000", 74.5, "ON TRACK", "#298A5B", "#E8F5E9"),
        ("Dining Out", "₹ 6,850", "₹ 8,000", 85.6, "NEAR LIMIT", "#B8862E", "#FFF8E1"),
        ("Entertainment", "₹ 5,300", "₹ 5,000", 106.0, "EXCEEDED", "#C2542C", "#FFEBEE"),
        ("Transportation", "₹ 3,120", "₹ 6,000", 52.0, "ON TRACK", "#298A5B", "#E8F5E9")
    ]
    by = 230
    for cat, spent, limit, pct, status, stat_col, stat_bg in budgets:
        draw.rounded_rectangle([250, by, w-30, by+95], radius=10, fill="#FFFFFF", outline="#E4E0D6", width=1)
        draw.text([275, by+16], cat, fill="#1B1F23", font=f_bold)
        draw.text([275, by+40], f"Spent: {spent} of {limit}", fill="#6E6759", font=f_norm)
        # Status Pill
        draw.rounded_rectangle([w-160, by+15, w-50, by+42], radius=12, fill=stat_bg)
        draw.text([w-145, by+21], status, fill=stat_col, font=f_small)
        # Progress Bar
        draw.rounded_rectangle([275, by+65, w-60, by+77], radius=6, fill="#F0EDE6")
        fill_w = min(int((w-60-275) * (pct / 100)), w-60-275)
        bar_col = "#C2542C" if pct >= 100 else ("#B8862E" if pct >= 80 else "#2F6F4E")
        draw.rounded_rectangle([275, by+65, 275+fill_w, by+77], radius=6, fill=bar_col)
        draw.text([w-115, by+42], f"{pct:.1f}%", fill=bar_col, font=f_bold)
        by += 110

    out_path = os.path.join(out_dir, "budgets_view.png")
    img.save(out_path, dpi=(300, 300))
    print("Saved budgets_view.png")

generate_dashboard_screenshot()
generate_budgets_screenshot()
