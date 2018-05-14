# PyGDELT

PyGDELT is an easy to use interface for the [GDELT](https://www.gdeltproject.org/) datasets.
It currently supports both versions of GDELT datasets 1.0 and 2.0.

## To install
    pip install pygdelt

## Usage

### GDELT Version 1.0

```python
from pygdelt.gdeltv1 import Events
from datetime import datetime

ev = Events()
ev.query(datetime(2018, 4, 22))
```

### GDELT Version 2.0

```python
from pygdelt.gdeltv2 import Events, GKG, Mentions
from datetime import datetime

ev = Events()
ev.query(datetime(2018, 7, 21))

mtn = Mentions()
mtn.query(datetime(2018, 7, 21))

gkg = GKG()
gkg.query(datetime(2018, 7, 21))
```

## ToDo

 - [ ] Return as dataframe
 - [ ] Use preivous downloads
 - [ ] Parallel Downloads for GDELT 2.0
 - [ ] Query over a date range for GDELT 1.0

## Contributing

Feel free to give a PR
