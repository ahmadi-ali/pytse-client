import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry

from pytse_client import config


def requests_retry_session(
    retries=5,
    backoff_factor=0.3,
    status_forcelist=(500, 502, 504, 503),
    session=None,
) -> requests.Session:
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    if config.PROXY:
        session.proxies = {"http": config.PROXY, "https": config.PROXY}
    return session
