class Solution:
    def processStr(self, s: str) -> str:
        result = ""
        for char in s:
            if char.isalpha():
                result += char
            elif char == '*':
                result = result[:-1]
            elif char == '#':
                result += result
            elif char == '%':
                result = result[::-1]
        return result