Solutions
=========

Python 3
--------

.. code-block:: python

    from datetime import datetime
    
    FORMAT = '%H:%M:%S'
    current = datetime.strptime(input(), FORMAT)
    explosion = datetime.strptime(input(), FORMAT)
    if current == explosion:
        print('24:00:00')
    else:
        d = explosion - current
        hours, remainder = divmod(d.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        print('{}:{}:{}'.format(str(hours).zfill(2), str(minutes).zfill(2), str(seconds).zfill(2)))