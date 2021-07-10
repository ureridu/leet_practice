from functools import lru_cache
from collections import defaultdict


class Solution:
    # def lengthOfLIS(self, nums):
    #     trees = {float('-inf'): []}
    #     for num in nums:
    #         self.recur(num, trees)
    #     return self.count(trees, 0)
    #
    # def recur(self, num, tree):
    #     added = 0
    #     for node, nexts in tree.items():
    #         if num > node:
    #             for next in nexts:
    #                 a = self.recur(num, next)
    #                 added += a
    #             if not added:
    #                 nexts.append({num: []})
    #                 added = 1
    #         elif num == node:
    #             added = 1
    #     return added
    #
    # def count(self, tree, count):
    #     counts = [count]
    #     for node, nexts in tree.items():
    #         for next in nexts:
    #             c = self.count(next, count+1)
    #             counts.append(c)
    #     return max(counts)


    # def lengthOfLIS(self, nums):
    #     self.graph = defaultdict(list)
    #     self.graph[(0, nums[0])].append((-1, float('-inf'), 0))
    #     threads = [(0, nums[0], 1)]
    #     for i, num in enumerate(nums[1:]):
    #         i += 1
    #         new_threads = defaultdict(list)
    #         for (ti, tnum, c) in threads:
    #             if tnum < num:
    #                 new_threads[(i, num)].append(c+1)
    #                 self.graph[(i, num)].append((ti, tnum, c))
    #             else:
    #                 new_threads[(ti, tnum)].append(c)
    #                 if tnum > num:
    #                     new_threads[(i, num)].append(self.recur(i, num, ti, tnum))
    #         threads = [(i, num, max(c)) for (i, num), c in new_threads.items()]
    #     self.recur.cache_clear()
    #     return max([c for (_, _, c) in threads])
    #
    # @lru_cache(maxsize=None)
    # def recur(self, i, num, ti, tnum):
    #     counts = [0]
    #     for (j, jnum, c) in self.graph[(ti, tnum)]:
    #         if num < jnum:
    #             counts.append(self.recur(i, num, j, jnum))
    #         elif (num > jnum and i != j) or j == -1:
    #             self.graph[(i, num)].append((j, jnum, c))
    #             counts.append(c+1)
    #         elif (num == jnum and i != j):
    #             counts.append(c)
    #     return max(counts)

    def lengthOfLIS(self, nums):
        n = len(nums)
        if n == 1:
            return 1
        dp = [1] * n
        for i, a in enumerate(nums):
            for j, b in enumerate(nums[i:]):
                j += i
                if b > a and dp[i] + 1 > dp[j]:
                    dp[j] = dp[i] + 1
        return max(dp)


#
# class Solution:
#     def lengthOfLIS(self, nums):
#         snums = sorted(nums)
#         lookup = {v: ~i for i, v in enumerate(nums[::-1])}
#         snums = sorted([(v, i) for i, v in enumerate(nums)], key=lambda x: x[0])
#         lis = 0
#         c = 1
#         prev_i, prev_v = snums[0]
#         for (v, i) in snums[1:]:
#             if v == prev_v:
#                 continue
#             if i > prev_i:
#                 c += 1
#                 prev_i = i
#         return c



if __name__ == '__main__':
    s = Solution()
    cases = [
        ([10,9,2,5,3,7,101,18], 4),
        ([0,1,0,3,2,3], 4),
        ([7,7,7,7,7,7,7], 1),
        ([10,9,8,7,6,5], 1),
        ([1], 1),
        ([2, 3, 4, 1, 5], 4),
        ([1,2,3,1,2,1,2,1,2], 3),
        ([1,2,3,4,5,4], 5),
        ([1,3,6,7,9,4,10,5,6], 6),
        ([3,5,6,2,5,4,19,5,6,7,12], 6)

    ]
    for (i, o) in cases:
        r = s.lengthOfLIS(i)
        print(i, r, o == r)