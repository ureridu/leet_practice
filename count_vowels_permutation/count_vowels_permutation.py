class Solution:

    LOOKUP = {'a': {0: 1},
              'e': {0: 1},
              'i': {0: 1},
              'o': {0: 1},
              'u': {0: 1}
              }

    MAP = {'a': ['e'],
              'e': ['a', 'i'],
              'i': ['a', 'e', 'o', 'u'],
              'o': ['u', 'i'],
              'u': ['a'],
              }

    def countVowelPermutation(self, n):
        out = 0
        for v in self.MAP.keys():
            out += self.recur(v, n-1) % 1000000007
        return out % 1000000007

    def recur(self, v, n):
        if n in self.LOOKUP[v]:
            return self.LOOKUP[v][n] % 1000000007
        else:
            self.LOOKUP[v][n] = 0
            for i in self.MAP[v]:
                self.LOOKUP[v][n] += self.recur(i, n-1) % 1000000007
            return self.LOOKUP[v][n] % 1000000007


if __name__ == '__main__':
    a = Solution()
    print(a.countVowelPermutation(2))