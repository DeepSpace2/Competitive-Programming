Solutions
=========

Python 3
--------

.. code-block:: python

    import re
    
    print('hiss' if re.search(r's{2}', input()) else 'no hiss')

For this solution we can use a very simple regex that searches for two consecutive ``s`` characters in the input string.