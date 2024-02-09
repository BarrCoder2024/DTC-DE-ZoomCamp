import io
import pandas as pd
import requests
from pandas import DataFrame

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@data_loader
def load_data_from_api(**kwargs) -> DataFrame:
    """
    Template for loading data from API
    """
    # List of URLs
    urls = [
        "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-10.csv.gz",
        "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-11.csv.gz",
        "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-12.csv.gz"
        ]
    # List to store DataFrames
    dfs = []
        # Loop through each URL
    for url in urls:

        taxi_dtypes = {
            'VendorID': pd.Int64Dtype(),
            'passenger_count': pd.Int64Dtype(),
            'trip_distance': float,
            'RatecodeID':pd.Int64Dtype(),
            'store_and_fwd_flag':str,
            'PULocationID':pd.Int64Dtype(),
            'DOLocationID':pd.Int64Dtype(),
            'payment_type': pd.Int64Dtype(),
            'fare_amount': float,
            'extra':float,
            'mta_tax':float,
            'tip_amount':float,
            'tolls_amount':float,
            'improvement_surcharge':float,
            'total_amount':float,
            'congestion_surcharge':float
            }
        # native date parsing 
        parse_dates = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']
        # Read CSV from URL into DataFrame
        df = pd.read_csv(
            url, sep=',', compression='gzip', dtype=taxi_dtypes, parse_dates=parse_dates
            )
        # Append DataFrame to list
        dfs.append(df)


    return pd.concat(dfs, ignore_index=True)



@test
def test_output(df) -> None:
    """
    Template code for testing the output of the block.
    """
    assert df is not None, 'The output is undefined'

