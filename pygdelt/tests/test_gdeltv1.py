"""Tests for pygdelt.gdeltv1"""

from unittest.mock import patch

from pygdelt import gdeltv1 as gdelt


class TestEvents(object):

    def test_url(self):
        ev = gdelt.Events()

        assert ev._url == "http://data.gdeltproject.org/events"

    def test_query(self):
        with patch.object(gdelt.GDELTV1, '_download') as mock_download:
            mock_download.return_value = 'pygdelt/v1/20180127.export.CSV.zip'

            ev = gdelt.Events()
            res = ev.query('20180127')

            assert res == 'pygdelt/v1/20180127.export.CSV.zip'
