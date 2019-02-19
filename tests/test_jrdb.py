from jrdb import __version__
from jrdb.client import JRDBClient


def test_version():
    assert __version__ == '0.1.0'


def test_fetch_latest_urls():
    client = JRDBClient(('id', 'pw'))
    urls = client.fetch_latest_urls()
    print(urls)
