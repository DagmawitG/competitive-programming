class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        teams = []
        for i in range(len(scores)):
            teams.append([scores[i], ages[i]])
        teams.sort()
        dp = [teams[i][0] for i in range(len(teams))]

      
        for i in range(len(teams)):
            score, age = teams[i]
            for j in range(i):
                curr_score, curr_age = teams[j]
                if age >= curr_age:
                    dp[i] = max(dp[i], score + dp[j])
      
        return max(dp)        
