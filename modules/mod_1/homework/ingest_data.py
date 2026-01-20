#!/usr/bin/env python
# coding: utf-8

import click
import pandas as pd
from sqlalchemy import create_engine


@click.command()
@click.option("--pg-user", default="root", help="PostgreSQL user")
@click.option("--pg-pass", default="root", help="PostgreSQL password")
@click.option("--pg-host", default="localhost", help="PostgreSQL host")
@click.option("--pg-port", default=5432, type=int, help="PostgreSQL port")
@click.option("--pg-db", default="ny_taxi", help="PostgreSQL database name")
@click.option("--target-table", required=True, help="Target table name")
def run(
    pg_user,
    pg_pass,
    pg_host,
    pg_port,
    pg_db,
    target_table,
):
    """Ingest NYC zonal data into postgres db"""

    if target_table == "zones":
        df = pd.read_csv("taxi_zone_lookup.csv")
    elif target_table == "green_trip_data":
        df = pd.read_parquet("green_tripdata_2025-11.parquet")
    else:
        raise ValueError("No such table in the database")

    # Ingesting data into postgres
    engine = create_engine(
        f"postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}"
    )

    # create the table
    df.head(0).to_sql(name=target_table, con=engine, if_exists="replace")

    print("Table created")

    # populate the table
    df.to_sql(
        name=target_table,
        con=engine,
        if_exists="append",
    )

    print("Data completely inserted")


if __name__ == "__main__":
    run()
