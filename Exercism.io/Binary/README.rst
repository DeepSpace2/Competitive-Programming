Exercism.io\\Binary
===================

Description
-----------

Convert a binary number, represented as a string (e.g. `'101010'`), to its decimal equivalent using first principles.

Implement binary to decimal conversion. Given a binary input string, your program should produce a decimal output. The program should handle invalid inputs.

Input
-----

A string representing a binary number.

Output
------

An integer in base-10.

Sample Input/Output
-------------------

.. csv-table::
    :header: "Input", "Output"

    "`0`", "`0`"
    "`1`", "`1`"
    "`10`", "`2`"
    "`11`", "`3`"
    "`11010`", "`26`"
    "`000011111`", "`31`"
    "`2`", "`ArgumentError`"
    "`01201`", "`ArgumentError`"
