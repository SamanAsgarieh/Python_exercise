'''
Minimum Domino Rotations For Equal Row
In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom 
halves of the ith domino. (A domino is a tile with two numbers from 1 to 
6 - one on each half of the tile.)
We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

Return the minimum number of rotations so that all the values in tops are 
the same, or all the values in bottoms are the same.

If it cannot be done, return -1.

Example:
Input: tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by tops and bottoms: 
before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in 
the top row equal to 2, as indicated by the second figure.
'''

from collections import Counter
class Solution:    
    def minDominoRotations(self, A, B) -> int:
        a, b = Counter(A), Counter(B)
        c = a + b
        print(c.items())
        num = max(c.items(), key=lambda n: n[1])[0]
        if any(A[i] != num and B[i] != num for i in range(len(A))):
            return -1
        return len(A) - max(a[num], b[num])

tops = [2,1,2,4,2,2]
bottoms = [5,2,6,2,3,2]

# tops = [1,1,1,1,1]
# bottoms = [1,1,1,1,1]

test = Solution()
print(test.minDominoRotations(tops,bottoms))
