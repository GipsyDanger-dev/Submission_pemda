import pandas as pd
import numpy as np
from utils.transform import transform_data

def test_transform_logic():
    data = {
        'Title': ['Kemeja Casual', 'Unknown Product'],
        'Price': ['$10.00', '$20.00'],
        'Rating': ['4.5 / 5', '3.0 / 5'],
        'Colors': ['3 Colors', '1 Colors'],
        'Size': ['Size: XL', 'Size: M'],
        'Gender': ['Gender: Men', 'Gender: Women']
    }
    df = pd.DataFrame(data)
    clean_df = transform_data(df)
    

    assert len(clean_df) == 1

    assert float(clean_df.iloc[0]['Price']) == 160000.0

    assert int(clean_df.iloc[0]['Colors']) == 3

def test_transform_empty():
    assert transform_data(pd.DataFrame()).empty