class Solution:
    def validate_clips(self,clips,time):
        max_jump = [0]*101
        for l,r in clips:
            max_jump[l] = max(max_jump[l],r)

        res=lo=hi = 0
        while hi<time:
            lo,hi = hi,max(max_jump[lo:hi+1])
            if hi<lo:
                return -1
            res+=1
        return res

sol = Solution()
clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]]
print(sol.validate_clips(clips,10))