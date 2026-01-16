#!/usr/bin/env python
import pandas as pd
from sqlalchemy import create_engine
from tqdm.auto import tqdm

dtype = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64",
}

parse_dates = ["tpep_pickup_datetime", "tpep_dropoff_datetime"]

prefix = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/"

df = pd.read_csv(
    prefix + "yellow_tripdata_2021-01.csv.gz",
    nrows=100,
    dtype=dtype,
    parse_dates=parse_dates,
)


# Ingesting data into postgres
engine = create_engine("postgresql://root:root@localhost:5432/ny_taxi")


# create the table
df.head(n=0).to_sql(name="yellow_taxi_data", con=engine, if_exists="replace")


# Ingesting data in chunks
df_iter = pd.read_csv(
    prefix + "yellow_tripdata_2021-01.csv.gz",
    iterator=True,
    chunksize=100000,
)


first_chunk = next(df_iter)

first_chunk.head(0).to_sql(name="yellow_taxi_data", con=engine, if_exists="replace")
first_chunk.to_sql(
    name="yellow_taxi_data",
    con=engine,
    if_exists="append",
)

for df_chunk in tqdm(df_iter):
    df_chunk.to_sql(
        name="yellow_taxi_data",
        con=engine,
        if_exists="append",
    )
    print("Inserted chunk: ", len(df_chunk))
