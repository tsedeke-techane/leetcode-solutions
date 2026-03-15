class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loser = Counter([match[1] for match in matches])
        winner = Counter([match[0] for match in matches])
        ans = [[], []]
        for num in winner:
            if num not in loser:
                ans[0].append(num)
        for num in loser:
            if loser[num] == 1:
                ans[1].append(num)
        for num in ans:
            num.sort()
        return ans

