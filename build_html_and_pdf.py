import os
import subprocess
import pymupdf

base_dir = r"d:\Expense-Management"
assets_dir = os.path.join(base_dir, "report_assets")
html_out = os.path.join(base_dir, "Industrial_Training_Report_Ajay_Kumar.html")
pdf_out = os.path.join(base_dir, "Industrial_Training_Report_Ajay_Kumar.pdf")

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Industrial Training Report — Kancharla Ajay Kumar</title>
<style>
  @page {
    size: A4 portrait;
    margin: 16mm 18mm 16mm 18mm;
  }

  body {
    font-family: "Times New Roman", Times, serif;
    font-size: 10.5pt;
    line-height: 1.26;
    color: #111;
    margin: 0;
    padding: 0;
  }

  .report-page {
    height: 263mm;
    max-height: 263mm;
    box-sizing: border-box;
    position: relative;
    page-break-after: always;
    break-after: page;
    overflow: hidden;
  }

  h1.chapter-title {
    font-size: 14pt;
    font-weight: bold;
    text-transform: uppercase;
    color: #111;
    margin-top: 0;
    margin-bottom: 8px;
    border-bottom: 1.5px solid #2F6F4E;
    padding-bottom: 3px;
  }

  h2.section-title {
    font-size: 11.5pt;
    font-weight: bold;
    color: #222;
    margin-top: 8px;
    margin-bottom: 4px;
  }

  p {
    text-align: justify;
    margin-top: 0;
    margin-bottom: 5px;
    text-justify: inter-word;
  }

  ul {
    margin-top: 2px;
    margin-bottom: 5px;
    padding-left: 18px;
  }

  li {
    text-align: justify;
    margin-bottom: 3px;
  }

  .header-bar {
    font-size: 8.5pt;
    color: #666;
    border-bottom: 1px solid #ccc;
    padding-bottom: 3px;
    margin-bottom: 10px;
    text-align: right;
  }

  .footer-bar {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    display: flex;
    justify-content: space-between;
    font-size: 8.5pt;
    color: #666;
    border-top: 1px solid #ccc;
    padding-top: 3px;
    background: #fff;
  }

  table.academic-table {
    width: 100%;
    border-collapse: collapse;
    margin: 6px 0 8px 0;
    font-size: 8.8pt;
    line-height: 1.2;
  }

  table.academic-table th {
    background-color: #2A2F35;
    color: #FFFFFF;
    font-weight: bold;
    text-align: left;
    padding: 4px 6px;
    border: 1px solid #2A2F35;
  }

  table.academic-table td {
    padding: 3.5px 6px;
    border: 1px solid #E0E0E0;
    vertical-align: top;
  }

  table.academic-table tr:nth-child(even) td {
    background-color: #F8F9FA;
  }

  .code-block {
    background-color: #F4F6F8;
    border-left: 3px solid #2F6F4E;
    font-family: "Courier New", Courier, monospace;
    font-size: 8.2pt;
    line-height: 1.2;
    padding: 5px 8px;
    margin: 5px 0;
    white-space: pre-wrap;
    border-radius: 2px;
  }

  .figure-container {
    text-align: center;
    margin: 6px 0 8px 0;
  }

  .figure-container img {
    border-radius: 4px;
    border: 1px solid #E0E0E0;
  }

  .figure-caption {
    font-size: 8.8pt;
    font-style: italic;
    color: #444;
    margin-top: 4px;
  }

  .cover-container {
    text-align: center;
    padding-top: 5px;
  }
  .cover-inst {
    font-size: 14.5pt;
    font-weight: bold;
    margin-bottom: 3px;
  }
  .cover-city {
    font-size: 12.5pt;
    font-weight: bold;
    margin-bottom: 6px;
  }
  .cover-dept {
    font-size: 11.5pt;
    font-weight: bold;
    margin-bottom: 14px;
  }
  .cover-title {
    font-size: 17pt;
    font-weight: bold;
    margin-top: 14px;
    margin-bottom: 4px;
    letter-spacing: 0.5px;
  }
  .cover-proj {
    font-size: 15pt;
    font-weight: bold;
    color: #2F6F4E;
    margin-top: 10px;
    margin-bottom: 14px;
  }
  table.cover-table {
    width: 82%;
    margin: 15px auto 8px auto;
    border-collapse: collapse;
    font-size: 10pt;
  }
  table.cover-table td {
    padding: 5px 8px;
    border: 1px solid #999;
  }
  table.cover-table td.label {
    font-weight: bold;
    width: 42%;
    background-color: #F8F9FA;
  }
</style>
</head>
<body>

<!-- PAGE 1: COVER PAGE -->
<div class="report-page cover-container">
  <div class="cover-inst">MAULANA AZAD NATIONAL INSTITUTE OF TECHNOLOGY</div>
  <div class="cover-city">BHOPAL</div>
  <div class="cover-dept">Department of Computer Science and Engineering</div>

  <div style="margin: 15px 0;">
    <img src="report_assets/manit_logo.jpeg" style="width: 135px; height: auto;" alt="MANIT Bhopal Emblem">
  </div>

  <div class="cover-title">INDUSTRIAL TRAINING REPORT</div>
  <div style="font-size: 11.5pt; font-style: italic; margin-bottom: 4px;">on</div>
  <div class="cover-proj">SPENDWISE — PERSONAL FINANCE AND EXPENSE<br>MANAGEMENT SYSTEM</div>

  <div style="font-size: 11.5pt; font-weight: bold; margin-bottom: 10px;">Training undertaken at<br><span style="font-size: 13.5pt; letter-spacing: 1px;">UNSTOP</span></div>

  <div style="font-size: 10pt; font-style: italic; margin-bottom: 18px;">
    Submitted in partial fulfillment of the Requirements for the Award degree of<br>
    <strong>BACHELOR OF TECHNOLOGY</strong><br>
    in<br>
    <strong>COMPUTER SCIENCE AND ENGINEERING</strong>
  </div>

  <table class="cover-table">
    <tr>
      <td class="label">Scholar Name</td>
      <td><strong>Kancharla Ajay Kumar</strong></td>
    </tr>
    <tr>
      <td class="label">Scholar No.</td>
      <td><strong>24112011237</strong></td>
    </tr>
    <tr>
      <td class="label">Programme and Semester</td>
      <td>B.Tech. (CSE), V Semester</td>
    </tr>
    <tr>
      <td class="label">Section</td>
      <td>1</td>
    </tr>
    <tr>
      <td class="label">Academic Session</td>
      <td>2026–27</td>
    </tr>
  </table>

  <div style="font-size: 10.5pt; font-weight: bold; margin-top: 25px;">July / November 2026</div>
</div>

<!-- PAGE 2: CERTIFICATE -->
<div class="report-page">
  <div class="header-bar">SpendWise — MERN Expense Tracker | MANIT Bhopal</div>
  <div style="text-align: center; font-size: 15pt; font-weight: bold; margin-bottom: 12px;">CERTIFICATE</div>
  
  <div style="text-align: center; margin: 10px 0 15px 0; border: 2px solid #2F6F4E; padding: 8px; border-radius: 6px; background: #FAFCFA;">
    <img src="report_assets/unstop_certificate.png" style="width: 100%; max-width: 580px; border-radius: 4px;" alt="Unstop Certificate of Completion">
  </div>

  <p>This is to certify that <strong>Kancharla Ajay Kumar</strong> (Scholar Number: <strong>24112011237</strong>), a bonafide student of Bachelor of Technology in Computer Science and Engineering at Maulana Azad National Institute of Technology (MANIT), Bhopal, has successfully completed the online industrial training course in <strong>MERN Full Stack</strong> provided by <strong>Unstop</strong>.</p>
  
  <p>During the training period, the candidate demonstrated technical proficiency, diligence, and applied the core architectural concepts of MongoDB, Express.js, React.js, and Node.js towards developing a comprehensive full-stack capstone project titled <strong>"SpendWise — Personal Finance and Expense Management System"</strong>.</p>

  <p style="font-size: 9.5pt; color: #444;"><strong>Online Certificate Verification:</strong> <a href="https://unstop.com/certificate-preview/2fe44ee8-7ea5-40ad-8f8c-b391ea250bd7" style="color: #2F6F4E;">https://unstop.com/certificate-preview/2fe44ee8-7ea5-40ad-8f8c-b391ea250bd7</a></p>
  
  <div class="footer-bar"><span>Department of Computer Science and Engineering, MANIT Bhopal</span><span>Page 2</span></div>
</div>

<!-- PAGE 3: ACKNOWLEDGEMENT -->
<div class="report-page">
  <div class="header-bar">SpendWise — MERN Expense Tracker | MANIT Bhopal</div>
  <h1 class="chapter-title" style="border: none; font-size: 15pt; text-align: left; margin-bottom: 15px;">Acknowledgement</h1>

  <p>I express my sincere gratitude to the Department of Computer Science and Engineering, Maulana Azad National Institute of Technology (MANIT), Bhopal, for providing the academic environment, computing infrastructure, and institutional encouragement necessary to pursue this industrial training.</p>

  <p>I would like to thank my project supervisor and faculty coordinator for their invaluable guidance, constructive suggestions, and continuous feedback that helped shape the direction, technical depth, and engineering rigour of this work. Their emphasis on clean architectural separation, secure authentication standards, and thorough empirical validation was instrumental to the successful completion of this project.</p>

  <p>I extend my gratitude to the faculty members of the department for strengthening my foundational understanding of software engineering, database management systems, computer networks, and full-stack web architectures.</p>

  <p>I gratefully acknowledge Unstop for designing and offering the comprehensive <strong>MERN Full Stack</strong> development course. The curriculum provided structured learning modules, industry-aligned practical assignments, and the conceptual foundation required for architecting scalable cloud-native web systems.</p>

  <p>I also acknowledge the open-source software communities behind Node.js, Express.js, React, MongoDB, Vite, Tailwind CSS, Recharts, and Axios. These tools provided the modern ecosystem required for creating an interactive, performant, and resilient web application.</p>

  <p>Finally, I thank my family and friends for their constant encouragement, patience, and support throughout the completion of this project.</p>

  <div style="margin-top: 35px; text-align: right;">
    <p style="margin: 0;"><strong>Kancharla Ajay Kumar</strong></p>
    <p style="margin: 0; color: #444; font-size: 9.5pt;">Scholar No: 24112011237</p>
    <p style="margin: 0; color: #444; font-size: 9.5pt;">B.Tech. Computer Science and Engineering</p>
    <p style="margin: 0; color: #444; font-size: 9.5pt;">MANIT Bhopal</p>
  </div>
  <div class="footer-bar"><span>Department of Computer Science and Engineering, MANIT Bhopal</span><span>Page 3</span></div>
