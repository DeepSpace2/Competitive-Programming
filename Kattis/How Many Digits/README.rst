# Kattis\How Many Digits

## Description

Often times it is sufficient to know the rough size of a number, rather than its exact value. For example, a human can reason about which store to visit to buy milk if one store is roughly `1` kilometer away, and another store is roughly `100` kilometers away. The exact distance to each store is irrelevant to the decision at hand; only the sizes of the numbers matter.

For this problem, determine the ‘size’ of the factorial of an integer. By size, we mean the number of digits required to represent the answer in base-10.

## Input

Input consists of up to `10000` integers, one per line. Each is in the range `[0, 1000000]`. Input ends at end of file.

## Output

For each integer `n`, print the number of digits required to represent `n!` in base-10.

## Sample Input/Output

|Input|Output|
|:-:|:-:|
|`0`<br>`1`<br>`3`<br>`10`<br>`20`|`1`<br>`1`<br>`1`<br>`7`<br>`19`|