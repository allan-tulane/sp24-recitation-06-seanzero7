# CMPS 2200 Recitation 06
## Answers

**Name:**_____Sean Hall____________________
**Name:**_____Tony Shen____________________


Place all written answers from `recitation-07.md` here for easier grading.



- **2)** W = 2W(n-1) + 1 for the longest branch
         W = 2W(n-2) +1 for the shortest branch 
        - Total work between O(2^n) and O(sqrt(2)^n)

- **3)** Longest branch: S(n) = S(n-1) + 1
        - Span = O(n)
         Shortest branch: S(n) = S(n-2) + 1
        - Span = O(n/2) = O(n)

- **4)** I printed the counts at each iteration when recursively getting the fib number at the 9th index.
The pattern is printed below
[0, 0, 0, 0, 0, 0, 0, 1]
[0, 0, 0, 0, 0, 0, 1, 1]
[0, 0, 0, 0, 0, 1, 1, 1]
[0, 0, 0, 0, 1, 1, 1, 1]
[0, 0, 0, 1, 1, 1, 1, 1]
[0, 0, 1, 1, 1, 1, 1, 1]
[1, 2, 2, 1, 1, 1, 1, 1]
[2, 3, 2, 2, 1, 1, 1, 1]
[2, 3, 3, 2, 1, 1, 1, 1]
[3, 5, 3, 2, 2, 1, 1, 1]
[3, 5, 3, 3, 2, 1, 1, 1]
[3, 5, 4, 3, 2, 1, 1, 1]
[4, 7, 5, 3, 2, 1, 1, 1]
[5, 8, 5, 3, 2, 2, 1, 1]
[5, 8, 5, 3, 3, 2, 1, 1]
[5, 8, 5, 4, 3, 2, 1, 1]
[5, 8, 6, 4, 3, 2, 1, 1]
[6, 10, 7, 4, 3, 2, 1, 1]
[7, 11, 7, 5, 3, 2, 1, 1]
[7, 11, 8, 5, 3, 2, 1, 1]


I first notice a triangle like sequence.
The initial rows start with a series of 0 and 1s, changing the right most 0 to 1 at the nth position of the array. This occurs until a one reaches the leftmost position. Column wise they somewhat resemble the fib sequence, although not applicable for every row.

It also shows how much duplicate work is done. 

- **6)** The maximum number of calls for any value i will be AT MOST one. The function checks if the value is equal to -1. If it is, it has been uninitialized and will have to be computed. Once computed, the value is changed and will not be computed again, only used in further computations (addition)

So the work will be O(n) and because the function is sequential, the span will also be O(n)

- **8)**
.  The maximum number of times that F_i will get read is n-2 times and cannot parallelized the algorithm. So the work and span for the Bottom-up will be O(n)