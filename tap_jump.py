class Solution:
    def minTaps(self, n, ranges) -> int:
        # start = end = taps = 0
        # while end<n:
        #     for i in range (len(ranges)):
        #         if i-ranges[i]<=start and i+ranges[i]>end:
        #             end=i+ranges[i]
        #         if start == end:
        #             return -1
        #         taps +=1
        #         start = end
        # return taps
        start, end = 0, 0
        taps = 0
        
        while end< n:
            for i in range(len(ranges)):
                if i-ranges[i] <= start and i+ ranges[i]>end:
                    end = i + ranges[i]
            if start == end:
                return -1
            taps +=1
            start = end
        return taps
sol = Solution()
print(sol.minTaps(5,[3,4,1,1,0,0]))
