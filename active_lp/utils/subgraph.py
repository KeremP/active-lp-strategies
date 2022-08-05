from sqlite3 import Date
import requests
from datetime import datetime
from typing import Any

def run_query(query: str, graph_url: str) -> Any:
    """
    Send query request to subgraph endpoint
    """
    request = requests.post(graph_url, json={'query':query})

    if request.status_code == 200:
        return request.json()
    else:
        raise Exception(f'Query returned code: {request.status_code}')

def _convert_date(date: str) -> int:
    date_arr = date.split('-')
    if len(date_arr) == 1:
        date_arr = date.split('/')
    date_arr = [int(d) for d in date_arr]
    timestamp = int(datetime(*date_arr).timestamp())
    return timestamp