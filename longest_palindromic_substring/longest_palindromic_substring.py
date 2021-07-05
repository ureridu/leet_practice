class Solution:
    def longestPalindrome(self, s):
        if len(s) == 1:
            return s
        ps = []
        start = None
        start3 = None
        for i, c in enumerate(s):
            j = i - 1
            k = j - 1
            if j >= 0 and c == s[j] and start is None:
                start = j
            elif j >= 0 and c != s[j] and start is not None:
                ps.append((start, j))
                start = None
            if k >= 0 and c == s[k]:
                if start3 is None:
                    start3 = k
            elif k >= 0 and c != s[k] and start3 is not None:
                if s[j] == s[start3]:
                    ps.append((start3, j))
                else:
                    ps.append((start3, k))
                start3 = None
        if start is not None:
            ps.append((start, i))
        if start3 is not None:
            ps.append((start3, i))

        mp = ((0, 0), 0)
        for (i, j) in ps:
            while i >= 0 and j < len(s):
                if s[i] == s[j]:
                    cl = j - i + 1
                    if cl > mp[-1]:
                        mp = ((i, j), cl)
                    i -= 1
                    j += 1
                else:
                    break

        return s[mp[0][0]:mp[0][1] + 1]


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome('aacabdkacaa'))