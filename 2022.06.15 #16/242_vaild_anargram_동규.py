class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for i in 'abcdefghijklmnopqrstuvwxyz':
            if s.count(i) != t.count(i):
                return False
        return True
