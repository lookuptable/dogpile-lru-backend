from dogpile.cache.api import CacheBackend
from dogpile.cache.api import NO_VALUE
from lru import LRU

class LruBackend(CacheBackend):
  """A dogpile cache backend that uses LRU as the size management."""

  def __init__(self, arguments):
    capacity = arguments.get("capacity", 100)
    self._lru = LRU(capacity)

  def get(self, key):
    return self._lru[key] if key in self._lru else NO_VALUE

  def set(self, key, value):
    self._lru[key] = value
