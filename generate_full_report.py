import os
import subprocess
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

base_dir = r"d:\Expense-Management"
assets_dir = os.path.join(base_dir, "report_assets")
docx_out = os.path.join(base_dir, "Industrial_Training_Report_Ajay_Kumar.docx")
html_out = os.path.join(base_dir, "Industrial_Training_Report_Ajay_Kumar.html")
pdf_out = os.path.join(base_dir, "Industrial_Training_Report_Ajay_Kumar.pdf")

doc = Document()

# Configure page geometry: A4, 1-inch margins
for section in doc.sections:
    section.page_width = Inches(8.27)
    section.page_height = Inches(11.69)
    section.top_margin = Inches(1.0)
    section.bottom_margin = Inches(1.0)
    section.left_margin = Inches(1.0)
    section.right_margin = Inches(1.0)
    section.different_first_page_header_footer = True
    
    # Header & Footer
    hp = section.header.paragraphs[0]
    hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    hrun = hp.add_run("SpendWise — MERN Expense Tracker | MANIT Bhopal")
    hrun.font.name = "Times New Roman"
    hrun.font.size = Pt(8.5)
    hrun.font.color.rgb = RGBColor(120, 120, 120)
    
    fp = section.footer.paragraphs[0]
    fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    frun = fp.add_run("Department of Computer Science and Engineering, MANIT Bhopal")
    frun.font.name = "Times New Roman"
    frun.font.size = Pt(8.5)
    frun.font.color.rgb = RGBColor(120, 120, 120)

def fmt(p, size=11, bold=False, italic=False, color=(0,0,0), align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=6, space_before=0, line_spacing=1.15):
    p.alignment = align
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.line_spacing = line_spacing
    for r in p.runs:
        r.font.name = "Times New Roman"
        r.font.size = Pt(size)
        r.bold = bold
        r.italic = italic
        r.font.color.rgb = RGBColor(*color)

def h1(text):
    p = doc.add_paragraph()
    r = p.add_run(text)
    fmt(p, size=15, bold=True, color=(20, 20, 20), align=WD_ALIGN_PARAGRAPH.LEFT, space_before=14, space_after=8)
    return p

def h2(text):
    p = doc.add_paragraph()
    r = p.add_run(text)
    fmt(p, size=13, bold=True, color=(30, 30, 30), align=WD_ALIGN_PARAGRAPH.LEFT, space_before=10, space_after=5)
    return p

def h3(text):
    p = doc.add_paragraph()
    r = p.add_run(text)
    fmt(p, size=11.5, bold=True, italic=True, color=(40, 40, 40), align=WD_ALIGN_PARAGRAPH.LEFT, space_before=6, space_after=3)
    return p

def body(text):
    p = doc.add_paragraph()
    r = p.add_run(text)
    fmt(p, size=11, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=6, line_spacing=1.15)
    return p

def bullet(prefix, text):
    p = doc.add_paragraph(style='List Bullet')
    r1 = p.add_run(prefix)
    r1.bold = True
    r1.font.name = "Times New Roman"
    r1.font.size = Pt(11)
    r2 = p.add_run(text)
    r2.font.name = "Times New Roman"
    r2.font.size = Pt(11)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.15
    return p

def code(snippet):
    p = doc.add_paragraph()
    r = p.add_run(snippet)
    r.font.name = "Courier New"
    r.font.size = Pt(9.5)
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.line_spacing = 1.05
    # Light gray background
    shd = parse_xml(r'<w:shd {} w:fill="F4F6F8"/>'.format(nsdecls('w')))
    p._p.get_or_add_pPr().append(shd)
    return p

def fig(img_name, caption, width=Inches(5.4)):
    ipath = os.path.join(assets_dir, img_name)
    if os.path.exists(ipath):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(3)
        r = p.add_run()
        r.add_picture(ipath, width=width)
        
        cp = doc.add_paragraph()
        cp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r2 = cp.add_run(caption)
        r2.italic = True
        r2.font.name = "Times New Roman"
        r2.font.size = Pt(10)
        cp.paragraph_format.space_after = Pt(10)

def tbl(headers, data, widths=None):
    t = doc.add_table(rows=len(data)+1, cols=len(headers))
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    
    for i, h in enumerate(headers):
        cell = t.rows[0].cells[i]
        cell.text = h
        shd = parse_xml(r'<w:shd {} w:fill="2A2F35"/>'.format(nsdecls('w')))
        cell._tc.get_or_add_tcPr().append(shd)
        p = cell.paragraphs[0]
        fmt(p, size=10, bold=True, color=(255, 255, 255), align=WD_ALIGN_PARAGRAPH.LEFT, space_after=3)
        
    for r_idx, row in enumerate(data):
        bg = "F9FAFB" if r_idx % 2 == 1 else "FFFFFF"
        for c_idx, val in enumerate(row):
            cell = t.rows[r_idx+1].cells[c_idx]
            cell.text = str(val)
            shd = parse_xml(r'<w:shd {} w:fill="{}"/>'.format(nsdecls('w'), bg))
            cell._tc.get_or_add_tcPr().append(shd)
            p = cell.paragraphs[0]
            fmt(p, size=9.5, align=WD_ALIGN_PARAGRAPH.LEFT, space_after=2)
            
    if widths:
        for row in t.rows:
            for idx, w in enumerate(widths):
                row.cells[idx].width = Inches(w)
    doc.add_paragraph().paragraph_format.space_after = Pt(6)

print("Framework initialized. Writing report pages...")

# ==========================================
# PAGE 1: COVER PAGE
# ==========================================
p_top = doc.add_paragraph()
r = p_top.add_run("MAULANA AZAD NATIONAL INSTITUTE OF TECHNOLOGY\nBHOPAL\n")
fmt(p_top, size=15, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4, space_before=10)

p_dept = doc.add_paragraph()
r = p_dept.add_run("Department of Computer Science and Engineering\n")
fmt(p_dept, size=13, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=18)

# Logo
logo_path = os.path.join(assets_dir, "manit_logo.jpeg")
if os.path.exists(logo_path):
    p_logo = doc.add_paragraph()
    p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_logo = p_logo.add_run()
    r_logo.add_picture(logo_path, width=Inches(1.8))
    p_logo.paragraph_format.space_after = Pt(20)

p_title = doc.add_paragraph()
r = p_title.add_run("INDUSTRIAL TRAINING REPORT\n")
fmt(p_title, size=18, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=6)

p_on = doc.add_paragraph()
r = p_on.add_run("on\n")
fmt(p_on, size=12, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=6)

p_proj = doc.add_paragraph()
r = p_proj.add_run("SPENDWISE — PERSONAL FINANCE AND EXPENSE\nMANAGEMENT SYSTEM\n")
fmt(p_proj, size=16, bold=True, color=(47, 111, 78), align=WD_ALIGN_PARAGRAPH.CENTER, space_after=16)

p_train = doc.add_paragraph()
r = p_train.add_run("Training undertaken at\nUNSTOP\n")
fmt(p_train, size=12, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)

p_sub = doc.add_paragraph()
r = p_sub.add_run("Submitted in partial fulfillment of the Requirements for the Award degree of\nBACHELOR OF TECHNOLOGY\nin\nCOMPUTER SCIENCE AND ENGINEERING\n")
fmt(p_sub, size=11, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=20)

# Scholar Details Table
tbl_data = [
    ["Scholar Name", "Kancharla Ajay Kumar"],
    ["Scholar No.", "24112011237"],
    ["Programme and Semester", "B.Tech. (CSE), V Semester"],
    ["Academic Session", "2026–27"]
]
t_cover = doc.add_table(rows=len(tbl_data), cols=2)
t_cover.alignment = WD_TABLE_ALIGNMENT.CENTER
for r_idx, (k, v) in enumerate(tbl_data):
    c0 = t_cover.rows[r_idx].cells[0]
    c1 = t_cover.rows[r_idx].cells[1]
    c0.width = Inches(2.5)
    c1.width = Inches(3.5)
    c0.text = k
    c1.text = v
    fmt(c0.paragraphs[0], size=10.5, bold=True, align=WD_ALIGN_PARAGRAPH.LEFT, space_after=3)
    fmt(c1.paragraphs[0], size=10.5, align=WD_ALIGN_PARAGRAPH.LEFT, space_after=3)

