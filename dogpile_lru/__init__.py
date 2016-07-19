from dogpile.cache import register_backend

LRU_CACHE = "lru-cache"

register_backend(LRU_CACHE, "dogpile_lru.backends", "LruBackend")