</div>

<!-- PAGE 4: ABSTRACT -->
<div class="report-page">
  <div class="header-bar">SpendWise — MERN Expense Tracker | MANIT Bhopal</div>
  <h1 class="chapter-title" style="border: none; font-size: 15pt; text-align: left; margin-bottom: 15px;">Abstract</h1>

  <p>Effective personal financial management requires disciplined tracking of income, expenses, and budgetary allocations. Conventional tracking mechanisms, such as paper ledgers and manual spreadsheets, suffer from high entry friction, lack of real-time validation, vulnerability to data loss, and an inability to deliver automated visual analytics or proactive budgetary threshold warnings. Conversely, many commercial financial tools impose intrusive third-party data tracking, complex subscription fees, or overly rigid schemas that fail to address the needs of students and working professionals seeking an intuitive, private, and customizable tracking system.</p>

  <p>To overcome these challenges, <strong>SpendWise</strong> was designed and implemented as an end-to-end full-stack web application leveraging the MERN Stack (MongoDB, Express.js, React.js, Node.js). The application architecture follows a decoupled, three-tier client-server model. The frontend is built with React 18 and Vite, utilizing Tailwind CSS for a responsive, theme-switchable user interface and Recharts for interactive visual analytics. The backend is implemented as a stateless RESTful service using Node.js and Express, secured with JSON Web Token (JWT) authentication, bcryptjs password hashing, Helmet HTTP headers, Mongo-Sanitize injection defenses, and rate limiting.</p>

  <p>Key functional features include complete transaction lifecycle management (CRUD) for categorized income and expense entries, monthly category budgets featuring proactive three-state alert triggers (On Track, Warning, Exceeded), high-throughput MongoDB aggregation pipelines for monthly comparative summaries and 12-month net savings trends, multi-currency formatting via the native Intl API, and instant client-side CSV data export. The system was validated through extensive functional, integration, and security test suites, and deployed to production cloud infrastructure utilizing MongoDB Atlas for database persistence, Render for backend API hosting, and Vercel for frontend distribution.</p>

  <p style="margin-top: 14px;"><strong>Keywords:</strong> MERN Stack, React.js, Node.js, Express.js, MongoDB Atlas, RESTful API, JWT Authentication, Financial Analytics, Expense Management, Cloud Deployment.</p>
  <div class="footer-bar"><span>Department of Computer Science and Engineering, MANIT Bhopal</span><span>Page 4</span></div>
</div>

<!-- PAGE 5: TOC PART 1 -->
<div class="report-page">
  <div class="header-bar">SpendWise — MERN Expense Tracker | MANIT Bhopal</div>
  <h1 class="chapter-title" style="text-align: center; border: none; margin-bottom: 14px;">TABLE OF CONTENTS</h1>

  <table style="width: 100%; border-collapse: collapse; font-size: 9.5pt; line-height: 1.45;">
    <tr style="font-weight: bold;"><td>CHAPTER 1 INTRODUCTION</td><td style="text-align: right;">8</td></tr>
    <tr><td style="padding-left: 15px;">1.1 Background and Motivation</td><td style="text-align: right;">8</td></tr>
    <tr><td style="padding-left: 15px;">1.2 Project Overview</td><td style="text-align: right;">8</td></tr>
    <tr><td style="padding-left: 15px;">1.3 Scope of the Project</td><td style="text-align: right;">8</td></tr>
    <tr style="font-weight: bold;"><td>CHAPTER 2 TRAINING PROGRAMME OVERVIEW</td><td style="text-align: right;">9</td></tr>
    <tr><td style="padding-left: 15px;">2.1 About the Training Programme (Unstop)</td><td style="text-align: right;">9</td></tr>
    <tr><td style="padding-left: 15px;">2.2 Course Content and Syllabus Covered</td><td style="text-align: right;">9</td></tr>
    <tr><td style="padding-left: 15px;">2.3 Mapping Course Topics to Project Implementation</td><td style="text-align: right;">10</td></tr>
    <tr><td style="padding-left: 15px;">2.4 Skills and Competencies Acquired</td><td style="text-align: right;">10</td></tr>
    <tr style="font-weight: bold;"><td>CHAPTER 3 PROBLEM STATEMENT AND OBJECTIVES</td><td style="text-align: right;">11</td></tr>
    <tr><td style="padding-left: 15px;">3.1 Problem Statement</td><td style="text-align: right;">11</td></tr>
    <tr><td style="padding-left: 15px;">3.2 Project Objectives</td><td style="text-align: right;">11</td></tr>
    <tr><td style="padding-left: 15px;">3.3 Expected Outcomes</td><td style="text-align: right;">11</td></tr>
    <tr style="font-weight: bold;"><td>CHAPTER 4 LITERATURE SURVEY AND RELATED CONCEPTS</td><td style="text-align: right;">11</td></tr>
    <tr><td style="padding-left: 15px;">4.1 Evolution of Personal Finance Management Tools</td><td style="text-align: right;">11</td></tr>
    <tr><td style="padding-left: 15px;">4.2 Contemporary Web Architectures and MERN Stack</td><td style="text-align: right;">11</td></tr>
    <tr style="font-weight: bold;"><td>CHAPTER 5 REQUIREMENT ANALYSIS</td><td style="text-align: right;">12</td></tr>
    <tr><td style="padding-left: 15px;">5.1 Functional Requirements</td><td style="text-align: right;">12</td></tr>
    <tr><td style="padding-left: 15px;">5.2 Non-Functional Requirements</td><td style="text-align: right;">12</td></tr>
    <tr><td style="padding-left: 15px;">5.3 Hardware and Software System Requirements</td><td style="text-align: right;">12</td></tr>
    <tr style="font-weight: bold;"><td>CHAPTER 6 SYSTEM ARCHITECTURE</td><td style="text-align: right;">13</td></tr>
    <tr><td style="padding-left: 15px;">6.1 High-Level Three-Tier Architecture</td><td style="text-align: right;">13</td></tr>
    <tr><td style="padding-left: 15px;">6.2 Client-Server Communication Flow</td><td style="text-align: right;">13</td></tr>
  </table>
  <div class="footer-bar"><span>Department of Computer Science and Engineering, MANIT Bhopal</span><span>Page 5</span></div>
</div>

<!-- PAGE 6: TOC PART 2 -->
<div class="report-page">
  <div class="header-bar">SpendWise — MERN Expense Tracker | MANIT Bhopal</div>
  <table style="width: 100%; border-collapse: collapse; font-size: 9.5pt; line-height: 1.45;">
    <tr style="font-weight: bold;"><td>CHAPTER 7 TECHNOLOGY STACK</td><td style="text-align: right;">14</td></tr>
    <tr><td style="padding-left: 15px;">7.1 Core Technologies and Frameworks</td><td style="text-align: right;">14</td></tr>
    <tr><td style="padding-left: 15px;">7.2 Technology Stack Summary Table</td><td style="text-align: right;">14</td></tr>
    <tr style="font-weight: bold;"><td>CHAPTER 8 DATABASE DESIGN</td><td style="text-align: right;">15</td></tr>
    <tr><td style="padding-left: 15px;">8.1 MongoDB Document Model and Schema Architecture</td><td style="text-align: right;">15</td></tr>
    <tr><td style="padding-left: 15px;">8.2 Data Schemas: User, Expense, and Budget</td><td style="text-align: right;">15</td></tr>
    <tr><td style="padding-left: 15px;">8.3 Aggregation Pipelines and Query Optimization</td><td style="text-align: right;">15</td></tr>
    <tr style="font-weight: bold;"><td>CHAPTER 9 METHODOLOGY AND WORKING</td><td style="text-align: right;">16</td></tr>
    <tr><td style="padding-left: 15px;">9.1 Agile Development Workflow</td><td style="text-align: right;">16</td></tr>
    <tr><td style="padding-left: 15px;">9.2 User Authentication and Session Security Workflow</td><td style="text-align: right;">16</td></tr>
    <tr><td style="padding-left: 15px;">9.3 CRUD Transaction and Budget Computation Logic</td><td style="text-align: right;">16</td></tr>
    <tr style="font-weight: bold;"><td>CHAPTER 10 FRONTEND IMPLEMENTATION</td><td style="text-align: right;">17</td></tr>
    <tr><td style="padding-left: 15px;">10.1 React Application Structure and Component Hierarchy</td><td style="text-align: right;">17</td></tr>
    <tr><td style="padding-left: 15px;">10.2 State Management via React Context API</td><td style="text-align: right;">17</td></tr>
    <tr><td style="padding-left: 15px;">10.3 Form Validation and User Experience</td><td style="text-align: right;">17</td></tr>
    <tr><td style="padding-left: 15px;">10.4 Theming Engine (Light and Dark Mode)</td><td style="text-align: right;">17</td></tr>
    <tr style="font-weight: bold;"><td>CHAPTER 11 BACKEND IMPLEMENTATION</td><td style="text-align: right;">18</td></tr>
    <tr><td style="padding-left: 15px;">11.1 Express Server Initialization and Security Middleware</td><td style="text-align: right;">18</td></tr>
    <tr><td style="padding-left: 15px;">11.2 Authentication Controller and Password Hashing</td><td style="text-align: right;">18</td></tr>
    <tr><td style="padding-left: 15px;">11.3 Expense and Statistical Controllers</td><td style="text-align: right;">19</td></tr>
    <tr><td style="padding-left: 15px;">11.4 Budget Progress Controller</td><td style="text-align: right;">19</td></tr>
    <tr><td style="padding-left: 15px;">11.5 Centralized Error Handler and Validation Middleware</td><td style="text-align: right;">20</td></tr>
    <tr style="font-weight: bold;"><td>CHAPTER 12 APPLICATION MODULES</td><td style="text-align: right;">21</td></tr>
    <tr><td style="padding-left: 15px;">12.1 Authentication and Profile Module</td><td style="text-align: right;">21</td></tr>
    <tr><td style="padding-left: 15px;">12.2 Dashboard Analytics Module</td><td style="text-align: right;">21</td></tr>
    <tr><td style="padding-left: 15px;">12.3 Transaction Ledger Module</td><td style="text-align: right;">21</td></tr>
    <tr><td style="padding-left: 15px;">12.4 Budget Tracking Module</td><td style="text-align: right;">21</td></tr>
    <tr><td style="padding-left: 15px;">12.5 CSV Data Export Module</td><td style="text-align: right;">21</td></tr>
  </table>
  <div class="footer-bar"><span>Department of Computer Science and Engineering, MANIT Bhopal</span><span>Page 6</span></div>