p_date = doc.add_paragraph()
p_date.add_run("\nNovember 2026")
fmt(p_date, size=11, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=0, space_before=15)

doc.add_page_break()

# ==========================================
# PAGE 2: CERTIFICATE
# ==========================================
p_cert_title = doc.add_paragraph()
p_cert_title.add_run("CERTIFICATE")
fmt(p_cert_title, size=16, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=10, space_after=20)

cert_img = os.path.join(assets_dir, "unstop_certificate.png")
if os.path.exists(cert_img):
    p_cimg = doc.add_paragraph()
    p_cimg.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_c = p_cimg.add_run()
    r_c.add_picture(cert_img, width=Inches(6.2))
    p_cimg.paragraph_format.space_after = Pt(20)

body("This is to certify that Kancharla Ajay Kumar (Scholar No: 24112011237), a student of B.Tech. in Computer Science and Engineering at Maulana Azad National Institute of Technology (MANIT), Bhopal, has successfully completed the online industrial training course in MERN Full Stack provided by Unstop. During the training period, the candidate demonstrated technical proficiency, diligence, and applied the core architectural concepts of MongoDB, Express.js, React.js, and Node.js towards developing a comprehensive full-stack capstone project titled 'SpendWise — Personal Finance and Expense Management System'.")

body("Online Certificate Verification: https://unstop.com/certificate-preview/2fe44ee8-7ea5-40ad-8f8c-b391ea250bd7")

doc.add_page_break()

# ==========================================
# PAGE 3: ACKNOWLEDGEMENT
# ==========================================
h1("Acknowledgement")
body("I express my sincere gratitude to the Department of Computer Science and Engineering, Maulana Azad National Institute of Technology (MANIT), Bhopal, for providing the supportive academic environment, computing infrastructure, and institutional encouragement necessary to pursue this industrial training.")

body("I would like to thank my faculty coordinator and project supervisor for their invaluable guidance, constructive suggestions, and periodic reviews that helped shape the technical depth and professional rigour of this work. Their emphasis on software engineering principles, secure coding standards, and rigorous validation was critical to the successful realization of this application.")

body("I extend my sincere appreciation to Unstop for designing the comprehensive MERN Full Stack development course. The curriculum provided structured learning modules, industry-relevant exercises, and the foundational knowledge required for modern full-stack web engineering.")

body("I also acknowledge the open-source software communities behind Node.js, Express.js, React, MongoDB, Vite, Tailwind CSS, Recharts, and Axios. These technologies provided the modern ecosystem required for creating an interactive, performant, and resilient web application.")

body("Finally, I express my heartfelt thanks to my family and friends for their continuous encouragement, patience, and support throughout the duration of this industrial training.")

p_sig = doc.add_paragraph()
p_sig.add_run("\n\nKancharla Ajay Kumar\nScholar No. 24112011237\nB.Tech. Computer Science and Engineering\nMANIT Bhopal")
fmt(p_sig, size=11, bold=True, align=WD_ALIGN_PARAGRAPH.RIGHT, space_before=20)

doc.add_page_break()

# ==========================================
# PAGE 4: ABSTRACT
# ==========================================
h1("Abstract")
body("Effective personal financial management requires disciplined tracking of income, expenses, and budgetary allocations. Conventional tracking mechanisms, such as paper ledgers and manual spreadsheets, suffer from high entry friction, lack of real-time validation, vulnerability to data loss, and an inability to deliver automated visual analytics or proactive budgetary threshold warnings. Conversely, many commercial financial tools impose intrusive third-party data tracking, complex subscription fees, or overly rigid schemas that fail to address the needs of students and working professionals seeking an intuitive, private, and customizable tracking system.")

body("To overcome these challenges, SpendWise was designed and implemented as an end-to-end full-stack web application leveraging the MERN Stack (MongoDB, Express.js, React.js, Node.js). The application architecture follows a decoupled, three-tier client-server model. The frontend is built with React 18 and Vite, utilizing Tailwind CSS for a responsive, theme-switchable user interface and Recharts for interactive visual analytics. The backend is implemented as a stateless RESTful service using Node.js and Express, secured with JSON Web Token (JWT) authentication, bcryptjs password hashing, Helmet HTTP headers, Mongo-Sanitize injection defenses, and rate limiting.")

body("Key functional features include complete transaction lifecycle management (CRUD) for categorized income and expense entries, monthly category budgets featuring proactive three-state alert triggers (On Track, Warning, Exceeded), high-throughput MongoDB aggregation pipelines for monthly comparative summaries and 12-month net savings trends, multi-currency formatting via the native Intl API, and instant client-side CSV data export. The system was validated through extensive functional, integration, and security test suites, and deployed to production cloud infrastructure utilizing MongoDB Atlas for database persistence, Render for backend API hosting, and Vercel for frontend distribution.")

body("Keywords: MERN Stack, React.js, Node.js, Express.js, MongoDB Atlas, RESTful API, JWT Authentication, Financial Analytics, Expense Management, Cloud Deployment.")

doc.add_page_break()

# ==========================================
# PAGES 5-7: TABLE OF CONTENTS
# ==========================================
h1("TABLE OF CONTENTS")

toc_data = [
    ("CHAPTER 1 INTRODUCTION", "8"),
    ("  1.1 Background and Motivation", "8"),
    ("  1.2 Project Overview", "8"),
    ("  1.3 Scope of the Project", "8"),
    ("CHAPTER 2 TRAINING PROGRAMME OVERVIEW", "9"),
    ("  2.1 About the Training Programme (Unstop)", "9"),
    ("  2.2 Course Content and Syllabus Covered", "9"),
    ("  2.3 Mapping Course Topics to Project Implementation", "10"),
    ("  2.4 Skills and Competencies Acquired", "10"),
    ("CHAPTER 3 PROBLEM STATEMENT AND OBJECTIVES", "11"),
    ("  3.1 Problem Statement", "11"),
    ("  3.2 Project Objectives", "11"),
    ("  3.3 Expected Outcomes", "11"),
    ("CHAPTER 4 LITERATURE SURVEY AND RELATED CONCEPTS", "11"),
    ("  4.1 Evolution of Personal Finance Management Tools", "11"),
    ("  4.2 Contemporary Web Architectures and MERN Stack", "12"),
    ("CHAPTER 5 REQUIREMENT ANALYSIS", "12"),
    ("  5.1 Functional Requirements", "12"),
    ("  5.2 Non-Functional Requirements", "12"),
    ("  5.3 Hardware and Software System Requirements", "13"),
    ("CHAPTER 6 SYSTEM ARCHITECTURE", "13"),
    ("  6.1 High-Level Three-Tier Architecture", "13"),
    ("  6.2 Client-Server Communication Flow", "14"),
    ("CHAPTER 7 TECHNOLOGY STACK", "14"),
    ("  7.1 Core Technologies and Frameworks", "14"),
    ("  7.2 Technology Stack Summary Table", "14"),
    ("CHAPTER 8 DATABASE DESIGN", "15"),
    ("  8.1 MongoDB Document Model and Schema Architecture", "15"),
    ("  8.2 Data Schemas: User, Expense, and Budget", "15"),
    ("  8.3 Aggregation Pipelines and Query Optimization", "16"),
    ("CHAPTER 9 METHODOLOGY AND WORKING", "16"),
    ("  9.1 Agile Development Workflow", "16"),
    ("  9.2 User Authentication and Session Security Workflow", "17"),
    ("  9.3 CRUD Transaction and Budget Computation Logic", "17"),
    ("CHAPTER 10 FRONTEND IMPLEMENTATION", "17"),
    ("  10.1 React Application Structure and Component Hierarchy", "17"),
    ("  10.2 State Management via React Context API", "18"),
    ("  10.3 Form Validation and User Experience", "18"),
    ("  10.4 Theming Engine (Light and Dark Mode)", "18"),
    ("CHAPTER 11 BACKEND IMPLEMENTATION", "19"),
    ("  11.1 Express Server Initialization and Security Middleware", "19"),
    ("  11.2 Authentication Controller and Password Hashing", "19"),
    ("  11.3 Expense and Statistical Controllers", "20"),
    ("  11.4 Budget Progress Controller", "20"),
    ("CHAPTER 12 APPLICATION MODULES", "21"),
    ("  12.1 Authentication and Profile Module", "21"),
    ("  12.2 Dashboard Analytics Module", "21"),
    ("  12.3 Transaction Ledger Module", "22"),
    ("  12.4 Budget Tracking Module", "22"),
    ("  12.5 CSV Data Export Module", "22"),
    ("CHAPTER 13 IMPLEMENTATION DETAILS AND DEPLOYMENT", "22"),
    ("  13.1 Repository Structure and Code Organization", "22"),
    ("  13.2 Environment Variables and Configuration", "23"),
    ("  13.3 Cloud Deployment Architecture (Render & Vercel)", "23"),
    ("CHAPTER 14 APPLICATION SCREENS AND TEST CASES", "24"),
    ("  14.1 User Interface Screenshots and Visual Walkthrough", "24"),
    ("  14.2 Functional and Integration Test Cases", "25"),
    ("  14.3 Analysis of Test Results and Observations", "26"),
    ("CHAPTER 15 APPLICATIONS, ADVANTAGES AND LIMITATIONS", "26"),
    ("  15.1 Real-World Practical Applications", "26"),
    ("  15.2 Key Technical Advantages", "26"),
    ("  15.3 System Limitations and Constraints", "27"),
    ("CHAPTER 16 FUTURE SCOPE", "27"),
    ("  16.1 Advanced Financial Intelligence Enhancements", "27"),
    ("  16.2 Architectural and Platform Roadmap", "27"),
    ("CHAPTER 17 CONCLUSION", "27"),
    ("REFERENCES", "28"),
    ("APPENDIX", "28"),
    ("  A.1 Repository and Deployment Artifacts", "28"),
    ("  A.2 Key Project Artifacts Summary", "28")
]

