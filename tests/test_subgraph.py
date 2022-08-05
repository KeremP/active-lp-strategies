from datetime import datetime

from active_lp.get_historical_prices import get_pricing_data
from active_lp.utils.subgraph import _convert_date

def test_convert_date():
    date_str = '2022-08-05'

    timestamp = _convert_date(date_str)

    assert timestamp == int(datetime(2022,8,5).timestamp())

def test_get_historical_price():

    date_start = _convert_date('2021-08-05')
    date_end = _convert_date('2022-08-05')

    pool = "0x8ad599c3A0ff1De082011EFDDc58f1908eb6e6D8"

    data = get_pricing_data(pool, timestamps=[date_start, date_end])
    
    assert data


