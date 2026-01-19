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
@click.option("--target-table", default="yellow_taxi_data", help="Target table name")
def run(
    pg_user,
    pg_pass,
    pg_host,
    pg_port,
    pg_db,
    target_table,
):
    """Ingest NYC zonal data into postgres db"""
    url = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv"

    df = pd.read_csv(url)

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
