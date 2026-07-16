class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_sorted = "".join(sorted(s, key=str.lower))
        t_sorted = "".join(sorted(t, key=str.lower))
        if s_sorted == t_sorted:
            return True
        return False