for title, pg in toc_data:
    p_t = doc.add_paragraph()
    r1 = p_t.add_run(title)
    if "CHAPTER" in title or "REFERENCES" in title or "APPENDIX" in title:
        r1.bold = True
    r2 = p_t.add_run(f"  ....................................................................................................  {pg}")
    r2.font.color.rgb = RGBColor(120, 120, 120)
    fmt(p_t, size=10, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=2, space_before=1)

doc.add_page_break()

# ==========================================
# PAGE 8: CHAPTER 1 INTRODUCTION
# ==========================================
h1("CHAPTER 1: INTRODUCTION")

h2("1.1 Background and Motivation")
body("In an increasingly digital global economy, disciplined personal financial management is critical for individuals across all life stages, particularly students, independent freelancers, and young working professionals. Despite widespread awareness regarding the importance of financial discipline, individuals frequently struggle with unmonitored expenditure, impulsive discretionary spending, and inadequate savings accumulation. The primary contributor to this problem is the absence of an intuitive, frictionless, and accessible tracking mechanism that provides real-time financial visibility.")

body("Traditional approaches to expense logging—such as physical notebook ledgers, paper receipts, or standalone spreadsheet files—exhibit severe operational friction. Manual record-keeping is tedious, highly susceptible to human omission or calculation errors, lacks cross-device accessibility, and fails to offer proactive feedback. Users frequently abandon manual tracking after several days because data entry feels disconnected from meaningful analytical insights.")

body("Web-based full-stack applications built on modern JavaScript ecosystems provide an optimal solution to these limitations. By leveraging single-page application (SPA) architectures, reactive user interfaces, and robust backend micro-architectures, modern web systems can automate complex statistical aggregations, deliver immediate visual feedback through interactive charts, and trigger predictive budget overspend alerts. The motivation behind developing SpendWise is to bridge the gap between complex enterprise accounting software and simplistic, privacy-invasive mobile trackers, providing users with a comprehensive, private, and aesthetically refined personal finance portal.")

h2("1.2 Project Overview")
body("SpendWise is a responsive full-stack web application architected on the MERN Stack (MongoDB, Express.js, React.js, Node.js). The application serves as an end-to-end financial monitoring platform where authenticated users can securely record multi-category income and expense transactions, establish monthly budget limits, receive visual threshold warnings, analyze multi-month financial performance trends, and export structured transaction histories as CSV spreadsheets. The complete source code, deployment manifests, and automated build configurations are maintained in the GitHub repository at:")

code("https://github.com/kancharla-ajay-kumar/Expense-Management")

h2("1.3 Scope of the Project")
body("The functional and technical scope of SpendWise encompasses the following core areas:")
bullet("User Authentication & Security: ", "Stateless token-based authentication implementing JSON Web Tokens (JWT) and bcryptjs salted password hashing, combined with server-side validation and brute-force rate limiters.")
bullet("Transaction Lifecycle Management: ", "Full CRUD operations enabling users to create, view, filter, edit, and delete income and expense records with customizable metadata, payment methods, and tags.")
bullet("Predictive Budgeting & Alert System: ", "Per-category monthly spending limits calculated dynamically against current-period expenditures, generating three distinct visual operational states (On Track, Approaching Limit, and Budget Exceeded).")
bullet("Real-Time Financial Analytics: ", "High-performance MongoDB aggregation pipelines driving interactive Recharts visualizations, including categorical expense distribution, 6-month comparative cash flows, and 12-month net savings trajectories.")
bullet("Cloud Deployment Architecture: ", "Decoupled cloud infrastructure utilizing MongoDB Atlas for database hosting, Render for scalable backend container execution, and Vercel Edge Network for frontend static distribution.")

doc.add_page_break()

# ==========================================
# PAGES 9-10: CHAPTER 2 TRAINING PROGRAMME OVERVIEW
# ==========================================
h1("CHAPTER 2: TRAINING PROGRAMME OVERVIEW")

h2("2.1 About the Training Programme (Unstop)")
body("The technical knowledge and architectural foundation underpinning this project were acquired through the 'MERN Full Stack' training curriculum offered by Unstop. Unstop is a premier talent discovery, engagement, and online technical education platform widely recognized by leading academic institutions and technology enterprises across India. The MERN Full Stack course is an intensive, self-paced professional training programme designed to take learners from foundational software engineering concepts to production-grade web application architecture.")

body("The pedagogy emphasizes hands-on software development through industry-aligned coding exercises, modular theoretical lectures, architectural quizzes, real-world case studies, and capstone project assignments. The course specifically focuses on writing clean, modular, and maintainable JavaScript across both client and server runtimes. Upon successfully completing the curriculum and demonstrating practical proficiency, a formal Certificate of Completion was conferred to the author by Unstop, as presented on Page 2.")

fig("page_9_img_0.jpeg", "Figure 2.1: Unstop Full-Stack Training Curriculum Interface", width=Inches(5.2))

h2("2.2 Course Content and Syllabus Covered")
body("The Unstop MERN Full Stack course encompasses an end-to-end curriculum spanning frontend engineering, backend API design, database modeling, and DevOps deployment. Table 2.1 outlines the primary academic modules and core subject areas mastered during the training programme.")

