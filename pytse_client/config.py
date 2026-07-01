import os
from typing import Optional

FINANCIAL_INDEX_BASE_PATH = "financial_index_data"
DATA_BASE_PATH = "tickers_data"
STATS_BASE_PATH = "stats_data"
CLIENT_TYPES_DATA_BASE_PATH = "client_types_data"
SHAREHOLDERS_HISTORY_PATH = "shareholders_data"
ASKS_BIDS_PATH = "asks_bids_data"
ORDER_BOOK_HIST_PATH = "orderbook_hist_data"
TRADE_DETAILS_HIST_PATH = "trade_details_history"
pytse_dir = os.path.dirname(__file__)
LOGGER_NAME = "pytse"

# Optional proxy URL (e.g. "socks5h://127.0.0.1:10808") applied to all outbound requests.
# Set via pytse_client.set_proxy() instead of OS-wide/env-var proxy configuration.
PROXY: Optional[str] = None


def set_proxy(proxy: Optional[str]) -> None:
    """Route all subsequent pytse_client requests through the given proxy URL.

    Pass None to disable. Requires the `PySocks` package installed for socks5:// URLs.
    """
    global PROXY
    PROXY = proxy
