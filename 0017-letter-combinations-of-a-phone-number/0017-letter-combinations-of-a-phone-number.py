class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        result = [""]

        if digits == "":
            return []

        for digit in digits:
            temp = []
            for prefix in result:
                for char in letters[digit]:
                    temp.append(prefix + char)
            result = temp

        return result
        