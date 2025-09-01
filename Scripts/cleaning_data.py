# ============================
# data_cleaning.py
# Data Cleaning & Logging Script
# ============================

import pandas as pd
import os

def main():
    # Paths
    raw_data_path = "dataset/mobile_money_transactions.csv"  # replace with your dataset path
    cleaned_data_path = "cleaned/cleaned_data.csv"
    log_folder = "log"

    # Create folders if they don't exist
    os.makedirs("cleaned", exist_ok=True)
    os.makedirs(log_folder, exist_ok=True)

    # Load data
    df = pd.read_csv(raw_data_path)
    print(f"Original data shape: {df.shape}")

    # -------------------------------
    # 1️⃣ Remove duplicates
    # -------------------------------
    duplicates = df[df.duplicated()]
    if not duplicates.empty:
        duplicates.to_csv(os.path.join(log_folder, "deleted_duplicates.csv"), index=False)
        print(f"Logged {len(duplicates)} duplicate rows.")
    df = df.drop_duplicates()
    print(f"Shape after removing duplicates: {df.shape}")

    # -------------------------------
    # 2️⃣ Handle missing values
    # -------------------------------
    missing_rows = df[df.isnull().any(axis=1)]
    if not missing_rows.empty:
        missing_rows.to_csv(os.path.join(log_folder, "deleted_missing.csv"), index=False)
        print(f"Logged {len(missing_rows)} rows with missing values.")
    df = df.dropna()
    print(f"Shape after removing missing values: {df.shape}")

    # -------------------------------
    # 3️⃣ Filter invalid transactions
    # -------------------------------
    invalid_amounts = df[df['amount'] <= 0]
    if not invalid_amounts.empty:
        invalid_amounts.to_csv(os.path.join(log_folder, "deleted_invalid_amounts.csv"), index=False)
        print(f"Logged {len(invalid_amounts)} rows with invalid amounts.")
    df = df[df['amount'] > 0]
    print(f"Shape after removing invalid amounts: {df.shape}")

    # -------------------------------
    # 4️⃣ Optional: drop irrelevant columns
    # -------------------------------
    # Uncomment and adjust if needed
    # df = df.drop(columns=['nameOrig', 'nameDest'])
    # print(f"Shape after dropping irrelevant columns: {df.shape}")

    # -------------------------------
    # 5️⃣ Save cleaned data
    # -------------------------------
    df.to_csv(cleaned_data_path, index=False)
    print(f"Cleaned data saved to '{cleaned_data_path}'")

    # -------------------------------
    # 6️⃣ Summary
    # -------------------------------
    print("✅ Data cleaning completed successfully!")
    print(f"Final dataset shape: {df.shape}")
    print("Check the 'log/' folder for deleted rows.")

if __name__ == "__main__":
    main()
