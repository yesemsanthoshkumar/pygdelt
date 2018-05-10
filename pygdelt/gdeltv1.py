"""Has all data and utility functions for dealing with
GDELT data version 1.0
"""

import os

import pandas as pd
import requests as rq
from tqdm import tqdm

from pygdelt.gdelt_base import GDELT

_DATA_DIR = 'pygdelt\\v1'
_VERSION = '1.0'


class GDELTV1(GDELT):
    """Base GDELT Version 1.0 interface

    Method
    ------
    to_df
        Returns a dataframe of the previously queried date
    _download
        Downloads the data files for the given date

    See Also
    --------
    Events
    """

    def __init__(self):
        self._url = 'http://data.gdeltproject.org/events'

    def to_df(self, **kwargs):
        """Reads the given file and returns a dataframe

        Parameters
        ----------
        kwargs
            Arguments to pandas.read_csv
        """
        return pd.read_csv(self._filepath, **kwargs)

    def _download(self, req_date, hide_progress=True):
        """Download the data file

        Parameters
        ----------
        req_date  :   datetime.datetime
            Represents the date of the event data to _download
        hide_progress   :   boolean, defaults to True
            Set this False to hide progress bar while downloading

        Returns
        -------
        Path to the downloaded file
        """
        if not os.path.exists(_DATA_DIR):
            os.makedirs(_DATA_DIR)

        dt_strf = req_date.strftime("%Y%m%d")
        f_name = "{0}.zip".format(dt_strf)
        pref_loc = os.path.join(_DATA_DIR, f_name)

        url_formatted = "{0}/{1}.{3}".format(self._url, dt_strf, self._suffix)
        resp = rq.get(self._url, stream=True)

        with open(pref_loc, 'wb') as data_file:
            for chunk in tqdm(resp.iter_content(), disable=hide_progress):
                data_file.write(chunk)

        return pref_loc

    def __repr__(self):
        return "PyGDELT - {0} for GDELT Version {1}".format(
            __class__.__name__,
            _VERSION
        )


class Events(GDELTV1):
    """Handles all the queyring for events table in  GDELT version 1.0"""

    def __init__(self):
        super().__init__()
        self._suffix = 'export.CSV.zip'

    def query(self, req_date, hide_progress=True):
        """Query the data for the specified datetime

        Parameters
        ----------
        req_date  :   datetime.datetime
            Represents the date of the event data to download
        hide_progress   :   boolean, defaults to True
            Set this False to hide progress bar while downloading
        """
        return self._download(req_date, hide_progress)
