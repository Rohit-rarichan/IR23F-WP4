import urllib.request
import urllib.parse
import json

def is_valid_url(url):
    try:
        result = urllib.parse.urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def fetch_data_from_api(api_url):
    if not is_valid_url(api_url):
        raise ValueError("Invalid URL")

    with urllib.request.urlopen(api_url) as response:
        if response.getcode() == 200:
            data = response.read()
            return json.loads(data)
        else:
            raise Exception("Failed to fetch data from API")