</div>

<!-- PAGE 7: TOC PART 3 -->
<div class="report-page">
  <div class="header-bar">SpendWise — MERN Expense Tracker | MANIT Bhopal</div>
  <table style="width: 100%; border-collapse: collapse; font-size: 9.5pt; line-height: 1.45;">
    <tr style="font-weight: bold;"><td>CHAPTER 13 IMPLEMENTATION DETAILS AND DEPLOYMENT</td><td style="text-align: right;">22</td></tr>
    <tr><td style="padding-left: 15px;">13.1 Repository Structure and Code Organization</td><td style="text-align: right;">22</td></tr>
    <tr><td style="padding-left: 15px;">13.2 Environment Variables and Configuration</td><td style="text-align: right;">22</td></tr>
    <tr><td style="padding-left: 15px;">13.3 Cloud Deployment Architecture (Render & Vercel)</td><td style="text-align: right;">22</td></tr>
    <tr><td style="padding-left: 15px;">13.4 Local Development Execution Sequence</td><td style="text-align: right;">22</td></tr>
    <tr style="font-weight: bold;"><td>CHAPTER 14 APPLICATION SCREENS AND TEST CASES</td><td style="text-align: right;">23</td></tr>
    <tr><td style="padding-left: 15px;">14.1 User Interface Screenshots and Visual Walkthrough</td><td style="text-align: right;">23</td></tr>
    <tr><td style="padding-left: 15px;">14.2 Functional and Integration Test Cases</td><td style="text-align: right;">24</td></tr>
    <tr><td style="padding-left: 15px;">14.3 Analysis of Test Results and Observations</td><td style="text-align: right;">25</td></tr>
    <tr style="font-weight: bold;"><td>CHAPTER 15 APPLICATIONS, ADVANTAGES AND LIMITATIONS</td><td style="text-align: right;">25</td></tr>
    <tr><td style="padding-left: 15px;">15.1 Real-World Practical Applications</td><td style="text-align: right;">25</td></tr>
    <tr><td style="padding-left: 15px;">15.2 Key Technical Advantages</td><td style="text-align: right;">25</td></tr>
    <tr><td style="padding-left: 15px;">15.3 System Limitations and Constraints</td><td style="text-align: right;">26</td></tr>
    <tr style="font-weight: bold;"><td>CHAPTER 16 FUTURE SCOPE</td><td style="text-align: right;">26</td></tr>
    <tr><td style="padding-left: 15px;">16.1 Advanced Financial Intelligence Enhancements</td><td style="text-align: right;">26</td></tr>
    <tr><td style="padding-left: 15px;">16.2 Architectural and Platform Roadmap</td><td style="text-align: right;">26</td></tr>
    <tr style="font-weight: bold;"><td>CHAPTER 17 CONCLUSION</td><td style="text-align: right;">27</td></tr>
    <tr style="font-weight: bold;"><td>REFERENCES</td><td style="text-align: right;">28</td></tr>
    <tr style="font-weight: bold;"><td>APPENDIX</td><td style="text-align: right;">28</td></tr>
    <tr><td style="padding-left: 15px;">A.1 Repository and Deployment Artifacts</td><td style="text-align: right;">28</td></tr>
    <tr><td style="padding-left: 15px;">A.2 Key Project Artifacts Summary</td><td style="text-align: right;">28</td></tr>
  </table>
  <div class="footer-bar"><span>Department of Computer Science and Engineering, MANIT Bhopal</span><span>Page 7</span></div>
</div>

<!-- PAGE 8: CHAPTER 1 -->
<div class="report-page">
  <div class="header-bar">SpendWise — MERN Expense Tracker | MANIT Bhopal</div>
  <h1 class="chapter-title">1 INTRODUCTION</h1>

  <h2 class="section-title">1.1 Background and Motivation</h2>
  <p>In an increasingly digital global economy, disciplined personal financial management is critical for individuals across all life stages, particularly students, independent freelancers, and young working professionals. Despite widespread awareness regarding the importance of financial discipline, individuals frequently struggle with unmonitored expenditure, impulsive discretionary spending, and inadequate savings accumulation. The primary contributor to this problem is the absence of an intuitive, frictionless, and accessible tracking mechanism that provides real-time financial visibility.</p>

  <p>Traditional approaches to expense logging—such as physical notebook ledgers, paper receipts, or standalone spreadsheet files—exhibit severe operational friction. Manual record-keeping is tedious, highly susceptible to human omission or calculation errors, lacks cross-device accessibility, and fails to offer proactive feedback. Users frequently abandon manual tracking after several days because data entry feels disconnected from meaningful analytical insights.</p>

  <p>Web-based full-stack applications built on modern JavaScript ecosystems provide an optimal solution to these limitations. By leveraging single-page application (SPA) architectures, reactive user interfaces, and robust backend micro-architectures, modern web systems can automate complex statistical aggregations, deliver immediate visual feedback through interactive charts, and trigger predictive budget overspend alerts. The motivation behind developing SpendWise is to bridge the gap between complex enterprise accounting software and simplistic, privacy-invasive mobile trackers, providing users with a comprehensive, private, and aesthetically refined personal finance portal.</p>

  <h2 class="section-title">1.2 Project Overview</h2>
  <p>SpendWise is a responsive full-stack web application architected on the MERN Stack (MongoDB, Express.js, React.js, Node.js). The application serves as an end-to-end financial monitoring platform where authenticated users can securely record multi-category income and expense transactions, establish monthly budget limits, receive visual threshold warnings, analyze multi-month financial performance trends, and export structured transaction histories as CSV spreadsheets. The complete source code, deployment manifests, and automated build configurations are maintained in the GitHub repository at:</p>

  <div class="code-block">https://github.com/kancharla-ajay-kumar/Expense-Management</div>

  <h2 class="section-title">1.3 Scope of the Project</h2>
  <p>The functional and technical scope of SpendWise encompasses the following core areas:</p>
  <ul>
    <li><strong>User Authentication & Security:</strong> Stateless token-based authentication implementing JSON Web Tokens (JWT) and bcryptjs salted password hashing, combined with server-side validation and brute-force rate limiters.</li>
    <li><strong>Transaction Lifecycle Management:</strong> Full CRUD operations enabling users to create, view, filter, edit, and delete income and expense records with customizable metadata, payment methods, and tags.</li>
    <li><strong>Predictive Budgeting & Alert System:</strong> Per-category monthly spending limits calculated dynamically against current-period expenditures, generating three distinct visual operational states (On Track, Approaching Limit, and Budget Exceeded).</li>
    <li><strong>Real-Time Financial Analytics:</strong> High-performance MongoDB aggregation pipelines driving interactive Recharts visualizations, including categorical expense distribution, 6-month comparative cash flows, and 12-month net savings trajectories.</li>
    <li><strong>Cloud Deployment Architecture:</strong> Decoupled cloud infrastructure utilizing MongoDB Atlas for database hosting, Render for scalable backend container execution, and Vercel Edge Network for frontend static distribution.</li>
  </ul>
  <div class="footer-bar"><span>Department of Computer Science and Engineering, MANIT Bhopal</span><span>Page 8</span></div>
</div>