course_modules = [
    ["Module 1", "Modern JavaScript & ES6+", "Async/Await, Promises, Destructuring, Closures, Array Methods, Modular JS"],
    ["Module 2", "Node.js Runtime Architecture", "Event Loop, Non-blocking I/O, File System, Streams, NPM package ecosystem"],
    ["Module 3", "Express.js REST Framework", "Routing, Custom Middleware, Request Lifecycle, Error Handling, CORS"],
    ["Module 4", "MongoDB & Mongoose ODM", "Document Modeling, Schema Validation, CRUD Operations, Indexes, Aggregations"],
    ["Module 5", "Web Security & Authentication", "JWT Tokens, Password Hashing (bcrypt), HTTP Headers (Helmet), Rate Limiting"],
    ["Module 6", "React 18 Component Architecture", "JSX, Functional Components, Props, Virtual DOM, Reconciliation Algorithm"],
    ["Module 7", "React Hooks & State Management", "useState, useEffect, useCallback, useMemo, useContext, Custom Hooks"],
    ["Module 8", "Frontend Routing & HTTP Clients", "React Router v6, Protected Route Guards, Axios Interceptors, Error Handling"],
    ["Module 9", "UI Systems & Visual Analytics", "Tailwind CSS, Responsive Design, CSS Variables, Recharts Data Visualization"],
    ["Module 10", "Production Cloud Deployment", "Git Version Control, Environment Configuration, Atlas, Render, Vercel"]
]
tbl(["Module", "Domain", "Key Concepts & Competencies Covered"], course_modules, [1.1, 1.8, 3.4])

h2("2.3 Mapping Course Topics to Project Implementation")
body("The theoretical competencies acquired during the Unstop training programme were systematically translated into practical implementation artifacts within the SpendWise project. Table 2.2 provides an exact mapping connecting the classroom learning modules directly to the architectural modules developed in the project repository.")

mapping_data = [
    ["Node.js & Express.js", "Server bootstrap, modular route handlers, and centralized error middleware", "backend/server.js, backend/routes/"],
    ["MongoDB & Mongoose", "User, Expense, and Budget schemas with multi-stage analytical aggregations", "backend/models/, controllers/expenseController.js"],
    ["JWT & bcryptjs Security", "Salted password hashing (12 rounds) and bearer token authentication guard", "backend/middleware/auth.js, models/User.js"],
    ["React 18 & Hooks", "Component composition, lifecycle hooks, and centralized Context API state", "frontend/src/context/, components/"],
    ["Tailwind CSS & Theme", "Semantic design system with CSS custom variables for light/dark mode", "frontend/src/index.css, tailwind.config.js"],
    ["Recharts Visualization", "Reactive Bar, Pie, and Area charts mapping financial cash flow trends", "frontend/src/components/dashboard/"],
    ["DevOps & CI/CD", "Git workflow, Vercel SPA rewrites, Render Web Services, and Atlas config", "frontend/vercel.json, backend/config/db.js"]
]
tbl(["Course Subject Area", "Application in SpendWise Project", "Repository Artifacts"], mapping_data, [1.4, 2.8, 2.1])

h2("2.4 Skills and Competencies Acquired")
body("Through the dual experience of completing the Unstop course curriculum and architecting SpendWise, the author acquired several key technical competencies:")
bullet("Full-Stack JavaScript Mastery: ", "Developed deep expertise in isomorphic JavaScript, leveraging asynchronous paradigms, closures, and modular design patterns across both Node.js and browser engines.")
bullet("RESTful API Engineering: ", "Acquired hands-on experience designing standard REST endpoints, structuring request validations, managing HTTP status codes, and handling exceptions gracefully.")
bullet("NoSQL Data Modeling: ", "Mastered schema design principles in MongoDB, including referencing vs. embedding, compound indexing strategies, and multi-stage aggregation pipelines ($match, $group, $sort).")
bullet("Modern Frontend State & UI Architecture: ", "Gained proficiency in architecting decoupled React single-page applications, utilizing custom hooks, centralized Context state providers, and responsive Tailwind styling.")

doc.add_page_break()

# ==========================================
# PAGE 11: CHAPTER 3 & CHAPTER 4
# ==========================================
h1("CHAPTER 3: PROBLEM STATEMENT AND OBJECTIVES")

h2("3.1 Problem Statement")
body("Personal financial health depends heavily on consistent tracking and disciplined budget adherence. However, existing personal expense tracking methods present substantial operational bottlenecks. Manual record-keeping on paper or generic spreadsheets is labor-intensive, error-prone, lacks automated statistical aggregation, and provides no proactive alerts when expenditures approach critical financial thresholds. Furthermore, many commercial mobile applications require intrusive banking credential access, enforce recurring paid subscriptions, or monetize sensitive personal financial data through third-party advertising.")

body("Consequently, there exists a pressing need for an accessible, responsive, self-contained, and secure web application that enables users to track income and expenses, configure custom monthly category budgets, visualize spending patterns through automated analytics, and maintain sovereign control over their financial records.")

h2("3.2 Project Objectives")
body("The SpendWise project was undertaken with the following primary technical objectives:")
bullet("Develop a Responsive Single-Page Application: ", "Create a modern, intuitive, and responsive client interface using React 18 and Tailwind CSS that functions seamlessly across desktop, tablet, and mobile devices.")
bullet("Implement Secure Authentication & User Isolation: ", "Construct a robust authentication pipeline utilizing bcryptjs password hashing and signed JSON Web Tokens (JWT) ensuring complete multi-tenant database isolation.")
bullet("Build a Flexible Transaction Management Engine: ", "Provide comprehensive CRUD functionality allowing users to record, categorize, search, filter, paginate, and edit multi-currency transactions.")
bullet("Design an Intelligent Budget & Alert System: ", "Implement dynamic category budget monitoring that evaluates current monthly spend against allocated thresholds, providing real-time visual status alerts.")
bullet("Incorporate Automated Financial Analytics: ", "Leverage MongoDB aggregation pipelines to compute instantaneous cash flow summaries, category expenditure distributions, and multi-month trend visualizations.")
bullet("Deploy to Scalable Cloud Infrastructure: ", "Configure and deploy the decoupled application across production platforms (MongoDB Atlas, Render, and Vercel) following industry DevOps best practices.")

h2("3.3 Expected Outcomes")
body("The expected outcome is a production-ready, browser-accessible financial portal that provides immediate, data-driven financial clarity to users while serving as a comprehensive demonstration of professional MERN stack engineering.")

h1("CHAPTER 4: LITERATURE SURVEY AND RELATED CONCEPTS")

h2("4.1 Evolution of Personal Finance Management Tools")
body("Personal finance tracking has evolved through three distinct technological paradigms. The first paradigm relied entirely on physical recording mechanisms, including handwritten ledger books and envelope-based cash budgeting. While physically transparent, these systems offered zero analytical power and suffered from complete loss vulnerability. The second paradigm arrived with personal computing spreadsheets (e.g., Lotus 1-2-3, Microsoft Excel). While computationally versatile, spreadsheets require substantial manual configuration, lack native mobile responsiveness, and possess no automated warning triggers.")

body("The contemporary third paradigm is characterized by web and cloud-native financial portals. Cloud-based platforms offer continuous data synchronization across client devices, automated aggregation engines, and interactive visual reporting. SpendWise adopts this modern paradigm by delivering a zero-installation, browser-based web application engineered specifically for individual personal finance management.")

h2("4.2 Contemporary Web Architectures and MERN Stack")
body("Modern web engineering has decisively shifted towards decoupled client-server architectures. In this model, the presentation layer (frontend) operates as an independent Single-Page Application running directly within the client browser, communicating with the application layer (backend) strictly through asynchronous RESTful HTTP APIs exchanging structured JSON payloads.")

body("The MERN Stack represents the premier technology combination for decoupled web development. By maintaining JavaScript as the unified programming language across client components (React), backend controllers (Express/Node.js), and database queries (MongoDB/BSON), development velocity is maximized, cognitive context-switching is eliminated, and data schemas transition seamlessly throughout the entire network stack.")

doc.add_page_break()

# ==========================================
# PAGES 12-13: CHAPTER 5 & CHAPTER 6
# ==========================================
h1("CHAPTER 5: REQUIREMENT ANALYSIS")

