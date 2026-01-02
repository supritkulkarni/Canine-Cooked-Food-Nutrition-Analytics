import os
import pandas as pd
from sqlalchemy import create_engine

# Paths
DATA_PATH = os.path.join("data", "UK_Canine_Cooked_Foods.csv")
DB_PATH = os.path.join("data", "canine_nutrition.db")

def load_raw_data(path: str) -> pd.DataFrame:
    """Load the CSV exactly as-is."""
    return pd.read_csv(path)

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Minimal cleaning:
    - Standardise column names
    - Strip whitespace
    - Convert Yes/Some to booleans
    """
    # Standardise column names
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

    # Strip whitespace from text fields
    text_cols = [
        "brand", "price_500g_raw", "price_1kg_raw",
        "minimum_order_raw", "website", "availability", "notes"
    ]
    for col in text_cols:
        df[col] = df[col].astype(str).str.strip()

    # Convert Yes/Some to booleans
    df["has_multiple_proteins_flag"] = df["has_multiple_proteins"].fillna("").str.lower().eq("yes")
    df["single_protein_some_flag"] = df["single_protein_options"].fillna("").str.lower().eq("some")

    return df

def write_to_sqlite(df: pd.DataFrame, db_path: str):
    """Write cleaned data to SQLite."""
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    engine = create_engine(f"sqlite:///{db_path}")
    df.to_sql("uk_cooked_foods_raw", con=engine, if_exists="replace", index=False)
    print(f"Loaded {len(df)} rows into uk_cooked_foods_raw")

if __name__ == "__main__":
    df_raw = load_raw_data(DATA_PATH)
    df_clean = clean_data(df_raw)
    write_to_sqlite(df_clean, DB_PATH)