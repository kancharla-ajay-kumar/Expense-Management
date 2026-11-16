import os
from PIL import Image, ImageDraw, ImageFont

out_dir = r"d:\Expense-Management\report_assets"
os.makedirs(out_dir, exist_ok=True)

# 1. Generate Architecture Diagram (Figure 6.1)
def generate_architecture_diagram():
    w, h = 1000, 420
    img = Image.new("RGB", (w, h), "#FFFFFF")
    draw = ImageDraw.Draw(img)
    
    # Fonts
    try:
        font_title = ImageFont.truetype("arial.ttf", 20)
        font_box = ImageFont.truetype("arialbd.ttf", 16)
        font_sub = ImageFont.truetype("arial.ttf", 13)
        font_arrow = ImageFont.truetype("arial.ttf", 12)
    except:
        font_title = font_box = font_sub = font_arrow = ImageFont.load_default()
        
    # Draw 4 main blocks: Client Browser -> Frontend (Vercel) -> Backend (Render) -> Database (MongoDB Atlas)
    boxes = [
        ("Client Browser", ["React 18 SPA", "Tailwind CSS", "User Dashboard"], 40, 100, 200, 260, "#E8F5E9", "#2E7D32"),
        ("Frontend Host (Vercel)", ["Vite Static Hosting", "Global Edge CDN", "SPA Client Routing"], 280, 100, 440, 260, "#E3F2FD", "#1565C0"),
        ("Backend API (Render)", ["Node.js / Express", "JWT Auth & Middleware", "REST Controllers"], 520, 100, 680, 260, "#FFF3E0", "#E65100"),
        ("Database (Atlas)", ["MongoDB Cluster", "User & Expense Collections", "Aggregation Pipelines"], 760, 100, 920, 260, "#EDE7F6", "#512DA8")
    ]
    
    for title, items, x1, y1, x2, y2, bg, border in boxes:
        draw.rounded_rectangle([x1, y1, x2, y2], radius=10, fill=bg, outline=border, width=2)
        draw.text((x1 + 15, y1 + 15), title, fill=border, font=font_box)
        y_text = y1 + 50
        for it in items:
            draw.text((x1 + 20, y_text), f"• {it}", fill="#333333", font=font_sub)
            y_text += 26
            
    # Connect with arrows
    arrow_pairs = [
        ((200, 180), (280, 180), "HTTPS / CDN"),
        ((440, 180), (520, 180), "REST API / JSON"),
        ((680, 180), (760, 180), "Mongoose Driver")
    ]
    
    for (start, end, label) in arrow_pairs:
        draw.line([start, end], fill="#555555", width=2)
        # arrow head
        draw.polygon([(end[0], end[1]), (end[0]-10, end[1]-6), (end[0]-10, end[1]+6)], fill="#555555")
        draw.text((start[0] + 8, start[1] - 22), label, fill="#444444", font=font_arrow)
        
    out_path = os.path.join(out_dir, "system_architecture.png")
    img.save(out_path, dpi=(300, 300))
    print("Saved system_architecture.png")

# 2. Generate Authentication Flow Diagram (Figure 9.1)
def generate_auth_flow_diagram():
    w, h = 900, 380
    img = Image.new("RGB", (w, h), "#FFFFFF")
    draw = ImageDraw.Draw(img)
    try:
        font_box = ImageFont.truetype("arialbd.ttf", 15)
        font_sub = ImageFont.truetype("arial.ttf", 13)
        font_step = ImageFont.truetype("arial.ttf", 11)
    except:
        font_box = font_sub = font_step = ImageFont.load_default()
        
    # Columns: Client / Browser -> Express Auth Guard -> MongoDB
    steps = [
        ("1. POST /api/auth/login", (160, 80), (450, 80), "right"),
        ("2. findOne({ email })", (450, 130), (740, 130), "right"),
        ("3. Return user doc with hash", (740, 170), (450, 170), "left"),
        ("4. bcrypt.compare() & sign JWT", (450, 200), (450, 220), "self"),
        ("5. Return JWT token & user obj", (450, 250), (160, 250), "left"),
        ("6. Subsequent reqs: Bearer <token>", (160, 310), (450, 310), "right"),
    ]
    
    # Lifelines
    lifelines = [
        ("React Client", 160),
        ("Express Server / JWT Guard", 450),
        ("MongoDB Database", 740)
    ]
    for name, x in lifelines:
        draw.rounded_rectangle([x-80, 20, x+80, 55], radius=6, fill="#F5F5F5", outline="#9E9E9E", width=1)
        draw.text((x-70, 30), name, fill="#212121", font=font_box)
        draw.line([(x, 55), (x, 350)], fill="#BDBDBD", width=2)
        
    for text, (x1, y1), (x2, y2), direction in steps:
        if direction == "right":
            draw.line([(x1, y1), (x2, y2)], fill="#1E88E5", width=2)
            draw.polygon([(x2, y2), (x2-8, y2-5), (x2-8, y2+5)], fill="#1E88E5")
            draw.text(((x1+x2)/2 - 80, y1-18), text, fill="#0D47A1", font=font_step)
        elif direction == "left":
            draw.line([(x1, y1), (x2, y2)], fill="#43A047", width=2)
            draw.polygon([(x2, y2), (x2+8, y2-5), (x2+8, y2+5)], fill="#43A047")
            draw.text(((x1+x2)/2 - 80, y1-18), text, fill="#1B5E20", font=font_step)
        elif direction == "self":
            draw.rounded_rectangle([x1-75, y1, x1+75, y2+15], radius=4, fill="#FFF9C4", outline="#FBC02D")
            draw.text((x1-70, y1+5), text, fill="#F57F17", font=font_step)

    out_path = os.path.join(out_dir, "auth_workflow.png")
    img.save(out_path, dpi=(300, 300))
    print("Saved auth_workflow.png")

generate_architecture_diagram()
generate_auth_flow_diagram()
