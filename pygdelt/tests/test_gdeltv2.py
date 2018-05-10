"""Tests for pygdelt.gdeltv2"""

from pygdelt import gdeltv2 as gdelt
from unittest.mock import patch


class TestEvents(object):

    def test_url(self):
        ev = gdelt.Events()

        assert ev._url == "http://data.gdeltproject.org/gdeltv2"

    def test_query(self):
        with patch.object(gdelt.GDELTV2, '_download') as mock_download:
            mock_download.return_value = 'pygdelt/v2/20180127'

            ev = gdelt.Events()
            res = ev.query('20180127')

            assert res == 'pygdelt/v2/20180127'


class TestMentions(object):

    def test_url(self):
        mn = gdelt.Mentions()

        assert mn._url == "http://data.gdeltproject.org/gdeltv2"

    def test_query(self):
        with patch.object(gdelt.GDELTV2, '_download') as mock_download:
            mock_download.return_value = 'pygdelt/v2/20180127'

            mn = gdelt.Mentions()
            res = mn.query('20180127')

            assert res == 'pygdelt/v2/20180127'


class TestGKG(object):

    def test_url(self):
        gkg = gdelt.GKG()

        assert gkg._url == "http://data.gdeltproject.org/gdeltv2"

    def test_query(self):
        with patch.object(gdelt.GDELTV2, '_download') as mock_download:
            mock_download.return_value = 'pygdelt/v2/20180127'

            gkg = gdelt.GKG()
            res = gkg.query('20180127')

            assert res == 'pygdelt/v2/20180127'
