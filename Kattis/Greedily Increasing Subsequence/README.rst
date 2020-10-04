Kattis\\Greedily Increasing Subsequence
=======================================

Description
-----------

Given a permutation `A` = (`a`:subscript:`1`, `a`:subscript:`2`, …, `a`:subscript:`N`) of the integers `1, 2, …, N`, we define the greedily increasing subsequence (GIS) in the following way.

Let `g`:subscript:`1` = `a`:subscript:`1`. For every `i > 1`, let `g`:subscript:`i` be the leftmost integer in `A` that is strictly larger than `g`:subscript:`i-1`. If there for a given `i` is no such integer, we say that the GIS of the sequence is the sequence (`g`:subscript:`1` , `g`:subscript:`2`, ..., `g`:subscript:`i−1`).

Your task is to, given a permutation `A`, compute the GIS of `A`.

Input
-----

The first line of input contains an integer `1 ≤ N ≤ 10`:superscript:`6`, the number of elements of the permutation `A`. The next line contains `N` distinct integers between `1` and `N`, the elements `a`:subscript:`1`, … , `a`:subscript:`N` of the permutation `A`.

Output
------

First, output a line containing the length `l` of the GIS of `A`. Then, output `l` integers, containing (in order) the elements of the GIS.

Sample Input/Output
-------------------

.. csv-table::
    :header: Input, Output

    "| 7
    | 2 3 1 5 4 7 6", "| 4
    | 2 3 5 7"
    "| 5
    | 1 2 3 4 5", "| 5
    | 1 2 3 4 5"
    "| 5
    | 5 4 3 2 1", "| 1
    | 5"