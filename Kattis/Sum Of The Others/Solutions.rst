Solutions
=========

Python 3
--------

.. code-block:: python

    while True:
        try:
            line = input().strip()
        except EOFError:
            break
        line = list(map(int, line.split()))
        for num in line:
            num_index = line.index(num)
            excluded_line = line[:num_index] + line[num_index + 1:]
            if sum(excluded_line) == num:
                print(num)
                break