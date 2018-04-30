"""Tests for pygdelt.gdeltv1"""

import unittest
from pygdelt.gdeltv1 import Events


class TestEvents(unittest.TestCase):

    def test_download(self):
        d_file = Events().query('20180127')

        self.assertEqual(
            d_file,
            'gdelt-data/output.zip'
        )
