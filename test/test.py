#!/usr/bin/env python3

import unittest


class TestMatches(unittest.TestCase):
    """
    Unit tests for matches
    """


    def setUp(self):
        self.names = {"me": "Pablo", "You": "I don't know!" }
        self.my_name = "Pablo"


    def test_matches_returns_correct_value_for_key(self):
        match = matches(self.names, "me")
        self.assertEqual(self.my_name, match)


    def test_matches_returns_None_as_default(self):
        match = matches(self.names, "She")
        self.assertIsNone(match)


    def test_matches_returns_default_value_passed(self):
        match = matches(self.names, "She", "Not found!")
        self.assertIsNotNone(match)


if __name__ == "__main__":
    unittest.main(verbosity=5)
