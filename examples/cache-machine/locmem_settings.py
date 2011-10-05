from settings import *

CACHES = {
    'default': {
        'BACKEND': 'caching.backends.locmem.CacheClass',
    },
    'secondary': {
        'BACKEND': 'caching.backends.locmem.CacheClass',
        'LOCATION': 'secondary',
    },
}

