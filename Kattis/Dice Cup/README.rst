Kattis\\Dice Cup
================

Description
-----------

Write a program to compute the most likely outcomes for the sum of two dice rolls. Assume each die has numbered faces starting at `1` and that each face has equal roll probability.

Input
-----

The input consists of a single line with two integer numbers, `N` and `M`, specifying the number of faces of the two dice.

Constraints
-----------

`4 ≤ N`, `M ≤ 20`

Output
------

A line with the most likely outcome for the sum; in case of several outcomes with the same probability, they must be listed from lowest to highest value in separate lines.

Sample Input/Output
--------------------

.. csv-table::
    :header: Input, Output

    6 6, 7
    6 4, "| 5
    | 6
    | 7"
    12 20, "| 13
    | 14
    | 15
    | 16
    | 17
    | 18
    | 19
    | 20
    | 21"