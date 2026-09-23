import pandas as pd
from pathlib import Path

# ---------------------------------------
# Project paths
# ---------------------------------------

project_root = Path(__file__).resolve().parents[1]

raw_file = project_root / "Data" / "raw" / "inventory.csv"
processed_file = project_root / "Data" / "processed" / "inventory_clean.csv"


# ---------------------------------------
# STEP 1: INGEST
# ---------------------------------------

print("\n========== STEP 1: INGEST ==========")

inventory = pd.read_csv(raw_file)

print(f"Raw records loaded: {len(inventory):,}")
print(f"Columns loaded: {len(inventory.columns)}")


# ---------------------------------------
# STEP 2: DUPLICATE CHECK
# ---------------------------------------

print("\n========== STEP 2: DUPLICATE CHECK ==========")

duplicate_count = inventory.duplicated().sum()

print(f"Duplicate rows found: {duplicate_count}")

if duplicate_count > 0:
    inventory = inventory.drop_duplicates()
    print(f"Duplicate rows removed: {duplicate_count}")
else:
    print("No duplicate rows to remove.")


# ---------------------------------------
# STEP 3: DATE VALIDATION
# ---------------------------------------

print("\n========== STEP 3: DATE VALIDATION ==========")

inventory["inventory_date"] = pd.to_datetime(
    inventory["inventory_date"],
    errors="coerce"
)

invalid_date_count = inventory["inventory_date"].isna().sum()

print(f"Invalid inventory dates: {invalid_date_count}")


# ---------------------------------------
# STEP 4: STOCK VALIDATION
# ---------------------------------------

print("\n========== STEP 4: STOCK VALIDATION ==========")

invalid_stock_mask = inventory["stock_quantity"] < 0

invalid_stock_count = invalid_stock_mask.sum()

print(f"Negative stock quantities found: {invalid_stock_count}")

inventory.loc[
    invalid_stock_mask,
    "stock_quantity"
] = pd.NA

print("Negative stock quantities converted to NULL.")


# ---------------------------------------
# STEP 5: REORDER LEVEL VALIDATION
# ---------------------------------------

print("\n========== STEP 5: REORDER LEVEL VALIDATION ==========")

invalid_reorder_count = (
    inventory["reorder_level"] < 0
).sum()

print(f"Negative reorder levels: {invalid_reorder_count}")


# ---------------------------------------
# STEP 6: FINAL QUALITY CHECK
# ---------------------------------------

print("\n========== STEP 6: FINAL QUALITY CHECK ==========")

print(f"Final records: {len(inventory):,}")

print("\nMissing values:")
print(inventory.isna().sum())

print("\nDuplicate rows:")
print(inventory.duplicated().sum())

print("\nNegative stock remaining:")
print(
    (inventory["stock_quantity"] < 0).sum()
)


# ---------------------------------------
# SAVE CLEAN DATA
# ---------------------------------------

inventory.to_csv(processed_file, index=False)

print("\n========== PIPELINE COMPLETE ==========")
print("Clean inventory data saved to:")
print(processed_file)