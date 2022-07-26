"""
Copyright (c) 2008-2022 synodriver <synodriver@gmail.com>
"""
from random import randint
from unittest import TestCase

from pyclhash import RANDOM_BYTES_NEEDED_FOR_CLHASH, get_random_seed, hash


class TestAll(TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_hash(self):
        for i in range(1000):
            seed = get_random_seed(1, 2)
            self.assertEqual(hash(b"12", seed), hash(b"12", seed))

    def test_hash_with_key(self):
        for i in range(1000):
            seed = bytes(
                [randint(0, 255) for _ in range(RANDOM_BYTES_NEEDED_FOR_CLHASH)]
            )
            self.assertEqual(hash(b"12", seed), hash(b"12", seed))


if __name__ == "__main__":
    import unittest

    unittest.main()