<!-- PAGE 9: CHAPTER 2 PART 1 -->
<div class="report-page">
  <div class="header-bar">SpendWise — MERN Expense Tracker | MANIT Bhopal</div>
  <h1 class="chapter-title">2 TRAINING PROGRAMME OVERVIEW</h1>

  <h2 class="section-title">2.1 About the Training Programme (Unstop)</h2>
  <p>The theoretical foundation and practical software engineering principles for this project were developed through the <strong>MERN Full Stack</strong> course offered by Unstop. Unstop is a prominent online talent discovery and technical education platform that delivers industry-aligned training programs. The course is a comprehensive, self-paced curriculum designed to teach modern full-stack web application development using JavaScript across the entire software stack.</p>

  <p>The curriculum emphasizes hands-on software development through modular video lectures, architectural quizzes, practical coding exercises, case studies, and capstone project assignments. The course specifically focuses on writing clean, modular, and maintainable JavaScript across both client and server runtimes. Upon successfully completing the curriculum and demonstrating practical proficiency, a formal Certificate of Completion was conferred to the author by Unstop, as presented on Page 2.</p>

  <div class="figure-container">
    <img src="report_assets/page_9_img_0.jpeg" style="width: 78%; max-height: 140px;" alt="Unstop Course Platform Interface">
    <div class="figure-caption">Figure 2.1: Unstop Full-Stack Training Curriculum Interface</div>
  </div>

  <h2 class="section-title">2.2 Course Content and Syllabus Covered</h2>
  <p>The course curriculum starts with core asynchronous JavaScript and progresses through server-side programming, database management, and reactive client development. Table 2.1 summarizes the primary learning modules covered during the training.</p>

  <table class="academic-table">
    <tr>
      <th style="width: 18%;">Module</th>
      <th style="width: 28%;">Domain Area</th>
      <th>Key Topics and Technologies Covered</th>
    </tr>
    <tr><td>Module 1</td><td>Modern JavaScript & ES6+</td><td>Async/Await, Promises, Destructuring, Closures, Array Methods, Modular JS</td></tr>
    <tr><td>Module 2</td><td>Node.js Runtime Architecture</td><td>Event Loop, Non-blocking I/O, File System, Streams, NPM package ecosystem</td></tr>
    <tr><td>Module 3</td><td>Express.js REST Framework</td><td>Routing, Custom Middleware, Request Lifecycle, Error Handling, CORS</td></tr>
    <tr><td>Module 4</td><td>MongoDB & Mongoose ODM</td><td>Document Modeling, Schema Validation, CRUD Operations, Indexes, Aggregations</td></tr>
    <tr><td>Module 5</td><td>Web Security & Auth</td><td>JWT Tokens, Password Hashing (bcrypt), HTTP Headers (Helmet), Rate Limiting</td></tr>
    <tr><td>Module 6</td><td>React 18 Component Model</td><td>JSX, Functional Components, Props, Virtual DOM, Reconciliation Algorithm</td></tr>
    <tr><td>Module 7</td><td>React Hooks & State</td><td>useState, useEffect, useCallback, useMemo, useContext, Custom Hooks</td></tr>
    <tr><td>Module 8</td><td>Routing & HTTP Clients</td><td>React Router v6, Protected Route Guards, Axios Interceptors, Error Handling</td></tr>
  </table>
  <div class="footer-bar"><span>Department of Computer Science and Engineering, MANIT Bhopal</span><span>Page 9</span></div>
</div>

<!-- PAGE 10: CHAPTER 2 PART 2 -->
<div class="report-page">
  <div class="header-bar">SpendWise — MERN Expense Tracker | MANIT Bhopal</div>
  <table class="academic-table" style="margin-top: 2px;">
    <tr>
      <th style="width: 18%;">Module</th>
      <th style="width: 28%;">Domain Area</th>
      <th>Key Topics and Technologies Covered</th>
    </tr>
    <tr><td>Module 9</td><td>UI Systems & Analytics</td><td>Tailwind CSS, Responsive Design, CSS Variables, Recharts Data Visualization</td></tr>
    <tr><td>Module 10</td><td>Cloud Deployment & DevOps</td><td>Git Version Control, Environment Configuration, Atlas, Render, Vercel</td></tr>
  </table>

  <h2 class="section-title">2.3 Mapping Course Topics to Project Implementation</h2>
  <p>The concepts acquired in the Unstop training programme were directly applied to implement the SpendWise system. Table 2.2 maps the theoretical concepts to the concrete code modules in the project repository.</p>

  <table class="academic-table">
    <tr>
      <th style="width: 25%;">Course Topic</th>
      <th style="width: 45%;">Implementation in SpendWise</th>
      <th>Project Artifacts</th>
    </tr>
    <tr><td>Node.js & Express.js</td><td>Server initialization, modular route handlers, and centralized error middleware</td><td>backend/server.js, backend/routes/</td></tr>
    <tr><td>MongoDB & Mongoose</td><td>User, Expense, and Budget schemas with multi-stage analytical aggregations</td><td>backend/models/, controllers/</td></tr>
    <tr><td>JWT & Password Security</td><td>Salted password hashing (12 rounds) and bearer token authentication guard</td><td>backend/middleware/auth.js, models/User.js</td></tr>
    <tr><td>React 18 & Hooks</td><td>Component composition, lifecycle hooks, and centralized Context API state</td><td>frontend/src/context/, components/</td></tr>
    <tr><td>Tailwind CSS Theming</td><td>Semantic design system with CSS custom variables for light/dark mode</td><td>frontend/src/index.css, tailwind.config.js</td></tr>
    <tr><td>Recharts Visualization</td><td>Reactive Bar, Pie, and Area charts mapping financial cash flow trends</td><td>frontend/src/components/dashboard/</td></tr>
    <tr><td>DevOps & Cloud Hosting</td><td>Git workflow, Vercel SPA rewrites, Render Web Services, and Atlas config</td><td>frontend/vercel.json, backend/config/db.js</td></tr>
  </table>

  <h2 class="section-title">2.4 Skills and Competencies Acquired</h2>
  <p>Completing the course curriculum and implementing SpendWise developed several key competencies:</p>
  <ul>
    <li><strong>Full-Stack JavaScript Mastery:</strong> Deep understanding of isomorphic JavaScript, leveraging asynchronous paradigms, closures, and modular design patterns across both Node.js and browser engines.</li>
    <li><strong>RESTful API Engineering:</strong> Designing standard REST endpoints, structuring request validations, managing HTTP status codes, and handling exceptions gracefully.</li>
    <li><strong>NoSQL Data Modeling:</strong> Schema design principles in MongoDB, including referencing vs. embedding, compound indexing strategies, and multi-stage aggregation pipelines ($match, $group, $sort).</li>
    <li><strong>Modern Frontend Architecture:</strong> Architecting decoupled React single-page applications, utilizing custom hooks, centralized Context state providers, and responsive Tailwind styling.</li>
  </ul>
  <div class="footer-bar"><span>Department of Computer Science and Engineering, MANIT Bhopal</span><span>Page 10</span></div>
</div>

<!-- PAGE 11: CHAPTER 3 & 4 -->
<div class="report-page">
  <div class="header-bar">SpendWise — MERN Expense Tracker | MANIT Bhopal</div>
  <h1 class="chapter-title">3 PROBLEM STATEMENT AND OBJECTIVES</h1>

  <h2 class="section-title">3.1 Problem Statement</h2>
  <p>Personal financial health depends heavily on consistent tracking and disciplined budget adherence. However, existing personal expense tracking methods present substantial operational bottlenecks. Manual record-keeping on paper or generic spreadsheets is labor-intensive, error-prone, lacks automated statistical aggregation, and provides no proactive alerts when expenditures approach critical financial thresholds. Furthermore, many commercial mobile applications require intrusive banking credential access, enforce recurring paid subscriptions, or monetize sensitive personal financial data through third-party advertising.</p>

  <p>Consequently, there exists a pressing need for an accessible, responsive, self-contained, and secure web application that enables users to track income and expenses, configure custom monthly category budgets, visualize spending patterns through automated analytics, and maintain sovereign control over their financial records.</p>

  <h2 class="section-title">3.2 Project Objectives</h2>
  <p>The SpendWise project was undertaken with the following primary technical objectives:</p>
  <ul>
    <li><strong>Develop a Responsive Single-Page Application:</strong> Create an intuitive client interface using React 18 and Tailwind CSS functioning across desktop, tablet, and mobile devices.</li>
    <li><strong>Implement Secure Authentication:</strong> Construct a robust authentication pipeline utilizing bcryptjs hashing and signed JWTs ensuring multi-tenant database isolation.</li>
    <li><strong>Build a Transaction Engine:</strong> Provide comprehensive CRUD functionality allowing users to record, categorize, search, filter, paginate, and edit multi-currency transactions.</li>
    <li><strong>Design an Intelligent Budget System:</strong> Implement dynamic category budget monitoring that evaluates monthly spend against thresholds, providing real-time visual alerts.</li>
    <li><strong>Deploy to Scalable Cloud:</strong> Configure and deploy the decoupled application across production platforms (MongoDB Atlas, Render, and Vercel) following DevOps best practices.</li>
  </ul>

  <h1 class="chapter-title" style="margin-top: 8px;">4 LITERATURE SURVEY AND RELATED CONCEPTS</h1>

  <h2 class="section-title">4.1 Evolution of Personal Finance Management Tools</h2>
  <p>Personal finance tracking has evolved through three distinct technological paradigms: physical recording (handwritten ledgers, envelope cash budgeting), desktop computing spreadsheets (Lotus 1-2-3, Microsoft Excel), and contemporary cloud-native financial portals. Cloud platforms offer continuous cross-device synchronization, automated calculation engines, and interactive reporting. SpendWise adopts this modern paradigm by delivering a zero-installation, browser-based web application engineered specifically for individual personal finance management.</p>

  <h2 class="section-title">4.2 Contemporary Web Architectures and MERN Stack</h2>
  <p>Modern web engineering has decisively shifted towards decoupled client-server architectures where the presentation layer operates as an independent Single-Page Application communicating with the backend strictly through asynchronous RESTful HTTP APIs exchanging JSON. The MERN Stack represents the premier technology combination for decoupled development, unifying JavaScript across client components (React), backend controllers (Express/Node.js), and database queries (MongoDB/BSON).</p>
  <div class="footer-bar"><span>Department of Computer Science and Engineering, MANIT Bhopal</span><span>Page 11</span></div>
</div>

