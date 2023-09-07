def sol(used, target, candidates):
    fst, *rest = candidates
    solutions = []
    mult = 0
    while fst*mult <= target:
        use_this = {**used, fst: mult}
        if fst * mult == target:
            solutions.append(use_this)
            break
        if rest:
            solutions.extend(sol(use_this, target - fst*mult, rest))
        mult += 1
    return solutions

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        solutions = []
        for solution in sol({}, target, candidates):
            s = []
            for k, v in solution.items():
                s.extend([k]*v)
            solutions.append(s)
        return solutions
