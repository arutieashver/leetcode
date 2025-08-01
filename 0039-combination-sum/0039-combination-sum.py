class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start:int, current:List[int], total:int):
            #base case
            if total == target:
                result.append(list(current))
                return
            
            if total > target:
                return
            
            for i in range(start, len(candidates)):
                current.append(candidates[i])
                backtrack(i, current, total + candidates[i])
                current.pop()

        backtrack(0, [], 0)
        return result