<!-- PAGE 12: CHAPTER 5 -->
<div class="report-page">
  <div class="header-bar">SpendWise — MERN Expense Tracker | MANIT Bhopal</div>
  <h1 class="chapter-title">5 REQUIREMENT ANALYSIS</h1>

  <h2 class="section-title">5.1 Functional Requirements</h2>
  <p>Functional requirements define the core operational behaviors and user services provided by SpendWise:</p>
  <ul>
    <li><strong>User Identity Management:</strong> User registration with validated credentials, secure authentication with JWT issuance, profile customization (name, currency, income goal), and password modification.</li>
    <li><strong>Transaction Record Management:</strong> Complete CRUD capabilities for expense and income records with category tags, custom notes, payment methods, transaction timestamps, and recurring flags.</li>
    <li><strong>Filtering and Search Engine:</strong> Real-time client/server query filtering supporting text search (title/notes), category selection, transaction type toggles, date ranges, sorting, and pagination.</li>
    <li><strong>Category Budgeting Engine:</strong> Setting and updating per-category monthly limits with custom alert thresholds, calculating dynamic spending progress, and computing operational status.</li>
    <li><strong>Analytical Dashboard:</strong> Real-time computation of net balances, monthly cash flow ratios, categorical spend breakdowns (Pie Chart), and historical 12-month trajectory curves (Bar/Area Charts).</li>
    <li><strong>Data Portability:</strong> Instant client-side generation and downloading of structured RFC-4180 compliant CSV exports containing complete user transaction histories.</li>
  </ul>

  <h2 class="section-title">5.2 Non-Functional Requirements</h2>
  <p>Non-functional requirements specify system quality attributes, security standards, and performance constraints:</p>
  <ul>
    <li><strong>Security & Privacy:</strong> Cryptographic hashing of passwords using bcryptjs with 12 salt rounds; stateless JWT tokens with 7-day expiration; complete user data isolation enforced at the database query level.</li>
    <li><strong>System Performance:</strong> Sub-200ms API response latency for standard CRUD endpoints; sub-500ms execution time for multi-stage MongoDB aggregations; optimized Vite bundle size under 800 kB.</li>
    <li><strong>Responsive Usability:</strong> Mobile-first responsive interface utilizing adaptive drawer sidebars, flexible card grids, and semantic light/dark mode switching without flash-of-unstyled-theme.</li>
    <li><strong>Availability & Reliability:</strong> Centralized backend exception handling preventing process crashes; resilient database reconnection handling; 99.9% uptime powered by cloud infrastructure.</li>
  </ul>

  <h2 class="section-title">5.3 Hardware and Software System Requirements</h2>
  <p>Table 5.1 outlines the development, testing, and production runtime specifications required for SpendWise.</p>

  <table class="academic-table">
    <tr>
      <th style="width: 30%;">Requirement Category</th>
      <th>Technical Specification & Operational Environment</th>
    </tr>
    <tr><td>Client Hardware</td><td>Any device with 2 GB RAM, 1 GHz CPU, and modern web browser (Desktop/Mobile)</td></tr>
    <tr><td>Server Runtime</td><td>Node.js v18.0.0 or higher, 512 MB RAM minimum (Render Free Tier compatible)</td></tr>
    <tr><td>Operating System</td><td>Cross-platform: Windows 10/11, Linux (Ubuntu/Debian), macOS for development and hosting</td></tr>
    <tr><td>Database Service</td><td>MongoDB Community Server 6.0+ (Local) or MongoDB Atlas Shared M0 Cloud Cluster</td></tr>
    <tr><td>Development Tooling</td><td>Visual Studio Code, Git v2.40+, Google Chrome DevTools, Postman / REST Client</td></tr>
  </table>
  <div class="footer-bar"><span>Department of Computer Science and Engineering, MANIT Bhopal</span><span>Page 12</span></div>
</div>

<!-- PAGE 13: CHAPTER 6 -->
<div class="report-page">
  <div class="header-bar">SpendWise — MERN Expense Tracker | MANIT Bhopal</div>
  <h1 class="chapter-title">6 SYSTEM ARCHITECTURE</h1>

  <h2 class="section-title">6.1 High-Level Three-Tier Architecture</h2>
  <p>SpendWise is engineered following a clean, decoupled Three-Tier Architecture comprising the Presentation Tier, Application Logic Tier, and Data Persistence Tier, as illustrated in Figure 6.1.</p>

  <div class="figure-container">
    <img src="report_assets/system_architecture.png" style="width: 90%; max-height: 185px;" alt="SpendWise System Architecture Diagram">
    <div class="figure-caption">Figure 6.1: High-Level Three-Tier System Architecture of SpendWise</div>
  </div>

  <h2 class="section-title">6.2 Client-Server Communication Flow</h2>
  <p>The interaction between system layers follows a structured, asynchronous request-response cycle:</p>
  <ul>
    <li><strong>Presentation Tier (Vercel CDN):</strong> The client loads static HTML, CSS, and pre-compiled React JavaScript bundles delivered via Vercel's global Edge Network. The client application renders UI components dynamically and executes client-side routing via React Router.</li>
    <li><strong>Application Logic Tier (Render Web Service):</strong> Client interactions initiate asynchronous HTTP requests via Axios. The Express server processes requests through security layers (Helmet, CORS, Rate Limiters, Mongo-Sanitize) before passing them to the JWT Authentication Guard. Authenticated requests are routed to domain-specific controllers.</li>
    <li><strong>Data Tier (MongoDB Atlas):</strong> Controllers execute Mongoose ODM queries against the managed cloud database. Complex aggregations compute real-time analytical metrics, which are returned as JSON responses to the frontend.</li>
  </ul>
  <div class="footer-bar"><span>Department of Computer Science and Engineering, MANIT Bhopal</span><span>Page 13</span></div>
</div>

<!-- PAGE 14: CHAPTER 7 -->
<div class="report-page">
  <div class="header-bar">SpendWise — MERN Expense Tracker | MANIT Bhopal</div>
  <h1 class="chapter-title">7 TECHNOLOGY STACK</h1>

  <h2 class="section-title">7.1 Core Technologies and Frameworks</h2>
  <p>The SpendWise technical stack was carefully selected to maximize developer productivity, operational reliability, cross-platform responsiveness, and runtime execution speed.</p>
  <ul>
    <li><strong>MongoDB:</strong> A document-oriented NoSQL database that stores transaction and user data in flexible BSON structures, perfectly mirroring JavaScript object representations.</li>
    <li><strong>Express.js:</strong> A fast, minimalist backend web framework for Node.js providing robust routing, middleware chaining, and HTTP utility methods.</li>
    <li><strong>React.js (v18):</strong> A declarative, component-based frontend library powering the reactive single-page user interface through a lightweight Virtual DOM reconciliation engine.</li>
    <li><strong>Node.js:</strong> An asynchronous event-driven JavaScript runtime built on Chrome's V8 engine, executing high-throughput non-blocking server processes.</li>
    <li><strong>Tailwind CSS:</strong> A utility-first CSS framework enabling rapid styling, consistent spacing hierarchies, and responsive layout management without writing repetitive CSS stylesheets.</li>
    <li><strong>Recharts:</strong> A composable charting library built on React components and SVG elements, providing performant, responsive financial data visualizations.</li>
  </ul>

  <h2 class="section-title">7.2 Technology Stack Summary Table</h2>
  <p>Table 7.1 provides a comprehensive overview of the libraries, runtime tools, and frameworks utilized across SpendWise.</p>

  <table class="academic-table">
    <tr>
      <th style="width: 25%;">Layer / Component</th>
      <th style="width: 28%;">Technology & Version</th>
      <th>Architectural Role in SpendWise</th>
    </tr>
    <tr><td>Frontend Framework</td><td>React.js 18.3.1</td><td>Component-driven declarative presentation layer</td></tr>
    <tr><td>Build Tool & Bundler</td><td>Vite 5.4.10</td><td>Ultra-fast HMR and optimized Rollup production builds</td></tr>
    <tr><td>Routing Engine</td><td>React Router DOM 7.18.3</td><td>Client-side SPA navigation and protected route handling</td></tr>
    <tr><td>HTTP Client</td><td>Axios 1.7.7</td><td>Promise-based asynchronous API requests with interceptors</td></tr>
    <tr><td>Styling & Theming</td><td>Tailwind CSS 3.4.11</td><td>Utility-first design with CSS variable-driven light/dark themes</td></tr>
    <tr><td>Data Visualization</td><td>Recharts 2.12.7</td><td>Interactive SVG Bar, Pie, and Area chart components</td></tr>
    <tr><td>Icons & Feedback</td><td>Lucide React & Toastify</td><td>Modern UI vector glyphs and non-blocking toast alerts</td></tr>
    <tr><td>Backend Runtime</td><td>Node.js (v18+ / v24)</td><td>Server-side asynchronous JavaScript execution environment</td></tr>
    <tr><td>Web Server Framework</td><td>Express.js 4.19.2</td><td>RESTful API routing, middleware, and request pipeline</td></tr>
    <tr><td>Database & ODM</td><td>MongoDB Atlas & Mongoose 8.6.3</td><td>Managed cloud NoSQL database with schema modeling</td></tr>
    <tr><td>Security Libraries</td><td>bcryptjs, jsonwebtoken, helmet</td><td>Password hashing, JWT token signing, and HTTP hardening</td></tr>
  </table>
  <div class="footer-bar"><span>Department of Computer Science and Engineering, MANIT Bhopal</span><span>Page 14</span></div>
</div>

