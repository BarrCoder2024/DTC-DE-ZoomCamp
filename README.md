# DTC-DE-ZoomCamp

#HW3

-- Set up

-- External Data

CREATE OR REPLACE EXTERNAL TABLE `ny_taxi.green_taxi_external_data_2022`
OPTIONS(
  format = 'Parquet',
  uris =['gs://hw3_zoomcamp/hw3_green_taxi/bc4568ed478d4a66bfdf27c795fa41e6-0.parquet']
);

-- Materialised Data


CREATE OR REPLACE TABLE `powerful-star-412710.ny_taxi.green_taxi_data_non_partitioned_2022`
AS 
  SELECT * 
  FROM `powerful-star-412710.ny_taxi.green_taxi_external_data_2022`
;


-- Q2


SELECT COUNT (DISTINCT PULocationID) 
FROM `powerful-star-412710.ny_taxi.green_taxi_external_data_2022`

--Scanning 0 MB of Data when run 

SELECT COUNT (DISTINCT PULocationID) 
FROM `powerful-star-412710.ny_taxi.green_taxi_data_non_partitioned_2022`

-- Scanning 6.41 MB of Data when run 


-- Q3


SELECT COUNT (fare_amount) 
FROM `powerful-star-412710.ny_taxi.green_taxi_external_data_2022`
WHERE fare_amount = 0;

--No of records with fare_amount = 0 is 1622


-- Q4 

CREATE OR REPLACE TABLE `powerful-star-412710.ny_taxi.green_taxi_data_partition_cluster_2022`
PARTITION BY(lpep_pickup_date)
CLUSTER BY(PULocationID)
 
AS 
  SELECT * 
  FROM `powerful-star-412710.ny_taxi.green_taxi_external_data_2022`;
  
-- Q5
  
SELECT * 
FROM `powerful-star-412710.ny_taxi.green_taxi_external_data_2022`
WHERE lpep_pickup_date BETWEEN '2022-06-01' AND '2022-06-30';
  
--Estimated 0 Bytes

SELECT * 
FROM `powerful-star-412710.ny_taxi.green_taxi_data_partition_cluster_2022`
WHERE lpep_pickup_date BETWEEN '2022-06-01' AND '2022-06-30';
  
--Estimated 10.51 Bytes
