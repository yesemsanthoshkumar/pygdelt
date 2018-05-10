"""Base for PyGDELT
"""


class GDELT(object):
    def query(self, req_date, **kwargs):
        raise NotImplementedError

    def to_df(self, **kwargs):
        raise NotImplementedError

    def _download(self, req_date):
        raise NotImplementedError
