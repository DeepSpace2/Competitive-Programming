Kattis\\Guessing Game
====================

Description
-----------

Stan and Ollie are playing a guessing game. Stan thinks of a number between `1` and `10` (inclusive) and Ollie guesses what the number might be. After each guess, Stan indicates whether Ollie’s guess is too high, too low, or right on.

After playing several rounds, Ollie has become suspicious that Stan cheats; that is, that he changes the number between Ollie’s guesses. To prepare his case against Stan, Ollie has recorded a transcript of several games. You are to determine whether or not each transcript proves that Stan is cheating.

Input
-----

Standard input consists of several transcripts. Each transcript consists of a number of paired guesses and responses. A guess is a line containing single integer between `1` and `10` (inclusive), and a response is a line containing `“too high”`, `“too low”`, or `“right on”`. Each game ends with `“right on”`. A line containing `0` follows the last transcript. There are at most `2500` guess-response pairs in total.

Output
------

For each game, output a line `“Stan is dishonest”` if Stan’s responses are inconsistent with the final guess and response. Otherwise, print `“Stan may be honest”`.

Sample Input/Output
-------------------

.. csv-table::
    :header: Input, Output

    "| 10
    | too high
    | 3
    | too low
    | 4
    | too high
    | 2
    | right on", "Stan is dishonest"
    "| 5
    | too low
    | 7
    | too high
    | 6
    | right on
    | 0", "Stan may be honest"