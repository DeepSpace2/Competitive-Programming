# Kattis\Greedily Increasing Subsequence

## Description

Given a permutation `A = (a`<sub>`1`</sub>`, a`<sub>`2`</sub>`, …, a`<sub>`N`</sub>`)` of the integers `1, 2, …, N`, we define the greedily increasing subsequence (GIS) in the following way.

Let `g`<sub>`1`</sub>` = a`<sub>`1`</sub>. For every `i > 1`, let `g`<sub>`i`</sub> be the leftmost integer in `A` that is strictly larger than `g`<sub>`i-1`</sub>. If there for a given `i` is no such integer, we say that the GIS of the sequence is the sequence `(g`<sub>`1`</sub>` , g`<sub>`2`</sub>`, ..., g`<sub>`i−1`</sub>`)`.

Your task is to, given a permutation `A`, compute the GIS of `A`.

## Input

The first line of input contains an integer `1 ≤ N ≤ 10`<sup>`6`</sup>, the number of elements of the permutation `A`. The next line contains `N` distinct integers between `1` and `N`, the elements `a`<sub>`1`</sub>`, … , a`<sub>`N`</sub> of the permutation `A`.

## Output

First, output a line containing the length `l` of the GIS of `A`. Then, output `l` integers, containing (in order) the elements of the GIS.

## Sample Input/Output

|Input|Output|
|:-:|:-:|
|`7`<br>`2 3 1 5 4 7 6`|`4`<br>`2 3 5 7`|
|`5`<br>`1 2 3 4 5`|`5`<br>`1 2 3 4 5`|
|`5`<br>`5 4 3 2 1`|`1`<br>`5`|