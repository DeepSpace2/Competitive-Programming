Kattis\\Sum of the Others
=========================

Description
-----------

Every day, your job requires you to add up long lists of integers, like the following:

`3 + 2 + −4 + 8 + 3 + −6 + 1 + 4 + 6 + −1 + −6 = 10`

That is, a sum of positive and negative integers, followed by an equals sign, followed by a single integer. To save yourself some time, you normally leave out the + and = signs as you write down your work, so the previous example would be:

`3 2 −4 8 3 −6 1 4 6 −1 −6 10`

After you work out these sums, your coworker Bob types them into the office computer system. Unfortunately, Bob has been sloppy and has rearranged many of the numbers in your work. He has not changed any of the values in your list, he’s just rearranged their order. Thus, your careful work might have been entered like:

`6 −4 3 10 1 4 −1 −6 8 3 2 −6`

After sharing your unhappiness with Bob, you realize that this is not that great a problem. You can write a program to determine which of the values is the sum (the integer on the right of the equals sign).

Input
-----

Input consists of up to `200` test cases, one per line. Each line contains `2` to `30` integers in the range ``[−500, 500]``. Input ends at end of file.

Output
------

For each test case, print the member of the list that is the sum of all the other integers in the list. Every test case will contain such a value.

Sample Input/Output
-------------------

.. csv-table::
    :header: Input, Output

    "| 1 2 3
    | 2 1 -1 1 -1 2", "| 3
    | 2"