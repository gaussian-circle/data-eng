# Q1
- Build a docker image using the given Dockerfile 
```bash
docker build -t hw:latest
```

- Run docker interactively using the image 
```bash
docker run -it hw:latest
```

- Find the pip version
```bash
$ python -m pip --version
pip 25.3 from /usr/local/lib/python3.13/site-packages/pip (python 3.13)
```

# Q3
```sql
SELECT
	COUNT(*)
FROM
	GREEN_TRIP_DATA
WHERE
	'2025-11-01' <= LPEP_PICKUP_DATETIME
	AND LPEP_PICKUP_DATETIME < '2025-12-01'
	AND TRIP_DISTANCE <= 1;
```
|count|
|-----|
|8007 |

# Q4
```sql
SELECT
	LPEP_PICKUP_DATETIME AS "Longest day"
FROM
	GREEN_TRIP_DATA
WHERE
	TRIP_DISTANCE < 100
ORDER BY
	TRIP_DISTANCE DESC
LIMIT
	1;
```
|Longest day|
|-----------|
|2025-11-14 15:36:27|

# Q5
```sql
SELECT
	ZONES."Zone",
	SUM(TRIPS.TOTAL_AMOUNT) AS "Total Amount"
FROM
	GREEN_TRIP_DATA TRIPS
	JOIN ZONES ON TRIPS."PULocationID" = ZONES."LocationID"
GROUP BY
	ZONES."Zone"
ORDER BY
	SUM(TRIPS.TOTAL_AMOUNT) DESC
LIMIT
	5;
```
|Zone|Total Amount      |
|----|------------------|
|East Harlem North|257684.7000000002 |
|East Harlem South|126791.81000000062|
|Morningside Heights|49146.64000000001 |
|Jamaica|46490.73999999994 |
|Central Park|45626.49999999998 |

# Q6
```sql
SELECT
	ZDO."Zone" AS "drop off zone",
	MAX(TRIPS."tip_amount") AS "largest tip"
FROM
	GREEN_TRIP_DATA TRIPS
	JOIN ZONES ZPU ON TRIPS."PULocationID" = ZPU."LocationID"
	JOIN ZONES ZDO ON TRIPS."DOLocationID" = ZDO."LocationID"
WHERE
	ZPU."Zone" = 'East Harlem North'
	AND ZDO."Zone" IS NOT NULL
GROUP BY
	ZDO."Zone"
ORDER BY
	MAX(TRIPS."tip_amount") DESC
LIMIT
	5;
```
|drop off zone|largest tip       |
|-------------|------------------|
|Yorkville West|81.89             |
|LaGuardia Airport|50                |
|East Harlem North|45                |
|Long Island City/Queens Plaza|34.25             |
|JFK Airport  |23.53             |
