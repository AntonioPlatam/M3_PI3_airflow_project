-- GOLD MASTER TABLE

DROP TABLE IF EXISTS gold_airbnb_master;

CREATE TABLE gold_airbnb_master AS
SELECT
    f.fact_id,
    f.listing_id,
    h.host_name,
    z.neighbourhood_group,
    n.neighbourhood,
    r.room_type,
    f.price_usd,
    f.price_mxn,
    f.price_ars,
    f.minimum_nights,
    f.number_of_reviews,
    f.reviews_per_month,
    f.availability_365,
    f.last_review,
    f.exchange_rate_timestamp
FROM fact_airbnb_listings f
JOIN dim_host h ON f.host_id = h.host_id
JOIN dim_neighbourhood n ON f.neighbourhood_id = n.neighbourhood_id
JOIN dim_zone z ON n.zone_id = z.zone_id
JOIN dim_room_type r ON f.room_type_id = r.room_type_id;
