class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()
        value = len(s) % k

        result = s[:value]

        for i in range(value, len(s), k):
            if result:
                result += "-"
            result += s[i:i+k]

        return result