"""Tests for pygdelt.gdeltv1"""

import unittest
from pygdelt import gdeltv1 as v1
from unittest.mock import patch

class TestEvents(unittest.TestCase):

    def test_event_creation(self):
        ev =  v1.Events()

        self.assertEqual(
            ev._url,
            "http://data.gdeltproject.org/events"
        )

    def test_events_query(self):
        with patch.object(v1, 'download') as mock_download:
            mock_download.return_value = 'pygdelt/data/20180127.export.CSV.zip'

            ev = v1.Events()
            ev.query('20180127')

            self.assertEqual(
                ev._filepath,
                'pygdelt/data/20180127.export.CSV.zip'
            )
