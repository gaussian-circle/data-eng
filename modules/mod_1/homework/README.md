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


