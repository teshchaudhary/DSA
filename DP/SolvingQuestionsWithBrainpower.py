"""
You are given a 0-indexed 2D integer array questions where questions[i] = [pointsi, brainpoweri].

The array describes the questions of an exam, where you have to process the questions in order (i.e., starting from question 0) and make a decision whether to solve or skip each question. Solving question i will earn you pointsi points but you will be unable to solve each of the next brainpoweri questions. If you skip question i, you get to make the decision on the next question.

For example, given questions = [[3, 2], [4, 3], [4, 4], [2, 5]]:
If question 0 is solved, you will earn 3 points but you will be unable to solve questions 1 and 2.
If instead, question 0 is skipped and question 1 is solved, you will earn 4 points but you will be unable to solve questions 2 and 3.
Return the maximum points you can earn for the exam.

 

Example 1:

Input: questions = [[3,2],[4,3],[4,4],[2,5]]
Output: 5
Explanation: The maximum points can be earned by solving questions 0 and 3.
- Solve question 0: Earn 3 points, will be unable to solve the next 2 questions
- Unable to solve questions 1 and 2
- Solve question 3: Earn 2 points
Total points earned: 3 + 2 = 5. There is no other way to earn 5 or more points.
"""

# Recursion
class Solution:
    def helper(self, questions, i, n, dp):
        # Base case: if the question is reachable
        if i > n-1:
            return 0

        # We can either
        # Solve the question and jump to the next question
        # questions[i][0] + self.helper(questions, i+questions[i][1]+1, n, dp)
        # or
        # We can skip the current question and start with next one
        # self.helper(questions, i+1, n, dp)

        return max(questions[i][0] + self.helper(questions, i+questions[i][1]+1, n), self.helper(questions, i+1, n))

    def mostPoints(self, questions) -> int:
        n = len(questions)
        return self.helper(questions, 0, n)

# Memoization
class Solution:
    def helper(self, questions, i, n, dp):
        if i > n-1:
            return 0

        if dp[i] != -1:
            return dp[i]
        
        dp[i] = max(questions[i][0] + self.helper(questions, i+questions[i][1]+1, n, dp), self.helper(questions, i+1, n, dp))

        return dp[i]

    def mostPoints(self, questions) -> int:
        n = len(questions)
        dp = [-1 for _ in range(n+1)]

        return self.helper(questions, 0, n, dp)

# Tabulation
class Solution:
    def mostPoints(self, questions) -> int:
        n = len(questions)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            points, brainpower = questions[i]
            next_question = i + brainpower + 1 

            take = points + (dp[next_question] if next_question < n else 0)
            skip = dp[i + 1]

            dp[i] = max(take, skip)
            
        return dp[0]