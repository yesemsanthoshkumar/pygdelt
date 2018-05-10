"""Has all data and utility functions for dealing with
GDELT data version 2.0
"""

import os
from datetime import timedelta

import pandas as pd
import requests as rq
from tqdm import tqdm

from pygdelt.gdelt_base import GDELT

_DATA_DIR = 'pygdelt\\v2'
_VERSION = '2.0'


def generate_day_range(req_date):
    """Generate the range of files to _download.
    The range are 15 minute intervals of the given date

    Parameters
    ----------
    req_date    :   datetime.datetime
        The date to which the intervals have to be generated
    """
    # 24 * 4 = 96 15 minute intervals in a day
    for i in range(96):
        yield req_date.strftime('%Y%m%d%H%M00')
        req_date = req_date + timedelta(seconds=900)


class GDELTV2(GDELT):
    """Base GDELT Version 2.0 interface

    Method
    ------
    to_df
        Returns a dataframe of the previously queried date
    _download
        Downloads the data files for the given date

    See Also
    --------
    Events, Mentions, GKG
    """
    _url = 'http://data.gdeltproject.org/gdeltv2'

    # def to_df(self, **kwargs):
    #     """Reads the given file and returns a dataframe

    #     Parameters
    #     ----------
    #     kwargs
    #         Arguments to pandas.read_csv
    #     """
    #     return pandas.read_csv(self._filepath, **kwargs)

    def _download(self, req_date, hide_progress=True):
        """Download the data file for the given date

        Parameters
        ----------
        req_date    :   datetime.dateime
            Date for which the data to be _downloaded
        hide_progress   :   boolean
            Set this False to hide progress bar while downloading

        Returns
        -------
        Path to the _downloaded folder
        """
        pref_loc = os.path.join(
            _DATA_DIR,
            req_date.strftime('%Y%m%d'),
            self._subfolder
        )
        if not os.path.exists(pref_loc):
            os.makedirs(pref_loc)
        # For verion 2.0 we download all the files under the folder inside
        # **_DATA_DIR/req_date** and return this folder

        for dt in generate_day_range(req_date):
            url_formatted = "{0}/{1}.{2}".format(self._url, dt, self._suffix)
            resp = rq.get(url_formatted, stream=True)

            f_name = os.path.join(pref_loc, dt + ".zip")
            with open(f_name, 'wb') as data_file:
                for chunk in tqdm(resp.iter_content(), disable=hide_progress):
                    data_file.write(chunk)

        return pref_loc

    def __repr__(self):
        return "PyGDELT - {0} for GDELT Version {1}".format(
            __class__.__name__,
            _VERSION
        )


class Events(GDELTV2):
    """Handles all the queyring for events table in  GDELT version 2.0"""

    def __init__(self):
        self._suffix = 'export.CSV.zip'
        self._subfolder = 'events'

    def query(self, req_date, hide_progress=True):
        """Query the data for the specified datetime

        Parameters
        ----------
        req_date  :   datetime.datetime
            Represents the date of the event data to _download
        hide_progress   :   boolean, defaults to True
            Set this False to hide progress bar while downloading
        """
        return self._download(req_date, hide_progress)


class Mentions(GDELTV2):

    def __init__(self):
        self._suffix = 'mentions.CSV.zip'
        self._subfolder = 'mentions'

    def query(self, req_date, hide_progress=True):
        """Query the data for the specified datetime

        Parameters
        ----------
        req_date  :   datetime.datetime
            Represents the date of the event data to _download
        hide_progress   :   boolean, defaults to True
            Set this False to hide progress bar while downloading
        """
        return self._download(req_date, hide_progress)


class GKG(GDELTV2):

    def __init__(self):
        self._suffix = 'gkg.csv.zip'
        self._subfolder = 'gkg'

    def query(self, req_date, hide_progress=True):
        """Query the data for the specified datetime

        Parameters
        ----------
        req_date  :   datetime.datetime
            Represents the date of the event data to _download
        hide_progress   :   boolean, defaults to True
            Set this False to hide progress bar while downloading
        """
        return self._download(req_date, hide_progress=True)
