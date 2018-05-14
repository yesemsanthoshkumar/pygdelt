GDELT VERSION 1.0
==========================

Version 1.0 of GDELT contains daily data of events categorised into various cameo codes.

::

    from pygdelt.gdeltv1 import Events
    from datetime import datetime

    ev = Events()
    ev.query(datetime(2018, 4, 22))
    # pygdelt/v1/20180422.zip
