# Canine Cooked Food Nutrition Analytics
Python • SQL • SQLite • Data Modelling • EDA

This project analyses cooked dog‑food products available in the UK, focusing on brand‑level differences, pricing patterns, protein options, and availability. It demonstrates how raw product data can be transformed into clean, analytics‑ready datasets using Python, SQL, and a lightweight analytics‑engineering workflow.

The project mirrors a modern dbt‑style modelling approach, including:
- Data ingestion and cleaning
- SQL data modelling (staging → intermediate → mart)
- Derived brand‑level metrics
- Exploratory data analysis
- Reproducible, script‑based workflow

The dataset is inspired by publicly available information from:
https://www.thebalancedcanine.co.uk/uk-cooked-foods

This project is for educational and analytics demonstration purposes only.
The Balanced Canine is not affiliated with or endorsing this project.

---

## Project Structure

canine-cooked-food-nutrition-analytics/
├── data/
│   ├── UK_Canine_Cooked_Foods.csv
│   └── canine_nutrition.db
├── plots/
│   ├── price_segments.png
│   ├── availability.png
│   └── protein_offerings.png
├── src/
│   ├── etl_uk_cooked_foods.py
│   └── eda_uk_cooked_foods.py
├── sql/
│   ├── 01_stg_uk_cooked_foods.sql
│   ├── 02_int_uk_cooked_foods_metrics.sql
│   └── 03_mart_uk_cooked_foods_brand_summary.sql
├── requirements.txt
├── LICENSE
└── README.md
12 directories, 14 files


---

## Tech Stack

- Python
- Pandas
- SQLAlchemy
- SQLite
- SQL
- Matplotlib
- Seaborn
- Git & GitHub

---

# How to Run This Project Locally

## 1. Clone the Repository

git clone git@github.com:supritkulkarni/Canine-Cooked-Food-Nutrition-Analytics.git

cd Canine-Cooked-Food-Nutrition-Analytics


## 2. Create and Activate a Virtual Environment

python3 -m venv venv

source venv/bin/activate


## 3. Install Dependencies

pip install -r requirements.txt


## 4. Run the ETL Pipeline

This script:
- Loads the CSV
- Cleans column names
- Creates boolean flags
- Writes uk_cooked_foods_raw into canine_nutrition.db

Run:

python3 src/etl_uk_cooked_foods.py


Expected output:

Loaded 8 rows into uk_cooked_foods_raw


---

## 5. Apply SQL Models

Run each SQL file against the SQLite database:

sqlite3 data/canine_nutrition.db < sql/01_stg_uk_cooked_foods.sql

sqlite3 data/canine_nutrition.db < sql/02_int_uk_cooked_foods_metrics.sql

sqlite3 data/canine_nutrition.db < sql/03_mart_uk_cooked_foods_brand_summary.sql


Verify:

sqlite3 data/canine_nutrition.db ".tables"


You should see:
- uk_cooked_foods_raw
- stg_uk_cooked_foods
- int_uk_cooked_foods_metrics
- mart_uk_cooked_foods_brand_summary

---

## 6. Run the EDA Script

This script:
- Loads all SQL views
- Prints summaries
- Generates plots into /plots

Run:

python3 src/eda_uk_cooked_foods.py


Plots will appear in:

plots/


---

# Key Insights

- Premium brands (e.g., Butternut Box, Monty’s Larder) consistently fall into the premium price segment.
- Mid‑range brands offer both multiple‑protein and single‑protein options.
- Online‑only brands dominate the dataset, reflecting a strong direct‑to‑consumer trend.
- Brands offering multiple proteins appear more frequently in mid‑range and premium categories.
- Minimum order requirements vary widely, from flexible “Not Stated” to fixed thresholds like 5kg or £25.

---

# Attribution Notice

Nutritional reference values and product information are adapted from publicly available sources provided by The Balanced Canine.
All transformations, modelling, and analysis are original work by Suprit Kulkarni.

---

# License

This project is licensed under the MIT License.

---

# Author

Suprit Kulkarni aka N3ur0n

• Python • SQL • Data Modelling

GitHub: https://github.com/supritkulkarni


