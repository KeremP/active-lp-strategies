import requests
from datetime import datetime
from typing import Any, Optional

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

def parse_data(data: str, key: str, query: str, dtype: Optional[object] = None):

    results = [result for result in [d['data'][query] for d in data]]
    if dtype is not None:
        output = [dtype(i[key]) for i in results[0]]
        return output
    output = [i[key] for i in results[0]]
    return output