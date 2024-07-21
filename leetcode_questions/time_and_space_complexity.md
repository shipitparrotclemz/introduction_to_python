## Glossary of Terms

### 1. Big O Notation
A way to describe how the running time or memory use of an algorithm grows as the size of the input gets bigger. It helps us understand the efficiency of an algorithm without worrying about the specific computer or programming language used.

#### Rules:
1. We don't take the scalar, only the power:
   - This means we ignore constants and focus on the term with the highest exponent.
   - **Example:** If an algorithm has three for-loops over a list, instead of having a worst-case time complexity of O(3N), we say it's O(N).

2. We take the highest base:
   - If an algorithm has multiple terms, we only consider the one with the largest growth rate.
   - **Example:** If an algorithm uses a merge sort algorithm that takes O(N log N) and another for-loop that takes O(N), instead of having a worst-case time complexity of O(N log N + N), we say it's O(N log N).

### 2. Average Time Complexity
The amount of time an algorithm usually takes to run for a typical input. It gives us an idea of how fast the algorithm will work most of the time.

### 3. Average Space Complexity
The amount of memory an algorithm usually needs for a typical input. It tells us how much space the algorithm will use on average.

### 4. Worst Case Time Complexity
The longest time an algorithm could take to finish for the worst possible input. It guarantees that the algorithm will never be slower than this time, no matter what input it gets.

### 5. Worst Case Space Complexity
The most memory an algorithm could use for the worst possible input. It guarantees that the algorithm will never need more space than this, no matter what input it gets.