<!-- PAGE 15: CHAPTER 8 -->
<div class="report-page">
  <div class="header-bar">SpendWise — MERN Expense Tracker | MANIT Bhopal</div>
  <h1 class="chapter-title">8 DATABASE DESIGN</h1>

  <h2 class="section-title">8.1 MongoDB Document Model and Schema Architecture</h2>
  <p>MongoDB stores data as flexible, schema-validated BSON documents grouped into collections. In SpendWise, data modeling follows an optimized hybrid strategy: entity boundaries that require independent querying, pagination, and indexing (Users, Expenses, Budgets) are structured as dedicated collections, while referential integrity is maintained through Mongoose ObjectId references.</p>

  <h2 class="section-title">8.2 Data Schemas: User, Expense, and Budget</h2>
  <p>Table 8.1 details the schema specifications, data types, constraints, and operational purposes across the three primary database models.</p>

  <table class="academic-table">
    <tr>
      <th style="width: 14%;">Collection</th>
      <th style="width: 20%;">Field Name</th>
      <th style="width: 14%;">BSON Type</th>
      <th style="width: 26%;">Validation Rules</th>
      <th>Functional Description</th>
    </tr>
    <tr><td>User</td><td>name</td><td>String</td><td>Required, Trimmed, 2–60 chars</td><td>Full user name displayed in UI</td></tr>
    <tr><td>User</td><td>email</td><td>String</td><td>Required, Unique, Lowercase</td><td>Login identifier and account key</td></tr>
    <tr><td>User</td><td>password</td><td>String</td><td>Required, Min 8 chars, select: false</td><td>bcrypt-hashed password string</td></tr>
    <tr><td>User</td><td>currency</td><td>String</td><td>Enum (USD, EUR, GBP, INR, etc.)</td><td>Default formatting currency</td></tr>
    <tr><td>User</td><td>monthlyIncomeGoal</td><td>Number</td><td>Default: 0, Min: 0</td><td>Target monthly income benchmark</td></tr>
    <tr><td>Expense</td><td>user</td><td>ObjectId</td><td>Required, ref: 'User', Indexed</td><td>Foreign reference to owning user</td></tr>
    <tr><td>Expense</td><td>type</td><td>String</td><td>Enum: ['expense', 'income']</td><td>Differentiates debit from credit</td></tr>
    <tr><td>Expense</td><td>title</td><td>String</td><td>Required, Trimmed, Max 100 chars</td><td>Brief transaction description</td></tr>
    <tr><td>Expense</td><td>amount</td><td>Number</td><td>Required, Min: 0.01</td><td>Monetary value of transaction</td></tr>
    <tr><td>Expense</td><td>category</td><td>String</td><td>Required, Validated against type</td><td>Budgeting and reporting category</td></tr>
    <tr><td>Expense</td><td>date</td><td>Date</td><td>Required, Default: Date.now, Indexed</td><td>Transaction occurrence timestamp</td></tr>
    <tr><td>Expense</td><td>paymentMethod</td><td>String</td><td>Enum: Card, Cash, Bank Transfer</td><td>Payment instrument utilized</td></tr>
    <tr><td>Budget</td><td>user</td><td>ObjectId</td><td>Required, ref: 'User', Compound Index</td><td>Owning user identifier</td></tr>
    <tr><td>Budget</td><td>category</td><td>String</td><td>Required, Enum: EXPENSE_CATEGORIES</td><td>Target expense category</td></tr>
    <tr><td>Budget</td><td>monthlyLimit</td><td>Number</td><td>Required, Min: 1</td><td>Allocated monthly spend ceiling</td></tr>
    <tr><td>Budget</td><td>alertThreshold</td><td>Number</td><td>Default: 80, Min: 1, Max: 100</td><td>Percentage triggering warning alert</td></tr>
  </table>

  <h2 class="section-title">8.3 Aggregation Pipelines and Query Optimization</h2>
  <p>To compute high-throughput analytical statistics without pulling thousands of raw documents into Node.js memory, SpendWise utilizes native MongoDB Aggregation Pipelines. In the dashboard statistics controller (getStats), an aggregate pipeline filters records by user and date bounds ($match), groups them by category ($group with $sum), and sorts them in descending order of spend ($sort). Compound indexing on { user: 1, date: -1 } ensures query execution operates with index-covered scans.</p>
  <div class="footer-bar"><span>Department of Computer Science and Engineering, MANIT Bhopal</span><span>Page 15</span></div>
</div>

<!-- PAGE 16: CHAPTER 9 -->
<div class="report-page">
  <div class="header-bar">SpendWise — MERN Expense Tracker | MANIT Bhopal</div>
  <h1 class="chapter-title">9 METHODOLOGY AND WORKING</h1>

  <h2 class="section-title">9.1 Agile Development Workflow</h2>
  <p>SpendWise was developed following an iterative Agile methodology. Development was divided into four distinct operational phases: Architectural Design & Schema Prototyping, Backend API & Security Engineering, Frontend Component & Analytics Construction, and Cloud Deployment & Validation. Continuous integration was maintained using Git version control, ensuring all components were verified prior to deployment.</p>

  <h2 class="section-title">9.2 User Authentication and Session Security Workflow</h2>
  <p>Authentication is implemented as a stateless, token-based architecture ensuring security across distributed cloud environments. Figure 9.1 illustrates the sequential flow of credentials, validation, token issuance, and protected resource access.</p>

  <div class="figure-container">
    <img src="report_assets/auth_workflow.png" style="width: 82%; max-height: 180px;" alt="SpendWise Authentication and Session Workflow">
    <div class="figure-caption">Figure 9.1: Sequential Authentication and Protected API Request Workflow</div>
  </div>

  <h2 class="section-title">9.3 CRUD Transaction and Budget Computation Logic</h2>
  <p>Transaction management follows a strict user-isolated lifecycle. When a transaction is submitted, the frontend validates input types before dispatching an HTTP POST request containing the Bearer token. The backend protect middleware decodes the JWT, verifies user existence, and injects req.user._id into the database write operation. For budgets, the system executes a real-time join between defined Budget limits and current-month Expense totals, dynamically assigning each category an operational status: 'ok' (&lt; 80%), 'warning' (80%–99%), or 'exceeded' (&gt;= 100%).</p>
  <div class="footer-bar"><span>Department of Computer Science and Engineering, MANIT Bhopal</span><span>Page 16</span></div>
</div>

<!-- PAGE 17: CHAPTER 10 -->
<div class="report-page">
  <div class="header-bar">SpendWise — MERN Expense Tracker | MANIT Bhopal</div>
  <h1 class="chapter-title">10 FRONTEND IMPLEMENTATION</h1>

  <h2 class="section-title">10.1 React Application Structure and Component Hierarchy</h2>
  <p>The client application is organized into a modular component hierarchy. The root App.jsx manages routing tables wrapped in global providers: ThemeProvider, AuthProvider, and DataProvider. Authenticated views are guarded by ProtectedRoute.jsx, which inspects authentication state and redirects unauthenticated requests to the login screen.</p>

  <h2 class="section-title">10.2 State Management via React Context API</h2>
  <p>Global state is distributed across three specialized React contexts:</p>
  <ul>
    <li><strong>AuthContext:</strong> Maintains the authenticated user profile, JWT token string, persistent localStorage synchronization, and login/register/logout actions.</li>
    <li><strong>ThemeContext:</strong> Governs visual appearance mode (light or dark), applying the .dark class to document.documentElement and persisting user preference in localStorage.</li>
    <li><strong>DataContext:</strong> Caches app-wide metadata (supported categories, payment methods, currency definitions) and exposes a refreshTick counter triggering reactive dashboard re-fetching.</li>
  </ul>

  <h2 class="section-title">10.3 Form Validation and User Experience</h2>
  <p>User data entry is powered by React Hook Form, providing frictionless client-side input validation with zero unnecessary component re-renders. Forms validate email syntax, password complexity requirements, positive monetary numbers, and required selection fields before dispatching network requests, providing immediate visual feedback.</p>

  <h2 class="section-title">10.4 Theming Engine (Light and Dark Mode)</h2>
  <p>SpendWise implements an advanced CSS Custom Properties (CSS variables) theming engine configured within index.css and tailwind.config.js. Colors are defined in RGB channel triples (--color-paper, --color-surface, --color-brand, --color-income, --color-expense), allowing Tailwind utilities to dynamically apply variable alpha transparencies while guaranteeing zero flash-of-wrong-theme during page reloads.</p>
  <div class="footer-bar"><span>Department of Computer Science and Engineering, MANIT Bhopal</span><span>Page 17</span></div>
</div>

<!-- PAGE 18: CHAPTER 11 PART 1 -->
<div class="report-page">
  <div class="header-bar">SpendWise — MERN Expense Tracker | MANIT Bhopal</div>
  <h1 class="chapter-title">11 BACKEND IMPLEMENTATION</h1>

  <h2 class="section-title">11.1 Express Server Initialization and Security Middleware</h2>
  <p>The backend entry point (server.js) initializes Express with a layered defense-in-depth security architecture. Helmet hardens HTTP response headers; Mongo-Sanitize strips prohibited '$' and '.' characters from incoming payloads to prevent NoSQL operator injection; CORS allows multi-origin requests from deployed Vercel domains and local dev servers; and rate limiters restrict request floods.</p>

  <div class="code-block">// backend/server.js - Security & Route Middleware Setup
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
app.use('/api/meta', require('./routes/metaRoutes'));</div>

  <h2 class="section-title">11.2 Authentication Controller and Password Hashing</h2>
  <p>User security is managed in User.js and authController.js. Passwords are automatically hashed prior to database persistence using a Mongoose pre-save hook configured with bcryptjs and 12 salt rounds. Password comparison occurs within an encapsulated model method.</p>

  <div class="code-block">// backend/models/User.js - Pre-Save bcryptjs Password Hashing
userSchema.pre('save', async function (next) {
  if (!this.isModified('password')) return next();
  const salt = await bcrypt.genSalt(12);
  this.password = await bcrypt.hash(this.password, salt);
  next();
});

userSchema.methods.matchPassword = async function (enteredPassword) {
  return bcrypt.compare(enteredPassword, this.password);
};</div>
  <div class="footer-bar"><span>Department of Computer Science and Engineering, MANIT Bhopal</span><span>Page 18</span></div>
</div>

<!-- PAGE 19: CHAPTER 11 PART 2 -->
<div class="report-page">
  <div class="header-bar">SpendWise — MERN Expense Tracker | MANIT Bhopal</div>
  <h2 class="section-title">11.3 Expense and Statistical Controllers</h2>
  <p>The expenseController.js file manages transaction CRUD operations and analytical data aggregation. The getStats controller executes parallel database aggregations via Promise.all to construct comprehensive monthly, categorical, and 12-month trend datasets.</p>

  <div class="code-block">// backend/controllers/expenseController.js - Aggregation Pipeline
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
});</div>

  <h2 class="section-title">11.4 Budget Progress Controller</h2>
  <p>The budgetController.js calculates live progress against defined monthly limits. Current-month spending is aggregated and mapped against each category budget, computing percentage utilization and alert status.</p>

  <div class="code-block">// backend/controllers/budgetController.js - Budget Calculation
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
});</div>
  <div class="footer-bar"><span>Department of Computer Science and Engineering, MANIT Bhopal</span><span>Page 19</span></div>
