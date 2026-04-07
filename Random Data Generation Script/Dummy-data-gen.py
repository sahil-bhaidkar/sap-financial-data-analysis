import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()
np.random.seed(42)
random.seed(42)

# -----------------------------
# CONFIG
# -----------------------------
N_ROWS = 50000
N_VENDORS = 200

# -----------------------------
# MASTER DATA
# -----------------------------
vendor_codes = [f"V{1000+i}" for i in range(N_VENDORS)]
vendor_names = [fake.company() for _ in range(N_VENDORS)]
vendor_map = dict(zip(vendor_codes, vendor_names))

gl_accounts = [f"{300000+i}" for i in range(50)]
business_areas = ["MUM", "DEL", "BLR", "CHE"]
currencies = ["INR"]*85 + ["USD"]*10 + ["EUR"]*5

doc_types = ["KR", "KZ", "KG"]  # Invoice, Payment, Credit Memo

# Simulate "bad vendors" (always late)
bad_vendors = set(random.sample(vendor_codes, 20))

# -----------------------------
# DATA GENERATION
# -----------------------------
data = []

for i in range(N_ROWS):
    
    vendor = random.choice(vendor_codes)
    vendor_name = vendor_map[vendor]
    
    status = random.choices(["O", "C"], weights=[30, 70])[0]
    
    posting_date = fake.date_between(start_date='-2y', end_date='today')
    document_date = posting_date - pd.Timedelta(days=random.randint(0, 5))
    
    payment_terms = random.choice([30, 45, 60])
    due_date = posting_date + pd.Timedelta(days=payment_terms)
    
    # Amount distribution (more realistic)
    amount = round(np.random.lognormal(mean=10, sigma=0.8), 2)
    
    doc_type = random.choice(doc_types)
    currency = random.choice(currencies)
    
    # Payment Block & Special GL
    payment_block = random.choices(["", "", "", "A", "B"], weights=[70,10,10,5,5])[0]
    special_gl = random.choices(["", "", "", "A", "W"], weights=[75,10,5,5,5])[0]
    
    # Clearing Logic
    if status == "C":
        if vendor in bad_vendors:
            delay = random.randint(60, 120)
        else:
            delay = random.randint(5, 60)
            
        clearing_date = posting_date + pd.Timedelta(days=delay)
        clearing_doc = f"CL{100000+i}"
    else:
        clearing_date = None
        clearing_doc = None
    
    data.append([
        status,
        vendor,
        vendor_name,
        fake.bothify(text="REF####"),
        fake.bothify(text="ASN####"),
        f"DOC{100000+i}",
        doc_type,
        document_date,
        payment_block,
        special_gl,
        due_date,
        amount,
        amount,
        currency,
        "INR",
        posting_date,
        random.choice(business_areas),
        random.choice(gl_accounts),
        clearing_doc,
        clearing_date,
        fake.sentence(nb_words=6)
    ])

# -----------------------------
# CREATE DATAFRAME
# -----------------------------
df = pd.DataFrame(data, columns=[
    "status",
    "vendor_code",
    "vendor_name",
    "reference",
    "assignment",
    "document_number",
    "document_type",
    "document_date",
    "payment_block",
    "special_gl",
    "due_date",
    "amount_doc_currency",
    "amount_local_currency",
    "doc_currency",
    "local_currency",
    "posting_date",
    "business_area",
    "gl_account",
    "clearing_document",
    "clearing_date",
    "text"
])

# -----------------------------
# SAVE FILE
# -----------------------------
df.to_csv("fbl1n_sap_like_50k.csv", index=False)

print("✅ Dataset created successfully: fbl1n_sap_like_50k.csv")
df.head(3)
