import pandas as pd

def load_to_csv(df, file_name='products.csv'):
    try:
        df.to_csv(file_name, index=False)
        print(f"Data berhasil disimpan ke {file_name}")
    except Exception as e:
        print(f"Error saat Load: {e}")