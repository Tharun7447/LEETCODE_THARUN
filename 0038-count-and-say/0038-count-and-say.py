class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        for _ in range(n - 1):
            i = 0
            cur = ""
            while i < len(res):
                cnt = 1
                while i + 1 < len(res) and res[i] == res[i + 1]:
                    i += 1
                    cnt += 1
                cur += str(cnt) + res[i]
                i += 1
            res = cur
        return res
