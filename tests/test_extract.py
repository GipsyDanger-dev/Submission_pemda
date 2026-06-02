import pandas as pd
from utils.extract import scrape_main
from unittest.mock import patch, MagicMock

@patch('requests.get')
def test_scrape_main(mock_get):

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.text = """
    <div class="card">
        <h5>Baju Uji</h5>
        <p>$10.00</p>
        <p>4.5 / 5</p>
        <p>3 Colors</p>
        <p>Size: L</p>
        <p>Gender: Men</p>
    </div>
    """
    mock_get.return_value = mock_response


    df = scrape_main()

    assert isinstance(df, pd.DataFrame)