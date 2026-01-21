class Solution:
    def removeSubstring(self, s: str, k: int) -> str:
        target = "(" * k + ")" * k
        while target in s:
            s = s.replace(target, "", 1)
        return s