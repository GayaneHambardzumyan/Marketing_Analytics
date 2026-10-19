# Step 3: convert the CIPA pdf (cr300.pdf) into data/cipa_shipments.csv
import re
import sys
import pandas as pd
import pdfplumber

pdf_path = sys.argv[1] if len(sys.argv) > 1 else "cr300.pdf"

with pdfplumber.open(pdf_path) as pdf:
    lines = pdf.pages[0].extract_text().splitlines()


def is_number(token):
    return re.fullmatch(r"\d{1,3}(,\d{3})*|\d+", token) is not None


header_idx = next(i for i, l in enumerate(lines) if "Quantity of Total Shipments" in l)
years = [int(t) for t in lines[header_idx + 1].split()]

label_idx = next(i for i, l in enumerate(lines) if l.strip() == "Digital Still Cameras Total")
values = [int(t.replace(",", "")) for t in lines[label_idx - 1].split() if is_number(t)]

assert len(years) == len(values), f"{len(years)} years vs {len(values)} values"

df = pd.DataFrame({"year": years, "units_thousands": values})
df.to_csv("data/cipa_shipments.csv", index=False)
print(df)
