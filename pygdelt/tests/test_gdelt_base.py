"""Test for gdelt_base
"""

import pytest
from pygdelt.gdelt_base import GDELT

from datetime import datetime


class TestGDELTBase(object):

    def test_query(self):
        with pytest.raises(NotImplementedError):
            GDELT().query(datetime.now())

    def test_download(self):
        with pytest.raises(NotImplementedError):
            GDELT()._download(datetime.now())

    def test_to_df(self):
        with pytest.raises(NotImplementedError):
            GDELT().to_df()
