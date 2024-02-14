import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@data_loader
def load_data_from_api(**kwargs):
    """
    Template for loading data from API
    """
    # List of URLs
    urls = [
        "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-01.parquet",
        "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-02.parquet",
        "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-03.parquet",
        "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-04.parquet",
        "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-05.parquet",
        "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-06.parquet",
        "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-07.parquet",
        "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-08.parquet",
        "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-09.parquet",
        "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-10.parquet",
        "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-11.parquet",
        "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-12.parquet"
        ]
    # Empty list to store DataFrames
    dfs = []
        # Loop through each URL
    for url in urls:
        # Read Parquet files from URL into DataFrame
        df = pd.read_parquet(url)
        # Append DataFrame to list
        dfs.append(df)
    return pd.concat(dfs, ignore_index=True) 

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
