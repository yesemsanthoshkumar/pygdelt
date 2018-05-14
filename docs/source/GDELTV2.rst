GDELT VERSION 2.0
==========================

Version 2.0 of GDELT contains daily data of events categorised into various cameo codes.
This version of GDELT separates event details into various files of 15 minute intervals.

::

    from pygdelt.gdeltv2 import Events, GKG, Mentions
    from datetime import datetime

    ev = Events()
    ev.query(datetime(2018, 7, 21))
    # pygdelt/v2/events/20180721

    mtn = Mentions()
    mtn.query(datetime(2018, 7, 21))
    # pygdelt/v2/mentions/20180721

    gkg = GKG()
    gkg.query(datetime(2018, 7, 21))
    # pygdelt/v2/gkg/20180721
