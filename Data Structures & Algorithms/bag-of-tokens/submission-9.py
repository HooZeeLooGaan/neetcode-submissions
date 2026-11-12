class Solution:

    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        low = 0
        high = len(tokens) - 1
        score = 0
        tokens.sort()
        max_score = 0

        while low <= high:
            if tokens[low] <= power:
                power -= tokens[low]
                low += 1
                score += 1
                max_score = max(max_score, score)

            elif score > 0:
                power += tokens[high]
                score -= 1
                high -= 1
            else:
                break

        return max_score
                
