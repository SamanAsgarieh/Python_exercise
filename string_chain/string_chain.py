from collections import defaultdict

class Solution:
    def longestStrChain(self, words) -> int:
        words.sort(key=lambda x: len(x))
        trans_count=defaultdict(int)
        for word in words:
            trans_count[word] = 1
            for i in range(len(word)):
                subword = word[:i]+word[i+1:]
                if subword in trans_count:
                    trans_count[word]=max(trans_count[subword]+1,trans_count[word])

        return max(trans_count.values())

sol = Solution()
print(sol.longestStrChain(["xbc","pcxbcf","xb","cxbc","pcxbc"]))