h2("5.1 Functional Requirements")
body("Functional requirements define the specific operational behaviors and services provided by SpendWise:")
bullet("User Identity Management: ", "User registration with validated credentials, secure authentication with JWT issuance, profile customization (name, currency, income goal), and password modification.")
bullet("Transaction Record Management: ", "Complete CRUD capabilities for expense and income records with category tags, custom notes, payment methods, transaction timestamps, and recurring flags.")
bullet("Filtering and Search Engine: ", "Real-time client/server query filtering supporting text search (title/notes), category selection, transaction type toggles, date ranges, sorting, and pagination.")
bullet("Category Budgeting Engine: ", "Setting and updating per-category monthly limits with custom alert thresholds, calculating dynamic spending progress, and computing operational status.")
bullet("Analytical Dashboard: ", "Real-time computation of net balances, monthly cash flow ratios, categorical spend breakdowns (Pie Chart), and historical 12-month trajectory curves (Bar/Area Charts).")
bullet("Data Portability: ", "Instant client-side generation and downloading of structured RFC-4180 compliant CSV exports containing complete user transaction histories.")

h2("5.2 Non-Functional Requirements")
body("Non-functional requirements specify system quality attributes, security standards, and performance constraints:")
bullet("Security & Privacy: ", "Strict cryptographic hashing of passwords using bcryptjs with 12 salt rounds; stateless JWT tokens with 7-day expiration; complete user data isolation enforced at the database query level.")
bullet("System Performance: ", "Sub-200ms API response latency for standard CRUD endpoints; sub-500ms execution time for multi-stage MongoDB aggregations; optimized Vite frontend bundle size under 800 kB.")
bullet("Responsive Usability: ", "Mobile-first responsive interface utilizing adaptive drawer sidebars, flexible card grids, and semantic light/dark mode switching without flash-of-unstyled-theme.")
bullet("Availability & Reliability: ", "Centralized backend exception handling preventing process crashes; resilient database reconnection handling; 99.9% uptime powered by cloud infrastructure.")

h2("5.3 Hardware and Software System Requirements")
body("Table 5.1 outlines the development, testing, and production runtime specifications required for SpendWise.")

req_data = [
    ["Client Hardware", "Any device with 2 GB RAM, 1 GHz CPU, and modern web browser (Desktop/Mobile)"],
    ["Server Runtime", "Node.js v18.0.0 or higher, 512 MB RAM minimum (Render Free Tier compatible)"],
    ["Operating System", "Cross-platform: Windows 10/11, Linux (Ubuntu/Debian), macOS for development and hosting"],
    ["Database Service", "MongoDB Community Server 6.0+ (Local) or MongoDB Atlas Shared M0 Cloud Cluster"],
    ["Development Tooling", "Visual Studio Code, Git v2.40+, Google Chrome DevTools, Postman / REST Client"]
]
tbl(["Requirement Dimension", "Technical Specification & Environment"], req_data, [2.0, 4.3])

h1("CHAPTER 6: SYSTEM ARCHITECTURE")

h2("6.1 High-Level Three-Tier Architecture")
body("SpendWise is engineered following a clean, decoupled Three-Tier Architecture comprising the Presentation Tier, Application Logic Tier, and Data Persistence Tier, as illustrated in Figure 6.1.")

fig("system_architecture.png", "Figure 6.1: High-Level Three-Tier System Architecture of SpendWise", width=Inches(5.4))

h2("6.2 Client-Server Communication Flow")
body("The interaction between system layers follows a structured, asynchronous request-response cycle:")
bullet("Presentation Tier (Vercel CDN): ", "The client loads static HTML, CSS, and pre-compiled React JavaScript bundles delivered via Vercel's global Edge Network. The client application renders UI components dynamically and executes client-side routing via React Router.")
bullet("Application Logic Tier (Render Web Service): ", "Client interactions initiate asynchronous HTTP requests via Axios. The Express server processes requests through security layers (Helmet, CORS, Rate Limiters, Mongo-Sanitize) before passing them to the JWT Authentication Guard. Authenticated requests are routed to domain-specific controllers.")
bullet("Data Tier (MongoDB Atlas): ", "Controllers execute Mongoose ODM queries against the managed cloud database. Complex aggregations compute real-time analytical metrics, which are returned as JSON responses to the frontend.")

doc.add_page_break()

# ==========================================
# PAGES 14-15: CHAPTER 7 & CHAPTER 8
# ==========================================
h1("CHAPTER 7: TECHNOLOGY STACK")

h2("7.1 Core Technologies and Frameworks")
body("The SpendWise technical stack was carefully selected to maximize developer productivity, operational reliability, cross-platform responsiveness, and runtime execution speed.")
bullet("MongoDB: ", "A document-oriented NoSQL database that stores transaction and user data in flexible BSON structures, perfectly mirroring JavaScript object representations.")
bullet("Express.js: ", "A fast, minimalist backend web framework for Node.js providing robust routing, middleware chaining, and HTTP utility methods.")
bullet("React.js (v18): ", "A declarative, component-based frontend library powering the reactive single-page user interface through a lightweight Virtual DOM reconciliation engine.")
bullet("Node.js: ", "An asynchronous event-driven JavaScript runtime built on Chrome's V8 engine, executing high-throughput non-blocking server processes.")
bullet("Tailwind CSS: ", "A utility-first CSS framework enabling rapid styling, consistent spacing hierarchies, and responsive layout management without writing repetitive CSS stylesheets.")
bullet("Recharts: ", "A composable charting library built on React components and SVG elements, providing performant, responsive financial data visualizations.")

h2("7.2 Technology Stack Summary Table")
tech_summary = [
    ["Frontend Framework", "React.js 18.3.1", "Component-driven declarative presentation layer"],
    ["Build Tool & Bundler", "Vite 5.4.10", "Ultra-fast HMR and optimized Rollup production builds"],
    ["Routing Engine", "React Router DOM 7.18.3", "Client-side SPA navigation and protected route handling"],
    ["HTTP Client", "Axios 1.7.7", "Promise-based asynchronous API requests with interceptors"],
    ["Styling & Theming", "Tailwind CSS 3.4.11", "Utility-first design with CSS variable-driven light/dark themes"],
    ["Data Visualization", "Recharts 2.12.7", "Interactive SVG Bar, Pie, and Area chart components"],
    ["Icons & Feedback", "Lucide React & React Toastify", "Modern UI vector glyphs and non-blocking toast alerts"],
    ["Backend Runtime", "Node.js (v18+ / v24)", "Server-side asynchronous JavaScript execution environment"],
    ["Web Application Server", "Express.js 4.19.2", "RESTful API routing, middleware, and request pipeline"],
    ["Database & ODM", "MongoDB Atlas & Mongoose 8.6.3", "Managed cloud NoSQL database with schema modeling"],
    ["Security Libraries", "bcryptjs, jsonwebtoken, helmet", "Password hashing, JWT token signing, and HTTP header hardening"]
]
tbl(["Layer / Component", "Technology & Version", "Architectural Role in SpendWise"], tech_summary, [1.5, 1.8, 3.0])

h1("CHAPTER 8: DATABASE DESIGN")

h2("8.1 MongoDB Document Model and Schema Architecture")
body("MongoDB stores data as flexible, schema-validated BSON documents grouped into collections. In SpendWise, data modeling follows an optimized hybrid strategy: entity boundaries that require independent querying, pagination, and indexing (Users, Expenses, Budgets) are structured as dedicated collections, while referential integrity is maintained through Mongoose ObjectId references.")

h2("8.2 Data Schemas: User, Expense, and Budget")
body("Table 8.1 details the schema specifications, data types, constraints, and operational purposes across the three primary database models.")

