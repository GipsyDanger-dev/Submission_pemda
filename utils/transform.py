import pandas as pd
import numpy as np

# JANGAN ADA BARIS: from utils.transform import transform_data

def transform_data(df):
    if df.empty:
        return df
    
    try:
        df = df.copy()

        # 1. Hapus 'Unknown Product'
        df = df[df['Title'] != "Unknown Product"]
        
        # 2. Transform Price: Ambil angka, kali 16000
        df['Price'] = df['Price'].astype(str).str.replace(r'[^\d.]', '', regex=True)
        df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
        
        # 3. Transform Rating: Ambil angka pertama
        df['Rating'] = df['Rating'].astype(str).str.extract(r'(\d+\.?\d*)')[0]
        df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')
        
        # 4. Bersihkan baris kosong
        df = df.dropna(subset=['Price', 'Rating'])
        df['Price'] = df['Price'] * 16000
        
        # 5. Transform Colors
        df['Colors'] = df['Colors'].astype(str).str.extract(r'(\d+)')[0].fillna(0).astype(int)
        
        # 6. Transform Size & Gender
        df['Size'] = df['Size'].astype(str).str.replace(r'Size:\s*', '', case=False, regex=True)
        df['Gender'] = df['Gender'].astype(str).str.replace(r'Gender:\s*', '', case=False, regex=True)
        
        # 7. Hapus Duplikat
        df = df.drop_duplicates()

        # --- SYARAT LULUS: PAKSA KE OBJECT ---
        df['Title'] = df['Title'].astype('object')
        df['Size'] = df['Size'].astype('object')
        df['Gender'] = df['Gender'].astype('object')
        df['timestamp'] = df['timestamp'].astype('object')
        
        return df
    
    except Exception as e:
        print(f"Error Transform: {e}")
        return pd.DataFrame()