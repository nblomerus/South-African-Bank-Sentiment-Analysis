import sys
sys.path.append('../')
import pandas as pd
import pytest
from utilities import split_dataframe_to_excel
import os

expected_dtypes = {'Datetime':  'datetime64[ns, UTC]', 'Tweet_Id':  'int64', 'Tweet': 'string', 'Username': 'string', \
        'Reply_Count': 'int64', 'Retweet_Count': 'int64', 'Like_Count': 'int64', 'Bank': 'string'}

def test_df_not_equal_with_different_search_using_same_terms():
    df_search_1 = pd.read_parquet('test_data/search_1.parquet')
    df_search_2 = pd.read_parquet('test_data/search_2.parquet')
    assert not df_search_1.equals(df_search_2)

def test_df_contains_no_null_values():
    df = pd.read_parquet('test_data/full_analysis.parquet')
    assert not df.isnull().values.any()

def test_column_dtypes():
    df = pd.read_parquet('test_data/full_analysis.parquet')
    for col, expected_type in expected_dtypes.items():
        actual_type = df[col].dtype
        assert actual_type == expected_type, f"Column {col} has dtype {actual_type}, expected {expected_type}"

# test the splitting of dataframes into excel files containing the specified number of rows and no null values
def test_split_dataframe_to_excel():
    df = pd.read_parquet('test_data/search_1.parquet')
    df['Datetime'] = df['Datetime'].dt.tz_localize(None)
    # calculate the number of files to create
    n_rows_in_split = 10000
    num_files = (len(df) - 1) // n_rows_in_split + 1
    split_dataframe_to_excel(df, 'test_data', 'test_split', n_rows_in_split)
    
    for i in range(1, num_files + 1):
        df_test = pd.read_excel(f'test_data/test_split_{i}.xlsx')

        # check for any null values
        assert not df_test.isnull().values.any()
        # if it's the last file, the number of rows should be the remainder
        if i == num_files:
            assert len(df_test) == len(df) % n_rows_in_split
        else:
            assert len(df_test) == n_rows_in_split
    # remove the test files
    for i in range(1, num_files + 1):
        os.remove(f'test_data/test_split_{i}.xlsx')
