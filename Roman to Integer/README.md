## Roman to Integer Conversion

Roman numerals are represented by seven different symbols: I, V, X, L, C, D, and M. Here are the corresponding values for each symbol:

Symbol Value
I       1
V       5
X      10
L      50
C      100
D      500
M      1000


However, Roman numerals have a unique representation system where certain symbols can be placed before others to denote subtraction. For instance, IV represents 4 (5 - 1) and IX represents 9 (10 - 1).

Given a Roman numeral string, you need to convert it to an integer. Implement a function `romanToInt(s: str) -> int` that accepts a Roman numeral string `s` and returns its integer value.

### Examples:

1. Input: `s = "III"`
   Output: `3`
   Explanation: III is equivalent to 3.

2. Input: `s = "LVIII"`
   Output: `58`
   Explanation: L = 50, V = 5, III = 3.

3. Input: `s = "MCMXCIV"`
   Output: `1994`
   Explanation: M = 1000, CM = 900, XC = 90, and IV = 4.

### Constraints:

- 1 <= s.length <= 15
- `s` contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
- It is guaranteed that `s` is a valid Roman numeral in the range [1, 3999].
