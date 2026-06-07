# 🗄️ DecodeLabs | Data Analytics | Project 3 — SQL Data Analysis

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightblue?style=for-the-badge&logo=sqlite)
![VS Code](https://img.shields.io/badge/VS%20Code-Editor-blue?style=for-the-badge&logo=visualstudiocode)
![DecodeLabs](https://img.shields.io/badge/DecodeLabs-Batch%202026-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)

---

## 📌 About This Project

This is **Project 3** of the **DecodeLabs Industrial Training Program (Batch 2026)** under the **Data Analytics** track.

The goal of this project is to perform **SQL Data Analysis** on a real-world orders dataset using **Python + SQLite**. The project demonstrates the ability to extract actionable business insights from raw data using structured SQL queries.

> *"This track isn't about viewing spreadsheets — it's about Querying for Truth."*
> — DecodeLabs

---

## 🎯 Project Goal

Use SQL queries to extract meaningful insights from an orders dataset containing **1,200 rows** and **14 columns**.

---

## 📊 Dataset Overview

| Column | Type | Example |
|---|---|---|
| OrderID | TEXT | ORD200000 |
| Date | DATE | 2023-01-04 |
| CustomerID | TEXT | C72649 |
| Product | TEXT | Laptop, Phone, Monitor... |
| Quantity | INTEGER | 1 – 10 |
| UnitPrice | DECIMAL | 570.62 |
| ShippingAddress | TEXT | 928 Main St |
| PaymentMethod | TEXT | Credit Card, Cash... |
| OrderStatus | TEXT | Delivered, Shipped... |
| TrackingNumber | TEXT | TRK37947903 |
| ItemsInCart | INTEGER | 3 – 10 |
| CouponCode | TEXT | SAVE10, FREESHIP |
| ReferralSource | TEXT | Instagram, Referral... |
| TotalPrice | DECIMAL | 2853.10 |

**Products:** Laptop, Phone, Monitor, Tablet, Printer, Chair, Desk

**Order Statuses:** Delivered, Shipped, Pending, Cancelled, Returned

**Payment Methods:** Credit Card, Debit Card, Cash, Online, Gift Card

---

## 🛠️ Tools & Technologies

- **Language:** Python 3.11
- **Database:** SQLite3 (built into Python)
- **Editor:** Visual Studio Code
- **Library:** openpyxl (to read Excel file)
- **Extension:** SQLite Viewer (VS Code)

---

## 📁 Project Structure

```
sql_project3/
│
├── load_data.py        ← Reads Excel and loads into SQLite database
├── queries.py          ← All 7 SQL queries with formatted output
├── results.txt         ← Terminal output of all query results
└── README.md           ← Project documentation
```

> ⚠️ The dataset (.xlsx) and database (.db) files are not included in this repository.

---

## ⚙️ How to Run This Project

### 1. Clone the Repository
```bash
git clone https://github.com/fannushaik16-rgb/decodelabs-data-analytics-project3.git
cd decodelabs-data-analytics-project3
```

### 2. Install Required Library
```bash
pip install openpyxl
```

### 3. Add the Dataset
Place your `Dataset_for_Data_Analytics_3.xlsx` file in the project folder.

### 4. Load Data into Database
```bash
python load_data.py
```
This creates `orders.db` — your SQLite database with all 1,200 rows.

### 5. Run All SQL Queries
```bash
python queries.py
```

### 6. Save Results to File
```bash
python queries.py > results.txt
```

---

## 🔍 SQL Queries Covered

### Q1 — SELECT: View First 10 Orders
```sql
SELECT OrderID, Product, Quantity, TotalPrice
FROM orders
LIMIT 10;
```

### Q2 — WHERE: Filter Delivered Orders
```sql
SELECT OrderID, Product, OrderStatus, TotalPrice
FROM orders
WHERE OrderStatus = 'Delivered';
```

### Q3 — ORDER BY: Top 10 Highest Value Orders
```sql
SELECT OrderID, Product, TotalPrice
FROM orders
ORDER BY CAST(TotalPrice AS REAL) DESC
LIMIT 10;
```

### Q4 — GROUP BY + COUNT: Orders per Product
```sql
SELECT Product, COUNT(*) AS TotalOrders
FROM orders
GROUP BY Product
ORDER BY TotalOrders DESC;
```

### Q5 — SUM: Total Revenue per Product
```sql
SELECT Product,
       ROUND(SUM(CAST(TotalPrice AS REAL)), 2) AS TotalRevenue
FROM orders
GROUP BY Product
ORDER BY TotalRevenue DESC;
```

### Q6 — AVG: Average Order Value per Payment Method
```sql
SELECT PaymentMethod,
       ROUND(AVG(CAST(TotalPrice AS REAL)), 2) AS AvgOrderValue
FROM orders
GROUP BY PaymentMethod
ORDER BY AvgOrderValue DESC;
```

### Q7 — FULL SUMMARY: COUNT + SUM + AVG per Product
```sql
SELECT Product,
       COUNT(*) AS TotalOrders,
       ROUND(SUM(CAST(TotalPrice AS REAL)), 2) AS TotalRevenue,
       ROUND(AVG(CAST(TotalPrice AS REAL)), 2) AS AvgRevenue
FROM orders
GROUP BY Product
ORDER BY TotalRevenue DESC;
```

---

## 📈 Key Insights Found

- 📦 **Printer** had the highest number of orders (173)
- 💰 Total revenue and average order value calculated per product
- 🚚 Filtered and analyzed orders by delivery status
- 💳 Compared average spending across all payment methods
- 🔢 Full business summary table generated with COUNT, SUM, and AVG

---

## 📚 Key SQL Concepts Used

| Concept | Purpose |
|---|---|
| `SELECT` | Choose which columns to display |
| `FROM` | Specify the table |
| `WHERE` | Filter rows by condition |
| `ORDER BY` | Sort results ASC or DESC |
| `GROUP BY` | Group rows into categories |
| `COUNT()` | Count number of rows |
| `SUM()` | Calculate total of a column |
| `AVG()` | Calculate average of a column |
| `ROUND()` | Round decimal values |
| `LIMIT` | Restrict number of rows returned |

---

## 🧠 SQL Execution Order Learned

```
1. FROM        → Locate the table
2. WHERE       → Filter individual rows
3. GROUP BY    → Group into buckets
4. HAVING      → Filter groups
5. SELECT      → Pick columns & aliases
6. ORDER BY    → Sort final output
```

---

## 🏆 Project Status

| Requirement | Status |
|---|---|
| Write SELECT queries | ✅ Done |
| Use WHERE clause | ✅ Done |
| Use ORDER BY | ✅ Done |
| Use GROUP BY | ✅ Done |
| Use COUNT aggregation | ✅ Done |
| Use SUM aggregation | ✅ Done |
| Use AVG aggregation | ✅ Done |

---
## 👤 Author
**fannu**
- 🎓 DecodeLabs Industrial Training — Batch 2026
- 🌐 [GitHub Profile](https://github.com/fannushaik16-rgb)
- 📧 fannushaik16@gmail.com

---

## 🏢 About DecodeLabs

DecodeLabs is an industrial training program that provides hands-on, real-world project experience in Data Analytics, Web Development, and more.

- 🌐 [www.decodelabs.tech](https://www.decodelabs.tech)
- 📧 decodelabs.tech@gmail.com
- 📞 +91 89330 06408
- 📍 Greater Lucknow, India

---

⭐ *If you found this helpful, give the repo a star!*
