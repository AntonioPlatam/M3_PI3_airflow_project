DROP TABLE IF EXISTS bronze_airbnb_raw;

CREATE TABLE bronze_airbnb_raw (
    id INT,
    name TEXT,
    host_id INT,
    host_name TEXT,
    neighbourhood_group VARCHAR(255),
    neighbourhood VARCHAR(255),
    latitude DECIMAL(10,7),
    longitude DECIMAL(10,7),
    room_type VARCHAR(100),
    price VARCHAR(50),
    minimum_nights INT,
    number_of_reviews INT,
    last_review DATE,
    reviews_per_month DECIMAL(6,2),
    calculated_host_listings_count INT,
    availability_365 INT
);

DROP TABLE IF EXISTS bronze_exchange_rates_raw;

CREATE TABLE bronze_exchange_rates_raw (
    id INT AUTO_INCREMENT PRIMARY KEY,
    base_currency VARCHAR(10),
    mxn_rate VARCHAR(50),
    ars_rate VARCHAR(50),
    rate_timestamp DATETIME,
    loaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
