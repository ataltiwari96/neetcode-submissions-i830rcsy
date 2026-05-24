class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ""
        for a in s:
            if a.isalnum():
                st+=a.lower()
        if st == st[::-1]:
            return True
        else:
            return False
