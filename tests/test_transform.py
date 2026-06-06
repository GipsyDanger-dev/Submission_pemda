import pandas as pd
import numpy as np
from utils.transform import transform_data

def test_transform_logic():
    # Tambahkan kolom 'timestamp' agar tidak Error Transform
    data = {
        'Title': ['Kemeja Casual', 'Unknown Product'],
        'Price': ['$10.00', '$20.00'],
        'Rating': ['4.5 / 5', '3.0 / 5'],
        'Colors': ['3 Colors', '1 Colors'],
        'Size': ['Size: XL', 'Size: M'],
        'Gender': ['Gender: Men', 'Gender: Women'],
        'timestamp': ['2024-01-01 00:00:00', '2024-01-01 00:00:00']
    }
    df = pd.DataFrame(data)
    clean_df = transform_data(df)
    
    # 1. Cek apakah Unknown Product dihapus (sisa 1 data)
    assert len(clean_df) == 1
    
    # 2. Cek tipe data (Harus Object sesuai permintaan Reviewer)
    # Di Pandas, tipe 'O' adalah singkatan dari Object
    assert clean_df['Title'].dtype == 'O'
    assert clean_df['Size'].dtype == 'O'
    assert clean_df['Gender'].dtype == 'O'
    
    # 3. Cek konversi harga
    assert float(clean_df.iloc[0]['Price']) == 160000.0

def test_transform_empty():
    assert transform_data(pd.DataFrame()).empty