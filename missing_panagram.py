class Solution:
    def missingPanagram(self, s):

        if len(set(sorted(s.lower()))) == 26:
            return -1
        arr = "abcdefghijklmnopqrstuvwxyz"
        s = s.lower()
        out = ""
        for a in arr:
            if a not in s:
                out = out + a
        return out

if __name__ == "__main__":
    s = input()
    obj = Solution()
    print(obj.missingPanagram(s))