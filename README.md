# 📊 SAP FBL1N Vendor Analysis & Risk Intelligence System

## 🔍 Overview

This project analyzes SAP FBL1N (Vendor Line Item) data to uncover payment behavior patterns, identify overdue exposure, and build a vendor risk intelligence system.

It combines:

* 📈 Descriptive Analytics
* 🤖 Machine Learning
* 🧠 Vendor Segmentation (Clustering)
* ⚡ Business Recommendations

---

## 🎯 Business Problem

Finance teams often struggle with:

* Tracking overdue invoices
* Identifying high-risk vendors
* Managing cash flow effectively

This project solves these challenges by transforming raw SAP data into **actionable insights and predictive models**.

---

## 🛠 Tech Stack

* **Python** (Pandas, NumPy)
* **Scikit-learn** (ML Models)
* **Matplotlib & Seaborn** (Visualization)
* **Jupyter Notebook**

---

## 📂 Dataset

* Simulated SAP FBL1N dataset (~50,000 rows)
* Includes:

  * Vendor details
  * Invoice amounts
  * Posting, due, and clearing dates
  * Payment blocks & Special G/L indicators
  * Invoice status (Open / Cleared)

> ⚠️ Note: Dummy data is used to maintain data privacy.

---

## ⚙️ Feature Engineering

Key business-driven features:

| Feature              | Description                   |
| -------------------- | ----------------------------- |
| **days_outstanding** | Time since invoice was posted |
| **overdue_days**     | Delay beyond due date         |
| **payment_days**     | Time taken to clear invoice   |
| **sla_breach**       | Whether invoice was paid late |

---

## 📊 Key Analysis

### 🔹 Aging Analysis

Invoices categorized into:

* 0–30 days
* 31–60 days
* 61–90 days
* 90+ days

### 🔹 Vendor Contribution

* Identified top vendors contributing to outstanding exposure
* Highlighted concentration risk

### 🔹 Payment Behavior

* Distribution of payment days
* Detection of delayed payment trends

---

## 🤖 Machine Learning Models

### 🔸 1. SLA Breach Prediction (Classification)

* Model: Random Forest Classifier
* Objective: Predict whether an invoice will be paid late

**Performance:**

* Accuracy: ~54%
* Balanced precision & recall

---

### 🔸 2. Payment Days Prediction (Regression)

* Model: Random Forest Regressor
* Objective: Predict number of days to clear invoices

**Performance:**

* MAE: ~15 days
* R² Score: ~0.42

---

## 🧠 Vendor Risk Clustering

### 🔹 Objective

Segment vendors based on payment behavior and financial exposure.

### 🔹 Features Used

* Average overdue days
* SLA breach rate
* Total outstanding amount
* Invoice volume

### 🔹 Method

* Algorithm: K-Means Clustering
* Optimal clusters determined using **Elbow Method (k = 4)**

### 🔹 Risk Segments

| Risk Level       | Description                       |
| ---------------- | --------------------------------- |
| 🟢 Low Risk      | Consistent payments, low exposure |
| 🟡 Medium Risk   | Occasional delays                 |
| 🟠 High Risk     | Frequent delays                   |
| 🔴 Critical Risk | High overdue + high outstanding   |

---

## ⚡ Recommendation Engine

Based on vendor risk level:

* 🔴 **Critical Risk** → Immediate follow-up
* 🟠 **High Risk** → Weekly monitoring
* 🟡 **Medium Risk** → Prioritize payments
* 🟢 **Low Risk** → Routine monitoring

---

## 📈 Key Insights

* A small group of vendors contributes to a large portion of outstanding balance
* Significant number of invoices fall into overdue categories
* Payment behavior varies widely across vendors
* High-risk vendors identified using clustering

---

## 💡 Business Impact

* Improves cash flow visibility
* Enables proactive vendor management
* Reduces overdue exposure
* Supports data-driven financial decisions

---

## 🚀 Future Enhancements

* 📊 Power BI Dashboard (interactive visuals)
* ⚡ Real-time SAP data integration
* 🤖 Advanced ML models (XGBoost, LightGBM)
* 📅 Time-series forecasting for cash flow
* 🔔 Automated alerts for high-risk vendors

---

## 📁 Project Structure

```
sap-financial-data-analysis/
│
├── Dataset/
├── Notebook/
├── Random Data Generation Script/
├── README.md
```

---

## 👨‍💻 Author

**Sahil Bhaidkar**

---

## 🏆 Project Summary

This project evolves from:

➡️ Descriptive Analytics
➡️ Predictive Modeling
➡️ Prescriptive Decision-Making

Delivering a complete **end-to-end analytics solution** aligned with real-world finance operations.
