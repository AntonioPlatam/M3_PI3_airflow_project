--silver
DROP TABLE IF EXISTS airbnb_silver;

CREATE TABLE airbnb_silver AS
SELECT
    a.id,
    a.name,
    a.host_id,
    a.host_name,
    a.neighbourhood_group,
    a.neighbourhood,
    a.room_type,

    CAST(a.price AS DECIMAL(10,2)) AS price_usd,
    CAST(r.mxn_rate AS DECIMAL(18,6)) * CAST(a.price AS DECIMAL(10,2)) AS price_mxn,
    CAST(r.ars_rate AS DECIMAL(18,6)) * CAST(a.price AS DECIMAL(10,2)) AS price_ars,

    a.minimum_nights,
    a.number_of_reviews,
    a.reviews_per_month,
    a.availability_365,
    a.last_review,
    r.rate_timestamp AS exchange_rate_timestamp

FROM bronze_airbnb_raw a
CROSS JOIN (
    SELECT mxn_rate, ars_rate, rate_timestamp
    FROM bronze_exchange_rates_raw
    ORDER BY rate_timestamp DESC
    LIMIT 1
) r
WHERE a.price IS NOT NULL
  AND a.price REGEXP '^[0-9]+(\\.[0-9]+)?$'
  AND CAST(a.price AS DECIMAL(10,2)) > 0
  AND a.room_type IS NOT NULL
  AND a.neighbourhood IS NOT NULL;


--dimensiones
DROP TABLE IF EXISTS dim_zone;

CREATE TABLE dim_zone (
    zone_id INT AUTO_INCREMENT PRIMARY KEY,
    neighbourhood_group VARCHAR(255) UNIQUE
);

INSERT INTO dim_zone (neighbourhood_group)
SELECT DISTINCT neighbourhood_group FROM airbnb_silver;


DROP TABLE IF EXISTS dim_neighbourhood;

CREATE TABLE dim_neighbourhood (
    neighbourhood_id INT AUTO_INCREMENT PRIMARY KEY,
    neighbourhood VARCHAR(255),
    zone_id INT,
    UNIQUE(neighbourhood, zone_id)
);

INSERT INTO dim_neighbourhood (neighbourhood, zone_id)
SELECT DISTINCT s.neighbourhood, z.zone_id
FROM airbnb_silver s
JOIN dim_zone z ON s.neighbourhood_group = z.neighbourhood_group;


DROP TABLE IF EXISTS dim_room_type;

CREATE TABLE dim_room_type (
    room_type_id INT AUTO_INCREMENT PRIMARY KEY,
    room_type VARCHAR(255) UNIQUE
);

INSERT INTO dim_room_type (room_type)
SELECT DISTINCT room_type FROM airbnb_silver;


DROP TABLE IF EXISTS dim_host;

CREATE TABLE dim_host (
    host_id INT PRIMARY KEY,
    host_name VARCHAR(255)
);

INSERT INTO dim_host (host_id, host_name)
SELECT DISTINCT host_id, host_name FROM airbnb_silver;


--fact
DROP TABLE IF EXISTS fact_airbnb_listings;

CREATE TABLE fact_airbnb_listings (
    fact_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    listing_id INT,
    host_id INT,
    neighbourhood_id INT,
    room_type_id INT,

    price_usd DECIMAL(10,2),
    price_mxn DECIMAL(10,2),
    price_ars DECIMAL(10,2),

    minimum_nights INT,
    number_of_reviews INT,
    reviews_per_month DECIMAL(6,2),
    availability_365 INT,
    last_review DATE,
    exchange_rate_timestamp DATETIME
);

INSERT INTO fact_airbnb_listings (
    listing_id,
    host_id,
    neighbourhood_id,
    room_type_id,
    price_usd,
    price_mxn,
    price_ars,
    minimum_nights,
    number_of_reviews,
    reviews_per_month,
    availability_365,
    last_review,
    exchange_rate_timestamp
)
SELECT
    s.id,
    s.host_id,
    n.neighbourhood_id,
    r.room_type_id,
    s.price_usd,
    s.price_mxn,
    s.price_ars,
    s.minimum_nights,
    s.number_of_reviews,
    s.reviews_per_month,
    s.availability_365,
    s.last_review,
    s.exchange_rate_timestamp
FROM airbnb_silver s
JOIN dim_neighbourhood n ON s.neighbourhood = n.neighbourhood
JOIN dim_room_type r ON s.room_type = r.room_type;

