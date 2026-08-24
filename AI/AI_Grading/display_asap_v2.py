# File: display_asap_v2.py
# Run: python display_asap_v2.py

import sys
import pandas as pd

# Reconfigure stdout to utf-8
sys.stdout.reconfigure(encoding="utf-8")

# Load dataset
df = pd.read_excel("ASAP-v2.xlsx")

print(f"Total Rows: {len(df)}")
print(f"Total Columns: {df.shape[1]}")

print("\n--- Column Names in File ---")
for col in df.columns:
    print(f"  - {col}")

# Summary view
print("\n--- Summary View (First 10 Rows) ---")
print(
    df[[
        "essay_id",
        "prompt_name",
        "score",
        "gender",
        "race_ethnicity",
    ]].head(10).to_string(index=False)
)

# Detailed view of 1 full record
print("\n" + "=" * 50)
print("--- Full Data for Record #1 ---")
first_record = df.iloc[0]

for col in df.columns:
    val = first_record[col]
    print(f"\n[{col}]:")
    
    if pd.isna(val):
        print("NaN")
    else:
        # Convert to string and strip corrupt bytes that break PowerShell output
        text = str(val).encode("ascii", "ignore").decode("ascii").strip()
        print(text)

# Force a clean newline buffer at the end
print("\n" + "=" * 50)
print("Done displaying record.\n\n", flush=True)