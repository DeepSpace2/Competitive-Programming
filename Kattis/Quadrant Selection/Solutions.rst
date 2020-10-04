Solutions
=========

Python 3
--------

.. code-block:: python

    x, y = map(int, (input() for _ in range(2)))
    if x > 0:
        print(1 if y > 0 else 4)
    else:
        print(2 if y > 0 else 3)
