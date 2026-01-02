DROP VIEW IF EXISTS mart_uk_cooked_foods_brand_summary;

CREATE VIEW mart_uk_cooked_foods_brand_summary AS
SELECT
    brand,
    website,
    availability,
    COUNT(*) AS record_count,
    MAX(has_multiple_proteins_flag) AS offers_multiple_proteins,
    MAX(single_protein_some_flag) AS offers_single_protein_options,
    MAX(price_segment) AS dominant_price_segment
FROM int_uk_cooked_foods_metrics
GROUP BY brand, website, availability;