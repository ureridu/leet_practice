class Solution:
    def kthSmallest(self, matrix, k):
        if k == 1:
            return matrix[0][0]
        n = len(matrix)
        s = n
        sm = [matrix.pop(0)]
        r = []
        while matrix and (s <= k or sm[-1][-1] >= matrix[0][0]):
            b = matrix.pop(0)
            if b[0] < sm[-1][-1]:
                sm.append(b)
            else:
                if len(sm) > 1:
                    r += sorted(sum(sm, []))
                else:
                    r += sm[0]
                sm = [b]
            s += len(set(b))
        if sm:
            r += sorted(sum(sm, []))
            del sm
        return r[k-1]





if __name__ == '__main__':
    import copy
    s = Solution()
    cases = [
        ([[1,5,9],[10,11,13],[12,13,15]], 8, 13),
        ([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5, 5),
        ([[1,5],[10,11]], 4, 11),
        ([[-5]], 1, -5)
    ]
    for (m, k, o) in cases:
        r = s.kthSmallest(copy.copy(m), k)
        print(m, r, r == o)
