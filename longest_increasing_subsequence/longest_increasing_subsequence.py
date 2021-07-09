class Solution:
    def lengthOfLIS(self, nums):
        trees = []
        seen = set()
        for num in nums:
            if num in seen:
                continue
            added = False
            for tree in trees:
            seen.add(num)





if __name__ == '__main__':
    s = Solution()
    cases = [
        ([10,9,2,5,3,7,101,18], 4),
        ([0,1,0,3,2,3], 4),
        ([7,7,7,7,7,7,7], 1),
        ([10,9,8,7,6,5], 1),
    ]
    for (i, o) in cases:
        r = s.lengthOfLIS(*i)
        print(i, r, o == r)