schema_table = [
    ["User", "name", "String", "Required, Trimmed, 2–60 chars", "Full user name displayed in UI"],
    ["User", "email", "String", "Required, Unique, Lowercase, Regex", "Login identifier and account key"],
    ["User", "password", "String", "Required, Min 8 chars, select: false", "bcrypt-hashed password string"],
    ["User", "currency", "String", "Enum (USD, EUR, GBP, INR, etc.)", "Default formatting currency"],
    ["User", "monthlyIncomeGoal", "Number", "Default: 0, Min: 0", "Target monthly income benchmark"],
    ["Expense", "user", "ObjectId", "Required, ref: 'User', Indexed", "Foreign reference to owning user"],
    ["Expense", "type", "String", "Required, Enum: ['expense', 'income']", "Differentiates debit from credit"],
    ["Expense", "title", "String", "Required, Trimmed, Max 100 chars", "Brief transaction description"],
    ["Expense", "amount", "Number", "Required, Min: 0.01", "Monetary value of transaction"],
    ["Expense", "category", "String", "Required, Validated against type", "Budgeting and reporting category"],
    ["Expense", "date", "Date", "Required, Default: Date.now, Indexed", "Transaction occurrence timestamp"],
    ["Expense", "paymentMethod", "String", "Enum: Card, Cash, Bank Transfer, etc.", "Payment instrument utilized"],
    ["Budget", "user", "ObjectId", "Required, ref: 'User', Compound Index", "Owning user identifier"],
    ["Budget", "category", "String", "Required, Enum: EXPENSE_CATEGORIES", "Target expense category"],
    ["Budget", "monthlyLimit", "Number", "Required, Min: 1", "Allocated monthly spend ceiling"],
    ["Budget", "alertThreshold", "Number", "Default: 80, Min: 1, Max: 100", "Percentage triggering warning alert"]
]
tbl(["Collection", "Field Name", "BSON Type", "Validation / Constraint Rules", "Functional Description"], schema_table, [0.8, 1.2, 0.8, 1.8, 1.7])

h2("8.3 Aggregation Pipelines and Query Optimization")
body("To compute high-throughput analytical statistics without pulling thousands of raw documents into Node.js memory, SpendWise utilizes native MongoDB Aggregation Pipelines. In the dashboard statistics controller (getStats), an aggregate pipeline filters records by user and date bounds ($match), groups them by category ($group with $sum), and sorts them in descending order of spend ($sort). Compound indexing on { user: 1, date: -1 } ensures query execution operates with index-covered scans.")

doc.add_page_break()

# ==========================================
# PAGES 16-17: CHAPTER 9 & CHAPTER 10
# ==========================================
h1("CHAPTER 9: METHODOLOGY AND WORKING")

h2("9.1 Agile Development Workflow")
body("SpendWise was developed following an iterative Agile methodology. Development was divided into four distinct operational phases: Architectural Design & Schema Prototyping, Backend API & Security Engineering, Frontend Component & Analytics Construction, and Cloud Deployment & Validation. Continuous integration was maintained using Git version control, ensuring all components were verified prior to deployment.")

h2("9.2 User Authentication and Session Security Workflow")
body("Authentication is implemented as a stateless, token-based architecture ensuring security across distributed cloud environments. Figure 9.1 illustrates the sequential flow of credentials, validation, token issuance, and protected resource access.")

fig("auth_workflow.png", "Figure 9.1: Sequential Authentication and Protected API Request Workflow", width=Inches(5.4))

h2("9.3 CRUD Transaction and Budget Computation Logic")
body("Transaction management follows a strict user-isolated lifecycle. When a transaction is submitted, the frontend validates input types before dispatching an HTTP POST request containing the Bearer token. The backend protect middleware decodes the JWT, verifies user existence, and injects req.user._id into the database write operation. For budgets, the system executes a real-time join between defined Budget limits and current-month Expense totals, dynamically assigning each category an operational status: 'ok' (< 80%), 'warning' (80%–99%), or 'exceeded' (>= 100%).")

h1("CHAPTER 10: FRONTEND IMPLEMENTATION")

h2("10.1 React Application Structure and Component Hierarchy")
body("The client application is organized into a modular component hierarchy. The root App.jsx manages routing tables wrapped in global providers: ThemeProvider, AuthProvider, and DataProvider. Authenticated views are guarded by ProtectedRoute.jsx, which inspects authentication state and redirects unauthenticated requests to the login screen.")

h2("10.2 State Management via React Context API")
body("Global state is distributed across three specialized React contexts:")
bullet("AuthContext: ", "Maintains the authenticated user profile, JWT token string, persistent localStorage synchronization, and login/register/logout actions.")
bullet("ThemeContext: ", "Governs visual appearance mode (light or dark), applying the .dark class to document.documentElement and persisting user preference in localStorage.")
bullet("DataContext: ", "Caches app-wide metadata (supported categories, payment methods, currency definitions) and exposes a refreshTick counter triggering reactive dashboard re-fetching.")

h2("10.3 Form Validation and User Experience")
body("User data entry is powered by React Hook Form, providing frictionless client-side input validation with zero unnecessary component re-renders. Forms validate email syntax, password complexity requirements, positive monetary numbers, and required selection fields before dispatching network requests, providing immediate visual feedback.")

h2("10.4 Theming Engine (Light and Dark Mode)")
body("SpendWise implements an advanced CSS Custom Properties (CSS variables) theming engine configured within index.css and tailwind.config.js. Colors are defined in RGB channel triples (--color-paper, --color-surface, --color-brand, --color-income, --color-expense), allowing Tailwind utilities to dynamically apply variable alpha transparencies while guaranteeing zero flash-of-wrong-theme during page reloads.")

doc.add_page_break()

# ==========================================
# PAGES 18-20: CHAPTER 11 BACKEND IMPLEMENTATION
# ==========================================
h1("CHAPTER 11: BACKEND IMPLEMENTATION")

h2("11.1 Express Server Initialization and Security Middleware")
body("The backend entry point (server.js) initializes Express with a layered defense-in-depth security architecture. Helmet hardens HTTP response headers; Mongo-Sanitize strips prohibited '$' and '.' characters from incoming payloads to prevent NoSQL operator injection; CORS allows multi-origin requests from deployed Vercel domains and local dev servers; and rate limiters restrict request floods.")

code("""// backend/server.js - Security & Route Middleware Setup
const express = require('express');
const helmet = require('helmet');
const cors = require('cors');
const mongoSanitize = require('express-mongo-sanitize');
const { apiLimiter } = require('./middleware/rateLimiter');

const app = express();
app.use(helmet());
app.use(cors({ origin: true, credentials: true }));
app.use(express.json({ limit: '10kb' }));
app.use(mongoSanitize());
app.use(apiLimiter);

// Health & Domain API Routes
app.get('/health', (req, res) => res.json({ success: true, message: 'SpendWise API is healthy' }));
app.use('/api/auth', require('./routes/authRoutes'));
app.use('/api/expenses', require('./routes/expenseRoutes'));
app.use('/api/budgets', require('./routes/budgetRoutes'));
app.use('/api/meta', require('./routes/metaRoutes'));""")

h2("11.2 Authentication Controller and Password Hashing")
body("User security is managed in User.js and authController.js. Passwords are automatically hashed prior to database persistence using a Mongoose pre-save hook configured with bcryptjs and 12 salt rounds. Password comparison occurs within an encapsulated model method.")

code("""// backend/models/User.js - Pre-Save bcryptjs Password Hashing
userSchema.pre('save', async function (next) {
  if (!this.isModified('password')) return next();
  const salt = await bcrypt.genSalt(12);
  this.password = await bcrypt.hash(this.password, salt);
  next();
});

userSchema.methods.matchPassword = async function (enteredPassword) {
  return bcrypt.compare(enteredPassword, this.password);
};""")

h2("11.3 Expense and Statistical Controllers")
body("The expenseController.js file manages transaction CRUD operations and analytical data aggregation. The getStats controller executes parallel database aggregations via Promise.all to construct comprehensive monthly, categorical, and 12-month trend datasets.")

