from typing import List, Optional, Any
from .utils.subgraph import run_query


def generate_payload(address: str, timestamps: List[int],  first: bool = False, num_results: int = 100, n_query: Optional[int] = None) -> str:

    if not first:
        payload = f"""
        {{
            poolDayDatas(
                first:{num_results}
                skip:{n_query}
                orderBy: date
                orderDirection: asc
                where: {{
                    pool: "{address}"
                    date_gte:{timestamps[0]}, date_lte:{timestamps[1]}
                }}
                ) {{
                    id
                    date
                    txCount
                    volumeUSD
                    token0Price
                    token1Price
                    sqrtPrice
                    open
                    high
                    low
                    close
                }}
        }}
        """
        return payload
    
    payload = f"""
        {{
            poolDayDatas(
                first:{num_results}
                orderBy: date
                orderDirection: asc
                where: {{
                    pool: "{address}",
                    date_gte:{timestamps[0]}, date_lte:{timestamps[1]}
                }}
                ) {{
                    id
                    date
                    txCount
                    volumeUSD
                    token0Price
                    token1Price
                    sqrtPrice
                    open
                    high
                    low
                    close
                }}
        }}
        """
    return payload
    


def get_pricing_data(pool: str, num_results: int = 1000, timestamps: Optional[List[str]] = None,  endpoint: str = "https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v3") -> Any:
    """
    Query subgraph data for daily pool data
    """


    pool = pool.lower()

    results = []
    skip = 0
    while True:
        if skip == 0:
            payload = generate_payload(pool, timestamps, True, num_results)
        elif skip > 5000:
            return results
        else:
            payload = generate_payload(pool, timestamps, False, num_results, skip)

        resp = run_query(payload, endpoint)

        if len(resp['data']['poolDayDatas']) == 0:
            return results
        elif 'errors' in resp.keys() and len(resp['errors']) > 0:
            raise Exception(resp['errors'])
        
        results.append(resp)
        skip+=num_results