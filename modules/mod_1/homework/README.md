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

