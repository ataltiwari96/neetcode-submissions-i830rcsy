class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ""
        for a in s:
            if a >= 'a' and a<='z' or a>='A' and a<='Z' or a>=str(0) and a<=str(9):
                st+=a
        if st.lower() == st.lower()[::-1]:
            return True
        else:
            return False
