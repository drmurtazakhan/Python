# Run: Python extract_samples_asap.py

# File: extract_full_records.py

import pandas as pd

# 1. Load the original file (loads all 14 columns)
input_file = "ASAP-v1.xlsx"
print(f"Loading '{input_file}'...")
df = pd.read_excel(input_file)

# 2. Extract 5 complete records per 'prompt_name' category
# This preserves all 14 columns for every row selected
sampled_df = df.groupby("prompt_name").head(5)

# 3. Confirm all columns are present
print(f"\nSuccessfully extracted {len(sampled_df)} total rows.")
print(f"Total columns preserved: {sampled_df.shape[1]}")
print("\nList of all 14 columns included:")
for col in sampled_df.columns:
    print(f"  - {col}")

# 4. Display a sample of the extracted records on screen
print("\n--- First 5 extracted rows ---")
print(sampled_df.head())

# 5. Save all 14 columns and 35 rows to ASAP-v2.xlsx
output_file = "ASAP-v2.xlsx"
sampled_df.to_excel(output_file, index=False)

print(f"\nDone! All 14 columns for each record have been saved to '{output_file}'.")