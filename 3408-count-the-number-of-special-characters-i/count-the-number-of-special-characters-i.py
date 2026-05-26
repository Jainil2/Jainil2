class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s = set()
        n = set()
        count = 0
        for char in word:
            t = ord(char)
            print(t)
            if t in n:
                continue
            elif (t - 32) in s or (t + 32) in s:
                count += 1
                n.add(t) 
            else:
                s.add(ord(char))
        return count
