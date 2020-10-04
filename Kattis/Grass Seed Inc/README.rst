Kattis\\Grass Seed Inc.
======================

Description
-----------

Many years ago after another unfruitful day in Cubicle Land, banging her head against yet another cutting edge, marketing buzzword-filled JavaScript framework, Janice the engineer looked out of the window and decided that time was ripe for a change.

So swapping her keyboard and mouse for a fork and a spade, she started her own gardening company.

After years of hard outdoor work Janice now has biceps like Van Damme and owns the premiere landscaping company in the whole of the South West, and has just been lucky enough to broker a large contract to sow lawns for landed gentry.

Each contract details the size of the lawns that need to be seeded, and the cost of seed per square metre. How much do you need to spend on seed?

Input
-----

- One line containing a real number `C` (`0 < C ≤ 100`), the cost of seed to sow one square metre of lawn.

- One line containing an integer `L` (`0 < L ≤ 100`), the number of lawns to sow.

- `L` lines, each containing two positive real numbers: `w`:subscript:`i` (`0 ≤ w`:subscript:`i` `≤ 100`), the width of the lawn, and `l`:subscript:`i` (`0 ≤ l`:subscript:`i` `≤ 100`), the length of the lawn.

Output
------

- One line containing a real number: the cost to sow all of the lawns.

All output must be accurate to an absolute or relative error of at most `10`:superscript:`−6`.

Sample Input/Output
-------------------

.. csv-table::
    :header: Input, Output
    
    "| 2
    | 3
    | 2 3
    | 4 5
    | 5 6", 112.0000000
    "| 0.75
    | 2
    | 2 3.333
    | 3.41 4.567", 16.6796025