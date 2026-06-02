import pandas as pd
import re

def transform_data(df):
    if df.empty:
        return df
    
    try:
        df = df[df['Title'] != "Unknown Product"].copy()
        
        df['Price'] = df['Price'].astype(str).str.replace(',', '', regex=False)
        df['Price'] = df['Price'].str.extract(r'(\d+\.?\d*)')[0]

        df['Rating'] = df['Rating'].astype(str).str.extract(r'(\d+\.?\d*)')[0]

        df = df.dropna(subset=['Price', 'Rating'])

        df['Price'] = df['Price'].astype(float) * 16000
        df['Rating'] = df['Rating'].astype(float)

        df['Colors'] = df['Colors'].astype(str).str.extract(r'(\d+)')[0].fillna(0).astype(int)

        df['Size'] = df['Size'].astype(str).str.replace(r'Size:\s*', '', case=False, regex=True)
        df['Gender'] = df['Gender'].astype(str).str.replace(r'Gender:\s*', '', case=False, regex=True)

        df = df.drop_duplicates()
        
        return df
    
    except Exception as e:
        print(f"Error Transform: {e}")
        return pd.DataFrame()