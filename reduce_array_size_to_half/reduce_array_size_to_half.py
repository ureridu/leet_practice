from collections import Counter

class Solution:

    def minSetSize(self, arr):
        counts = [v for v in sorted(Counter(arr).values())]
        n = len(arr)
        sum = 0
        rm = 0
        while sum < n/2:
            sum += counts.pop(-1)
            rm += 1
        return rm


if __name__ == '__main__':
    s = Solution()
    cases = [
        ([3,3,3,3,5,5,5,2,2,7], 2),
        ([7,7,7,7,7,7], 1),
        ([1,9], 1),
        ([1000,1000,3,7], 1),
        ([1,2,3,4,5,6,7,8,9,10], 5),
        ([1], 1)
    ]
    for (i, o) in cases:
        r = s.minSetSize(i)
        print(i, r, o == r)