</div>

<!-- PAGE 20: CHAPTER 11 PART 3 -->
<div class="report-page">
  <div class="header-bar">SpendWise — MERN Expense Tracker | MANIT Bhopal</div>
  <h2 class="section-title">11.5 Centralized Error Handler and Validation Middleware</h2>
  <p>To prevent server crashes and provide actionable error feedback to the client, SpendWise implements centralized error and validation middleware. All asynchronous controller functions are wrapped in express-async-handler, routing rejected promises to errorHandler.js.</p>

  <div class="code-block">// backend/middleware/errorHandler.js - Centralized Exception Handling
const notFound = (req, res, next) => {
  res.status(404);
  next(new Error(`Route not found - ${req.originalUrl}`));
};

const errorHandler = (err, req, res, next) => {
  let statusCode = res.statusCode && res.statusCode !== 200 ? res.statusCode : 500;
  let message = err.message || 'Server error';

  if (err.name === 'CastError' && err.kind === 'ObjectId') {
    statusCode = 404;
    message = 'Resource not found';
  }
  if (err.code === 11000) {
    statusCode = 400;
    message = 'An account with this email already exists';
  }
  res.status(statusCode).json({
    success: false,
    message,
    stack: process.env.NODE_ENV === 'production' ? undefined : err.stack
  });
};

module.exports = { notFound, errorHandler };</div>

  <div class="code-block">// backend/middleware/validate.js - express-validator Formatter
const { validationResult } = require('express-validator');

const validate = (req, res, next) => {
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(400).json({
      success: false,
      message: 'Validation failed',
      errors: errors.array().map((e) => ({ field: e.path, message: e.msg }))
    });
  }
  next();
};

module.exports = validate;</div>
  <div class="footer-bar"><span>Department of Computer Science and Engineering, MANIT Bhopal</span><span>Page 20</span></div>
</div>

<!-- PAGE 21: CHAPTER 12 -->
<div class="report-page">
  <div class="header-bar">SpendWise — MERN Expense Tracker | MANIT Bhopal</div>
  <h1 class="chapter-title">12 APPLICATION MODULES</h1>

  <h2 class="section-title">12.1 Authentication and Profile Module</h2>
  <p>The Authentication module manages user identity, onboarding, and persistent credentials. It encompasses the Login and Register views, AuthContext provider, and Profile settings page. Users can update their display name, adjust preferred currency formatting, and establish monthly baseline income benchmarks.</p>

  <h2 class="section-title">12.2 Dashboard Analytics Module</h2>
  <p>The Dashboard module functions as the command center of SpendWise. It presents four top-tier summary KPI cards (Total Balance, Monthly Income, Monthly Expenses, Net Monthly Cash Flow). The analytical section renders a dual-metric Recharts Bar Chart showing income vs. expense cash flows across six months, alongside an interactive Category Pie Chart detailing expenditure proportions.</p>

  <h2 class="section-title">12.3 Transaction Ledger Module</h2>
  <p>The Transactions module provides comprehensive record management. Users can search entries by keyword, filter by transaction type or category, apply custom date ranges, and paginate through records. A responsive modal dialog facilitates adding and editing transactions with immediate validation.</p>

  <h2 class="section-title">12.4 Budget Tracking Module</h2>
  <p>The Budget module empowers users to establish category-specific spending caps. Dynamic progress bars visually indicate percentage utilization, automatically shifting color from green to amber and rust as thresholds are approached and exceeded.</p>

  <h2 class="section-title">12.5 CSV Data Export Module</h2>
  <p>The Data Export module provides one-click data portability. The backend streams RFC-4180 compliant CSV files with appropriate Content-Disposition attachment headers, allowing users to export their transaction records into Microsoft Excel, Google Sheets, or tax preparation software.</p>
  <div class="footer-bar"><span>Department of Computer Science and Engineering, MANIT Bhopal</span><span>Page 21</span></div>
</div>

