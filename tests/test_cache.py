import unittest

from dogpile.cache import make_region
from dogpile.cache.api import NO_VALUE
from dogpile_lru import LRU_CACHE


class LruBackendTest(unittest.TestCase):

  def setUp(self):
    self._lru_cache = make_region().configure(LRU_CACHE)

  def testGet(self):
    self.assertEquals(NO_VALUE, self._lru_cache.get("non-existent-key"))

    self._lru_cache.set("key", "value")
    self.assertEquals("value", self._lru_cache.get("key"))
