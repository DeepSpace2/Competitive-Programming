Solutions
=========

One thing that stands out when approaching this problem is the fact this problem is all about the parity of the number of stones. This suggests that we can use the modulos operator.

Python 3
--------

.. code-block:: python

    print('Bob' if int(input()) % 2 == 0 else 'Alice')

In this one-liner solution we 1:superscript:st read the input (the number of stones) and convert it to an integer. Then we print ``'Bob'`` if the number of stones is even or ``'Alice'`` if it is odd. 