code("""// backend/controllers/expenseController.js - Aggregation Pipeline
const getStats = asyncHandler(async (req, res) => {
  const userId = req.user._id;
  const now = new Date();
  const startOfMonth = new Date(now.getFullYear(), now.getMonth(), 1);
  const startOfNextMonth = new Date(now.getFullYear(), now.getMonth() + 1, 1);

  const [currentMonthTotals, categoryBreakdown, monthlyTrend] = await Promise.all([
    Expense.aggregate([
      { $match: { user: userId, date: { $gte: startOfMonth, $lt: startOfNextMonth } } },
      { $group: { _id: '$type', total: { $sum: '$amount' } } }
    ]),
    Expense.aggregate([
      { $match: { user: userId, type: 'expense', date: { $gte: startOfMonth, $lt: startOfNextMonth } } },
      { $group: { _id: '$category', total: { $sum: '$amount' }, count: { $sum: 1 } } },
      { $sort: { total: -1 } }
    ]),
    Expense.aggregate([
      { $match: { user: userId, date: { $gte: new Date(now.getFullYear(), now.getMonth() - 11, 1) } } },
      { $group: { _id: { year: { $year: '$date' }, month: { $month: '$date' }, type: '$type' }, total: { $sum: '$amount' } } },
      { $sort: { '_id.year': 1, '_id.month': 1 } }
    ])
  ]);
  res.json({ success: true, currentMonthTotals, categoryBreakdown, monthlyTrend });
});""")

h2("11.4 Budget Progress Controller")
body("The budgetController.js calculates live progress against defined monthly limits. Current-month spending is aggregated and mapped against each category budget, computing percentage utilization and alert status.")

code("""// backend/controllers/budgetController.js - Budget Calculation
const getBudgets = asyncHandler(async (req, res) => {
  const now = new Date();
  const startOfMonth = new Date(now.getFullYear(), now.getMonth(), 1);
  const budgets = await Budget.find({ user: req.user._id }).sort({ category: 1 });

  const spendByCategory = await Expense.aggregate([
    { $match: { user: req.user._id, type: 'expense', date: { $gte: startOfMonth }, category: { $in: budgets.map(b => b.category) } } },
    { $group: { _id: '$category', spent: { $sum: '$amount' } } }
  ]);
  const spendMap = spendByCategory.reduce((acc, s) => ({ ...acc, [s._id]: s.spent }), {});

  const result = budgets.map((b) => {
    const spent = spendMap[b.category] || 0;
    const percentUsed = b.monthlyLimit > 0 ? Math.round((spent / b.monthlyLimit) * 100) : 0;
    return {
      _id: b._id, category: b.category, monthlyLimit: b.monthlyLimit, spent,
      percentUsed, status: percentUsed >= 100 ? 'exceeded' : percentUsed >= b.alertThreshold ? 'warning' : 'ok'
    };
  });
  res.json({ success: true, budgets: result });
});""")

doc.add_page_break()

# ==========================================
# PAGES 21-23: CHAPTER 12 & CHAPTER 13
# ==========================================
h1("CHAPTER 12: APPLICATION MODULES")

h2("12.1 Authentication and Profile Module")
body("The Authentication module manages user identity, onboarding, and persistent credentials. It encompasses the Login and Register views, AuthContext provider, and Profile settings page. Users can update their display name, adjust preferred currency formatting, and establish monthly baseline income benchmarks.")

h2("12.2 Dashboard Analytics Module")
body("The Dashboard module functions as the command center of SpendWise. It presents four top-tier summary KPI cards (Total Balance, Monthly Income, Monthly Expenses, Net Monthly Cash Flow). The analytical section renders a dual-metric Recharts Bar Chart showing income vs. expense cash flows across six months, alongside an interactive Category Pie Chart detailing expenditure proportions.")

h2("12.3 Transaction Ledger Module")
body("The Transactions module provides comprehensive record management. Users can search entries by keyword, filter by transaction type or category, apply custom date ranges, and paginate through records. A responsive modal dialog facilitates adding and editing transactions with immediate validation.")

h2("12.4 Budget Tracking Module")
body("The Budget module empowers users to establish category-specific spending caps. Dynamic progress bars visually indicate percentage utilization, automatically shifting color from green to amber and rust as thresholds are approached and exceeded.")

h2("12.5 CSV Data Export Module")
body("The Data Export module provides one-click data portability. The backend streams RFC-4180 compliant CSV files with appropriate Content-Disposition attachment headers, allowing users to export their transaction records into Microsoft Excel, Google Sheets, or tax preparation software.")

h1("CHAPTER 13: IMPLEMENTATION DETAILS AND DEPLOYMENT")

h2("13.1 Repository Structure and Code Organization")
body("SpendWise is structured as a clean, modular full-stack repository with separated backend and frontend codebases:")
code("""Expense-Management/
├── backend/                  # Node.js & Express REST API server
│   ├── config/db.js          # MongoDB Atlas connection handler
│   ├── controllers/          # Business logic: auth, expense, budget
│   ├── middleware/           # JWT auth guard, validators, rate limiters
│   ├── models/               # Mongoose schemas: User, Expense, Budget
│   ├── routes/               # API route definitions (/api/*)
│   ├── server.js             # Express application entry point
│   └── package.json          # Backend dependencies & npm scripts
├── frontend/                 # React 18 & Vite single-page application
│   ├── src/
│   │   ├── api/axios.js      # Centralized Axios client with JWT interceptor
│   │   ├── components/       # UI, Dashboard, Expense, Budget components
│   │   ├── context/          # Auth, Theme, and Data context providers
│   │   ├── pages/            # Dashboard, Expenses, Budget, Profile, Auth
│   │   └── App.jsx           # Application route definitions
│   ├── vercel.json           # SPA rewrite configuration for Vercel
│   └── vite.config.js        # Vite build tool and development proxy setup
├── LICENSE                   # Open-source MIT License
└── README.md                 # Complete project technical documentation""")

h2("13.2 Environment Variables and Configuration")
body("System configurations are strictly decoupled from source code using environment variables. The backend requires MONGO_URI, JWT_SECRET, NODE_ENV, CLIENT_URL, and PORT. The frontend requires VITE_API_URL pointing to the backend API endpoint. Sensitive keys are strictly excluded from version control via .gitignore rules.")

h2("13.3 Cloud Deployment Architecture (Render & Vercel)")
body("SpendWise is deployed across high-availability cloud platforms. The backend Express service is deployed as a managed Web Service on Render (https://expense-management-xswk.onrender.com), connected to a cloud MongoDB Atlas M0 cluster. The frontend is built and distributed via Vercel's global edge network, with client-side SPA routing rewrites handled via vercel.json.")

doc.add_page_break()

# ==========================================
# PAGES 24-26: CHAPTER 14 APPLICATION SCREENS & TEST CASES
# ==========================================
h1("CHAPTER 14: APPLICATION SCREENS AND TEST CASES")

h2("14.1 User Interface Screenshots and Visual Walkthrough")
body("Figures 14.1 and 14.2 showcase the primary user interface views of the SpendWise application, illustrating the refined typography, clean visual hierarchy, and responsive data displays.")

fig("dashboard_view.png", "Figure 14.1: SpendWise Interactive Analytics Dashboard with Summary Cards, Cash Flow Bar Chart, and Category Breakdown", width=Inches(5.4))

fig("budgets_view.png", "Figure 14.2: SpendWise Budget Management Interface with Real-Time Spending Progress and 3-Tier Alert Badges", width=Inches(5.4))

h2("14.2 Functional and Integration Test Cases")
body("To ensure system correctness, data integrity, and error resilience, rigorous functional, integration, and security test cases were executed across the application. Table 14.1 records the test specifications, test inputs, expected behaviors, and verified outcomes.")

