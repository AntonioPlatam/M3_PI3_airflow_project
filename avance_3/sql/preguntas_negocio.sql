-- Zonas más caras
SELECT neighbourhood_group, AVG(price_usd) avg_price
FROM gold_airbnb_master
GROUP BY neighbourhood_group
ORDER BY avg_price DESC;

-- Precio promedio por barrio
SELECT neighbourhood, AVG(price_usd)
FROM gold_airbnb_master
GROUP BY neighbourhood;

-- Tipos de habitación más comunes
SELECT room_type, COUNT(*) 
FROM gold_airbnb_master
GROUP BY room_type;

-- Hosts top
SELECT host_name, COUNT(*) total_listings, AVG(price_usd)
FROM gold_airbnb_master
GROUP BY host_name
ORDER BY total_listings DESC
LIMIT 10;
