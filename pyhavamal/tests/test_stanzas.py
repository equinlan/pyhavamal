from unittest import TestCase

import pyhavamal

class TestStanzas(TestCase):
    def test_stanza_count(self):
        self.assertEqual(len(pyhavamal.all()), 165)
    
    def test_all_numbered(self):
        self.assertIsInstance(pyhavamal.all(True), dict)

    def test_find_good_number(self):
        self.assertIsInstance(pyhavamal.find_by_number(1), str)
    
    def test_find_bad_number(self):
        self.assertIsNone(pyhavamal.find_by_number(0))

    def test_random(self):
        self.assertIsInstance(pyhavamal.random(), str)

    def test_wide_range(self):
        self.assertEqual(len(pyhavamal.range_by_number(0,166)), 167)