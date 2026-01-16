#!/usr/bin/env python
# coding: utf-8

# # The NYC Taxi Dataset

# In[1]:


import pandas as pd


# In[2]:


prefix = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/'


# In[3]:


df = pd.read_csv(prefix + 'yellow_tripdata_2021-01.csv.gz', nrows=100)


# In[4]:


df.head()


# In[5]:


df.dtypes


# In[6]:


df.shape


# In[7]:


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
    "congestion_surcharge": "float64"
}

parse_dates = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime"
]

df = pd.read_csv(
    prefix + 'yellow_tripdata_2021-01.csv.gz', 
    nrows=100, 
    dtype=dtype, 
    parse_dates=parse_dates
)


# In[8]:


df.dtypes


# In[9]:


df.head()


# # Ingesting data into postgres

# In[14]:


from sqlalchemy import create_engine
engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')


# In[15]:


engine


# In[16]:


# get ddl schema
print(pd.io.sql.get_schema(df, name="yellow_taxi_data", con=engine))


# In[17]:


# create the table
df.head(n=0).to_sql(name="yellow_taxi_data", con=engine, if_exists='replace')


# # Ingesting data in chunks

# In[18]:


df_iter = pd.read_csv(
    prefix + 'yellow_tripdata_2021-01.csv.gz',
    iterator=True,
    chunksize=100000,
)


# In[19]:


first_chunk = next(df_iter)

first_chunk.head(0).to_sql(
    name="yellow_taxi_data",
    con=engine,
    if_exists='replace'
)


# In[20]:


first_chunk.to_sql(
    name="yellow_taxi_data",
    con=engine,
    if_exists='append',
)


# In[21]:


from tqdm.auto import tqdm

for df_chunk in tqdm(df_iter):
    df_chunk.to_sql(
        name='yellow_taxi_data',
        con=engine,
        if_exists='append',
    )
    print("Inserted chunk: ", len(df_chunk))

