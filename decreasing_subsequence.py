"""
Decreasing Subsequences
Given an int array nums of length n. Split it into strictly 
decreasing subsequences. Output the min number of subsequences 
you can get by splitting.
Example:
Input: [5, 2, 4, 3, 1, 6]
Output: 3
Explanation:
You can split this array into: [5, 2, 1], [4, 3], [6]. 
And there are 3 subsequences you get.
Or you can split it into [5, 4, 3], [2, 1], [6]. 
Also 3 subsequences.
But [5, 4, 3, 2, 1], [6] is not legal because [5, 4, 3, 2, 1] 
is not a subsuquence of the original array.
"""
import math
class Solution:
    def decreasing_subsequence(self, sequence):
        total = result = []

        for i in range(len(sequence)):
            if sequence[i] != float(math.inf):
                result = [sequence[i]]
                base = sequence[i]
                for j in range(i,len(sequence)):
                    if sequence[j] < base:
                        base = sequence[j]
                        result.append(sequence[j])
                        sequence[j] = float(math.inf)
                total.append(result)
        return len(total)
                
test = Solution()
input = [5, 2, 4, 3, 1, 6]
input2 = [2, 9, 12, 13, 4, 7, 6, 5, 10]
print(test.decreasing_subsequence(input))
print(test.decreasing_subsequence(input2))