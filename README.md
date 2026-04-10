# SAP FBL1N Vendor Analysis & Risk Intelligence System

## Overview

Working in finance means constantly keeping tabs on vendor payments — which invoices are overdue, which vendors are becoming risky, and how all of it affects cash flow. This project takes raw SAP FBL1N (Vendor Line Item) data and turns it into something actually useful: a vendor risk intelligence system that combines descriptive analytics, machine learning, and clustering to move from *"here's what happened"* to *"here's what to do about it."*

---

## The Problem

Finance teams deal with a familiar set of headaches — overdue invoices pile up, high-risk vendors go unnoticed until it's too late, and cash flow visibility is always playing catch-up. The goal here was to build something that addresses all three: not just flagging problems after the fact, but predicting and preventing them.

---

## Tech Stack

- **Python** — Pandas, NumPy for data wrangling
- **Scikit-learn** — machine learning models
- **Matplotlib & Seaborn** — visualizations
- **Jupyter Notebook** — development environment

---

## Dataset

The analysis runs on a simulated SAP FBL1N dataset (~50,000 rows) covering vendor details, invoice amounts, posting/due/clearing dates, payment blocks, Special G/L indicators, and invoice status (Open vs. Cleared).

> **Note:** Dummy data is used throughout to keep things privacy-safe.

---

## Feature Engineering

Rather than using raw fields directly, the project builds business-meaningful features:

| Feature | What It Captures |
|---|---|
| `days_outstanding` | How long since the invoice was posted |
| `overdue_days` | How far past the due date it sits |
| `payment_days` | How long it actually took to clear |
| `sla_breach` | Whether payment came in late |

---

## Analysis

**Aging Buckets** — Invoices are grouped into 0–30, 31–60, 61–90, and 90+ day buckets to give a clear picture of where exposure is concentrated.

**Vendor Contribution** — A small number of vendors typically account for a disproportionately large share of outstanding balances. This analysis surfaces that concentration risk explicitly.

**Payment Behavior** — Distribution of payment days across the vendor base, with delayed payment trends highlighted.

---

## Machine Learning Models

### 1. SLA Breach Prediction (Classification)

A Random Forest Classifier trained to predict whether a given invoice will be paid late. It's not a perfect predictor — finance data rarely is — but with ~54% accuracy and balanced precision/recall, it adds genuine signal for prioritization.

### 2. Payment Days Prediction (Regression)

A Random Forest Regressor that estimates how many days an invoice will take to clear. The model achieves an MAE of ~15 days and an R² of ~0.42, which is reasonable given how much payment behavior varies across vendors and invoice types.

---

## Vendor Risk Clustering

This is where the analysis gets most actionable. Using K-Means clustering (k=4, selected via the Elbow Method), vendors are segmented based on:

- Average overdue days
- SLA breach rate
- Total outstanding amount
- Invoice volume

The result is four distinct risk tiers:

| Segment | Profile |
|---|---|
| 🟢 Low Risk | Consistent payers, minimal exposure |
| 🟡 Medium Risk | Occasional delays, worth watching |
| 🟠 High Risk | Frequent delays, needs active management |
| 🔴 Critical Risk | High overdue + high outstanding — act now |

---

## Recommendation Engine

Risk tier drives a clear action:

| Risk Level | Action |
|---|---|
| 🔴 Critical | Immediate follow-up |
| 🟠 High | Weekly monitoring |
| 🟡 Medium | Prioritize in payment runs |
| 🟢 Low | Routine monitoring only |

---

## Key Insights

- A small cluster of vendors accounts for a large share of total outstanding exposure
- Many invoices sit in overdue buckets longer than they should
- Payment behavior varies dramatically across the vendor base — meaning a one-size-fits-all approach to AP management leaves real risk unmanaged

---

## Business Impact

This system improves cash flow visibility, lets finance teams get ahead of problems rather than react to them, and gives leadership data-driven ground to stand on when making vendor decisions.

---

## What's Next

- 📊 Interactive Power BI dashboard
- ⚡ Real-time SAP data integration
- 🤖 Upgraded models (XGBoost, LightGBM)
- 📅 Time-series cash flow forecasting
- 🔔 Automated alerts for high-risk vendors

---

## Project Structure

```
sap-financial-data-analysis/
│
├── Dataset/
├── Notebook/
├── Random Data Generation Script/
└── README.md
```

---

## Author

**Sahil Bhaidkar**

---

## Project Summary

This project follows a deliberate progression:

**Descriptive Analytics → Predictive Modeling → Prescriptive Recommendations**

The aim was a complete, end-to-end solution that mirrors how finance teams actually think — not just analyzing the past, but informing what happens next.