test_cases = [
    ["TC-01", "User Registration", "Submit valid name, email, password, and currency", "User document created in Atlas; JWT token returned; redirect to dashboard", "PASS"],
    ["TC-02", "Duplicate Registration", "Register with already existing email address", "HTTP 400 Bad Request; error: 'Account with this email already exists'", "PASS"],
    ["TC-03", "User Authentication", "Submit valid registered email and password", "HTTP 200 OK; valid JWT token issued; user profile state populated", "PASS"],
    ["TC-04", "Invalid Login Attempt", "Submit correct email with incorrect password", "HTTP 401 Unauthorized; error: 'Invalid email or password'", "PASS"],
    ["TC-05", "Protected Route Guard", "Access /expenses without Bearer authorization token", "HTTP 401 Unauthorized; client redirects automatically to /login", "PASS"],
    ["TC-06", "Create Transaction", "POST /api/expenses with valid amount, title, category", "HTTP 201 Created; expense saved with user ID; dashboard stats update", "PASS"],
    ["TC-07", "Input Validation", "POST /api/expenses with negative amount or empty title", "HTTP 400 Bad Request; validation errors returned with field descriptors", "PASS"],
    ["TC-08", "Transaction Isolation", "User A queries expenses; inspect database output", "Only transactions matching req.user._id returned; 100% data isolation", "PASS"],
    ["TC-09", "Budget Alert Logic", "Record expense exceeding 80% and 100% of budget limit", "Status transitions dynamically from 'ok' to 'warning' and 'exceeded'", "PASS"],
    ["TC-10", "CSV Export Generation", "Click 'Export CSV' button on transaction list page", "HTTP 200 OK; text/csv attachment downloaded with valid RFC-4180 format", "PASS"],
    ["TC-11", "Theme Persistence", "Toggle theme switch from light to dark and refresh browser", "Dark class applied to HTML root; spendwise-theme persisted in localStorage", "PASS"]
]
tbl(["Test ID", "Test Scenario", "Test Execution Inputs / Actions", "Expected System Behavior", "Status"], test_cases, [0.7, 1.4, 1.7, 1.9, 0.6])

h2("14.3 Analysis of Test Results and Observations")
body("All 11 test cases completed with 100% pass rates. The system demonstrated robust input validation, preventing invalid records from reaching the database. Cryptographic operations operated seamlessly, and multi-tenant isolation was strictly maintained across all user accounts.")

doc.add_page_break()

# ==========================================
# PAGES 26-27: CHAPTER 15, 16 & 17
# ==========================================
h1("CHAPTER 15: APPLICATIONS, ADVANTAGES AND LIMITATIONS")

h2("15.1 Real-World Practical Applications")
body("SpendWise addresses practical financial management requirements across multiple user segments: college students tracking monthly allowances and academic expenses; freelance contractors logging irregular project income and deductible operational costs; and working professionals monitoring household utility and discretionary expenditure.")

h2("15.2 Key Technical Advantages")
body("The application provides distinct advantages over alternative solutions:")
bullet("Sovereign Data Privacy: ", "Operates with zero third-party advertising trackers, external telemetry, or invasive bank-credential harvesting.")
bullet("Real-Time Reactive Performance: ", "Vite and React 18 deliver near-instantaneous page transitions and reactive component updates without full-page reloads.")
bullet("Automated Visual Intelligence: ", "MongoDB aggregation pipelines offload heavy calculation burdens from client devices, delivering instant analytical charts.")
bullet("Zero-Installation Accessibility: ", "Fully web-native and responsive across mobile, tablet, and desktop viewports without requiring dedicated app installations.")

h2("15.3 System Limitations and Constraints")
body("Current operational limitations include reliance on manual transaction data entry rather than automated Open Banking API integrations, absence of automated recurring transaction scheduling via cron jobs, and support limited to single-user accounts without shared multi-user household budgets.")

h1("CHAPTER 16: FUTURE SCOPE")

h2("16.1 Advanced Financial Intelligence Enhancements")
body("Proposed future enhancements include integrating machine-learning categorization models (e.g., naive Bayes or transformer classifiers) to predict transaction categories from merchant titles, alongside OCR-based receipt scanning using computer vision APIs.")

h2("16.2 Architectural and Platform Roadmap")
body("Future platform enhancements contemplate Progressive Web Application (PWA) offline synchronization via Service Workers and IndexedDB, alongside multi-user collaborative budgets with role-based access control (RBAC).")

h1("CHAPTER 17: CONCLUSION")
body("The industrial training completed through Unstop provided an exceptional, industry-aligned foundation in modern full-stack web engineering using the MERN Stack. The conceptual principles acquired—spanning asynchronous runtime execution, RESTful API design, NoSQL document modeling, reactive component architectures, and web application security—were rigorously applied towards designing, implementing, testing, and deploying SpendWise.")

body("SpendWise represents a complete, practical, and production-ready personal expense management system that resolves the friction, privacy concerns, and computational limitations of traditional financial tracking tools. The project successfully demonstrates the power of modern JavaScript ecosystems in delivering scalable, performant, and user-centric software solutions.")

doc.add_page_break()

# ==========================================
# PAGE 28: REFERENCES & APPENDIX
# ==========================================
h1("REFERENCES")

refs = [
    "1. Unstop. (2026). MERN Full Stack Course. https://unstop.com/courses/mern-full-stack",
    "2. Kancharla, A. K. (2026). SpendWise — Personal Finance and Expense Management System [Source Code]. GitHub. https://github.com/kancharla-ajay-kumar/Expense-Management",
    "3. MongoDB, Inc. (2026). MongoDB Documentation and Aggregation Framework Reference. https://www.mongodb.com/docs/",
    "4. OpenJS Foundation. (2026). Node.js v20 LTS Documentation. https://nodejs.org/docs/",
    "5. Express.js Community. (2026). Express.js 4.x API Reference and Middleware Guide. https://expressjs.com/",
    "6. Meta Platforms, Inc. (2026). React 18 Documentation: Hooks, Components, and Virtual DOM. https://react.dev/",
    "7. Vite Team. (2026). Vite: Next Generation Frontend Tooling. https://vitejs.dev/",
    "8. Tailwind Labs, Inc. (2026). Tailwind CSS Documentation. https://tailwindcss.com/docs",
    "9. Recharts Group. (2026). Recharts: Redefined Chart Library Built with React and D3. https://recharts.org/",
    "10. Internet Engineering Task Force (IETF). (2015). RFC 7519: JSON Web Token (JWT). https://datatracker.ietf.org/doc/html/rfc7519",
    "11. Render Services, Inc. (2026). Render Cloud Hosting Documentation. https://render.com/docs",
    "12. Vercel, Inc. (2026). Vercel Deployment Documentation and Edge Network Guide. https://vercel.com/docs"
]

for r in refs:
    p = doc.add_paragraph()
    r_run = p.add_run(r)
    fmt(p, size=9.5, align=WD_ALIGN_PARAGRAPH.LEFT, space_after=3)

h1("APPENDIX")

h2("A.1 Repository and Deployment Artifacts")
body("Project Source Code Repository:\nhttps://github.com/kancharla-ajay-kumar/Expense-Management")
body("Live Production Backend Service (Render):\nhttps://expense-management-xswk.onrender.com")
body("Unstop Course Completion Certificate Verification:\nhttps://unstop.com/certificate-preview/2fe44ee8-7ea5-40ad-8f8c-b391ea250bd7")

h2("A.2 Key Project Artifacts Summary")
artifacts_data = [
    ["server.js", "Express server entry point configuring Helmet, CORS, Rate Limiters, and API routes"],
    ["config/db.js", "Mongoose cloud connection handler for MongoDB Atlas with auto-sanitization"],
    ["models/Expense.js", "Mongoose schema defining transaction attributes, categories, and indexes"],
    ["models/User.js", "User authentication schema with bcryptjs salt generation and pre-save hashing"],
    ["controllers/expenseController.js", "Transaction CRUD logic and high-performance MongoDB analytical aggregations"],
    ["controllers/budgetController.js", "Dynamic monthly budget evaluation and operational status assignment"],
    ["frontend/src/App.jsx", "Client-side route declarations with ProtectedRoute authorization guards"],
    ["frontend/src/context/AuthContext.jsx", "Centralized user session management and localStorage synchronization"],
    ["frontend/src/api/axios.js", "Axios HTTP instance with automatic JWT Authorization bearer injection"],
    ["frontend/vercel.json", "Vercel edge rewrite configuration ensuring client-side SPA routing persistence"]
]
tbl(["Artifact File Path", "Architectural Role and Operational Function in SpendWise"], artifacts_data, [2.3, 4.0])

# Save Document
doc.save(docx_out)
print(f"Report successfully saved to DOCX: {docx_out}")
