import pandas as pd
import os
from utils.load import load_to_csv

def test_load_to_csv():
    df = pd.DataFrame({'test': [1, 2, 3]})
    file_name = 'test_output.csv'
    
    load_to_csv(df, file_name)

    assert os.path.exists(file_name)

    os.remove(file_name)