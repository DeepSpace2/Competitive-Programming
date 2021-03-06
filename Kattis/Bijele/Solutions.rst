Solutions
=========

Python 3
--------

.. code-block:: python

    print(' '.join(str(valid - input_array) for valid, input_array in zip([1, 1, 2, 2, 2, 8], map(int, input().split()))))

A single-line solution that may look intimidating but is fairly straightforward:

1. ``[1, 1, 2, 2, 2, 8]`` is the representation of the valid set.
2. ``map(int, input().split()`` generates a similar representation for the inputted set.
3. ``zip`` then generates a 2-tuple, the first element being from the valid set and the second element from the inputted set.
4. The ``for`` loop itself calculates the difference between the 2 elements in each tuple and ``' '.join`` makes sure we get the output in the required format.