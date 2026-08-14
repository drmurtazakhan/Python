# File: display_asap_v2.py
# Run: python display_asap_v2.py

import pandas as pd

# Read ASAP-v2.xlsx
df = pd.read_excel("ASAP-v2.xlsx")

print(f"Total Rows: {len(df)}")
print(f"Total Columns: {df.shape[1]}")

print("\n--- Column Names in File ---")
for col in df.columns:
    print(f"  - {col}")

# Summary view of key metadata columns
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
    
    # Check for empty/NaN cells
    if pd.isna(val):
        print("NaN")
    else:
        # Convert to string, trim whitespace, and force a fresh newline after printing
        text = str(val).strip()
        print(text)

# Force an explicit newline and closing boundary so the prompt drops down
print("\n" + "=" * 50)
print("Done displaying record.\n")