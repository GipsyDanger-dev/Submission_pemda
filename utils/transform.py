import pandas as pd
import numpy as np

def transform_data(df):
    if df.empty:
        return df

    try:
        df = df[df['Title'] != "Unknown Product"].copy()

        df['Price'] = df['Price'].astype(str).str.replace(r'[^\d.]', '', regex=True)
        df = df[df['Price'] != ""].copy()
        df['Price'] = df['Price'].astype(float) * 16000

        df['Rating'] = df['Rating'].astype(str).str.split('/').str[0].str.strip()
        df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')

        df['Colors'] = df['Colors'].astype(str).str.extract(r'(\d+)')[0].fillna(0).astype(int)

        df['Size'] = df['Size'].astype(str).str.replace(r'Size:\s*', '', case=False, regex=True)
        df['Gender'] = df['Gender'].astype(str).str.replace(r'Gender:\s*', '', case=False, regex=True)

        df = df.dropna(subset=['Price', 'Rating'])
        df = df.drop_duplicates()

        df['Title'] = df['Title'].astype('object')
        df['Size'] = df['Size'].astype('object')
        df['Gender'] = df['Gender'].astype('object')
        df['timestamp'] = df['timestamp'].astype('object')

        return df

    except Exception as e:
        print(f"Error pada Transform: {e}")
        return pd.DataFrame()
