"""
Data loading utilities for the Sales Prediction project
"""

import pandas as pd

def load_advertising_data(filepath='data/Advertising.csv'):
    """
    Load the advertising dataset
    
    Parameters:
    filepath (str): Path to the CSV file
    
    Returns:
    pandas.DataFrame: Loaded dataset
    """
    try:
        df = pd.read_csv(filepath)
        print(f"✅ Data loaded from {filepath}")
        print(f"📊 Shape: {df.shape}")
        return df
    except FileNotFoundError:
        print(f"❌ File not found at {filepath}")
        return None

def get_data_info(df):
    """
    Display basic information about the dataset
    
    Parameters:
    df (pandas.DataFrame): The dataset
    """
    print("\n" + "="*50)
    print("DATA INFORMATION")
    print("="*50)
    print(f"Shape: {df.shape}")
    print(f"\nColumns: {list(df.columns)}")
    print(f"\nMissing values:\n{df.isnull().sum()}")
    print(f"\nData types:\n{df.dtypes}")

def get_statistics(df):
    """
    Display statistical summary of the dataset
    
    Parameters:
    df (pandas.DataFrame): The dataset
    """
    print("\n" + "="*50)
    print("STATISTICAL SUMMARY")
    print("="*50)
    print(df.describe())