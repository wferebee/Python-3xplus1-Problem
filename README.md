## Running through the first 10,000 numbers of the 3x + 1 Algebra
If the number is odd, then multiply by (3x+1)
If the number is even, the divide by 2
Stop when the number reaches 1
 - when a number reaches 1, it enters an infinite loop of "1 -> 4 -> 2 -> 1 -> 4..."

Scientist have worked out that atleast the very first 2^68 digits all reolve to the number loop of "-> 4 -> 2 -> 1 -> 4...",
but it has not been proven yet if this exists for all numbers

Here, I am just running through the first 10,000 digits as an exercise while learning Python
 - execution time < .5 seconds
 - after trying the first, 100, 500, 1000, so some values may have been stored already
