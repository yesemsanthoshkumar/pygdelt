"""Base for pyGDELT
"""


class GDELT(object):
    def query(self, req_date, **kwargs):
        raise NotImplementedError

    def as_df(self, **kwargs):
        raise NotImplementedError

    def __repr__(self):
        raise NotImplementedError
