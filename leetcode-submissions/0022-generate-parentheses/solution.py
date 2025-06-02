class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def generate(k):
            # Base case
            if k == 0:
                return [""]

            # Recursive case
            valid = []
            for i in range(k):
                for l in generate(i):
                    for r in generate(k - 1 - i):
                        valid.append("(" + l + ")" + r)

            return valid

        return generate(n)

