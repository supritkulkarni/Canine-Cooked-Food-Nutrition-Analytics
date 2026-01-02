DROP VIEW IF EXISTS stg_uk_cooked_foods;

CREATE VIEW stg_uk_cooked_foods AS
SELECT
    id,
    LOWER(brand) AS brand,
    price_500g_raw,
    price_1kg_raw,
    minimum_order_raw,
    website,
    has_multiple_proteins_flag,
    single_protein_some_flag,
    availability,
    notes
FROM uk_cooked_foods_raw;