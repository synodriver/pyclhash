"""
Copyright (c) 2008-2022 synodriver <synodriver@gmail.com>
"""
import os
os.environ["CLHASH_USE_CFFI"] = "1"

from unittest import TestCase

from pyclhash import get_random_seed, hash


class TestAll(TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_hash(self):
        for i in range(1000):
            seed = get_random_seed(1, 2)
            self.assertEqual(hash(b"12", seed), hash(b"12", seed))

if __name__ == "__main__":
    import unittest

    unittest.main()