from cachecontrol import CacheControl
import requests

ses = requests.session()
cached_session = CacheControl(ses)

res = cached_session.get('https://docs.python.org/3/')

print(res.from_cache)

res = cached_session.get('https://docs.python.org/3/')
print(res.from_cache)