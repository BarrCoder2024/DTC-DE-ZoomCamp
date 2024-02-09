if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    #Remove rows where the passenger count is equal to 0 and the trip distance is equal to zero.
    data = data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)]
    # Rename columns from Camel Case to Snake Case
    data.rename(columns={'VendorID': 'vendor_id', 'RatecodeID':'ratecode_id', 'PULocationID':'pul_location_id', 'DOLocationID':'dol_location_id'}, inplace=True)
    # Create a new column lpep_pickup_date by converting lpep_pickup_datetime to a date
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date
    
    return data

@test
def test_output(output, *args):
 
    assert output['passenger_count'].isin([0]).sum() ==  0, 'There are rides with zero passengers'

@test
def test_output(output, *args):
 
    assert output['trip_distance'].isin([0]).sum() ==  0, 'There are rides with zero distance'

