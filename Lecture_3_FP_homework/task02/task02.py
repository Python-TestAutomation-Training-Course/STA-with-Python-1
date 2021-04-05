# fix get_joke and get_bored functions so we can make valid response from the API's
# using get_bored function find the activity name with id=5977626 https://www.boredapi.com/documentation
# using get_joke function count number of Spooky jokes but not racist or sexist (other options are default) https://sv443.net/jokeapi/v2/

import requests


def build_request(method, base_url):
    def my_decorator(func):
        def _build_request(*args, **kwargs):
            uri = kwargs.get("uri")
            url = base_url + uri
            params = kwargs.get("params")
            kwargs.update(dict(url=url, method=method))
            resp = requests.request(url=url, method=method, params=params)
            kwargs.update(dict(resp=resp))
            return func(*args, **kwargs)
        return _build_request
    return my_decorator


@build_request(method="GET", base_url="https://v2.jokeapi.dev/joke")
def get_joke(**kwargs):
    return # fix me


@build_request(method="GET", base_url="http://www.boredapi.com/api")
def get_bored(): # fix me
    kwargs.get("whatever") # fix me


resp = get_joke(uri="/any")
print(resp.status_code)
print(resp.text)

resp = get_bored(uri="/activity")
print(resp.status_code)
print(resp.text)