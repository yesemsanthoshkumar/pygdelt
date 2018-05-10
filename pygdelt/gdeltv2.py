"""Has all data and utility functions for dealing with
GDELT data version 2.0
"""

import os

import pandas as pd
import requests as rq
from tqdm import tqdm

from pygdelt import V2_DATA_DIR as _DATA_DIR
from pygdelt import GDELT


def download(url, op_file='output'):
    """Download the data file

    Parameters
    ----------
    url     :   str
        URL of the file to be downloaded

    op_file :   str
        Output file name (Defaults to output.zip)

    Returns
    -------
    Path to the downloaded file
    """
    resp = rq.get(url, stream=True)
    if not os.path.exists(_DATA_DIR):
        os.makedirs(_DATA_DIR)
    pref_loc = os.path.join(_DATA_DIR, op_file + '.zip')

    with open(pref_loc, 'wb') as data_file:
        for chunk in tqdm(resp.iter_content()):
            data_file.write(chunk)

    return pref_loc


class Events(GDELT):
    """Handles all the queyring for events table in  GDELT version 2.0"""

    def __init__(self):
        self._url = 'http://data.gdeltproject.org/gdeltv2'

    def query(self, req_date):
        """Query the data for the specified datetime

        Parameters
        ----------
        req_date  :   str
            Represents the date of the event data to download
        """
        url = "%s/%s.export.CSV.zip" % (self._url, req_date)
        self._filepath = download(url, req_date)

    def as_df(self, **kwargs):
        """Reads the given file and returns a dataframe

        Parameters
        ----------
        kwargs
            Arguments to pandas.read_csv
        """
        return pd.read_csv(self._filepath, **kwargs)

    def __repr__(self):
        return "PyGDELT Version1 - Events Data"


class Mentions(GDELT):

    def __init__(self, *args, **kwargs):
        self._url = "http://data.gdeltproject.org/gdeltv2"

    def query(self, req_date):
        """Query the data for the specified datetime

        Parameters
        ----------
        req_date  :   str
            Represents the date of the event data to download
        """
        url = "%s/%s.mentions.CSV.zip" % (self._url, req_date)
        self._filepath = download(url, req_date)

    def as_df(self, **kwargs):
        """Reads the given file and returns a dataframe

        Parameters
        ----------
        kwargs
            Arguments to pandas.read_csv
        """
        return pd.read_csv(self._filepath, **kwargs)

    def __repr__(self):
        return "PyGDELT Version2 - Mentions Data"
