import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

plt.style.use("seaborn-v0_8")
sns.set_palette("Set2")

DB_PATH = os.path.join("data", "canine_nutrition.db")
PLOTS_DIR = os.path.join("plots")


def ensure_plot_dir():
    if not os.path.exists(PLOTS_DIR):
        os.makedirs(PLOTS_DIR)


def load_tables():
    engine = create_engine(f"sqlite:///{DB_PATH}")

    df_raw = pd.read_sql("SELECT * FROM uk_cooked_foods_raw", engine)
    df_stg = pd.read_sql("SELECT * FROM stg_uk_cooked_foods", engine)
    df_int = pd.read_sql("SELECT * FROM int_uk_cooked_foods_metrics", engine)
    df_mart = pd.read_sql("SELECT * FROM mart_uk_cooked_foods_brand_summary", engine)

    return df_raw, df_stg, df_int, df_mart


def plot_price_segments(df_int):
    plt.figure(figsize=(6, 4))
    sns.countplot(
        data=df_int,
        x="price_segment",
        order=["budget", "mid_range", "premium", "unknown"]
    )
    plt.title("Price Segment Distribution")
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, "price_segments.png"))
    plt.close()


def plot_availability(df_int):
    plt.figure(figsize=(6, 4))
    sns.countplot(data=df_int, x="availability")
    plt.title("Availability Types")
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, "availability.png"))
    plt.close()


def plot_protein_offerings(df_int):
    plt.figure(figsize=(6, 4))
    sns.countplot(data=df_int, x="has_multiple_proteins_flag")
    plt.title("Brands Offering Multiple Proteins")
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, "protein_offerings.png"))
    plt.close()


def main():
    ensure_plot_dir()

    print("Loading tables...")
    df_raw, df_stg, df_int, df_mart = load_tables()

    print("\n=== RAW TABLE ===")
    print(df_raw.head())

    print("\n=== INTERMEDIATE METRICS ===")
    print(df_int.head())

    print("\n=== MART SUMMARY ===")
    print(df_mart)

    print("\nGenerating plots...")
    plot_price_segments(df_int)
    plot_availability(df_int)
    plot_protein_offerings(df_int)

    print("\nEDA complete. Plots saved in /plots directory.")


if __name__ == "__main__":
    main()