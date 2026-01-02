DROP VIEW IF EXISTS int_uk_cooked_foods_metrics;

CREATE VIEW int_uk_cooked_foods_metrics AS
SELECT
    brand,
    website,
    availability,
    has_multiple_proteins_flag,
    single_protein_some_flag,

    -- Simple price segment classification based on text
    CASE
        WHEN price_500g_raw LIKE '%2.%' THEN 'budget'
        WHEN price_500g_raw LIKE '%3.%' THEN 'mid_range'
        WHEN price_500g_raw LIKE '%4.%' THEN 'premium'
        ELSE 'unknown'
    END AS price_segment,

    price_500g_raw,
    price_1kg_raw,
    minimum_order_raw,
    notes
FROM stg_uk_cooked_foods;