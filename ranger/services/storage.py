import numpy as np

# alternative: redis for shared in-memory cache

_storage = {}

def store(data):
    key = data.get('identifier')
    ranges = data.get('ranges', [])
    _storage[key] = {
        "ranges": ranges,
        "arrays": [np.array(xrange(x[0],x[1]+1)) for x in ranges if len(x) == 2]
    }
    return True

def get_storage():
    return _storage

