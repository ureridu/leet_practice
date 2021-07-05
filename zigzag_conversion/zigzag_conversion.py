class Solution:
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        d = {i: [] for i in range(numRows)}
        i = 0
        j = 1
        for c in s:
            d[i].append(c)
            if i + j == numRows or i + j < 0:
                j = -j
            i += j
        out = []
        for i in range(numRows):
            out += d[i]
        return ''.join(out)


if __name__ == '__main__':
    io = [('PAYPALISHIRING', 'PAHNAPLSIIGYIR', 3), ('PAYPALISHIRING', 'PINALSIGYAHRPI', 4), ('PAYPALISHIRING', 'PAYPALISHIRING', 1), ('AB', 'AB', 2)]
    s = Solution()
    for (i, o, n) in io:
        r = s.convert(i, n)
        print(i, r, o==r)