<!-- PAGE 22: CHAPTER 13 -->
<div class="report-page">
  <div class="header-bar">SpendWise — MERN Expense Tracker | MANIT Bhopal</div>
  <h1 class="chapter-title">13 IMPLEMENTATION DETAILS AND DEPLOYMENT</h1>

  <h2 class="section-title">13.1 Repository Structure and Code Organization</h2>
  <p>SpendWise is structured as a clean, modular full-stack repository with separated backend and frontend codebases:</p>
  <div class="code-block">Expense-Management/
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
└── README.md                 # Complete project technical documentation</div>

  <h2 class="section-title">13.2 Environment Variables and Configuration</h2>
  <p>System configurations are strictly decoupled from source code using environment variables. The backend requires MONGO_URI, JWT_SECRET, NODE_ENV, CLIENT_URL, and PORT. The frontend requires VITE_API_URL pointing to the backend API endpoint. Sensitive keys are strictly excluded from version control via .gitignore rules.</p>

  <h2 class="section-title">13.3 Cloud Deployment Architecture (Render & Vercel)</h2>
  <p>SpendWise is deployed across high-availability cloud platforms. The backend Express service is deployed as a managed Web Service on Render (https://expense-management-xswk.onrender.com), connected to a cloud MongoDB Atlas M0 cluster. The frontend is built and distributed via Vercel's global edge network, with client-side SPA routing rewrites handled via vercel.json.</p>
  <div class="footer-bar"><span>Department of Computer Science and Engineering, MANIT Bhopal</span><span>Page 22</span></div>
</div>

<!-- PAGE 23: CHAPTER 14 PART 1 -->
<div class="report-page">
  <div class="header-bar">SpendWise — MERN Expense Tracker | MANIT Bhopal</div>
  <h1 class="chapter-title">14 APPLICATION SCREENS AND TEST CASES</h1>

  <h2 class="section-title">14.1 User Interface Screenshots and Visual Walkthrough</h2>
  <p>Figure 14.1 illustrates the SpendWise Interactive Analytics Dashboard featuring KPI summary cards, monthly cash flows, category breakdown, and recent transaction records.</p>

  <div class="figure-container">
    <img src="report_assets/dashboard_view.png" style="width: 88%; max-height: 165px;" alt="SpendWise Interactive Analytics Dashboard">
    <div class="figure-caption">Figure 14.1: SpendWise Analytics Dashboard with Summary Cards and Charts</div>
  </div>

  <p>Figure 14.2 displays the SpendWise Budget Management interface, showing per-category spending progress bars and dynamic operational status badges.</p>

  <div class="figure-container">
    <img src="report_assets/budgets_view.png" style="width: 88%; max-height: 155px;" alt="SpendWise Budget Management Interface">
    <div class="figure-caption">Figure 14.2: SpendWise Budget Management Interface with Real-Time Progress and Alerts</div>
  </div>
  <div class="footer-bar"><span>Department of Computer Science and Engineering, MANIT Bhopal</span><span>Page 23</span></div>
</div>

<!-- PAGE 24: CHAPTER 14 PART 2 -->
<div class="report-page">
  <div class="header-bar">SpendWise — MERN Expense Tracker | MANIT Bhopal</div>
  <h2 class="section-title">14.2 Functional and Integration Test Cases</h2>
  <p>To ensure system correctness, data integrity, and error resilience, rigorous functional, integration, and security test cases were executed across the application. Table 14.1 records the test specifications, test inputs, expected behaviors, and verified outcomes.</p>

  <table class="academic-table">
    <tr>
      <th style="width: 10%;">Test ID</th>
      <th style="width: 22%;">Test Scenario</th>
      <th style="width: 28%;">Test Inputs / Actions</th>
      <th style="width: 30%;">Expected System Behavior</th>
      <th>Status</th>
    </tr>
    <tr><td>TC-01</td><td>User Registration</td><td>Submit valid name, email, password, and currency</td><td>User document created in Atlas; JWT token returned; redirect to dashboard</td><td>PASS</td></tr>
    <tr><td>TC-02</td><td>Duplicate Email</td><td>Register with already existing email address</td><td>HTTP 400 Bad Request; error: 'Account with this email already exists'</td><td>PASS</td></tr>
    <tr><td>TC-03</td><td>User Login</td><td>Submit valid registered email and password</td><td>HTTP 200 OK; valid JWT token issued; user profile state populated</td><td>PASS</td></tr>
    <tr><td>TC-04</td><td>Invalid Password</td><td>Submit correct email with incorrect password</td><td>HTTP 401 Unauthorized; error: 'Invalid email or password'</td><td>PASS</td></tr>
    <tr><td>TC-05</td><td>Protected Route</td><td>Access /expenses without Bearer authorization token</td><td>HTTP 401 Unauthorized; client redirects automatically to /login</td><td>PASS</td></tr>
    <tr><td>TC-06</td><td>Create Transaction</td><td>POST /api/expenses with valid amount, title, category</td><td>HTTP 201 Created; expense saved with user ID; dashboard stats update</td><td>PASS</td></tr>
    <tr><td>TC-07</td><td>Input Validation</td><td>POST /api/expenses with negative amount or empty title</td><td>HTTP 400 Bad Request; validation errors returned with field descriptors</td><td>PASS</td></tr>
    <tr><td>TC-08</td><td>Data Isolation</td><td>User A queries expenses; inspect database output</td><td>Only transactions matching req.user._id returned; 100% data isolation</td><td>PASS</td></tr>
    <tr><td>TC-09</td><td>Budget Alert Logic</td><td>Record expense exceeding 80% and 100% of budget limit</td><td>Status transitions dynamically from 'ok' to 'warning' and 'exceeded'</td><td>PASS</td></tr>
    <tr><td>TC-10</td><td>CSV Export</td><td>Click 'Export CSV' button on transaction list page</td><td>HTTP 200 OK; text/csv attachment downloaded with valid RFC-4180 format</td><td>PASS</td></tr>
    <tr><td>TC-11</td><td>Theme Switch</td><td>Toggle theme switch from light to dark and refresh</td><td>Dark class applied to HTML root; spendwise-theme persisted in storage</td><td>PASS</td></tr>
  </table>

  <h2 class="section-title">14.3 Analysis of Test Results and Observations</h2>
  <p>All 11 test cases completed with 100% pass rates. The system demonstrated robust input validation, preventing invalid records from reaching the database. Cryptographic operations operated seamlessly, and multi-tenant isolation was strictly maintained across all user accounts.</p>
  <div class="footer-bar"><span>Department of Computer Science and Engineering, MANIT Bhopal</span><span>Page 24</span></div>
</div>

<!-- PAGE 25: CHAPTER 15 -->
<div class="report-page">
  <div class="header-bar">SpendWise — MERN Expense Tracker | MANIT Bhopal</div>
  <h1 class="chapter-title">15 APPLICATIONS, ADVANTAGES AND LIMITATIONS</h1>

  <h2 class="section-title">15.1 Real-World Practical Applications</h2>
  <p>SpendWise addresses practical financial management requirements across multiple user segments: college students tracking monthly allowances and academic expenses; freelance contractors logging irregular project income and deductible operational costs; and working professionals monitoring household utility and discretionary expenditure.</p>

  <h2 class="section-title">15.2 Key Technical Advantages</h2>
  <p>The application provides distinct advantages over alternative solutions:</p>
  <ul>
    <li><strong>Sovereign Data Privacy:</strong> Operates with zero third-party advertising trackers, external telemetry, or invasive bank-credential harvesting.</li>
    <li><strong>Real-Time Reactive Performance:</strong> Vite and React 18 deliver near-instantaneous page transitions and reactive component updates without full-page reloads.</li>
    <li><strong>Automated Visual Intelligence:</strong> MongoDB aggregation pipelines offload heavy calculation burdens from client devices, delivering instant analytical charts.</li>
    <li><strong>Zero-Installation Accessibility:</strong> Fully web-native and responsive across mobile, tablet, and desktop viewports without requiring dedicated app installations.</li>
  </ul>

  <h2 class="section-title">15.3 System Limitations and Constraints</h2>
  <p>Current operational limitations include reliance on manual transaction data entry rather than automated Open Banking API integrations, absence of automated recurring transaction scheduling via cron jobs, and support limited to single-user accounts without shared multi-user household budgets.</p>
  <div class="footer-bar"><span>Department of Computer Science and Engineering, MANIT Bhopal</span><span>Page 25</span></div>
</div>

<!-- PAGE 26: CHAPTER 16 -->
<div class="report-page">
  <div class="header-bar">SpendWise — MERN Expense Tracker | MANIT Bhopal</div>
  <h1 class="chapter-title">16 FUTURE SCOPE</h1>

  <h2 class="section-title">16.1 Advanced Financial Intelligence Enhancements</h2>
  <p>Proposed future enhancements include integrating machine-learning categorization models (e.g., naive Bayes or transformer classifiers) to predict transaction categories from merchant titles, alongside OCR-based receipt scanning using computer vision APIs.</p>

  <h2 class="section-title">16.2 Architectural and Platform Roadmap</h2>
  <p>Future platform enhancements contemplate Progressive Web Application (PWA) offline synchronization via Service Workers and IndexedDB, alongside multi-user collaborative budgets with role-based access control (RBAC).</p>

  <h2 class="section-title">16.3 Open Banking and Automated Ingestion</h2>
  <p>Integrating Account Aggregator APIs will enable secure, consent-driven transaction synchronizations directly from financial institutions, eliminating manual data entry friction while preserving end-to-end user privacy.</p>
  <div class="footer-bar"><span>Department of Computer Science and Engineering, MANIT Bhopal</span><span>Page 26</span></div>
</div>

<!-- PAGE 27: CHAPTER 17 -->
<div class="report-page">
  <div class="header-bar">SpendWise — MERN Expense Tracker | MANIT Bhopal</div>
  <h1 class="chapter-title">17 CONCLUSION</h1>
  <p>The industrial training completed through Unstop provided an exceptional, industry-aligned foundation in modern full-stack web engineering using the MERN Stack. The conceptual principles acquired—spanning asynchronous runtime execution, RESTful API design, NoSQL document modeling, reactive component architectures, and web application security—were rigorously applied towards designing, implementing, testing, and deploying SpendWise.</p>

  <p>SpendWise represents a complete, practical, and production-ready personal expense management system that resolves the friction, privacy concerns, and computational limitations of traditional financial tracking tools. The project successfully demonstrates the power of modern JavaScript ecosystems in delivering scalable, performant, and user-centric software solutions.</p>

  <p>Through this project, the author achieved comprehensive hands-on proficiency in architecting decoupled cloud applications, implementing industry-standard authentication mechanisms, structuring complex database aggregation pipelines, and deploying distributed web services across modern cloud providers.</p>
  <div class="footer-bar"><span>Department of Computer Science and Engineering, MANIT Bhopal</span><span>Page 27</span></div>
</div>

<!-- PAGE 28: REFERENCES & APPENDIX -->
<div class="report-page">
  <div class="header-bar">SpendWise — MERN Expense Tracker | MANIT Bhopal</div>
  <h1 class="chapter-title" style="margin-bottom: 6px;">REFERENCES</h1>

  <div style="font-size: 8.5pt; line-height: 1.35;">
    <p>1. Unstop. (2026). MERN Full Stack Course. https://unstop.com/courses/mern-full-stack</p>
    <p>2. Kancharla, A. K. (2026). SpendWise — Personal Finance and Expense Management System [Source Code]. GitHub. https://github.com/kancharla-ajay-kumar/Expense-Management</p>
    <p>3. MongoDB, Inc. (2026). MongoDB Documentation and Aggregation Framework Reference. https://www.mongodb.com/docs/</p>
    <p>4. OpenJS Foundation. (2026). Node.js v20 LTS Documentation. https://nodejs.org/docs/</p>
    <p>5. Express.js Community. (2026). Express.js 4.x API Reference and Middleware Guide. https://expressjs.com/</p>
    <p>6. Meta Platforms, Inc. (2026). React 18 Documentation: Hooks, Components, and Virtual DOM. https://react.dev/</p>
    <p>7. Vite Team. (2026). Vite: Next Generation Frontend Tooling. https://vitejs.dev/</p>
    <p>8. Tailwind Labs, Inc. (2026). Tailwind CSS Documentation. https://tailwindcss.com/docs</p>
    <p>9. Recharts Group. (2026). Recharts: Redefined Chart Library Built with React and D3. https://recharts.org/</p>
    <p>10. Internet Engineering Task Force (IETF). (2015). RFC 7519: JSON Web Token (JWT). https://datatracker.ietf.org/doc/html/rfc7519</p>
    <p>11. Render Services, Inc. (2026). Render Cloud Hosting Documentation. https://render.com/docs</p>
    <p>12. Vercel, Inc. (2026). Vercel Deployment Documentation and Edge Network Guide. https://vercel.com/docs</p>
  </div>

  <h1 class="chapter-title" style="margin-top: 10px; margin-bottom: 6px;">APPENDIX</h1>

  <h2 class="section-title" style="margin-top: 4px; margin-bottom: 2px;">A.1 Repository and Deployment Artifacts</h2>
  <p style="font-size: 8.8pt; margin-bottom: 2px;"><strong>Project Source Code Repository:</strong> https://github.com/kancharla-ajay-kumar/Expense-Management</p>
  <p style="font-size: 8.8pt; margin-bottom: 2px;"><strong>Live Production Backend Service (Render):</strong> https://expense-management-xswk.onrender.com</p>
  <p style="font-size: 8.8pt; margin-bottom: 6px;"><strong>Unstop Course Certificate Verification:</strong> https://unstop.com/certificate-preview/2fe44ee8-7ea5-40ad-8f8c-b391ea250bd7</p>

  <h2 class="section-title" style="margin-top: 4px; margin-bottom: 2px;">A.2 Key Project Artifacts Summary</h2>
  <table class="academic-table" style="font-size: 8.5pt; margin-top: 3px;">
    <tr>
      <th style="width: 35%;">Artifact File Path</th>
      <th>Architectural Role and Operational Function in SpendWise</th>
    </tr>
    <tr><td>backend/server.js</td><td>Express server entry point configuring Helmet, CORS, Rate Limiters, and API routes</td></tr>
    <tr><td>backend/config/db.js</td><td>Mongoose cloud connection handler for MongoDB Atlas with auto-sanitization</td></tr>
    <tr><td>backend/models/Expense.js</td><td>Mongoose schema defining transaction attributes, categories, and indexes</td></tr>
    <tr><td>backend/models/User.js</td><td>User authentication schema with bcryptjs salt generation and pre-save hashing</td></tr>
    <tr><td>backend/controllers/expenseController.js</td><td>Transaction CRUD logic and high-performance MongoDB analytical aggregations</td></tr>
    <tr><td>backend/controllers/budgetController.js</td><td>Dynamic monthly budget evaluation and operational status assignment</td></tr>
    <tr><td>frontend/src/App.jsx</td><td>Client-side route declarations with ProtectedRoute authorization guards</td></tr>
    <tr><td>frontend/src/context/AuthContext.jsx</td><td>Centralized user session management and localStorage synchronization</td></tr>
    <tr><td>frontend/src/api/axios.js</td><td>Axios HTTP instance with automatic JWT Authorization bearer injection</td></tr>
    <tr><td>frontend/vercel.json</td><td>Vercel edge rewrite configuration ensuring client-side SPA routing persistence</td></tr>
  </table>
  <div class="footer-bar"><span>Department of Computer Science and Engineering, MANIT Bhopal</span><span>Page 28</span></div>
</div>

</body>
</html>
"""

with open(html_out, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated HTML report: {html_out}")
